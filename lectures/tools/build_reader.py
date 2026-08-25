"""Build the course reader PDF from the chapter Markdown sources.

    cd lectures/tools && .venv/bin/python build_reader.py

Typography and colour follow the lecture decks, so the reader and the slides read as
one course. Maths is written as $$...$$ in the Markdown and rendered as centred
display expressions — deliberately simple, since none of it needs a full TeX engine.
"""
import glob
import os
import re
import markdown
from weasyprint import HTML, CSS

READER = "../reader"
CHAPTERS = sorted(glob.glob(f"{READER}/ch*.md"))

CSS_TEXT = """
@page {
  size: A4;
  margin: 22mm 20mm 20mm 20mm;
  @bottom-center {
    content: counter(page);
    font-family: Georgia, serif; font-size: 9pt; color: #6B7680;
  }
  @top-right {
    content: string(chaptitle);
    font-family: Arial, sans-serif; font-size: 8pt; color: #9AA4AC;
    letter-spacing: .04em; text-transform: uppercase;
  }
}
@page :first { @top-right { content: normal; } }

html { font-size: 10.5pt; }
body {
  font-family: Georgia, "Times New Roman", serif;
  color: #1A1F24; line-height: 1.52; text-align: justify;
  hyphens: auto;
}

h1 {
  string-set: chaptitle content();
  font-family: Arial, sans-serif; font-size: 25pt; font-weight: bold;
  color: #1A1F24; line-height: 1.15;
  margin: 0 0 4mm 0; padding-bottom: 3mm;
  border-bottom: 3.5pt solid #0E7C86;
  page-break-before: always; text-align: left;
}
h1:first-of-type { page-break-before: avoid; }
h2 {
  font-family: Arial, sans-serif; font-size: 13.5pt; color: #0E7C86;
  margin: 8mm 0 2.5mm 0; text-align: left; page-break-after: avoid;
}
h3 {
  font-family: Arial, sans-serif; font-size: 11pt; color: #1A1F24;
  margin: 5mm 0 1.5mm 0; text-align: left; page-break-after: avoid;
}
p { margin: 0 0 2.6mm 0; }
strong { color: #12171C; }

/* lead-in list: the learning objectives */
h2 + ol { margin: 0 0 3mm 0; padding-left: 6mm; }
ol li, ul li { margin-bottom: 1.6mm; }

blockquote {
  margin: 4mm 0; padding: 3mm 4mm;
  background: #DCEDEF; border-left: 3.5pt solid #0E7C86;
  font-family: Arial, sans-serif; font-size: 10pt; text-align: left;
  page-break-inside: avoid;
}
blockquote p { margin: 0 0 1.5mm 0; }
blockquote p:last-child { margin-bottom: 0; }

table {
  width: 100%; border-collapse: collapse; margin: 3mm 0 2mm 0;
  font-family: Arial, sans-serif; font-size: 8.8pt;
  page-break-inside: avoid;
}
th {
  background: #1A1F24; color: #F7F5F1; text-align: left;
  padding: 1.8mm 2mm; font-weight: bold;
}
td { padding: 1.5mm 2mm; border-bottom: .5pt solid #E4E2DE; vertical-align: top; }
tr:nth-child(even) td { background: #F7F5F1; }

img { max-width: 100%; display: block; margin: 4mm auto 1.5mm auto; }

/* figure and table captions: a bolded lead paragraph right after an image */
.caption {
  font-family: Arial, sans-serif; font-size: 8.6pt; color: #4A555E;
  text-align: left; margin: 0 0 5mm 0; line-height: 1.4;
}

.math {
  letter-spacing: .01em;
  font-family: "Courier New", monospace; font-size: 10.5pt;
  text-align: center; margin: 3.5mm 0; color: #12171C;
  page-break-inside: avoid;
}

code {
  font-family: "Courier New", monospace; font-size: 9.5pt;
  background: #F0EEEA; padding: .3mm 1mm; border-radius: 1pt;
}

hr { border: none; border-top: .75pt solid #E4E2DE; margin: 6mm 0; }

.answers { page-break-before: always; }

/* title page */
.titlepage { page-break-after: always; text-align: left; }
.titlepage .rule { height: 4pt; width: 40mm; background: #D98324; margin: 6mm 0; }
.titlepage h1 {
  border: none; page-break-before: avoid; font-size: 30pt; margin-bottom: 2mm;
  string-set: chaptitle "";
}
.titlepage .sub { font-family: Arial, sans-serif; font-size: 13pt; color: #0E7C86;
  font-weight: bold; margin-bottom: 10mm; }
.titlepage .meta { font-family: Arial, sans-serif; font-size: 10pt; color: #6B7680;
  line-height: 1.7; }
.titlepage .note { font-family: Arial, sans-serif; font-size: 9pt; color: #6B7680;
  margin-top: 14mm; line-height: 1.55; border-top: .75pt solid #E4E2DE;
  padding-top: 4mm; text-align: left; }
"""

TITLE = """
<div class="titlepage">
  <div style="font-family:Arial;font-size:10pt;color:#0E7C86;font-weight:bold;
              letter-spacing:.08em">MICROELECTROMECHANICAL SYSTEMS AND SENSORS</div>
  <h1>Course reader</h1>
  <div class="sub">Chapters 1–2 · draft for review</div>
  <div class="rule"></div>
  <div class="meta">
    Bachelor programme · Electrical Engineering · 7th semester<br>
    Institute of Energy and Electrical Engineering<br>
    Draft, August 2026
  </div>
  <div class="note">
    <strong>How to use this reader.</strong> It does not replace a textbook. It carries the
    material that no textbook covers — the datasheet workflow, register-level interfacing,
    the specific parts on your bench — and points you at
    Morris &amp; Langari, <em>Measurement and Instrumentation</em> (3rd ed., Elsevier 2020)
    for the underlying theory. Each chapter ends with exercises and full answers; work them
    before the corresponding laboratory.<br><br>
    Numerical values in worked examples have been checked by computation. Component figures
    labelled &ldquo;Part A&rdquo;, &ldquo;Part B&rdquo; and &ldquo;Part C&rdquo; are
    representative of real commercial devices but are not attributed to a named product;
    always verify against the datasheet revision in your hand.
  </div>
</div>
"""


def render_math(html: str) -> str:
    """Display maths is written as plain Unicode between $$ … $$ — no TeX engine needed.

    Each line inside the delimiters becomes its own centred line, so multi-step
    derivations stack naturally. Editing these needs no LaTeX knowledge.
    """
    def sub(m):
        lines = [ln.strip() for ln in m.group(1).strip().split("\n") if ln.strip()]
        return "".join(f'<div class="math">{ln}</div>' for ln in lines)
    return re.sub(r"\$\$(.+?)\$\$", sub, html, flags=re.S)


def mark_captions(html: str) -> str:
    """A paragraph opening with <strong>Figure/Table is a caption."""
    return re.sub(r'<p>(<strong>(?:Figure|Table)\b.*?)</p>',
                  r'<p class="caption">\1</p>', html, flags=re.S)


parts = [TITLE]
for path in CHAPTERS:
    src = open(path).read()
    # the rule before Answers would otherwise be stranded alone on a page
    src = src.replace("\n---\n\n## Answers\n", "\n## Answers {: .answers }\n")
    src = src.replace("\n## Answers\n", "\n## Answers {: .answers }\n")
    html = markdown.markdown(src, extensions=["tables", "attr_list"])
    html = render_math(html)
    html = mark_captions(html)
    parts.append(html)

doc = f"<html><head><meta charset='utf-8'></head><body>{''.join(parts)}</body></html>"
out_html = f"{READER}/course-reader-ch1-2.html"
open(out_html, "w").write(doc)

HTML(string=doc, base_url=READER).write_pdf(
    f"{READER}/course-reader-ch1-2.pdf", stylesheets=[CSS(string=CSS_TEXT)])

os.remove(out_html)
print(f"built {READER}/course-reader-ch1-2.pdf from {len(CHAPTERS)} chapters")
