"""Lecture 2 — Sensor specifications and datasheet-based selection (80 min)."""
import math
from deck import *

D = Deck("MEMS & Sensors  ·  Lecture 2  ·  Specifications and datasheet-based selection")
S = D.slide


def spec_card(s, x, y, w, title, subtitle, rows, edge=GRAY, badge=None,
              badge_col=AMBER, h=Inches(3.72)):
    """A stylised datasheet front page."""
    card = box(s, x, y, w, h, "", fill=WHITE, edge=edge, edge_w=2,
               shape=MSO_SHAPE.RECTANGLE)
    box(s, x, y, w, Inches(0.62), title, fill=edge, edge=edge, tcolor=CREAM,
        size=19, bold=True, shape=MSO_SHAPE.RECTANGLE)
    txt(s, subtitle, x + Inches(0.18), y + Inches(0.75), w - Inches(0.36),
        Inches(0.4), 15, GRAY, italic=True)
    yy = y + Inches(1.14)
    for k, v in rows:
        txt(s, k, x + Inches(0.18), yy, w / 2 - Inches(0.2), Inches(0.3), 15, GRAY)
        txt(s, v, x + w / 2, yy, w / 2 - Inches(0.22), Inches(0.3), 15, INK,
            bold=True, font=MONO, align=PP_ALIGN.RIGHT)
        yy += Inches(0.38)
    if badge:
        box(s, x + Inches(0.18), y + h - Inches(0.55), w - Inches(0.36),
            Inches(0.44), badge, fill=badge_col, edge=badge_col, tcolor=DARK,
            size=13.5, bold=True)
    return card


# ───────────────────────────────────────────────────────── 1  title
s = S(bg=DARK, footer=False)
b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.34), H)
b.fill.solid(); b.fill.fore_color.rgb = TEAL
b.line.fill.background(); b.shadow.inherit = False
txt(s, "MICROELECTROMECHANICAL SYSTEMS AND SENSORS", Inches(1.15), Inches(1.5),
    Inches(11), Inches(0.4), 15, TEAL, bold=True)
txt(s, "Sensor specifications and\ndatasheet-based selection",
    Inches(1.15), Inches(2.25), Inches(11.3), Inches(2.2), 40, CREAM, bold=True,
    line=1.15)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.15), Inches(4.72), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "Lecture 2 of 16   ·   80 minutes   ·   Module A: Foundations",
    Inches(1.15), Inches(5.05), Inches(11), Inches(0.4), 18,
    RGBColor(0xB8, 0xC0, 0xC6))
txt(s, "Today one number decides a design — and it is not on any front page.",
    Inches(1.15), Inches(5.75), Inches(11), Inches(0.5), 17, GRAY)
D.notes(s, """
BEFORE THE BELL: have the muddiest-point list from Lecture 1 in front of you, and
have two real datasheets ready — printed, or on the students' laptops.

Open with the muddiest points (next slide). Do not skip it: answering last week's
confusions in the first two minutes is the single highest-return habit available
to you, and in a first offering it is also how you find out what is not landing.
""")


# ───────────────────────────────────────────────────────── 2  muddiest points
s = S()
heading(s, "Last week's muddiest points", "Your questions, answered before we start")
for i, t in enumerate(["1", "2", "3"]):
    box(s, M, Inches(2.25) + i * Inches(1.05), Inches(0.62), Inches(0.62), t,
        fill=TEAL, edge=TEAL, tcolor=CREAM, size=22, bold=True, font=MONO)
    box(s, M + Inches(0.95), Inches(2.25) + i * Inches(1.05), Inches(11.0),
        Inches(0.62), "", fill=WHITE, edge=GRAY_L, shape=MSO_SHAPE.RECTANGLE)
txt(s, "INSTRUCTOR: fill these three in from the exit tickets before class.",
    M + Inches(1.15), Inches(2.42), Inches(10.6), Inches(0.4), 17, GRAY_L,
    italic=True)
box(s, M, Inches(5.7), CONTENT_W, Inches(0.85),
    "Refer to concepts, never to students. Ninety seconds total, then move on.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 0:00–0:02. TEMPLATE SLIDE — you must fill it in before class.

Transcribe the three most frequent muddiest points from Lecture 1's exit tickets
and answer each in about 25 seconds. Name the concept, never the student.

If the tickets show that scaling (Poll 3) is still unresolved for a large part of
the room, put k ∝ L and m ∝ L³ back on the board now and leave them there — you
will want them again when noise density comes up at minute 50.

If you genuinely received no useful tickets, delete this slide rather than
improvising; a hollow version of this ritual is worse than none.
""")


# ───────────────────────────────────────────────────────── 3  retrieval
s = S()
heading(s, "Where are we today?", "Retrieval: last week's chain, this week's box")
chain(s, Inches(2.5), upto=7, highlight=(3,))
box(s, M, Inches(6.12), CONTENT_W, Inches(0.62),
    "Everything today happens BEFORE you own any hardware. This is the box you "
    "choose — and you choose it with arithmetic.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 0:02–0:05. RETRIEVAL PRACTICE, not review. Ask before you show:

"Without looking at your sheet — name the seven stages." Take them from the room,
in order, one student per stage. It costs 90 seconds and it is worth more than
re-explaining the diagram.

Then: "Today is stage 3 — the device itself. But notice: we are choosing it
before we have it. The only tools available are a document and arithmetic."
""")


# ───────────────────────────────────────────────────────── 4  hook: two front pages
s = S()
heading(s, "Two front pages", "You must order today. Which one?")
spec_card(s, M, Inches(1.98), Inches(5.85), "PART  A", "Accelerometer, 3-axis",
          [("Resolution", "16-bit"), ("Full scale", "±2 g"),
           ("Sensitivity", "0.061 mg/LSB"), ("Noise density", "100 µg/√Hz"),
           ("Unit price", "€1.80")],
          edge=TEAL, badge="“HIGH RESOLUTION · LOW NOISE”", badge_col=TEAL_L)
spec_card(s, M + Inches(6.35), Inches(1.98), Inches(5.85), "PART  B",
          "Accelerometer, 3-axis",
          [("Resolution", "14-bit"), ("Full scale", "±4 g"),
           ("Sensitivity", "0.488 mg/LSB"), ("Noise density", "100 µg/√Hz"),
           ("Unit price", "€4.20")],
          edge=GRAY, badge=None)
box(s, M, Inches(5.92), CONTENT_W, Inches(0.82),
    "The job:  report the tilt of a solar-tracker frame to ±0.5°, outdoors, 0 to 40 °C.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=21, bold=True)
D.notes(s, """
TIMING: 0:05–0:07. Show ONLY these two cards. Resist adding anything.

Read the two cards aloud, deadpan. Part A: eight times finer resolution, lower
price, and a marketing line. Part B: coarser, more expensive, nothing to say for
itself.

Then the job, and then the poll — immediately, before anyone can think too hard.

NOTE: these are representative commercial figures, not a named product, chosen so
the arithmetic is exact. Say so if a student asks — and praise the question.
""")


# ───────────────────────────────────────────────────────── 5  poll 1
opts1 = [("A", "Part A — eight times finer resolution, and cheaper"),
         ("B", "Part B"),
         ("C", "This cannot be decided from front pages alone")]
q1 = "Which part do you specify for a ±0.5° tilt measurement?"
s = poll(D, 1, q1, opts1, minute=7,
         note="Commit. In seventy minutes I will show you that most of this room just "
              "chose a part that cannot meet the requirement — and that its own datasheet "
              "said so, on page nine.")
D.notes(s, """
TIMING: 0:07–0:10. Baseline. Expect a clear majority for A (misconceptions M1
and M5 — resolution read as accuracy, headline read as truth).

Do NOT reveal. Record the distribution; you re-show it at minute 70.

If a sizeable group picks C, that is excellent — say "some of you are already
being careful, and you are right, but hold on to why."

Then set the agenda: "By minute fifty you will have computed the answer
yourselves. Everything between here and there is the equipment you need."
""")


# ───────────────────────────────────────────────────────── 6  the conversion
s = S()
heading(s, "First, turn the requirement into a number",
        "You cannot budget an error against an angle")
rich(s, M, Inches(2.3), CONTENT_W, Inches(1.2),
     [[("tilt of 0.5°  →  sin(0.5°) × 1 g  =  ", {"size": 25, "font": MONO}),
       ("8.73 mg", {"size": 31, "font": MONO, "bold": True, "color": TEAL})]],
     align=PP_ALIGN.CENTER)
box(s, M, Inches(3.85), CONTENT_W, Inches(1.05),
    "8.73 mg is the entire signal we are trying to measure.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=26, bold=True)
txt(s, "Every error term in this lecture gets compared against those 8.73 mg.\n"
       "Any term larger than that is fatal. Any term far below it is irrelevant — "
       "no matter how good it looks on a front page.",
    M, Inches(5.25), CONTENT_W, Inches(1.2), 21, INK, line=1.4)
D.notes(s, """
TIMING: 0:10–0:13. WRITE 8.73 mg ON THE PHYSICAL BOARD AND DO NOT ERASE IT.
You will point at it at least six times in the next hour.

Derive it live — it takes fifteen seconds and it models the habit: "a tilted
accelerometer sees a component of gravity, so half a degree is sin(0.5°) of one
g. Eight and three-quarter milli-g. That is the whole signal."

Then the sentence that makes the rest of the lecture make sense: "This single
number converts 'which is better?' — which is an opinion — into arithmetic."
""")


# ───────────────────────────────────────────────────────── 7  section C1
s = section(D, "chunk 1  ·  minutes 10–28", "The four words\nthat get confused",
            ["Accuracy. Precision. Resolution. Sensitivity.",
             "Most engineering arguments about sensors are really arguments about these."],
            minute="10:00")
D.notes(s, "TIMING: 0:13. Section marker, 15 seconds.")


# ───────────────────────────────────────────────────────── 8  target diagram
s = S()
heading(s, "Accuracy is not precision", "Same target, four different instruments")
labels = [("ACCURATE\nAND PRECISE", TEAL, [(0.02, 0.05), (-0.04, -0.02), (0.03, -0.05), (-0.02, 0.03)]),
          ("PRECISE, NOT\nACCURATE", RED, [(0.42, 0.30), (0.46, 0.36), (0.39, 0.35), (0.44, 0.27)]),
          ("ACCURATE, NOT\nPRECISE", AMBER, [(0.28, -0.26), (-0.30, 0.24), (0.04, 0.36), (-0.05, -0.34)]),
          ("NEITHER", GRAY, [(0.40, -0.28), (-0.18, 0.40), (0.44, 0.16), (-0.38, -0.20)])]
cx0, r_out = M + Inches(1.42), Inches(1.16)
for i, (name, col, pts) in enumerate(labels):
    cx = cx0 + i * Inches(3.0)
    cy = Inches(3.35)
    for rr, fl in ((r_out, GROUND), (r_out * 0.62, WHITE), (r_out * 0.26, TEAL_L)):
        o = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - rr, cy - rr, 2 * rr, 2 * rr)
        o.fill.solid(); o.fill.fore_color.rgb = fl
        o.line.color.rgb = GRAY_L; o.line.width = Pt(1)
        o.shadow.inherit = False
    for dx, dy in pts:
        dot(s, Emu(int(cx + r_out * dx * 2)), Emu(int(cy + r_out * dy * 2)),
            r=Inches(0.062), color=col)
    txt(s, name, cx - Inches(1.35), Inches(4.68), Inches(2.7), Inches(0.8), 16,
        col, bold=True, align=PP_ALIGN.CENTER, line=1.25)
box(s, M, Inches(5.72), CONTENT_W, Inches(0.95),
    "The centre of the target is the TRUE value. Precision is how tightly the shots "
    "group.\nAccuracy is where the group sits. They are independent — and only one of "
    "them is fixable by calibration.",
    fill=AMBER_L, edge=AMBER, size=17.5, bold=True)
D.notes(s, """
TIMING: 0:13–0:18.

Work left to right, but spend your time on the SECOND target — precise but
inaccurate. "This is the dangerous instrument. It looks superb. Every reading
agrees with every other reading. And they are all wrong by the same amount."

Then the question that carries the rest of the lecture — ask it, take answers:
"Which of these four can I fix with a calibration?"

Answer: target 2, completely (measure the offset once, subtract it). Target 3,
not at all by calibration — only by averaging, and averaging costs bandwidth.

Add resolution verbally: "Resolution is not on this picture at all. Resolution
is how finely I can report where the shot landed. I can report a wrong position
to six decimal places." (Misconception M1.)
""")


# ───────────────────────────────────────────────────────── 9–10  poll 2
opts2 = [("A", "Accurate but not precise"),
         ("B", "Precise but not accurate"),
         ("C", "Both — the spread is only 0.2 hPa"),
         ("D", "Neither, because the resolution is not stated")]
q2 = ("A pressure sensor in a chamber held at a true, constant 1000.0 hPa is read "
      "100 times. Every reading falls between 1012.3 and 1012.5 hPa. The device is:")
s = poll(D, 2, q2, opts2, minute=18,
         note="Vote alone, then find someone who disagrees.")
D.notes(s, """
TIMING: 0:18–0:22. TARGET 45–65 % first vote.

Full peer instruction: silent vote (45 s) → find a disagreeing partner (90 s) →
re-vote. Announce both percentages.

C is the target distractor: a 0.2 hPa spread LOOKS like quality. It is quality —
of the wrong kind. The device is 12.4 hPa wrong and beautifully consistent
about it.

RECORD BOTH NUMBERS.
""")
s = poll(D, 2, q2, opts2, minute=18, correct="B", reveal=True,
         note="12.4 hPa of offset, held to 0.2 hPa of scatter. Superb precision, useless "
              "accuracy — until somebody calibrates it.")
D.notes(s, """
Reveal, then IMMEDIATELY ask the follow-up (show of hands, no device):

  "Which of these two problems can I fix with a calibration?"

The 12.4 hPa offset — YES, single-point calibration against a reference.
The 0.2 hPa scatter — NO. Not removable, only reducible by averaging, and
averaging costs you bandwidth.

Then the rule on the next slide. This is the most portable thing in the lecture.
""")


# ───────────────────────────────────────────────────────── 11  the rule
s = S()
heading(s, "The rule worth memorising")
rules = [("SYSTEMATIC ERROR", "is a calibration problem", "offset, scale factor — measurable, removable", TEAL),
         ("RANDOM ERROR", "is a bandwidth problem", "noise — reducible only by averaging, which costs you speed", AMBER),
         ("DRIFT", "is a component-selection problem", "it moves after you calibrated — so you cannot calibrate it away", RED)]
y = Inches(2.2)
for k, v, sub, col in rules:
    box(s, M, y, Inches(3.55), Inches(0.92), k, fill=col, edge=col, tcolor=CREAM,
        size=18, bold=True)
    txt(s, v, M + Inches(3.85), y + Inches(0.05), Inches(8.2), Inches(0.45), 24,
        INK, bold=True)
    txt(s, sub, M + Inches(3.85), y + Inches(0.52), Inches(8.2), Inches(0.4), 17,
        GRAY)
    y += Inches(1.15)
box(s, M, Inches(5.85), CONTENT_W, Inches(0.8),
    "This rule is the spine of Lecture 14 and of Laboratories 3 and 5. "
    "You will use it in week six.",
    fill=GROUND, edge=GRAY, size=18, bold=True)
D.notes(s, """
TIMING: 0:22–0:25. Read the three headlines. Then the third line again, slowly.

"Drift is the one that ruins careers, because it passes every test you run on
the bench at 22 degrees and fails in the field in February."

That sentence is the bridge to the reveal at minute 70. Plant it deliberately.
""")


# ───────────────────────────────────────────────────────── 12  static/dynamic
s = S()
heading(s, "The vocabulary, sorted", "Static: what it does when nothing is moving. "
        "Dynamic: what it does when things change.")
box(s, M, Inches(2.25), Inches(5.85), Inches(0.62), "STATIC CHARACTERISTICS",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=17, bold=True)
box(s, M + Inches(6.35), Inches(2.25), Inches(5.85), Inches(0.62),
    "DYNAMIC CHARACTERISTICS", fill=AMBER, edge=AMBER, tcolor=DARK, size=17, bold=True)
stat = [("Range", "smallest to largest measurable value"),
        ("Sensitivity", "output change per unit of input"),
        ("Resolution", "smallest distinguishable change"),
        ("Offset", "output when the input is zero"),
        ("Linearity", "deviation from a straight line"),
        ("Hysteresis", "does it matter which way you came?"),
        ("Repeatability", "same input, same output, later")]
dyn = [("Bandwidth", "highest frequency reported faithfully"),
       ("Response time", "time to settle after a step"),
       ("ODR", "data rate — NOT bandwidth"),
       ("Noise density", "noise per √Hz"),
       ("Group delay", "how late the answer arrives"),
       ("Cross-sensitivity", "the axis you did not want"),
       ("Drift", "slow change with time and temperature")]
for i, ((k1, v1), (k2, v2)) in enumerate(zip(stat, dyn)):
    y = Inches(3.05) + i * Inches(0.535)
    txt(s, k1, M + Inches(0.05), y, Inches(1.9), Inches(0.3), 16, TEAL, bold=True)
    txt(s, v1, M + Inches(2.0), y, Inches(4.0), Inches(0.35), 14, GRAY)
    txt(s, k2, M + Inches(6.40), y, Inches(2.1), Inches(0.3), 16, AMBER, bold=True)
    txt(s, v2, M + Inches(8.60), y, Inches(3.5), Inches(0.35), 14, GRAY)
D.notes(s, """
TIMING: 0:25–0:28. DO NOT READ THIS SLIDE OUT. It is a reference page; say so.

Point at exactly two entries:

ODR is not bandwidth. "A sensor can hand you 200 numbers a second while telling
you nothing above 50 Hz. Students lose a whole afternoon to this every year, and
in Poll 3 I am going to catch some of you with it."

Cross-sensitivity: "an accelerometer that reports Z when you shake it in X. Every
real device does this. We come back to it in ten minutes with a question your
datasheet cannot answer."

Tell them this slide is in the handout so nobody transcribes it.
""")


# ───────────────────────────────────────────────────────── 13  section C2
s = section(D, "chunk 2  ·  minutes 28–46", "What the datasheet\nactually says",
            ["A datasheet is a legal document, not a promise.",
             "The headline is on page one. The truth is in the conditions."],
            minute="28:00")
D.notes(s, "TIMING: 0:28. Section marker.")


# ───────────────────────────────────────────────────────── 14  conditions first
s = S()
heading(s, "Read the conditions block first", "Then, and only then, read the number")
rows = [["Parameter", "Min", "Typ", "Max", "Unit", "Conditions"],
        ["Sensitivity", "—", "0.061", "—", "mg/LSB", "FS = ±2 g, 25 °C"],
        ["Zero-g level", "—", "±40", "—", "mg", "25 °C, after soldering"],
        ["Zero-g temp. coefficient", "—", "±0.5", "—", "mg/°C", "−40 to +85 °C"],
        ["Noise density", "—", "100", "—", "µg/√Hz", "ODR = 200 Hz, BW = 50 Hz"],
        ["Cross-axis sensitivity", "—", "±1", "—", "%", "package level, not board level"]]
table(s, M, Inches(2.15), CONTENT_W, rows, [0.26, 0.08, 0.10, 0.08, 0.11, 0.37],
      size=15, row_h=Inches(0.52), head_size=14.5, mono_cols=(1, 2, 3))
notes_pts = [("Every number is “typ”.", "No min, no max. You are being told the "
              "average of a production run, not a guarantee."),
             ("The conditions differ per row.", "Sensitivity at 25 °C. Drift over "
              "125 °C. Noise at one specific bandwidth. They are not comparable "
              "as printed.")]
y = Inches(5.35)
for k, v in notes_pts:
    txt(s, "▸  " + k, M, y, Inches(4.0), Inches(0.4), 18, RED, bold=True)
    txt(s, v, M + Inches(4.1), y, Inches(8.0), Inches(0.6), 17, INK, line=1.3)
    y += Inches(0.72)
D.notes(s, """
TIMING: 0:28–0:33. This is a REPRESENTATIVE extract, built to look exactly like
the ones they are about to open. Say that.

Teach the reading order explicitly, right to left: "Column six. Then column one.
Then, last, the number. Most people read it in exactly the opposite order and
that is how they get surprised in February."

The two red points are the lesson. On "typ": "typ means half the parts are worse.
If your design only works with a typ part, half your production does not work."

Now hand out the datasheets.
""")


# ───────────────────────────────────────────────────────── 15  the hunt
s = S()
heading(s, "The hunt", "Pairs · 8 minutes · write the page number next to every answer")
hunt = [("1", "Supply voltage range — and the separate I/O supply, if there is one"),
        ("2", "Sensitivity at EACH selectable full-scale range"),
        ("3", "Zero-offset level AND its temperature coefficient"),
        ("4", "Noise density — and the bandwidth it was measured at"),
        ("5", "The device-identification register and its expected value"),
        ("6", "Whether the headline numbers are typ, min or max — and at what temperature")]
y = Inches(2.15)
for n, t in hunt:
    box(s, M, y, Inches(0.55), Inches(0.55), n, fill=TEAL, edge=TEAL,
        tcolor=CREAM, size=17, bold=True, font=MONO)
    txt(s, t, M + Inches(0.85), y + Inches(0.1), Inches(11.2), Inches(0.45), 19, INK)
    y += Inches(0.68)
box(s, M, Inches(6.32), CONTENT_W, Inches(0.6),
    "Number 5 is not academic — you need it at the bench next week to prove your "
    "sensor is the sensor you think it is.",
    fill=AMBER_L, edge=AMBER, size=17.5, bold=True)
D.notes(s, """
TIMING: 0:33–0:41. Use the ACTUAL device from the lab kit so the skill transfers
directly to Lab 1 in week 2.

Circulate. Do not answer "where is it?" — answer "which section would a
manufacturer put that in?"

Number 4 is the one they will struggle with: the conditions are usually in a
footnote, and the ODR and the bandwidth are different numbers. That struggle IS
the learning; let it happen.

Number 5 is the WHO_AM_I register. Point out that they will type this value into
their code on Tuesday.

If the class is short on documents: project one page and run it as a whole-class
hunt, calling on pairs for each item.
""")


# ───────────────────────────────────────────────────────── 16  the unanswerable
s = statement(D, "“What is this device's\ncross-axis sensitivity after it\n"
                 "has been soldered to my board?”",
              "It is not in the datasheet. It cannot be. The figure is specified for the "
              "packaged die — and mounting stress, solder-joint asymmetry and PCB flex "
              "all change it.",
              size=32, eyebrow_text="now find this one", accent=RED)
D.notes(s, """
TIMING: 0:41–0:44. THE MOST IMPORTANT TWO MINUTES OF THE LECTURE.

Let them hunt for it for a genuine 60 seconds before you say anything. Some will
insist it must be there somewhere.

Then: "It is not there. And the manufacturer is not being evasive — they cannot
know what your board does to their part."

The habit to install, said in the first person: "The datasheet cannot tell me
this. I must measure it on my own assembled board."

That is why Lab 3 exists. Say so.
""")


# ───────────────────────────────────────────────────────── 17  break
s = S(bg=DARK)
eyebrow(s, "minute 44  ·  stand up", AMBER)
txt(s, "Which number was\nhardest to find?", M, Inches(1.85), Inches(11),
    Inches(1.8), 40, CREAM, bold=True, line=1.15)
txt(s, "Hands up. Then tell me why it was hard —\nnot what the answer was.",
    M, Inches(4.0), Inches(11), Inches(1.0), 24, RGBColor(0xB8, 0xC0, 0xC6), line=1.35)
box(s, M, Inches(5.4), CONTENT_W, Inches(0.95),
    "The conditions are where the truth lives.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=28, bold=True)
D.notes(s, """
TIMING: 0:44–0:46. Genuine state change — everyone stands, hands up, 90 seconds.

The usual winner is noise density (number 4), because its conditions are
buried in a footnote and ODR ≠ bandwidth.

Take two answers on WHY, not WHAT. "Because the number was in one place and the
conditions were in another" is the answer you are fishing for.

Then land the line and sit them down. Next: the arithmetic.
""")


# ───────────────────────────────────────────────────────── 18  section C3
s = section(D, "chunk 3  ·  minutes 46–70", "Now compute it",
            ["Four terms. One requirement. Twenty minutes.",
             "At the end of this you will know which part you should have chosen."],
            minute="46:00")
D.notes(s, "TIMING: 0:46. Section marker.")


# ───────────────────────────────────────────────────────── 19  noise arithmetic
s = S()
heading(s, "Noise density becomes noise", "…once you choose a bandwidth")
rich(s, M, Inches(2.2), CONTENT_W, Inches(0.9),
     [[("noise", {"size": 27, "font": MONO}),
       ("RMS", {"size": 18, "font": MONO}),
       ("  =  noise density  ×  √bandwidth", {"size": 27, "font": MONO, "bold": True})]],
     align=PP_ALIGN.CENTER)
box(s, M, Inches(3.42), CONTENT_W, Inches(0.98),
    "100 µg/√Hz  ×  √50 Hz  =  100 × 7.07  =  707 µg  =  0.71 mg",
    fill=WHITE, edge=TEAL, tcolor=INK, size=21, bold=True, font=MONO, edge_w=2.5)
pts = [("The units tell you the answer.",
        "µg/√Hz × √Hz = µg. If your units do not cancel, you have used the wrong number."),
       ("Bandwidth, not ODR.",
        "The ODR was 200 Hz. Using √200 gives 1.41 mg — a wrong answer that looks right."),
       ("Halve the bandwidth, gain √2.",
        "Noise is not a property of the sensor alone. It is a property of the sensor and "
        "the bandwidth you chose.")]
y = Inches(4.68)
for k, v in pts:
    txt(s, "▸  " + k, M, y, Inches(4.15), Inches(0.4), 17, TEAL, bold=True)
    txt(s, v, M + Inches(4.3), y, Inches(7.8), Inches(0.62), 15.5, INK, line=1.28)
    y += Inches(0.72)
D.notes(s, """
TIMING: 0:46–0:52. Do the arithmetic on the board with the units written out in
full. Unit cancellation — not the physics — is what actually blocks students here.

Emphasise the ODR trap explicitly before the poll. You WANT them to have been
warned; the ones who still fall for it have a genuine misconception, and that is
the diagnostic you need.

The third bullet is the conceptual payoff and it connects straight back to
Lecture 1's motor: bandwidth is a decision with consequences in both directions.
Too little and you miss the signal. Too much and you buy noise.
""")


# ───────────────────────────────────────────────────────── 20–21  poll 3
opts3 = [("A", "≈ 0.1 mg"), ("B", "≈ 0.7 mg"), ("C", "≈ 1.4 mg"), ("D", "≈ 5 mg")]
q3 = ("Noise density 100 µg/√Hz. You configure ODR = 200 Hz and measurement "
      "bandwidth = 50 Hz. What RMS noise appears in your readings?")
s = poll(D, 3, q3, opts3, minute=56,
         note="Every wrong answer here is a specific arithmetic mistake — so this is the "
              "most useful vote of the day. Take it seriously.")
D.notes(s, """
TIMING: 0:52–0:57. THE MOST DIAGNOSTIC POLL IN THE PILOT. Target 40–60 %.

Each distractor is a named procedural error, so the DISTRIBUTION tells you what
to re-teach:
  A — ignored bandwidth entirely
  B — correct: 100 × √50 = 707 µg
  C — used √ODR instead of √bandwidth (the M7 confusion)
  D — multiplied by bandwidth instead of its square root

RECORD THE FULL DISTRIBUTION, not just the correct percentage. If C is large,
that is your Lecture 3 opening. If D is large, the blocker is arithmetic, not
sensing — write √Hz on the board with units in full.

Peer instruction, then re-vote.
""")
s = poll(D, 3, q3, opts3, minute=56, correct="B", reveal=True,
         note="100 µg/√Hz × √50 Hz = 707 µg = 0.71 mg.  Now compare that with the "
              "8.73 mg we are trying to measure — and ask whether noise was ever the "
              "problem.")
D.notes(s, """
Reveal, then the reframe — this is the pivot of the whole lecture. Say it
almost casually:

"We just spent six minutes computing 0.71 mg of noise. Our signal is 8.73 mg.
So noise costs us about eight per cent of the measurand. Annoying. Survivable.
Now let me show you the term nobody computed."

Then go straight to drift.
""")


# ───────────────────────────────────────────────────────── 22  the other terms
s = S()
heading(s, "Three more terms, and one of them is not small")
terms = [("QUANTISATION", "LSB / √12", "A:  0.061/3.46 = 0.018\nB:  0.488/3.46 = 0.141",
          "Both utterly negligible against 8.73 mg.", TEAL),
         ("OFFSET", "calibrated out", "A:  ±40 mg  →  0\nB:  ±10 mg  →  0",
          "A single bench calibration removes this — at one temperature.", TEAL),
         ("OFFSET DRIFT", "TC × ΔT", "A:  0.5 × 20 = 10.0\nB:  0.1 × 20 =  2.0",
          "Calibrated at 20 °C, used 0–40 °C, so ΔT = ±20 °C.", RED)]
x = M
for name, formula, calc, note, col in terms:
    box(s, x, Inches(2.15), Inches(3.85), Inches(0.65), name, fill=col, edge=col,
        tcolor=CREAM, size=17, bold=True)
    box(s, x, Inches(2.9), Inches(3.85), Inches(0.62), formula, fill=WHITE,
        edge=col, tcolor=col, size=19, bold=True, font=MONO)
    txt(s, calc, x + Inches(0.12), Inches(3.72), Inches(3.65), Inches(0.9), 16,
        INK, font=MONO, line=1.4)
    txt(s, note, x + Inches(0.12), Inches(4.75), Inches(3.65), Inches(1.1), 16,
        GRAY, line=1.3)
    x += Inches(4.0)
box(s, M, Inches(5.85), CONTENT_W, Inches(0.9),
    "Part A drifts by 10 mg. The entire quantity we are trying to measure is 8.73 mg.",
    fill=RED_L, edge=RED, size=23, bold=True)
D.notes(s, """
TIMING: 0:57–1:02. Build left to right; the punch is on the right.

Quantisation: "Both are a rounding error on a rounding error. Note that Part A's
celebrated eight-times-finer resolution buys it 0.12 mg of advantage on a term
that was already invisible."

Offset: "Both fixable. This is the calibration column."

Drift: STOP HERE. "Part A's offset moves by ten milli-g across the temperature
range. Our signal is eight point seven three. The error is larger than the
thing being measured — and it appears after you calibrated, so no bench
procedure catches it."

Ask the room: "Which of the three columns did the front page mention?" None.
""")


# ───────────────────────────────────────────────────────── 23  the budget
s = S()
heading(s, "The error budget", "Root-sum-square, because the terms are independent")
rows = [["Term", "Part A", "Part B", "Where it came from"],
        ["Noise  (100 µg/√Hz × √50 Hz)", "0.707", "0.707", "datasheet × your bandwidth"],
        ["Quantisation  (LSB/√12)", "0.018", "0.141", "resolution and full scale"],
        ["Offset drift  (TC × ΔT)", "10.000", "2.000", "temp. coefficient × 20 °C"],
        ["TOTAL  (RSS)", "10.03", "2.13", "√(sum of squares)"],
        ["AS A TILT ANGLE", "0.574°", "0.122°", "asin(mg / 1000)"],
        ["AGAINST ±0.5°", "FAILS", "passes, 4× margin", "the requirement"]]
t = table(s, M, Inches(2.08), CONTENT_W, rows, [0.36, 0.15, 0.19, 0.30], size=16,
          row_h=Inches(0.525), head_size=16, mono_cols=(1, 2))
for j in (1, 2):
    for i in (4, 5, 6):
        cell = t.cell(i, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RED_L if j == 1 else TEAL_L
        cell.text_frame.paragraphs[0].runs[0].font.bold = True
txt(s, "All values in mg unless stated. Bandwidth 50 Hz, calibrated at 20 °C, "
       "used over 0–40 °C.",
    M, Inches(5.86), CONTENT_W, Inches(0.4), 15, GRAY, italic=True)
box(s, M, Inches(6.28), CONTENT_W, Inches(0.6),
    "One term dominates. It was on page nine, and it was not on either front page.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=18, bold=True)
D.notes(s, """
TIMING: 1:02–1:06. Reveal row by row if your tooling allows; otherwise walk down
with the cursor and make them predict the total before you say it.

Say the RSS rule and why: independent random terms add in quadrature, so the
LARGEST term dominates completely. 10 and 0.7 combine to 10.03 — the noise
term you spent six minutes on has changed the answer by three hundredths.

"That is the most important lesson in error budgeting: find the biggest term
first. Everything else is decoration."

Then the two bottom rows, slowly. FAILS. Passes with fourfold margin.
""")


# ───────────────────────────────────────────────────────── 24  reveal
s = poll(D, 1, q1, opts1, minute=70, correct="B", reveal=True,
         note="The right FIRST answer was C — you did not have enough information. "
              "The right SECOND answer, after twelve minutes of arithmetic, is B.")
D.notes(s, """
TIMING: 1:06–1:08. Show the minute-7 distribution next to this. The shift is the
lecture's evidence that it worked.

Say both halves explicitly — this is the professional habit, not a trick:

"If you chose C at minute seven, you were right, and you were right for the best
possible reason: you knew you could not decide. If you chose A, you were doing
what most engineers do — reading the headline. And if you now choose B, you can
defend it with a number, which is the only defence that survives a design
review."
""")


# ───────────────────────────────────────────────────────── 25  the statement
s = statement(D, "Part A resolves eight times finer\nthan Part B — and cannot do the job.",
              "Part B resolves 0.028° of tilt: eighteen times finer than the ±0.5° we "
              "need. Resolution was never the deciding variable. It only looked like it "
              "was, because it was the number on the front page.",
              size=34, eyebrow_text="the verdict", accent=RED)
D.notes(s, """
TIMING: 1:08–1:09. Silence, then read once.

Optional, if the room is with you: "And Part A was cheaper, and had a library.
Every incentive pointed at the wrong part."
""")


# ───────────────────────────────────────────────────────── 26  decision table
s = S()
heading(s, "Your turn: three candidates", "Teams of three · 8 minutes · commit to one")
rows = [["Criterion", "Weight", "A", "B", "C"],
        ["Meets ±0.5° over 0–40 °C", "pass/fail", "fail", "pass", "pass"],
        ["Total error as an angle", "high", "0.574°", "0.122°", "0.06°"],
        ["Unit price at 500 off", "medium", "€1.80", "€4.20", "€11.50"],
        ["Current draw", "medium", "0.15 mA", "0.18 mA", "0.90 mA"],
        ["Library already exists", "LOW", "yes", "no", "no"]]
table(s, M, Inches(2.1), Inches(8.5), rows, [0.40, 0.18, 0.14, 0.14, 0.14],
      size=15.5, row_h=Inches(0.50), head_size=15.5, mono_cols=(2, 3, 4))
box(s, M + Inches(8.8), Inches(2.1), Inches(3.35), Inches(1.0), "PART C",
    fill=GRAY, edge=GRAY, tcolor=CREAM, size=19, bold=True)
txt(s, "16-bit, ±2 g\n60 µg/√Hz\noffset ±5 mg\nTC ±0.05 mg/°C\n€11.50, 0.9 mA",
    M + Inches(8.95), Inches(3.25), Inches(3.2), Inches(1.5), 16, INK, font=MONO,
    line=1.45)
box(s, M, Inches(5.35), CONTENT_W, Inches(0.72),
    "Write one sentence:   “We specify Part ___ because ___”   — naming the "
    "DOMINANT ERROR TERM, not the headline.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
txt(s, "Part C is the trap in the other direction: technically the best part, six times "
       "the price, and it buys no capability the requirement asks for. "
       "Over-specifying is also an engineering failure.",
    M, Inches(6.25), CONTENT_W, Inches(0.7), 17, GRAY, italic=True, line=1.3)
D.notes(s, """
TIMING: 1:09–1:15. Teams of three, 8 minutes, one sheet. Circulate.

Two teams read their sentence aloud. Insist on the form: Part, then the dominant
term. "Because it is better" is not an answer.

IF A TEAM CHOOSES C: do not correct it — ask "what did the customer get for the
extra €4,850?" (500 units × €9.70.) Let them find it. Over-specification is a
real failure mode and this is the only place in the pilot that teaches it.

IF SHORT OF TIME: drop Part C, run it with two candidates in 5 minutes, set the
third as homework.
""")


# ───────────────────────────────────────────────────────── 27–28  poll 4 transfer
opts4 = [("A", "Sensor Q — five times better accuracy"),
         ("B", "Sensor P — its error is bounded over the whole temperature range; "
               "Q's is specified at one point only"),
         ("C", "Either — the temperature coefficient can be measured later"),
         ("D", "Sensor Q, calibrated at 25 °C before installation")]
q4 = ("New problem. Water level in an outdoor tank, 2 m deep (≈20 kPa full scale), "
      "to ±20 mm, water 5–35 °C.  P: total error band ±0.25 % FS over 0–50 °C.  "
      "Q: ±0.05 % FS at 25 °C, temperature coefficient not specified.")
s = poll(D, 4, q4, opts4, minute=72,
         note="Different measurand, different error term. Same question underneath.")
D.notes(s, """
TIMING: 1:15–1:18. TRANSFER — deliberately a new measurand so it tests the
principle, not memory of the tilt case. Target 55–75 %.

60 seconds, quick vote, short discussion.

THE POINT: P's ±0.25 % FS over the full range is 50 Pa ≈ 5 mm — comfortably
inside ±20 mm, and GUARANTEED across the operating temperature. Q's ±0.05 % FS
is 10 Pa ≈ 1 mm at 25 °C and UNKNOWN at 5 °C, because the temperature
coefficient is not specified at all.

You cannot write a defensible error budget for Q. That is the whole answer.

C and D are the "calibration fixes everything" misconception, now in a second
context. If students still pick them here after the drift lesson, note it — that
is a genuine finding for next year.
""")
s = poll(D, 4, q4, opts4, minute=72, correct="B", reveal=True,
         note="A total error band over the operating range beats a headline accuracy at "
              "one temperature. An unspecified coefficient is not a small error — it is "
              "an unbounded one.")
D.notes(s, """
Reveal. The sentence to land:

"An unspecified number is not a good number. It is an unknown number, and you
cannot put an unknown into a budget you have to sign."

Note the deliberate echo: in the tilt case the killer term was drift you could
compute. Here it is drift you cannot even compute. Same lesson, harder version.
""")


# ───────────────────────────────────────────────────────── 29  the rule
s = S()
heading(s, "The course's selection rule", "Quoted from your own semester plan")
box(s, M, Inches(2.35), CONTENT_W, Inches(1.5),
    "“Avoid selecting a part only because an Arduino library exists;\n"
    "students must still see the underlying configuration and data path.”",
    fill=DARK, edge=TEAL, tcolor=CREAM, size=23, bold=True, edge_w=3)
txt(s, "Part A had a library. Part A cannot do the job.", M, Inches(4.15),
    CONTENT_W, Inches(0.5), 26, RED, bold=True)
crit = ["selectable range and ODR", "documented bandwidth and noise",
        "self-test", "data-ready interrupt", "FIFO where relevant",
        "an accessible register map", "a complete datasheet"]
txt(s, "What to choose on instead — parts that expose the engineering:",
    M, Inches(4.95), CONTENT_W, Inches(0.4), 18, INK, bold=True)
x, y = M, Inches(5.45)
for i, c in enumerate(crit):
    if i == 4:
        x, y = M, Inches(6.05)
    b2 = box(s, x, y, Inches(2.85), Inches(0.50), c, fill=TEAL_L, edge=TEAL,
             size=13.5, bold=True)
    x += Inches(3.05)
D.notes(s, """
TIMING: 1:18–1:19. Ninety seconds.

Be honest about why the rule exists: "A library is a real asset and it will save
you a week. It is just not a specification. Rank it last, not zero."

The seven boxes are the plan's own component-selection criteria. Tell them these
are the features the lab kit was chosen to expose — which is why they will be
writing register values rather than calling someone's begin() function.
""")


# ───────────────────────────────────────────────────────── 30  summary
s = S()
heading(s, "Four things to keep")
keeps = [("01", "Turn the requirement into a number before you read any datasheet.",
          "0.5° became 8.73 mg, and 8.73 mg decided everything that followed."),
         ("02", "Find the dominant term. Everything else is decoration.",
          "10 mg and 0.7 mg combine to 10.03 mg. The small term never mattered."),
         ("03", "Resolution is not accuracy, and neither is precision.",
          "Systematic → calibration. Random → bandwidth. Drift → component choice."),
         ("04", "A number without its conditions is not a number.",
          "typ at 25 °C is not a guarantee, and an unspecified coefficient is unbounded.")]
y = Inches(2.05)
for n, t, sub in keeps:
    txt(s, n, M, y, Inches(0.75), Inches(0.5), 24, TEAL_L, bold=True, font=MONO)
    txt(s, t, M + Inches(0.85), y - Inches(0.02), Inches(11.2), Inches(0.45), 21,
        INK, bold=True)
    txt(s, sub, M + Inches(0.85), y + Inches(0.42), Inches(11.2), Inches(0.4), 17,
        GRAY)
    y += Inches(1.12)
D.notes(s, "TIMING: 1:19. Read the four bold lines only. Sixty seconds.")


# ───────────────────────────────────────────────────────── 31  exit ticket
s = S()
heading(s, "Exit ticket", "Anonymous · hand it in at the door")
cards = [("1  ·  COMPUTE", TEAL, CREAM,
          "A sensor gives 200 µg/√Hz.\nYou set a 100 Hz bandwidth.\n\n"
          "State the RMS noise."),
         ("2  ·  JUDGEMENT", AMBER, DARK,
          "Name the one specification you\nwill look for first, for the rest\n"
          "of your career, before the\nheadline number."),
         ("3  ·  MUDDIEST POINT", GRAY, CREAM,
          "What is the one thing today\nyou are least sure about?\n\nOne sentence.")]
x = M
for title, col, tc, body in cards:
    box(s, x, Inches(2.15), Inches(3.85), Inches(0.68), title, fill=col, edge=col,
        tcolor=tc, size=16.5, bold=True)
    txt(s, body, x + Inches(0.12), Inches(3.1), Inches(3.65), Inches(2.2), 18,
        INK, line=1.4)
    x += Inches(4.0)
box(s, M, Inches(5.75), CONTENT_W, Inches(0.75),
    "Question 1 is the one I will actually grade myself on. If the room cannot do it, "
    "I taught it badly.",
    fill=GROUND, edge=GRAY, size=18, bold=True)
D.notes(s, """
TIMING: 1:19–1:20.

Q1 key: 200 × √100 = 2000 µg = 2 mg. This is the independent check on L2.3 —
group work can hide an individual who cannot do it.

Q2 accepts either "the conditions block" or "offset drift / temperature
coefficient". Both are the right instinct.

Say the bottom line out loud. It is true, and it buys honest tickets.
""")


# ───────────────────────────────────────────────────────── 32  close
s = S(bg=DARK)
eyebrow(s, "next", TEAL)
txt(s, "Tuesday: Laboratory 1", M, Inches(1.35), Inches(11), Inches(0.8), 38,
    CREAM, bold=True)
txt(s, "Datasheet to data — bring the pre-lab sheet, signed",
    M, Inches(2.2), Inches(11), Inches(0.5), 25, TEAL, bold=True)
txt(s, "You already found number 5 on the hunt: the device-identification register.\n"
       "On Tuesday you read it off real silicon — and prove your sensor is the sensor\n"
       "you think it is.",
    M, Inches(2.95), Inches(11.6), Inches(1.3), 19, RGBColor(0xB8, 0xC0, 0xC6),
    line=1.4)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, Inches(4.45), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "AND THEN LECTURE 3", M, Inches(4.78), Inches(11), Inches(0.35), 14, AMBER,
    bold=True)
txt(s, "From physical quantity to trustworthy samples — sampling, aliasing,\n"
       "quantisation, and the ADC configuration that killed the motor.",
    M, Inches(5.2), Inches(11.3), Inches(1.0), 20, CREAM, line=1.4)
D.notes(s, """
TIMING: 1:20. End on time.

Close the loop with Lecture 1 explicitly: "In week one a motor died because
nobody specified a bandwidth. Next week we build the thing that specifies it."
""")


out = "../lecture-02/output/L2-sensor-specifications-and-selection.pptx"
D.save(out)
print(f"saved {out}")
