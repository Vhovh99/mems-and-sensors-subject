# -*- coding: utf-8 -*-
"""Produce the Armenian decks from the built English ones.

    cd lectures/tools && .venv/bin/python translate_deck.py

Reads   ../lecture-NN/output/LN-*.pptx  (all lectures, or the ones named on the command line)
Writes  ../lecture-NN/output/LN-*-HY.pptx   (never overwrites an existing one without --overwrite)

Nothing is translated in place: the English decks are untouched, so both languages
stay in step whenever build_l1.py / build_l2.py are re-run.

Fonts. Arial and Courier New carry no Armenian glyphs, so any run that ends up
containing Armenian is switched to DejaVu Sans (or DejaVu Sans Mono if it was
monospaced). Runs that stay Latin — register values, part numbers, units — keep
their original font, which preserves their digit metrics.

Note on Noto: "Noto Sans Armenian" was rejected deliberately. It has no Latin
digits, so LibreOffice substitutes them glyph by glyph and every number renders
with gaps ("0 . 0 6 1"). In a course made of numbers that is unusable.
"""
import glob
import os
import re
import sys

from pptx import Presentation
from pptx.util import Pt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import hy_part1, hy_part2, hy_part3, hy_part4, hy_part5  # noqa: E402
from i18n import hy_l3, hy_l4  # noqa: E402
from i18n import hy_instructor, hy_terms  # noqa: E402

# hy_instructor last: it holds the instructor's own hand-corrected wording,
# recovered from the -HY decks, and must win over the generated dictionaries.
HY = {}
for mod in (hy_part1, hy_part2, hy_part3, hy_part4, hy_part5,
            hy_l3, hy_l4, hy_instructor):
    HY.update(mod.HY)

ARM = re.compile(r"[԰-֏ﬓ-ﬗ]")
# strings that are pure number / unit / symbol need no translation and no font change
SKIP = re.compile(r"^[\s\d.,;:%×√±°µ/()|\-–—+=<>x\[\]{}A-Fa-f0-9€$≥≤≈∝²³₀]*$")

SANS_HY, MONO_HY = "DejaVu Sans", "DejaVu Sans Mono"

# Tokens that may appear in an otherwise wordless string — units, abbreviations and
# register mnemonics. Anything else alphabetic means the string is prose, and prose
# with no dictionary entry must be reported, never half-translated: applying the
# terminology pass to untranslated English produces sentences like
# "its datasheet resolution" -> "its տվյալների թերթիկ resolution".
UNITISH = {
    "mg", "kg", "hz", "khz", "mhz", "pa", "hpa", "kpa", "ma", "mv", "ms", "us",
    "lsb", "msb", "rms", "odr", "bw", "adc", "dac", "enob", "fifo", "spi", "i2c",
    "typ", "max", "min", "fs", "sram", "cpu", "csv", "led", "pcb", "rss", "si",
    "bit", "bits", "code", "codes", "count", "counts",
}
WORDS = re.compile(r"[A-Za-z]{2,}")


def is_wordless(text):
    """True when the string carries no English prose — only numbers and units."""
    return all(w.lower() in UNITISH for w in WORDS.findall(text))

missing, translated = [], 0
warnings = []          # (string, message) terminology calls left to a human


def font_for(original_name, text):
    """Pick a font that can actually render `text`."""
    if not ARM.search(text or ""):
        return original_name                      # still Latin: leave it alone
    if original_name and "Courier" in original_name:
        return MONO_HY
    return SANS_HY


def do_paragraph(para):
    """Translate a paragraph, collapsing its runs into one.

    Armenian word order rarely matches English, so translating run-by-run would
    scramble the sentence. Instead the whole paragraph is looked up as one string;
    the first run keeps its formatting and inherits bold if ANY run was bold.
    """
    global translated
    runs = para.runs
    if not runs:
        return
    whole = "".join(r.text for r in runs)
    key = whole.strip()
    if not key:
        return

    if key in HY:
        new = hy_terms.enforce(HY[key])
        translated += 1
    else:
        # A string with no dictionary entry may still carry a unit or an
        # abbreviation the course sets in Armenian — "60 µg/√Hz", "mg/LSB".
        # But only if it is not prose: see is_wordless().
        fixed = hy_terms.enforce(key) if is_wordless(key) else key
        if fixed != key:
            new = fixed
        elif SKIP.match(key):
            new = None                            # pure numerals: nothing to do
        else:
            missing.append(key)
            new = None
    if new is not None:
        for msg in hy_terms.lint(new):
            warnings.append((new, msg))

    keep = runs[0]
    if new is not None:
        any_bold = any(r.font.bold for r in runs)
        # preserve leading/trailing whitespace of the original
        lead = whole[: len(whole) - len(whole.lstrip())]
        trail = whole[len(whole.rstrip()):]
        keep.text = lead + new + trail
        for r in runs[1:]:
            r.text = ""
        if any_bold:
            keep.font.bold = True

    # Armenian runs ~10-25 % longer than English. Where a translated string grew,
    # ease the point size down so it still fits a box that was sized to the English.
    #
    # Short strings are labels, headings and table cells: they sit in boxes with no
    # room to reflow, and breaking one mid-word — "Էլեկտրամագնիսակա / ն" — is worse
    # than setting it a little smaller. Long strings are prose in generous boxes and
    # tolerate growth, so they are eased gently and keep a 14 pt-ish floor.
    if new is not None and keep.font.size and len(key) > 3:
        grow = len(new) / max(len(key), 1)
        if grow > 1.06:
            short = len(key) < 34
            exp, floor = (0.95, 0.74) if short else (0.55, 0.80)
            factor = max(floor, min(1.0, (1.0 / grow) ** exp))
            keep.font.size = Pt(round(keep.font.size.pt * factor, 1))

    keep.font.name = font_for(keep.font.name, keep.text)
    for r in runs[1:]:
        if r.text:
            r.font.name = font_for(r.font.name, r.text)


def walk(shape):
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            do_paragraph(para)
    if getattr(shape, "has_table", False) and shape.has_table:
        for row in shape.table.rows:
            for cell in row.cells:
                for para in cell.text_frame.paragraphs:
                    do_paragraph(para)
    if shape.shape_type == 6:                     # group
        for sub in shape.shapes:
            walk(sub)


def translate(path):
    out = path.replace(".pptx", "-HY.pptx")
    if os.path.exists(out) and "--overwrite" not in sys.argv:
        # L1 and L2 were hand-corrected inside the .pptx. Most of that wording
        # is now in i18n/hy_instructor.py, but sixteen paragraphs on the figure
        # slides could not be recovered, so a blind rebuild still loses work.
        print(f"· skipping {out} (exists — pass --overwrite to rebuild)")
        return out
    prs = Presentation(path)
    for slide in prs.slides:
        for shape in slide.shapes:
            walk(shape)
        # speaker notes: instructor-facing, kept in English on purpose (see README)
    prs.save(out)
    return out


if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if not a.startswith("-")]   # e.g. "03" "04"
    for n in (only or ["01", "02", "03", "04"]):
        for f in sorted(glob.glob(f"../lecture-{n}/output/L{int(n)}-*.pptx")):
            if f.endswith("-HY.pptx"):
                continue
            print("→", translate(f))

    uniq = sorted(set(missing))
    print(f"\ntranslated paragraphs : {translated}")
    print(f"untranslated strings   : {len(uniq)}")
    if uniq:
        with open("i18n/_untranslated.txt", "w") as fh:
            fh.write("\n".join(uniq))
        for s in uniq[:40]:
            print("   ·", s[:100])
        if len(uniq) > 40:
            print(f"   … {len(uniq) - 40} more in i18n/_untranslated.txt")

    if warnings:
        seen, groups = set(), {}
        for text, msg in warnings:
            if (text, msg) in seen:
                continue
            seen.add((text, msg))
            groups.setdefault(msg, []).append(text)
        print(f"\nterminology warnings   : {len(seen)}"
              f"  (judgement calls — see i18n/GLOSSARY-hy.md 'Open questions')")
        with open("i18n/_term_warnings.txt", "w") as fh:
            for msg, texts in sorted(groups.items()):
                print(f"   ⚠ {msg}  ×{len(texts)}")
                fh.write(f"## {msg}\n" + "".join(f"   {t}\n" for t in texts) + "\n")
