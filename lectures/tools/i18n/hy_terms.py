# -*- coding: utf-8 -*-
"""Canonical Armenian terminology for the MEMS & Sensors course.

WHY THIS FILE EXISTS
--------------------
The Armenian decks are generated, but between August and September 2026 the
instructor corrected terminology **by hand, inside the -HY.pptx files**. Around
350 paragraphs were changed, and none of it was in the dictionaries — so the next
`translate_deck.py` run would have silently thrown all of it away.

Those edits were recovered (per-slide sequence alignment against the English
decks) and cross-checked against `reader/ch0*-hy.md`, which the instructor
translated and reviewed end to end. Where the reader and the old deck
dictionaries disagreed, **the reader wins**: it is the reviewed artefact.

The result is below. `TERMS` is the bilingual record. `FIX` is applied to every
translated string, so a superseded term cannot come back no matter which of the
1 100 dictionary lines still holds the old wording — the correction lives in one
place instead of five. `LINT` flags the genuinely undecided cases for a human
rather than guessing at them.

HOW TO CHANGE A TERM
--------------------
Edit `TERMS` (the record) and `FIX` (the enforcement), then rerun
`translate_deck.py`. Every slide of every lecture follows in one pass.
"""
import re

# ---------------------------------------------------------------------------
# 1. The bilingual record.
#
# Source column:
#   ծրագիր  fixed by the accredited 2024 programme 1.11.1.17 — do not change
#           without telling the department
#   reader  established in the instructor-reviewed Armenian reader chapters
#   deck    established by the instructor's hand edits to the -HY decks
#   new     introduced for Lectures 3–4; no prior Armenian precedent in-course
# ---------------------------------------------------------------------------
TERMS = {
    # ---- measurement-chain vocabulary (L1) ----
    "sensor":                       ("տվիչ", "ծրագիր"),
    "actuator":                     ("ակտուատոր (գործարկիչ)", "ծրագիր+reader"),
    "transducer":                   ("փոխակերպիչ", "deck"),
    "measurand":                    ("չափվող մեծություն", "deck"),
    "measurement chain":            ("չափման շղթա", "deck"),
    "measurement system":           ("չափման համակարգ", "deck"),
    "proof mass":                   ("իներտ (սեյսմիկ) զանգված", "reader"),
    "stiffness":                    ("կոշտություն", "deck"),
    "resonant frequency":           ("ռեզոնանսային հաճախություն", "deck"),
    "scaling law":                  ("մասշտաբման օրենք", "deck"),
    "isotropic scaling":            ("իզոտրոպ մասշտաբավորում", "reader"),
    "stiction":                     ("ստիկցիա (կպչում)", "reader"),

    # ---- specification vocabulary (L2) ----
    "accuracy":                     ("ճշտություն", "reader"),
    "precision":                    ("ճշգրտություն", "reader"),
    "resolution":                   ("լուծաչափ", "reader"),
    "sensitivity":                  ("զգայունություն", "reader"),
    "range":                        ("չափման տիրույթ", "reader"),
    "full-scale range":             ("չափման լրիվ տիրույթ", "deck"),
    "offset":                       ("զրոյական շեղում", "reader"),
    "drift":                        ("դրեյֆ", "reader"),
    "temperature drift":            ("ջերմաստիճանային դրեյֆ", "reader"),
    "noise":                        ("աղմուկ", "ծրագիր"),
    "noise density":                ("աղմուկի սպեկտրային խտություն", "reader"),
    "bandwidth":                    ("հաճախականային թողունակություն", "reader"),
    "linearity":                    ("գծայնություն", "reader"),
    "hysteresis":                   ("հիստերեզիս", "new"),
    "repeatability":                ("կրկնելիություն", "reader"),
    "settling time":                ("հաստատման ժամանակ", "deck"),
    "step input":                   ("աստիճանաձև մուտք", "deck"),
    "group delay":                  ("խմբային հապաղում", "deck"),
    "cross-axis sensitivity":       ("միջառանցքային զգայունություն", "deck"),
    "cross-sensitivity":            ("խաչաձև զգայունություն", "reader"),
    "systematic error":             ("համակարգային սխալ", "reader"),
    "random error":                 ("պատահական սխալ", "reader"),
    "error term":                   ("սխալանքի բաղադրիչ", "deck"),
    "error budget":                 ("սխալների հաշվեկշիռ", "deck"),
    "root-sum-square (RSS)":        ("քառակուսիների գումարի քառակուսի արմատ (RSS)", "deck"),
    "spread / scatter":             ("ցրվածք", "deck"),
    "true value":                   ("իրական արժեք", "deck"),
    "calibration":                  ("չափաբերում", "reader"),
    "specification":                ("տեխնիկական բնութագիր", "deck"),
    "requirement":                  ("պահանջ", "deck"),
    "datasheet":                    ("տվյալների թերթիկ", "reader"),
    "typical (typ)":                ("բնորոշ (typ.)", "reader"),
    "guaranteed":                   ("երաշխավորված", "reader"),
    "margin":                       ("պաշար", "deck"),
    "trade-off":                    ("փոխզիջում", "deck"),

    # ---- acquisition vocabulary (L3) ----
    "analog signal":                ("անալոգային ազդանշան", "ծրագիր"),
    "digital signal":               ("թվային ազդանշան", "ծրագիր"),
    "digitisation":                 ("թվայնացում", "ծրագիր"),
    "ADC":                          ("ԱԹԿ — անալոգաթվային կերպափոխիչ", "ծրագիր"),
    "DAC":                          ("ԹԱԿ — թվաանալոգային կերպափոխիչ", "ծրագիր"),
    "amplifier":                    ("ուժեղարար", "ծրագիր"),
    "operational amplifier":        ("օպերացիոն ուժեղարար", "ծրագիր"),
    "instrumentation amplifier":    ("չափիչ ուժեղարար", "new"),
    "filter":                       ("զտիչ", "reader"),
    "low-pass filter":              ("ցածր հաճախությունների զտիչ", "new"),
    "anti-alias filter":            ("հակաալիասինգային զտիչ", "reader"),
    "sampling":                     ("նմուշառում", "reader"),
    "sample":                       ("նմուշ", "reader"),
    "sampling rate":                ("նմուշառման հաճախություն", "reader"),
    "Nyquist–Shannon theorem":      ("Նայքվիստ–Շենոնի նմուշառման թեորեմ", "reader"),
    "aliasing":                     ("ալիասինգ", "reader"),
    "alias frequency":              ("կեղծ (alias) հաճախականություն", "reader"),
    "quantisation":                 ("քվանտացում", "reader"),
    "quantisation error":           ("քվանտացման սխալ", "deck"),
    "quantisation noise":           ("քվանտացման աղմուկ", "deck"),
    "LSB":                          ("ԿՆԲ — կրտսեր նշանակալի բիթ", "reader"),
    "RMS":                          ("ՄՔՄ — միջին քառակուսային մեծություն", "reader"),
    "MSB":                          ("ԱՆԲ — ավագ նշանակալի բիթ", "new"),
    "bit":                          ("բիթ", "ծրագիր"),
    "code (raw code)":              ("թվային կոդ", "deck"),
    "reference voltage":            ("հենային լարում", "new"),
    "ratiometric measurement":      ("հարաբերակցային չափում", "new"),
    "Wheatstone bridge":            ("Ուիտսթոնի կամրջակ", "new"),
    "bridge excitation":            ("կամրջակի սնուցում", "new"),
    "voltage output":               ("լարման ելք", "new"),
    "current loop (4–20 mA)":       ("հոսանքային օղակ (4–20 mA)", "new"),
    "common-mode voltage":          ("համաֆազ լարում", "new"),
    "gain":                         ("ուժեղացման գործակից", "new"),
    "saturation":                   ("հագեցում", "new"),
    "grounding":                    ("հողանցում", "new"),
    "shielding":                    ("էկրանավորում", "new"),
    "ODR (output data rate)":       ("ելքային տվյալների հաճախություն (ODR)", "deck"),
    "ENOB":                         ("արդյունարար բիթայնություն (ENOB)", "new"),
    "jitter":                       ("ջիտեր (ժամանակային տարուբերում)", "new"),
    "timestamp":                    ("ժամանակային դրոշմ", "reader"),
    "data integrity":               ("տվյալների ամբողջականություն", "new"),
    "SI units":                     ("ՄՄ միավորներ", "deck"),
    "interface":                    ("ինտերֆեյս", "ծրագիր"),
    "serial peripheral interface":  ("հաջորդական պերիֆերային ինտերֆեյս (SPI)", "ծրագիր"),
    "register":                     ("ռեգիստր", "deck"),
    "register map":                 ("ռեգիստրային քարտեզ", "deck"),
    "interrupt":                    ("ընդհատում", "ծրագիր"),
    "data-ready interrupt":         ("տվյալների պատրաստ լինելու ընդհատում", "deck"),
    "polling":                      ("հարցախույզ", "new"),
    "two's complement":             ("երկուսի լրացում", "new"),
    "endianness":                   ("բայթերի կարգ", "new"),
    "little-endian":                ("կրտսեր բայթն առաջ", "new"),
    "microcontroller":              ("միկրոկոնտրոլլեր", "ծրագիր"),
    "self-test":                    ("ինքնաստուգման գործառույթ", "deck"),

    # ---- structures, transduction, fabrication (L4) ----
    "MEMS":                         ("MEMS", "deck"),
    "die":                          ("բյուրեղ", "reader"),
    "wafer":                        ("թիթեղ (wafer)", "new"),
    "substrate":                    ("հենք", "new"),
    "package":                      ("պատյան", "reader"),
    "packaging":                    ("պատյանավորում", "reader"),
    "cantilever beam":              ("կախովի հեծան", "new"),
    "flexure / suspension":         ("ճկուն կախոց", "reader"),
    "diaphragm":                    ("թաղանթ", "new"),
    "resonator":                    ("ռեզոնատոր", "new"),
    "comb structure / comb drive":  ("սանրաձև կառուցվածք", "new"),
    "gap":                          ("բացակ", "reader"),
    "capacitive transduction":      ("ունակային փոխակերպում", "ծրագիր"),
    "piezoresistive transduction":  ("պիեզոդիմադրական փոխակերպում", "new"),
    "piezoelectric transduction":   ("պիեզոէլեկտրական փոխակերպում", "new"),
    "thermal transduction":         ("ջերմային փոխակերպում", "new"),
    "electromagnetic transduction": ("էլեկտրամագնիսական փոխակերպում", "new"),
    "optical transduction":         ("օպտիկական փոխակերպում", "ծրագիր"),
    "gauge factor":                 ("տենզոզգայունության գործակից", "new"),
    "lithography":                  ("վիմագրություն", "reader"),
    "photoresist":                  ("լուսադիմադրողական շերտ", "new"),
    "deposition":                   ("նստեցում", "new"),
    "thin film":                    ("բարակ թաղանթ", "new"),
    "etching":                      ("փորագրում", "new"),
    "isotropic etching":            ("իզոտրոպ փորագրում", "new"),
    "anisotropic etching":          ("անիզոտրոպ փորագրում", "new"),
    "sacrificial layer":            ("զոհաբերվող շերտ", "new"),
    "release":                       ("ազատում", "new"),
    "bulk micromachining":          ("ծավալային միկրոմշակում", "new"),
    "surface micromachining":       ("մակերևութային միկրոմշակում", "new"),
    "mask":                         ("դիմակ", "new"),
    "residual stress":              ("մնացորդային լարվածություն", "new"),
    "mounting stress":              ("ամրացման լարվածություն", "reader"),
    "PCB / board":                  ("տպասալ", "reader"),
    "solder joint":                 ("զոդակ", "reader"),
    "soldering":                    ("զոդում", "deck"),
    "outgassing":                   ("գազազատում", "new"),
    "hermetic sealing":             ("հերմետիկ խափանում", "new"),
    "getter":                       ("գազակլանիչ", "new"),
    "ageing":                       ("ծերացում", "new"),
    "yield":                        ("ելքային բերք", "new"),

    # ---- classroom furniture ----
    "poll":                         ("քվեարկություն", "deck"),
    "answer":                        ("պատասխան", "deck"),
    "part (section of lecture)":    ("բաժին", "deck"),
    "discussion":                   ("քննարկում", "deck"),
    "conclusion / verdict":         ("եզրակացություն", "deck"),
    "retrieval":                    ("վերհիշում", "deck"),
    "exit ticket":                  ("ելքի տոմս", "deck"),
    "laboratory work":              ("լաբորատոր աշխատանք", "deck"),
    "engineering (adj.)":           ("ճարտարագիտական", "reader"),
    # The reader uses all three of եզրույթ, տերմին and հասկացություն. That is not an
    # inconsistency: եզրույթ is the named unit of vocabulary ("three terms we will use
    # precisely"), հասկացություն is the idea behind it, տերմին the loanword for either.
    "term (unit of vocabulary)":    ("եզրույթ", "reader"),
    "concept":                      ("հասկացություն", "reader"),
    "microphone":                   ("խոսափող", "reader"),
    "reliable, trustworthy":        ("հավաստի", "reader"),
    "component / term of a sum":    ("բաղադրիչ", "deck"),

    # ---- laboratory vocabulary, from the instructor's own lab-01 Armenian ----
    "board (the Nucleo)":           ("սալ", "lab"),
    "pin / pin-out":                ("ելուստ", "lab"),
    "serial console":               ("հաջորդական կապի վահանակ", "lab"),
    "raw code":                     ("հում կոդ", "lab"),
    "to compile":                   ("կազմարկել", "lab"),
    "toolchain":                    ("ծրագրային գործիքաշար", "lab"),
    "IMU":                          ("իներցիալ չափման միավոր (IMU)", "lab"),
    "pre-lab sheet":                ("նախալաբորատոր թերթիկ", "lab"),
    "capture (a data capture)":     ("գրանցում", "new"),
    "moving average":               ("սահող միջինացում", "new"),
    "standard deviation":           ("միջին քառակուսային շեղում", "new"),
    "to flash (a binary)":          ("ծրագրավորել", "lab"),
    "build (a binary)":             ("կազմարկված պատկեր", "new"),
}


# ---------------------------------------------------------------------------
# 2. Enforcement.
#
# Ordered longest-first. Each pair is expanded at import time into its
# lower-case, capitalised and upper-case forms, so ALL-CAPS slide labels are
# covered too. Armenian declines, so the inflected forms are listed explicitly
# wherever a bare stem swap would produce a wrong ending.
# ---------------------------------------------------------------------------
_PAIRS = [
    # resolution: -ություն noun -> -աչափ noun, so every case ending differs
    ("լուծունակությունները", "լուծաչափերը"),
    ("լուծունակություններ",  "լուծաչափեր"),
    ("լուծունակությունից",   "լուծաչափից"),
    ("լուծունակությամբ",     "լուծաչափով"),
    ("լուծունակությունն",    "լուծաչափն"),
    ("լուծունակությունը",    "լուծաչափը"),
    ("լուծունակության",      "լուծաչափի"),
    ("լուծունակություն",     "լուծաչափ"),

    # calibration: stem swap is safe for every form this course uses
    # (ստուգաչափում/-ման/-մամբ/-ված/-ելու -> չափաբերում/-ման/-մամբ/-ված/-ելու)
    ("ստուգաչափ", "չափաբեր"),

    # accelerometer: stem swap is safe (աքսելերոմետրը/-ի/-ով -> արագաչափը/-ի/-ով)
    ("աքսելերոմետր", "արագաչափ"),

    # datasheet: the Latin word carried an Armenian case ending with a hyphen
    ("datasheet-ներում", "տվյալների թերթիկներում"),
    ("datasheet-ներ",    "տվյալների թերթիկներ"),
    ("datasheet-ում",    "տվյալների թերթիկում"),
    ("datasheet-ից",     "տվյալների թերթիկից"),
    ("datasheet-ով",     "տվյալների թերթիկով"),
    ("datasheet-ի",      "տվյալների թերթիկի"),
    ("datasheet-ը",      "տվյալների թերթիկը"),
    ("datasheet-ն",      "տվյալների թերթիկն"),
    ("datasheet",        "տվյալների թերթիկ"),

    # timestamp / board / package: stem swaps, all forms safe
    ("ժամանականիշ",   "ժամանակային դրոշմ"),
    ("տպատախտակ",     "տպասալ"),
    ("փաթեթավոր",     "պատյանավոր"),
    ("փաթեթ",         "պատյան"),

    # error: only in these two fixed collocations — bare "սխալանք" is still the
    # right word for a term of an error budget, and must not be touched
    ("համակարգային սխալանքը", "համակարգային սխալը"),
    ("համակարգային սխալանքի", "համակարգային սխալի"),
    ("համակարգային սխալանք",  "համակարգային սխալ"),
    ("պատահական սխալանքը",    "պատահական սխալը"),
    ("պատահական սխալանքի",    "պատահական սխալի"),
    ("պատահական սխալանք",     "պատահական սխալ"),

    # scatter
    ("ցրվածությունը", "ցրվածքը"),
    ("ցրվածության",   "ցրվածքի"),
    ("ցրվածությամբ",  "ցրվածքով"),
    ("ցրվածություն",  "ցրվածք"),

    # group delay, engineering, true value
    ("խմբային ուշացում", "խմբային հապաղում"),
    ("ինժեներական",      "ճարտարագիտական"),
    ("ինժեներություն",   "ճարտարագիտություն"),
    ("ճշմարիտ արժեք",    "իրական արժեք"),

    # units the reader sets in Armenian
    ("mg/LSB", "mg/ԿՆԲ"),
]


def _expand(pairs):
    out = []
    for old, new in pairs:
        for f in (lambda s: s, lambda s: s[:1].upper() + s[1:], str.upper):
            o, n = f(old), f(new)
            if (o, n) not in out:
                out.append((o, n))
    # longest first, so "լուծունակությունը" is consumed before "լուծունակություն"
    return sorted(out, key=lambda p: -len(p[0]))


FIX = _expand(_PAIRS)

# noise density gains its qualifier only where it does not already have one
_ASD = re.compile(r"(?<!սպեկտրային )(?<!սպեկտր\. )(?<!սպ\. )"
                  r"([Աա]ղմուկի) (խտություն\w*)")

# Hz/kHz/MHz become Armenian in prose, but stay Latin inside a formula.
# "=" is the tell: the instructor kept "ODR = 200 Hz" and "µg/√Hz × √Hz = µg"
# Latin, while writing "20 Հց", "1520 Հց" and "√Հց-ի հաշվով" in Armenian.
_HZ = re.compile(r"(?<![A-Za-z])([kM]?)Hz(?![A-Za-z])")
_PA = re.compile(r"(?<![A-Za-z])Pa(?![A-Za-z])")
_HZ_MAP = {"": "Հց", "k": "կՀց", "M": "ՄՀց"}


def enforce(text):
    """Apply the canonical terminology to one translated string."""
    if not text:
        return text
    for old, new in FIX:
        if old in text:
            text = text.replace(old, new)
    text = _ASD.sub(lambda m: f"{m.group(1)} սպեկտրային {m.group(2)}", text)
    if "=" not in text:
        text = _HZ.sub(lambda m: _HZ_MAP[m.group(1)], text)
        text = _PA.sub("Պա", text)
    return text


# ---------------------------------------------------------------------------
# 3. Lint — genuinely undecided calls. These are reported, never rewritten,
#    because the right answer depends on a decision only the department can
#    make. See GLOSSARY-hy.md "Open questions".
# ---------------------------------------------------------------------------
LINT = [
    (re.compile(r"(?<![Ա-Ֆա-ֆ])ֆիլտր"),
     "ֆիլտր → the reader uses զտիչ; ֆիլտր is the accredited ծրագիր's word"),
    (re.compile(r"(?<![ԱաՈո])LSB"),
     "LSB → the reader uses ԿՆԲ everywhere"),
    (re.compile(r"[Թթ]ողունակություն(?!ը՝ ոչ)"),
     "թողունակություն → prose prefers հաճախականային թողունակություն"),
    (re.compile(r"Սարք [ԱԲԳ]"),
     "Սարք Ա/Բ/Գ → the reader labels candidates A, B, C in Latin"),
    (re.compile(r"\d+\s?(mm|µm|m)(?![A-Za-zԱ-Ֆա-ֆ])"),
     "mm/µm → the reader sets these as մմ / մկմ"),
    (re.compile(r"աքսելերոմետր"),
     "աքսելերոմետր → superseded by արագաչափ (should have been auto-fixed)"),
    (re.compile(r"(?<![Աա]նի)(?<![Իի])շեղում"),
     "շեղում → check: drift is դրեյֆ; only offset is զրոյական շեղում"),
]


def lint(text):
    """Return the terminology warnings for one string."""
    return [msg for rx, msg in LINT if rx.search(text or "")]
