"""Lecture 3 — From physical quantity to trustworthy samples (80 min).

Built from lecture-03/output/lecture-plan.md (the authoritative timeline) and
lecture-03/output/activities.md (poll wording, worked arithmetic).

Minute markers stay OFF on screen (deck.SHOW_MINUTES is False by default and is
deliberately not changed here). Timings live in the speaker notes only.
"""
import math
from deck import *

D = Deck("MEMS & Sensors  ·  Lecture 3  ·  From physical quantity to trustworthy samples")
S = D.slide


# ---------------------------------------------------------------- local helpers
def num_card(s, x, y, w, big, label, body, col, h=Inches(2.55)):
    """One of the lecture's three anchor numbers, as a card. Used on 4 and 39."""
    box(s, x, y, w, h, "", fill=WHITE, edge=col, edge_w=2.5,
        shape=MSO_SHAPE.RECTANGLE)
    txt(s, big, x, y + Inches(0.26), w, Inches(1.0), 50, col, bold=True,
        font=MONO, align=PP_ALIGN.CENTER)
    txt(s, label.upper(), x + Inches(0.16), y + Inches(1.30), w - Inches(0.32),
        Inches(0.55), 12, col, bold=True, align=PP_ALIGN.CENTER, line=1.2)
    txt(s, body, x + Inches(0.16), y + Inches(1.92), w - Inches(0.32),
        Inches(0.9), 15, INK, align=PP_ALIGN.CENTER, line=1.28)


def panel(s, x, y, w, h, title, col, tcolor=CREAM):
    """A titled panel. Returns the y at which its body may start."""
    box(s, x, y, w, h, "", fill=WHITE, edge=col, edge_w=2.5,
        shape=MSO_SHAPE.RECTANGLE)
    box(s, x, y, w, Inches(0.66), title, fill=col, edge=col, tcolor=tcolor,
        size=15.5, bold=True, shape=MSO_SHAPE.RECTANGLE)
    return y + Inches(0.86)


def pipeline(s, y, items, col, x=M, bw=Inches(2.4), gap=Inches(0.55),
             h=Inches(0.80), last_col=None):
    """A left-to-right run of boxes joined by arrows. Used twice on slide 21."""
    for i, label in enumerate(items):
        xx = x + i * (bw + gap)
        hot = (last_col is not None and i == len(items) - 1)
        box(s, xx, y, bw, h, label,
            fill=RED_L if hot else WHITE, edge=last_col if hot else col,
            tcolor=INK, size=13, bold=True, edge_w=2.5 if hot else 1.5)
        if i:
            arrow(s, xx - gap + Inches(0.07), y + h / 2 - Inches(0.11),
                  gap - Inches(0.14), color=col)


def poll_note(s, text, color=GRAY):
    """Caption under a poll's options. Kept below the option stack so long
    stems (which push the options down) never collide with it."""
    txt(s, text, M, Inches(6.26), CONTENT_W, Inches(0.62), 15, color,
        italic=True, line=1.25)


def bullet(s, y, k, v, col=TEAL, kw=Inches(4.15), size=17, vsize=16):
    txt(s, "▸  " + k, M, y, kw, Inches(0.4), size, col, bold=True)
    txt(s, v, M + kw + Inches(0.15), y, CONTENT_W - kw - Inches(0.15),
        Inches(0.7), vsize, INK, line=1.3)


# ───────────────────────────────────────────────────────── 1  title
s = S(bg=DARK, footer=False)
b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.34), H)
b.fill.solid(); b.fill.fore_color.rgb = TEAL
b.line.fill.background(); b.shadow.inherit = False
txt(s, "MICROELECTROMECHANICAL SYSTEMS AND SENSORS", Inches(1.15), Inches(1.5),
    Inches(11), Inches(0.4), 15, TEAL, bold=True)
txt(s, "From physical quantity to\ntrustworthy samples",
    Inches(1.15), Inches(2.25), Inches(11.3), Inches(2.2), 40, CREAM, bold=True,
    line=1.15)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.15), Inches(4.72), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "Lecture 3 of 16   ·   80 minutes   ·   Module A: Foundations",
    Inches(1.15), Inches(5.05), Inches(11), Inches(0.4), 18,
    RGBColor(0xB8, 0xC0, 0xC6))
txt(s, "One log file, and three numbers that decide how much of it is true.",
    Inches(1.15), Inches(5.75), Inches(11), Inches(0.5), 17, GRAY)
D.notes(s, """
TIMING: 00:00–00:01.

BEFORE THE BELL: the muddiest points from Lecture 2's exit tickets typed into the
next slide, the ISM330DHCX datasheet open at the accelerometer noise table, and
three board colours if you have them — teal, amber, red.

Do not preview the lecture. Say one sentence and move: "Last week you chose a
part and defended it with arithmetic. This week the part is on the bench, it is
filling a file with numbers, and I am going to ask you how much of that file is
true." Then the muddiest points.

No microcontrollers today. If students brought them, ask them to put them away —
this is the lecture before the bench, deliberately.
""")


# ───────────────────────────────────────────────────────── 2  muddiest points
s = S()
heading(s, "Last week's muddiest points", "Your questions, answered before we start")
for i, t in enumerate(["1", "2", "3"]):
    box(s, M, Inches(2.25) + i * Inches(1.05), Inches(0.62), Inches(0.62), t,
        fill=TEAL, edge=TEAL, tcolor=CREAM, size=22, bold=True, font=MONO)
    box(s, M + Inches(0.95), Inches(2.25) + i * Inches(1.05), Inches(11.0),
        Inches(0.62), "", fill=WHITE, edge=GRAY_L, shape=MSO_SHAPE.RECTANGLE)
txt(s, "INSTRUCTOR: fill these three in from Lecture 2's exit tickets before class.",
    M + Inches(1.15), Inches(2.42), Inches(10.6), Inches(0.4), 17, GRAY_L,
    italic=True)
box(s, M, Inches(5.7), CONTENT_W, Inches(0.85),
    "Refer to concepts, never to students. Ninety seconds total, then move on.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 00:01–00:02. TEMPLATE SLIDE — fill it in before class.

Twenty-five seconds each, no more. Name the concept, never the student.

Two answers are worth preparing in advance because they recur: "typ versus max"
and "why bandwidth appears in a noise calculation at all". Both come back today,
the second one at minute 56, so if they are on the list say "we settle that
properly in an hour" and move.

If Lecture 2's tickets showed the ODR-is-not-bandwidth confusion, do NOT fix it
here. It is today's Poll 3 and you want the misconception alive at minute 44.

If you received no useful tickets, delete this slide rather than improvising.
""")


# ───────────────────────────────────────────────────────── 3  retrieval
s = S()
heading(s, "Where are we today?",
        "Retrieval: the chain from Lecture 1 — today we live in boxes 5, 6 and 7")
chain(s, Inches(2.5), upto=7, highlight=(5, 6, 7))
box(s, M, Inches(6.12), CONTENT_W, Inches(0.62),
    "Stages 1–4 hand you a conditioned signal. Everything after that is arithmetic "
    "on numbers — and three of its errors cannot be undone.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 00:02–00:05. RETRIEVAL PRACTICE, not review. Ask before you show.

"Sheets down. Name the seven stages, in order." One student per stage, take them
from the room. It costs ninety seconds and beats re-explaining the diagram.

Then narrow: "Lecture 2 lived in box 3 — choosing the device. Today we live in
five, six and seven: sampling, codes to units, and the timestamp. That is the
part everyone assumes is bookkeeping."

If the room is slow on stages 5–7, that is your diagnostic for the whole hour:
slow down at minutes 34–50 and protect Poll 3 by cutting slide 35 later.
""")


# ───────────────────────────────────────────────────────── 4  hook: one log file
s = S()
heading(s, "One log file", "Ten minutes of data. 60 000 rows. No gaps, no outliers, "
        "plausible magnitudes.")
box(s, M, Inches(1.92), CONTENT_W, Inches(0.60),
    "ISM330DHCX  ·  ±2 g  ·  16-bit  ·  ODR = 104 Hz  ·  0.061 mg/LSB  ·  "
    "HAL_Delay(10) polling loop  ·  10 minutes",
    fill=WHITE, edge=GRAY, tcolor=INK, size=16, bold=True, font=MONO)
cw, cgap = Inches(3.76), Inches(0.30)
num_card(s, M, Inches(2.72), cw, "12.4",
         "bits of sixteen that carry information",
         "You bought a 16-bit number.\nYou own rather less than that.", TEAL)
num_card(s, M + cw + cgap, Inches(2.72), cw, "12 Hz",
         "a signal in your data that does not exist in the world",
         "It is not noise. It is a tone,\nand it looks entirely real.", RED)
num_card(s, M + 2 * (cw + cgap), Inches(2.72), cw, "12.1 s",
         "how wrong your timestamps are by the end",
         "Every event in the last part of\nthe log is stamped too early.", RED)
box(s, M, Inches(5.62), CONTENT_W, Inches(0.95),
    "Every one of these three was computable before a line of firmware was written.\n"
    "Two of the three cannot be repaired afterwards at any price.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=19, bold=True)
D.notes(s, """
TIMING: 00:05–00:07. This is the hook. Deliver it flat, like a fact.

Read the configuration line aloud, then: "This file is perfect. Monotonic
timestamps, no gaps, no outliers, magnitudes that look like an accelerometer on
a bench. And three numbers in it are lies."

Point at each card in turn and name it — twelve point four, twelve hertz, twelve
point one seconds — but do NOT explain any of them yet. Each one is a chunk of
the lecture.

Then the sentence that carries the eighty minutes: "Acquisition does not fail
loudly. It fails by handing you a file full of plausible numbers." Straight into
the poll — before anyone has time to get comfortable.
""")


# ───────────────────────────────────────────────────────── 5  poll 1 baseline
q1 = ("Your accelerometer is 16-bit, configured for ±2 g, so its datasheet "
      "resolution is 0.061 mg/LSB. You configure ODR = 104 Hz and log the output.\n"
      "What is the smallest change in acceleration your log can actually distinguish?")
opts1 = [("A", "0.061 mg — that is what the datasheet says"),
         ("B", "0.018 mg — the quantisation noise, LSB/√12"),
         ("C", "0.72 mg"),
         ("D", "It cannot be determined from what you have been told")]
s = poll(D, 1, q1, opts1, minute=7)
poll_note(s, "Commit to one. The answer is withheld until the end of the lecture — "
             "and by then you will have computed it yourselves.")
D.notes(s, """
TIMING: 00:07–00:11. Baseline. DO NOT REVEAL — the answer lands at minute 66.

Hands on a count, all at once. Expect 55–70 % on A: that is misconception M1 and
it is the reason this lecture exists. Expect 5–15 % on D, which is the only
defensible vote right now — you have not given them a noise density.

WRITE THE DISTRIBUTION ON THE BOARD and leave it there all hour. You re-show it
at minute 66 and the shift is your evidence the lecture worked.

If someone picks B, praise it and then use it: "you found the term that does not
matter — which one does?" If someone picks C, ask HOW; if they cannot say, it
was a guess, and say so kindly.

Then set the agenda and move. Do not argue with A now.
""")


# ───────────────────────────────────────────────────────── 6  the anchor number
s = S()
heading(s, "The number everyone trusts", "Where 0.061 mg/LSB comes from")
rich(s, M, Inches(2.30), CONTENT_W, Inches(1.0),
     [[("4000 mg  ÷  65 536 codes  =  ", {"size": 26, "font": MONO}),
       ("0.061 mg / LSB", {"size": 32, "font": MONO, "bold": True, "color": TEAL})]],
     align=PP_ALIGN.CENTER)
box(s, M, Inches(3.55), CONTENT_W, Inches(1.0),
    "One count of the register is 0.061 mg. That much is simply true.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=26, bold=True)
txt(s, "±2 g is 4000 mg of span. Sixteen bits is 65 536 codes. Divide one by the "
       "other and you get the size of one step of the number — which is exactly "
       "what the datasheet prints, on the same page as everything else we will use "
       "today.",
    M, Inches(4.95), CONTENT_W, Inches(1.2), 20, INK, line=1.4)
D.notes(s, """
TIMING: 00:11–00:13. Derive it live; it takes twenty seconds and models the habit.

"Full scale is plus or minus two g, so four thousand milli-g of span. Sixteen
bits is sixty-five thousand five hundred and thirty-six codes. Four thousand
over sixty-five five three six is zero point zero six one."

Then hold the line: "Notice I have not lied to you and neither has ST. This
number is correct. It is the size of one step of the number." Pause there — the
next slide is where the trouble is, and the pause is what makes it land.

If a student asks whether it should be 65 535, say yes, that convention exists,
and it changes nothing at the fourth decimal place. Do not spend two minutes on it.
""")


# ───────────────────────────────────────────────────────── 7  what it is not
s = S()
heading(s, "…and three things it is not", rule=RED)
nots = [("It is not the smallest change you can distinguish.",
         "That is set by the noise — and the noise depends on a bandwidth nobody has "
         "chosen yet."),
        ("It is not an accuracy.",
         "Offset, scale error and drift are separate numbers on separate rows. "
         "Lecture 2 spent an hour on them."),
        ("It is not a property of the sensor alone.",
         "Change the full scale and it moves. Change the bandwidth and the "
         "measurement changes while it stays put.")]
y = Inches(2.20)
for k, v in nots:
    box(s, M, y, Inches(0.42), Inches(0.42), "", fill=RED, edge=RED,
        shape=MSO_SHAPE.RECTANGLE)
    txt(s, k, M + Inches(0.70), y - Inches(0.04), Inches(11.1), Inches(0.45), 22,
        INK, bold=True)
    txt(s, v, M + Inches(0.70), y + Inches(0.46), Inches(11.1), Inches(0.6), 17,
        GRAY, line=1.3)
    y += Inches(1.20)
box(s, M, Inches(5.90), CONTENT_W, Inches(0.95),
    "ON THE BOARD, NOW, AND NOT ERASED:\n"
    "you bought 16 bits — how many of them do you own?",
    fill=DARK, edge=AMBER, tcolor=CREAM, size=22, bold=True, edge_w=3)
D.notes(s, """
TIMING: 00:13–00:14. WRITE THE BOARD LINE NOW and leave it up all hour.

Board work item 1 from the plan is `0.061 mg/LSB · noise 0.72 mg · 11.8 LSB ·
3.6 bits`. Write ONLY the first term and the question now. Writing 0.72 mg on
the board at minute 14 hands the class Poll 1's withheld answer, which the
activity sheet explicitly forbids. Complete the line at minute 56–60, term by
term, as the class derives each one. Same board, same place, finished in public.

Say the three "is not" lines quickly — thirty seconds total. They are a frame,
not content. The one to stress is the first: "the smallest step of the number
and the smallest change you can see are two different quantities, and today they
differ by a factor of twelve."
""")


# ───────────────────────────────────────────────────────── 8  section C1
s = section(D, "chunk 1", "The output and\nthe reference",
            ["What actually comes out of a sensor — and what the converter "
             "compares it against.",
             "One wire's difference between a measurement that survives a sagging "
             "rail and one that does not."])
D.notes(s, """
TIMING: 00:14–00:15. Section marker, fifteen seconds. Do not read the sub-lines.

Say only: "Before we can talk about samples, two pieces of vocabulary — what
comes out of a sensor, and what the converter measures it against. The second
one decides whether an entire class of measurement works, and it is free."

This chunk is the one to compress if the muddiest points overran: slides 9 and
10 are vocabulary and can be delivered in three minutes between you, but do NOT
compress slide 11 or the poll. The ratiometric result is the only thing in
chunk 1 that students consistently get wrong on the midterm, and it is also the
only place in the course where a measurement problem is solved by moving one
wire rather than by buying a better part.
""")


# ───────────────────────────────────────────────────────── 9  analog and digital
s = S()
heading(s, "What comes out of a sensor",
        "Three analog forms — and one where the conversion already happened, "
        "where you cannot see it")
forms = [("VOLTAGE", GRAY,
          "Tens of µV per °C from a thermocouple; a few mV from a bridge.\n"
          "Small enough that the wire is part of the measurement."),
         ("CURRENT  ·  4–20 mA", GRAY,
          "Unchanged by cable resistance, so distance does not matter.\n"
          "4 mA is a live zero: a broken wire reads 0 mA, and is detectable."),
         ("BRIDGE", GRAY,
          "Four elements in a diamond, excited by a voltage; the output follows "
          "the imbalance.\nStrain gauges, pressure sensors, load cells."),
         ("DIGITAL  ·  I²C / SPI", TEAL,
          "The ADC is inside the package. You receive a number, not a voltage.\n"
          "Almost every MEMS sensor here — and today's case.")]
x = M
for name, col, body in forms:
    box(s, x, Inches(2.10), Inches(2.85), Inches(0.62), name, fill=col, edge=col,
        tcolor=CREAM, size=15, bold=True)
    txt(s, body, x + Inches(0.10), Inches(2.88), Inches(2.65), Inches(1.9), 14,
        INK, line=1.35)
    x += Inches(3.02)
box(s, M, Inches(4.90), CONTENT_W, Inches(0.56),
    "VOCABULARY ONLY TODAY:   instrumentation amplifier   ·   common-mode range   ·"
    "   grounding and shielding   →   Lecture 12 in full",
    fill=GROUND, edge=GRAY, tcolor=GRAY, size=14.5, bold=True)
box(s, M, Inches(5.58), CONTENT_W, Inches(1.05),
    "A digital output does not remove the analog problems — it moves them inside "
    "the package, where you can neither see nor change them.\nAnd it adds two of "
    "its own: the byte order of the result, and when the conversion happened.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 00:15–00:18. Reference slide — do not read all four columns aloud.

Spend your time on two things. The 4–20 mA live zero: "the zero of the scale is
four milliamps, so a broken wire reads zero and is distinguishable from a
genuine zero. That is designed-in fault detection, and it is why a convention
from the 1950s has outlived the technology that prompted it." It comes back in
Poll 4.

Then the amber box, which is the actual content of the slide. Ask the room:
"Does a digital output make life easier?" Take the yes, then complicate it. The
two new problems it names are chunk 3 of this lecture.

Instrumentation amplifiers get one line and a forward reference. Resist.
""")


# ───────────────────────────────────────────────────────── 10  the reference
s = S()
heading(s, "What an ADC actually measures", "Not a voltage — a ratio")
rich(s, M, Inches(2.22), CONTENT_W, Inches(0.9),
     [[("count  =  ", {"size": 27, "font": MONO}),
       ("V_in / V_ref", {"size": 30, "font": MONO, "bold": True, "color": TEAL}),
       ("  ×  2^N", {"size": 27, "font": MONO, "bold": True})]],
     align=PP_ALIGN.CENTER)
box(s, M, Inches(3.28), CONTENT_W, Inches(0.95),
    "An ADC has no idea what a volt is.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=28, bold=True)
bullet(s, Inches(4.50), "It is a ratio, not a voltage.",
       "The count depends on the input compared with the reference. Read the "
       "formula again for what it says.", TEAL)
bullet(s, Inches(5.30), "Every V_ref error is a gain error.",
       "Not on one reading — on every reading, in the same direction, for as long "
       "as the reference is wrong.", AMBER)
box(s, M, Inches(6.12), CONTENT_W, Inches(0.62),
    "The rule: excite the sensor and reference the converter from the same thing, "
    "or from two things that are both stable.",
    fill=GROUND, edge=GRAY, size=17.5, bold=True)
D.notes(s, """
TIMING: 00:18–00:20. Put the formula on the board as well as the screen.

Read it out with the emphasis in the right place: "count equals V-in OVER V-ref,
times two to the N. The input alone appears nowhere in that expression."

Then the line, deadpan: "An ADC has no idea what a volt is. It is a ratio meter
with a reputation." Let that sit.

The bottom rule is the one to memorise, and the next slide is the two cases it
covers. Say explicitly that mixing one stable thing with one unstable thing is
the only combination that fails — and that it is the one that looks most
sophisticated on a schematic, which is why it gets built.
""")


# ───────────────────────────────────────────────────────── 11  ratiometric
s = S()
heading(s, "Two wirings, one sagging rail",
        "A 3.3 V rail sags to 3.2 V under load. Representative bridge figures, "
        "not a named product.")
pw = Inches(5.85)
iy = panel(s, M, Inches(2.05), pw, Inches(3.60),
           "RATIOMETRIC  —  bridge and ADC reference from the SAME rail", TEAL)
txt(s, "bridge output      ↓ 3 %\nADC counts         ↑ 3 %\n"
       "─────────────────────────\nreported strain    0 % error",
    M + Inches(0.22), iy, pw - Inches(0.44), Inches(1.25), 16, INK, font=MONO,
    line=1.45)
txt(s, "The code computes a ratio, and both terms moved together, so the ratio "
       "never changed. This is free — if you wired it deliberately.",
    M + Inches(0.22), iy + Inches(1.45), pw - Inches(0.44), Inches(1.1), 16,
    GRAY, line=1.32)
x2 = M + Inches(6.05)
iy = panel(s, x2, Inches(2.05), pw, Inches(3.60),
           "ABSOLUTE  —  precision 2.5 V reference, bridge still on the rail", RED)
txt(s, "bridge output      ↓ 3 %\nADC counts         unchanged\n"
       "─────────────────────────\nreported strain    3 % LOW",
    x2 + Inches(0.22), iy, pw - Inches(0.44), Inches(1.25), 16, INK, font=MONO,
    line=1.45)
txt(s, "Nothing cancels. And it is not a constant — it varies with whatever else "
       "the board is doing, so no calibration removes it.",
    x2 + Inches(0.22), iy + Inches(1.45), pw - Inches(0.44), Inches(1.1), 16,
    GRAY, line=1.32)
box(s, M, Inches(5.92), CONTENT_W, Inches(0.78),
    "Same components. Same cost. One wire's difference.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=24, bold=True)
D.notes(s, """
TIMING: 00:20–00:23. Draw both on the board while you talk; it is four lines.

Left panel first, slowly, because it is counter-intuitive: "the bridge output
falls by three per cent because its excitation fell. The counts rise by three
per cent because the reference fell. The quantity the code computes was a ratio
all along, so the two cancel exactly."

Then the right panel: "now give the ADC a precision reference and leave the
bridge on the rail. Same parts, same price. The sag no longer cancels."

DO NOT say which one the poll is about. Go straight into the vote — the whole
value of Poll 2 is that the room disagrees about the sign of an error that does
not exist.
""")


# ───────────────────────────────────────────────────────── 12  poll 2
q2 = ("A strain-gauge bridge is excited from the microcontroller's 3.3 V rail. The "
      "ADC that reads it uses the same 3.3 V rail as its reference. Under load, the "
      "rail sags to 3.2 V.\nThe reported strain:")
opts2 = [("A", "reads about 3 % high"),
         ("B", "reads about 3 % low"),
         ("C", "does not change"),
         ("D", "changes by an amount that depends on the gauge factor")]
s = poll(D, 2, q2, opts2, minute=23)
poll_note(s, "Vote alone first. Then find someone who voted differently and make "
             "them defend it.")
D.notes(s, """
TIMING: 00:23–00:25. Silent vote on a count, then ninety seconds of argument.

A and B will take the majority and split roughly evenly — that is what makes
this a good vote. The room is disagreeing about the SIGN of an error that is not
there. Say that out loud after the revote, not before.

Do not referee the discussion. Walk, listen for the phrase "but the reference
moved too", and if you hear it, ask that pair to say it to the room.

D is the student conflating sensitivity with reference error. It is a useful
answer: the gauge factor sets millivolts per microstrain and cancels out of the
ratio entirely.

Target 30–45 % correct after peer discussion. Record both numbers.
""")


# ───────────────────────────────────────────────────────── 13  poll 2 answer
s = poll(D, 2, q2, opts2, minute=23, correct="C", reveal=True)
poll_note(s, "The bridge output is proportional to its excitation; the counts are "
             "proportional to 1/reference. Both scale with the same rail, so the "
             "ratio the code computes never moved.", TEAL)
D.notes(s, """
TIMING: 00:25–00:26. Reveal, then the follow-up that makes it stick — ask it
immediately, hands only:

"Now the same bridge, but the ADC reference is a precision 2.5 V part and the
bridge still runs from the rail. What happens?"

Three per cent error, straight through, uncalibratable, because the two no
longer track. Same hardware cost. One wire's difference.

Then name the misconception you just caught (M6): a ratiometric error cannot be
calibrated out, because either it cancels by construction or it does not cancel
at all. There is no middle case where calibration helps.

Ninety seconds. Then quantisation.
""")


# ───────────────────────────────────────────────────────── 14  quantisation
s = S()
heading(s, "Quantisation",
        "The converter has a finite number of codes, so it must round")
rich(s, M, Inches(2.18), CONTENT_W, Inches(0.8),
     [[("LSB  =  full scale / 2^N  =  4000 mg / 65 536  =  ", {"size": 22, "font": MONO}),
       ("0.061 mg", {"size": 26, "font": MONO, "bold": True, "color": TEAL})]],
     align=PP_ALIGN.CENTER)
gx, gy, gw, amp = M + Inches(0.45), Inches(5.30), Inches(6.5), Inches(1.90)
axis(s, gx, gy, gw + Inches(0.35), GRAY_L)
curve(s, [(Emu(int(gx)), Emu(int(gy))),
          (Emu(int(gx + gw)), Emu(int(gy - amp)))], TEAL, 2.0)
steps, pts = 8, []
for i in range(steps):
    xa, xb = gx + gw * i / steps, gx + gw * (i + 1) / steps
    yv = gy - amp * i / steps
    pts += [(Emu(int(xa)), Emu(int(yv))), (Emu(int(xb)), Emu(int(yv)))]
    if i < steps - 1:
        pts.append((Emu(int(xb)), Emu(int(gy - amp * (i + 1) / steps))))
curve(s, pts, AMBER, 2.5)
txt(s, "the true value", gx + Inches(3.9), Inches(3.05), Inches(2.4), Inches(0.3),
    14, TEAL, bold=True, font=MONO)
txt(s, "what the code says", gx + Inches(0.05), gy + Inches(0.14), Inches(2.6),
    Inches(0.3), 14, AMBER, bold=True, font=MONO)
txt(s, "input  →", gx + gw - Inches(1.2), gy + Inches(0.14), Inches(1.5),
    Inches(0.3), 13, GRAY, font=MONO, align=PP_ALIGN.RIGHT)
tx = M + Inches(7.55)
txt(s, "Between two codes there is nothing.",
    tx, Inches(3.15), Inches(4.4), Inches(0.5), 20, INK, bold=True, line=1.25)
txt(s, "The converter reports the nearest step and throws the difference away. "
       "The error is uniformly distributed over one LSB, and it is there in every "
       "single sample.\n\n"
       "It is also the only error in this lecture that is perfectly predictable "
       "before you switch anything on.",
    tx, Inches(4.05), Inches(4.4), Inches(2.0), 16, GRAY, line=1.35)
D.notes(s, """
TIMING: 00:26–00:28. Trace the staircase with your hand while you talk.

"Here is the true value, rising smoothly. Here is what the code says — the
nearest step. The vertical gap between them is the quantisation error, and
notice that it never goes away: it is present in every sample, forever."

Ask: "What is the biggest that gap can be?" Half an LSB. "And on average?" That
is the next slide, and it is one line of arithmetic.

Keep this short. Quantisation is the error students expect to be important, and
the point of chunk 1 is to price it honestly so that chunk 3 can dismiss it with
evidence rather than assertion.
""")


# ───────────────────────────────────────────────────────── 15  quantisation noise
s = S()
heading(s, "The quantisation noise", "Rounding injects a known, computable amount of it")
rich(s, M, Inches(2.25), CONTENT_W, Inches(0.9),
     [[("σ_q  =  LSB / √12  =  0.061 / 3.464  =  ", {"size": 25, "font": MONO}),
       ("0.018 mg", {"size": 30, "font": MONO, "bold": True, "color": TEAL})]],
     align=PP_ALIGN.CENTER)
txt(s, "√12 is the standard deviation of a uniform distribution of unit width. "
       "Worth knowing where it comes from once; not worth deriving twice.",
    M, Inches(3.35), CONTENT_W, Inches(0.6), 18, GRAY, line=1.35)
box(s, M, Inches(4.15), CONTENT_W, Inches(0.95),
    "Note what this is NOT: it is the resolution of the number, not the resolution "
    "of the measurement.",
    fill=RED_L, edge=RED, size=21, bold=True)
box(s, M, Inches(5.40), CONTENT_W, Inches(1.10),
    "Hold on to 0.018 mg.\nLater we put it beside the sensor's own noise — "
    "and one of those two terms decides nothing at all.",
    fill=AMBER_L, edge=AMBER, size=20, bold=True)
D.notes(s, """
TIMING: 00:28–00:30. One line of arithmetic, then two warnings.

Do the division on the board: 0.061 over 3.464. Eighteen microg. Say the units
out loud — unit cancellation, not the statistics, is what actually blocks
students in this area.

If someone asks where √12 comes from: it is the standard deviation of a uniform
distribution one LSB wide. Offer the derivation at the end of class, not now.

The amber box is a deliberate cliff-hanger and it protects Poll 1. Do NOT say
"forty times smaller" yet, and do not say 0.72 mg — that is the withheld answer
and you give it away with one careless comparison. "One of those two terms
decides nothing" is as far as you go.
""")


# ───────────────────────────────────────────────────────── 16  more bits
s = S()
heading(s, "Why more bits is not more truth", rule=RED)
txt(s, "the noise floor of the measurement  —  identical in both",
    M, Inches(2.30), CONTENT_W, Inches(0.35), 16, AMBER, bold=True,
    align=PP_ALIGN.CENTER)
for bx, nlines, name, sub in ((M + Inches(0.30), 6, "16-BIT CONVERTER",
                               "one step = 0.061 mg"),
                              (M + Inches(6.20), 24, "20-BIT CONVERTER",
                               "one step = sixteen times finer")):
    bw2, by2, bh2 = Inches(5.35), Inches(2.75), Inches(1.75)
    box(s, bx, by2, bw2, bh2, "", fill=AMBER_L, edge=AMBER,
        shape=MSO_SHAPE.RECTANGLE)
    for i in range(1, nlines):
        axis(s, bx, by2 + Emu(int(bh2 * i / nlines)), bw2, TEAL, 0.75)
    txt(s, name, bx, by2 + bh2 + Inches(0.14), bw2, Inches(0.3), 16, INK,
        bold=True, align=PP_ALIGN.CENTER)
    txt(s, sub, bx, by2 + bh2 + Inches(0.46), bw2, Inches(0.3), 15, TEAL,
        font=MONO, align=PP_ALIGN.CENTER)
box(s, M, Inches(5.30), CONTENT_W, Inches(1.0),
    "Adding bits divides the step. It does not divide the noise.\n"
    "Bits below the noise floor are extra digits, not extra information.",
    fill=RED_L, edge=RED, size=21, bold=True)
txt(s, "Whether the last bits buy you anything depends on a number that is not on "
       "the front page — the noise density — and on a choice that is entirely "
       "yours: the bandwidth.",
    M, Inches(6.45), CONTENT_W, Inches(0.5), 17, GRAY, italic=True)
D.notes(s, """
TIMING: 00:30–00:32. The picture does the work; say four sentences over it.

"Same measurement, same noise floor — the amber band. On the left, sixteen bits:
the teal lines are the code steps. On the right, twenty bits: four more bits,
sixteen times finer steps, and precisely the same amount of information."

Then the callback, because it is the connective tissue of Module A: "Lecture 2
called this reading the headline. Same trap, new quantity."

Ask the room to predict, not to recall: "so what would you need to know to say
how many of the sixteen are worth having?" You want two words back — noise, and
bandwidth. If you get them, chunk 3 is already half taught.

Then stand them up.
""")


# ───────────────────────────────────────────────────────── 17  state change
s = S(bg=DARK)
eyebrow(s, "stand up  ·  60 seconds  ·  no talking", AMBER)
txt(s, "Draw the last three boxes\nof the chain from memory", M, Inches(1.75),
    Inches(11.5), Inches(1.9), 40, CREAM, bold=True, line=1.15)
txt(s, "Under each one, write the single thing that can be lost there.",
    M, Inches(3.95), Inches(11.5), Inches(0.5), 24, RGBColor(0xB8, 0xC0, 0xC6))
box(s, M, Inches(5.05), CONTENT_W, Inches(0.95),
    "SAMPLING          →          CODES TO UNITS          →          TIMESTAMP",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=22, bold=True)
txt(s, "Turn your paper over first. Nothing to hand in.",
    M, Inches(6.25), Inches(11.5), Inches(0.4), 17, GRAY, italic=True)
D.notes(s, """
TIMING: 00:32–00:34. A real state change: everyone on their feet, paper turned
over, sixty seconds, silence. This is the deliberate attention reset before the
hardest chunk of the lecture, and standing is the part that does the work.

Do not collect these. Walk two rows and look at three sheets so students know
they are seen — that is the whole enforcement mechanism.

Then take two answers aloud, thirty seconds: sampling loses frequencies above
Nyquist; codes to units loses the sign and the scale factor; the timestamp loses
when it happened. Say them back in those words, because those three sentences
are chunks 2 and 3.

THIS IS A DESIGNATED CUT if you are five minutes late. Cut it and slide 35.
""")


# ───────────────────────────────────────────────────────── 18  section C2
s = section(D, "chunk 2", "Output data rate\nis not bandwidth",
            ["The hardest idea in Module A.",
             "One register bit decides whether your data contains a signal that "
             "never existed."])
D.notes(s, """
TIMING: 00:34–00:35. Section marker. Fifteen seconds, and say it as a warning.

"This is the part of the course that costs people afternoons. If anything today
is going to be on the midterm in a form you did not expect, it is the next
twenty minutes."

Then straight into Nyquist — but as a design rule, not as a theorem. The framing
matters: Lecture 1 met aliasing as a mystery to be solved. Here it is a bit in a
register that ships at zero.
""")


# ───────────────────────────────────────────────────────── 19  nyquist
s = S()
heading(s, "Nyquist, as a design rule",
        "Lecture 1 met this as a discovery. Today it is a register setting.")
gx, gy, gw = M + Inches(0.15), Inches(3.95), Inches(8.1)
axis(s, gx, gy, gw, GRAY_L)
curve(s, sine(gx, gy, gw, Inches(0.95), 19), TEAL, 1.25)
txt(s, "the real signal  ·  19 cycles", gx, Inches(2.62), Inches(5), Inches(0.3),
    14, TEAL, bold=True, font=MONO)
for i in range(21):
    frac = i / 20.0
    dot(s, Emu(int(gx + gw * frac)),
        Emu(int(gy - Inches(0.95) * math.sin(2 * math.pi * 19 * frac))), color=RED)
curve(s, sine(gx, gy, gw, Inches(0.95), 1, phase=math.pi), RED, 3.0,
      dash=MSO_LINE_DASH_STYLE.DASH)
txt(s, "what the samples reconstruct  ·  1 cycle", gx, Inches(5.10), Inches(6),
    Inches(0.3), 14, RED, bold=True, font=MONO)
tx = M + Inches(8.70)
box(s, tx, Inches(2.35), Inches(3.20), Inches(0.75), "f_s  >  2 × f_max",
    fill=WHITE, edge=TEAL, tcolor=INK, size=20, bold=True, font=MONO, edge_w=2.5)
txt(s, "The theorem is not the design rule.\n\nThe design rule is its "
       "contrapositive: you must guarantee that nothing above f_max ever reaches "
       "the sampler.\n\nThat is a filter. It is not a sample rate.",
    tx, Inches(3.30), Inches(3.20), Inches(2.4), 15.5, INK, line=1.35)
box(s, M, Inches(6.05), CONTENT_W, Inches(0.62),
    "The samples are entirely correct. Their interpretation is not.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=20, bold=True)
D.notes(s, """
TIMING: 00:35–00:37. They saw this figure in Lecture 1. Use it as retrieval, not
as new material — ask before you explain.

"Somebody tell me what the red dots are." Then: "and the dashed line?" Ninety
seconds, from the room.

The one sentence to add today is the box on the right. Say it twice: "the
theorem tells you when reconstruction is possible. The design rule is the
contrapositive — you must guarantee nothing above your f-max reaches the
sampler. That guarantee is a component, not a configuration."

If the room reconstructs the figure quickly, go faster here; you will want the
time at minute 44.
""")


# ───────────────────────────────────────────────────────── 20  the folding rule
s = S()
heading(s, "Where a tone lands after sampling",
        "N is whichever integer multiple of the sample rate lies nearest to it")
box(s, M + Inches(2.9), Inches(2.10), Inches(6.1), Inches(0.85),
    "f_alias  =  | f  −  N × f_s |", fill=WHITE, edge=TEAL, tcolor=INK,
    size=26, bold=True, font=MONO, edge_w=2.5)
box(s, M + Inches(1.4), Inches(3.15), Inches(9.1), Inches(0.72),
    "Lecture 1's bearing tone, at today's ODR:   | 1520 − 15 × 104 |  =  "
    "| 1520 − 1560 |  =  40 Hz",
    fill=GROUND, edge=GRAY, tcolor=INK, size=18, bold=True, font=MONO)
x0, lw, ly = M + Inches(0.30), Inches(11.0), Inches(5.15)
box(s, Inches(1.295), Inches(4.42), Inches(10.17), Inches(0.26), "",
    fill=RED, edge=RED, shape=MSO_SHAPE.LEFT_ARROW)
txt(s, "folds back into the band you are keeping", Inches(3.0), Inches(4.10),
    Inches(6.5), Inches(0.3), 14, RED, bold=True, font=MONO,
    align=PP_ALIGN.CENTER)
axis(s, x0, ly, lw, GRAY)
box(s, x0, ly - Inches(0.13), Inches(0.357), Inches(0.26), "", fill=TEAL,
    edge=TEAL, shape=MSO_SHAPE.RECTANGLE)
dot(s, Emu(int(Inches(11.47))), Emu(int(ly)), r=Inches(0.075), color=RED)
txt(s, "0", x0 - Inches(0.1), ly + Inches(0.16), Inches(0.4), Inches(0.3), 13,
    GRAY, font=MONO)
txt(s, "52 Hz — the band you believe you are measuring", x0 + Inches(0.50),
    ly + Inches(0.16), Inches(5.0), Inches(0.3), 14, TEAL, bold=True, font=MONO)
txt(s, "1520 Hz", Inches(10.6), ly + Inches(0.16), Inches(1.6), Inches(0.3), 14,
    RED, bold=True, font=MONO)
box(s, M, Inches(6.05), CONTENT_W, Inches(0.62),
    "The sample rate alone tells you nothing about what is in your data.",
    fill=AMBER_L, edge=AMBER, size=19, bold=True)
D.notes(s, """
TIMING: 00:37–00:40. Do the arithmetic on the board, not from the slide.

"Fifteen times a hundred and four is one thousand five hundred and sixty. One
thousand five hundred and twenty minus that is minus forty. Take the modulus.
Forty hertz." Make them do the multiplication with you.

Then point at the number line: "the teal sliver is the whole band you told your
report you were measuring. Everything to the right of it still arrives at the
sampler, and everything to the right of it lands somewhere inside the sliver."

Do NOT do the 300 Hz case here — that is Poll 3 in four minutes and it is the
hardest vote of the lecture. If a student volunteers it, thank them, write the
number on a corner of the board face-down, and say "hold that".
""")


# ───────────────────────────────────────────────────────── 21  filter first
s = S()
heading(s, "The one ordering that cannot be repaired", rule=RED)
txt(s, "CORRECT  —  the filter sits before the sampler", M, Inches(2.02),
    Inches(8), Inches(0.3), 15, TEAL, bold=True)
pipeline(s, Inches(2.42),
         ["ANALOG\nSIGNAL", "ANTI-ALIAS\nFILTER", "SAMPLER\n/ ADC",
          "DIGITAL FILTER\n(optional)"], TEAL)
txt(s, "Out-of-band energy is removed while it is still separable from the signal. "
       "Everything downstream is then a choice, not a repair.",
    M, Inches(3.38), CONTENT_W, Inches(0.4), 16, GRAY)
txt(s, "WRONG  —  “we will filter it in software afterwards”", M, Inches(4.02),
    Inches(8), Inches(0.3), 15, RED, bold=True)
pipeline(s, Inches(4.42),
         ["ANALOG\nSIGNAL", "SAMPLER\n/ ADC", "DIGITAL FILTER\n(too late)",
          "300 Hz IS NOW\n12 Hz, FOREVER"], RED, last_col=RED)
txt(s, "By the time the data exists, a 300 Hz component and a genuine 12 Hz "
       "component are the same sequence of numbers. Not similar — identical. "
       "Nothing separates two things that are the same.",
    M, Inches(5.36), CONTENT_W, Inches(0.8), 16, GRAY, line=1.3)
box(s, M, Inches(6.28), CONTENT_W, Inches(0.60),
    "Everything else in the chain — a wrong gain, a missed sign, a unit muddle — "
    "can be fixed on a laptop a week later. This one cannot.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=18, bold=True)
D.notes(s, """
TIMING: 00:40–00:42. THE SLIDE THE LECTURE IS BUILT AROUND. Slow down.

Walk the teal row left to right, then the red row, and stop on the last red box.

The argument is arithmetic, not engineering, and you must say it that way:
"these are not two similar signals that a clever algorithm might tease apart.
They are the same numbers. There is nothing to separate."

Then the claim that makes it matter, and it is worth writing on the board: this
is the ONLY ordering constraint in the whole measurement chain with that
property. Invite counter-examples — a student who tries and fails to find one
has learned it better than one who was told.

This refutes M3, and M3 comes back on the exit ticket. Plant it deliberately.
""")


# ───────────────────────────────────────────────────────── 22  the register bit
s = S()
heading(s, "The bit that decides it",
        "ISM330DHCX  ·  CTRL1_XL (0x10)  ·  reset value 0x00")
cellw, cx0, cy0 = Inches(1.40), M + Inches(0.35), Inches(2.30)
fields = [("7", "ODR_XL3", TEAL), ("6", "ODR_XL2", TEAL), ("5", "ODR_XL1", TEAL),
          ("4", "ODR_XL0", TEAL), ("3", "FS1_XL", TEAL), ("2", "FS0_XL", TEAL),
          ("1", "LPF2_XL_EN", RED), ("0", "0", GRAY)]
for i, (bit, name, col) in enumerate(fields):
    xx = cx0 + i * cellw
    txt(s, "bit " + bit, xx, cy0 - Inches(0.30), cellw, Inches(0.28), 12, GRAY,
        font=MONO, align=PP_ALIGN.CENTER)
    box(s, xx, cy0, cellw, Inches(0.80), name,
        fill=RED_L if col == RED else WHITE, edge=col, tcolor=INK,
        size=11.5 if len(name) > 7 else 13, bold=True, font=MONO,
        shape=MSO_SHAPE.RECTANGLE, edge_w=2.5 if col == RED else 1.25)
txt(s, "output data rate  ·  0100 = 104 Hz", cx0, cy0 + Inches(0.90),
    cellw * 4, Inches(0.3), 13, TEAL, bold=True, align=PP_ALIGN.CENTER)
txt(s, "full scale", cx0 + cellw * 4, cy0 + Inches(0.90), cellw * 2, Inches(0.3),
    13, TEAL, bold=True, align=PP_ALIGN.CENTER)
txt(s, "the filter", cx0 + cellw * 6, cy0 + Inches(0.90), cellw, Inches(0.3), 13,
    RED, bold=True, align=PP_ALIGN.CENTER)
box(s, M, Inches(3.70), CONTENT_W, Inches(0.82),
    "LPF2_XL_EN = 0 after reset.  Your part ships with no anti-alias filter.",
    fill=RED, edge=RED, tcolor=CREAM, size=23, bold=True)
txt(s, "So the natural sequence of events is this. You set ODR = 104 Hz. You "
       "reason, correctly, that the Nyquist limit is 52 Hz. You write “52 Hz "
       "measurement bandwidth” in the report.\n"
       "Meanwhile the device is sampling a far wider analog band with no filter "
       "at all, and everything above 52 Hz folds back into your data.",
    M, Inches(4.62), CONTENT_W, Inches(1.35), 16.5, INK, line=1.35)
box(s, M, Inches(6.22), CONTENT_W, Inches(0.60),
    "0x40 gives ±2 g at 104 Hz — and leaves bit 1 clear. In Laboratory 2 you set "
    "it yourself.",
    fill=TEAL_L, edge=TEAL, size=17, bold=True)
D.notes(s, """
TIMING: 00:42–00:44. This is the slide that turns Lecture 1's story into today's
engineering. Say that transition explicitly.

"In week one, aliasing was something that happened to somebody else's motor.
Here is the difference between a lecture and a laboratory: a bit, at address
0x10, position one, and it is zero when the part powers up."

Have them find it in the datasheet — Table 41, sixty seconds, pairs. Then read
the paragraph in the middle of the slide out loud, slowly, in the second person.
Every step of it is correct except the conclusion, and that is what makes it a
trap worth teaching.

Do not resolve it. Vote immediately — the class now has everything Poll 3 needs.
""")


# ───────────────────────────────────────────────────────── 23  poll 3
q3 = ("You configure the accelerometer for ODR = 104 Hz and leave CTRL1_XL bit "
      "LPF2_XL_EN at its reset value of 0. A pump on the same frame vibrates at "
      "300 Hz.\nWhat appears in your logged data?")
opts3 = [("A", "nothing — 300 Hz is above the sample rate, so it is not sampled"),
         ("B", "a 300 Hz component, attenuated"),
         ("C", "a 12 Hz component, indistinguishable from real signal"),
         ("D", "broadband noise, raising the noise floor slightly")]
s = poll(D, 3, q3, opts3, minute=44)
poll_note(s, "Vote. Then two minutes in pairs: find someone who voted differently "
             "and make them defend it. Then we vote again — and only then do we do "
             "the arithmetic.")
D.notes(s, """
TIMING: 00:44–00:47. THE HARDEST VOTE OF THE LECTURE. Protect this segment; it
is one of the two things Laboratory 2 depends on.

Protocol, in this order: vote → two minutes in pairs → revote → THEN the
arithmetic. Do not do the arithmetic before the revote. The revote is the
measurement.

Expect 40–55 % on A: that is M2, and "above the sample rate" feels like "outside
the window". Target 20–35 % correct on the first vote, 50–65 % on the second.

B is the student who assumes a filter is always present — name that as a
reasonable design instinct and a fatal assumption. D is the student reaching for
"noise floor": distinguish them, noise is broadband and averages down, an alias
is a tone and averaging makes it cleaner.

IF THE FIRST VOTE IS UNDER 15 %: stop. Redraw Lecture 1's figure and revote.
""")


# ───────────────────────────────────────────────────────── 24  poll 3 answer
s = poll(D, 3, q3, opts3, minute=44, correct="C", reveal=True)
poll_note(s, "| 300 − 3 × 104 |  =  | 300 − 312 |  =  12 Hz.  Squarely inside the "
             "band a tilt or vibration measurement cares about, slow enough to look "
             "like real mechanical behaviour, and permanent.", TEAL)
D.notes(s, """
TIMING: 00:47–00:48. Reveal, then do the sum with the room, out loud.

"Three times a hundred and four is three hundred and twelve. Three hundred minus
three hundred and twelve is minus twelve. Twelve hertz."

WRITE |300 − 3 × 104| = 12 Hz ON THE BOARD — board work item 2 — and leave it up.

Then the refutation of A, which is the answer most of the room gave: "the pump
is absolutely sampled. Nothing filtered it out, because nothing was there to
filter it out. The samples are correct. What is wrong is the frequency you will
assign to them."

Finish on the word that matters: irreversible. It is the first of three today,
and it is the one they will meet again on the exit ticket.
""")


# ───────────────────────────────────────────────────────── 25  three numbers
s = S()
heading(s, "Three numbers, three jobs",
        "The sentence most often got wrong on the midterm")
rows = [["", "What it decides", "Who sets it", "On your part, today"],
        ["ODR — output data rate", "how often a new number appears at the output",
         "you, by register", "104 Hz  ·  CTRL1_XL bits 7:4"],
        ["Measurement bandwidth", "the highest frequency reported faithfully",
         "you — often by a different register", "52 Hz  ·  only if LPF2 is on"],
        ["Anti-alias cut-off", "what reaches the sampler at all",
         "the analog path — sometimes nobody", "none  ·  LPF2_XL_EN = 0"]]
table(s, M, Inches(2.10), CONTENT_W, rows, [0.24, 0.29, 0.23, 0.24], size=15,
      row_h=Inches(0.72), head_size=14.5)
box(s, M + Inches(2.4), Inches(5.10), Inches(7.1), Inches(0.82),
    "ODR   ≠   BW   ≠   f_cut", fill=DARK, edge=AMBER, tcolor=CREAM, size=28,
    bold=True, font=MONO, edge_w=3)
txt(s, "Set the ODR wrongly and you get more numbers, or fewer, and you waste bus "
       "and power.\nSet the cut-off wrongly and the data is wrong for ever.",
    M, Inches(6.05), CONTENT_W, Inches(0.7), 17, INK, bold=True, line=1.35)
D.notes(s, """
TIMING: 00:48–00:49. BOARD WORK ITEM 3: write ODR ≠ BW ≠ f_cut in your own
handwriting, now, and say why you are writing it: this is the sentence most
students get wrong on the midterm, and you would rather they copied it than
inferred it.

Go across the last column, because that column is the whole lesson: their part,
today, has an ODR of 104, a claimed bandwidth of 52, and no anti-alias cut-off
at all.

One question, hands: "which of the three, set wrongly, gives an error you cannot
undo?" The third. That is learning outcome L3.2 and it is on the exit ticket.

IF POLL 3's FIRST VOTE WAS OVER 60 %: skip straight here from the reveal and
give the minutes to the timestamp segment instead.
""")


# ───────────────────────────────────────────────────────── 26  faster is not a fix
s = S()
heading(s, "Sampling faster does not fix it", "Same pump, three configurations",
        rule=RED)
rows = [["Interfering tone", "Sampled at", "Appears at", ""],
        ["300 Hz — a pump on the same frame", "104 Hz", "12 Hz", "inside your band"],
        ["1520 Hz — Lecture 1's bearing", "104 Hz", "40 Hz", "inside your band"],
        ["300 Hz — the same pump", "100 Hz", "0 Hz", "it looks like an offset"]]
t = table(s, M, Inches(2.15), CONTENT_W, rows, [0.36, 0.16, 0.16, 0.32], size=16,
          row_h=Inches(0.62), head_size=15, mono_cols=(1, 2))
for i in (1, 2, 3):
    c = t.cell(i, 2)
    c.fill.solid(); c.fill.fore_color.rgb = RED_L
    c.text_frame.paragraphs[0].runs[0].font.bold = True
box(s, M, Inches(4.85), CONTENT_W, Inches(1.20),
    "At 100 Hz the pump becomes a DC offset. Somebody will spend a productive week "
    "calibrating it out — and will succeed, at that one pump speed.\n"
    "Succeeding is worse than failing: the calibration is then wrong at every other "
    "speed, and the sensor gets the blame.",
    fill=RED_L, edge=RED, size=17.5, bold=True)
box(s, M, Inches(6.18), CONTENT_W, Inches(0.62),
    "Raising the sample rate moves the alias. It does not remove it. Choose the "
    "band first, then the rate.",
    fill=TEAL_L, edge=TEAL, size=18, bold=True)
D.notes(s, """
TIMING: 00:49–00:50. This is the kicker, and it is the refutation of M2 for the
students who still have it after Poll 3.

Take the last row slowly. "Round numbers are more dangerous than awkward ones.
At a hundred hertz exactly, three hundred folds to zero — and a constant offset
is the single most calibratable-looking thing in the world."

Then the sentence that makes the room uncomfortable, which is the point: "they
will calibrate it out, and it will work, and their report will be excellent, and
the whole thing will be wrong the moment the pump changes speed."

Land the teal line and move — chunk 3 starts in sixty seconds and it is the
longest chunk of the lecture.
""")


# ───────────────────────────────────────────────────────── 27  section C3
s = section(D, "chunk 3", "Codes to\ntrustworthy values",
            ["Four conversions between the die and the CSV file.",
             "Each one has a way of going wrong that produces a perfectly "
             "plausible answer."])
D.notes(s, """
TIMING: 00:50–00:51. Section marker.

Say the framing once: "everything so far was about what reached the converter.
The next twenty minutes are about what happens to a number after it exists — and
the danger changes character. These errors do not look like errors. They look
like data."

Then the worked conversion, which you do WITH the class, on the board, asking
for each step before you write it. Do not show a finished derivation.
""")


# ───────────────────────────────────────────────────────── 28  worked conversion
s = S()
heading(s, "One register read, all the way to SI",
        "Ask the class for each step before you write it")
steps = [("OUTX_L_A (0x28) = 0x2C        OUTX_H_A (0x29) = 0xFF", WHITE, INK,
          "little-endian: the low byte is at the lower address"),
         ("raw  =  0xFF2C  =  65 324   as unsigned", WHITE, INK,
          "16-bit two's complement: bit 15 is set, so it is negative"),
         ("65 324  −  65 536  =  −212 counts", WHITE, INK,
          "× sensitivity, ±2 g → 0.061 mg/LSB"),
         ("−212  ×  0.061 mg  =  −12.9 mg", WHITE, INK,
          "→ SI, × 9.80665"),
         ("−0.0129 g  ×  9.80665  =  −0.127 m/s²", TEAL, CREAM, None)]
y = Inches(2.10)
for text, fill, tcol, ann in steps:
    box(s, M, y, Inches(7.6), Inches(0.62), text, fill=fill,
        edge=TEAL if fill == TEAL else GRAY, tcolor=tcol, size=17, bold=True,
        font=MONO, align=PP_ALIGN.LEFT, edge_w=2.5 if fill == TEAL else 1.25)
    if ann:
        down_arrow(s, M + Inches(1.0), y + Inches(0.66), Inches(0.30), color=TEAL)
        txt(s, ann, M + Inches(1.55), y + Inches(0.70), Inches(6.0), Inches(0.3),
            13.5, GRAY, italic=True)
    y += Inches(1.00)
box(s, M + Inches(8.05), Inches(2.10), Inches(3.83), Inches(2.30),
    "Four steps.\n\nFour ways to get an answer that looks entirely reasonable.\n\n"
    "All four turn up in real laboratory submissions.",
    fill=GROUND, edge=GRAY, tcolor=INK, size=17, bold=True, align=PP_ALIGN.LEFT,
    anchor=MSO_ANCHOR.TOP)
box(s, M + Inches(8.05), Inches(4.60), Inches(3.83), Inches(1.35),
    "The device is very nearly at rest, tilted slightly, on this axis.",
    fill=TEAL_L, edge=TEAL, size=17, bold=True)
D.notes(s, """
TIMING: 00:51–00:54. Do this on the board with the class. Do NOT project a
finished derivation and read it — ask for each step first.

"Two bytes. Which one is the high byte?" Take the wrong answer if it comes; it
is step one of the next slide.

"Bit fifteen is set. What does that mean?" If nobody says two's complement,
write 0xFF2C in binary and wait.

The subtraction is the step students skip in code without noticing, because C
will happily do the wrong thing with the wrong type. Say that: "int16_t, not
uint16_t, and not int. The type declaration IS the sign convention."

End on the plausibility statement: minus 12.9 milli-g is a device at rest,
slightly tilted. The answer being boring is the evidence it is right.
""")


# ───────────────────────────────────────────────────────── 29  four failures
s = S()
heading(s, "Four ways to a plausible wrong answer",
        "All four appear in real laboratory submissions", rule=RED)
rows = [["The mistake", "What you get", "Why it is dangerous"],
        ["Byte order — high byte read first", "0x2CFF = 11 519 = +703 mg",
         "a wrong answer of a believable magnitude, which is the dangerous kind"],
        ["Sign ignored — word read as unsigned", "65 324 = +3985 mg",
         "a device at rest reporting nearly 4 g; at least this one announces itself"],
        ["IF_INC — CTRL3_C written 0x00 “to start clean”", "six copies of one byte",
         "CTRL3_C resets to 0x04, so auto-increment was already on. You turned it off"],
        ["Units left implicit", "mg, g and m/s² in one file",
         "put the unit in the column header, once, and never in the prose"]]
table(s, M, Inches(2.10), CONTENT_W, rows, [0.30, 0.24, 0.46], size=14.5,
      row_h=Inches(0.74), head_size=14.5)
box(s, M, Inches(5.95), CONTENT_W, Inches(0.90),
    "The plausibility check that tests the whole chain at once: at rest, one axis "
    "reads about 9.81 m/s², and the vector sum of all three is 1 g in any orientation.",
    fill=TEAL_L, edge=TEAL, size=18, bold=True)
D.notes(s, """
TIMING: 00:54–00:56. Row two is misconception M7 and it deserves thirty seconds:
signed data is not a formatting detail. A missed sign bit does not produce a
small error; it produces a stationary device reporting four g.

Row one is the more dangerous of the two, and say why: plus 703 milli-g is not
absurd. Nobody notices. It survives into the report.

Row three is the one that catches the CONSCIENTIOUS student — the one who writes
0x00 to CTRL3_C to start from a clean state. Say that out loud; it is worth
knowing that carefulness has failure modes too.

Then the teal box, which is the habit to install: it is the only check in the
whole chain that tests everything at once, against a physical constant they
cannot misconfigure.
""")


# ───────────────────────────────────────────────────────── 30  16 → 12.4
s = S()
heading(s, "The bits you own",
        "Every figure below is already in the datasheet you have open")
rows = [["Quantity", "Arithmetic", "Result"],
        ["full scale, ±2 g", "—", "4000 mg"],
        ["codes, 16-bit", "2^16", "65 536"],
        ["LSB", "4000 / 65 536", "0.061 mg"],
        ["quantisation noise", "0.061 / √12", "0.018 mg"],
        ["bandwidth, ODR 104 Hz, LPF2 on", "104 / 2", "52 Hz"],
        ["sensor noise, 100 µg/√Hz (max)", "100 × √52", "0.721 mg"],
        ["noise, in LSB", "0.721 / 0.061", "11.8 LSB"],
        ["bits that are noise", "log₂ 11.8", "3.6 bits"],
        ["EFFECTIVE BITS", "16 − 3.6", "12.4 bits"]]
t = table(s, M, Inches(2.05), CONTENT_W, rows, [0.42, 0.30, 0.28], size=14.5,
          row_h=Inches(0.40), head_size=14.5, mono_cols=(1, 2))
for j in (0, 1, 2):
    c = t.cell(9, j)
    c.fill.solid(); c.fill.fore_color.rgb = TEAL_L
    c.text_frame.paragraphs[0].runs[0].font.bold = True
txt(s, "The quantisation noise is forty times smaller than the sensor noise. Every "
       "argument about the last bit of an ADC is, in this system, an argument about "
       "nothing.",
    M, Inches(6.20), CONTENT_W, Inches(0.6), 18, INK, bold=True, line=1.3)
D.notes(s, """
TIMING: 00:56–00:58. Do all nine lines on the board, out loud, with the class.
This is where board work item 1 finally gets finished — write noise 0.72 mg,
11.8 LSB and 3.6 bits onto the line you started at minute 14.

Make them supply the bandwidth line. "Noise density times root what?" If anyone
says root ODR, stop and fix it there: that was Lecture 2's Poll 3 and it is the
same error in a new costume.

Say the sentence at the bottom exactly as written, then the second one from the
activity sheet: "you did not buy a 16-bit measurement. You bought a 16-bit
number wrapped around a 12.4-bit measurement — and the datasheet was not lying
to you. It printed the noise density on the same page."
""")


# ───────────────────────────────────────────────────────── 31  the anchor lands
s = statement(D, "You bought 16 bits.\nYou own 12.4.",
              "With the datasheet's typ noise density of 60 µg/√Hz the same "
              "arithmetic gives 0.433 mg and 13.2 effective bits. The part's own two "
              "printed columns move the answer by 0.8 bits — Lecture 2's lesson, "
              "restated in a new quantity.",
              size=44, eyebrow_text="the anchor", accent=AMBER)
D.notes(s, """
TIMING: 00:58–01:00. Silence first, then read the two lines once. Do not
elaborate on them; the table did the work.

Then the typ column, and connect it back explicitly — this is the connective
tissue of Module A and it is worth saying in those words: "last week the two
columns straddled a pass/fail line. This week they move the effective resolution
by nearly a bit. Same lesson, different quantity: a number without its
conditions is not a number."

Ask which column they would design with. You want the same answer as Lecture 2:
max if you are guaranteeing the specification, typ only if you can measure every
unit — and never typ presented as a guarantee.

Sixty seconds. Then the clock.
""")


# ───────────────────────────────────────────────────────── 32  the loop is slow
s = S()
heading(s, "The clock you did not have", "HAL_Delay(10) is not a 100 Hz sample rate")
bx, by, bwid = M + Inches(0.35), Inches(2.45), Inches(10.8)
box(s, bx, by, Emu(int(bwid * 10.000 / 10.203)), Inches(0.72),
    "HAL_Delay(10)   ·   10.000 ms", fill=TEAL, edge=TEAL, tcolor=CREAM,
    size=17, bold=True, font=MONO, shape=MSO_SHAPE.RECTANGLE)
box(s, bx + Emu(int(bwid * 10.000 / 10.203)), by,
    Emu(int(bwid * 0.203 / 10.203)), Inches(0.72), "", fill=AMBER, edge=AMBER,
    shape=MSO_SHAPE.RECTANGLE)
txt(s, "I²C read  ·  202 µs", bx + Inches(7.6), by - Inches(0.34), Inches(3.2),
    Inches(0.3), 14, AMBER, bold=True, font=MONO, align=PP_ALIGN.RIGHT)
txt(s, "one loop iteration  —  drawn to scale", bx, by + Inches(0.82),
    Inches(6.0), Inches(0.3), 14, GRAY, italic=True)
box(s, M, Inches(3.65), Inches(5.85), Inches(0.95),
    "six bytes over I²C at 400 kHz\n81 bit-times  ÷  400 kHz  =  202 µs",
    fill=WHITE, edge=AMBER, tcolor=INK, size=17, bold=True, font=MONO, edge_w=2.5)
box(s, M + Inches(6.05), Inches(3.65), Inches(5.85), Inches(0.95),
    "10.000 + 0.202  =  10.203 ms\n→  98.0 Hz,  not 100 Hz",
    fill=WHITE, edge=RED, tcolor=INK, size=17, bold=True, font=MONO, edge_w=2.5)
txt(s, "Two per cent. Always in the same direction. Every single iteration.",
    M, Inches(4.90), CONTENT_W, Inches(0.5), 22, INK, bold=True)
box(s, M, Inches(5.65), CONTENT_W, Inches(1.0),
    "Nothing is broken. Nothing reports an error. The loop simply takes longer than "
    "you told it to —\nand a delay is a minimum, never a period.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=19, bold=True)
D.notes(s, """
TIMING: 01:00–01:02. Start by asking, not telling: "you called HAL_Delay(10).
What is your sample rate?" Everybody says a hundred hertz. Wait, then: "what
else does the loop do?"

The bar is to scale on purpose. Point at the amber sliver: "that is the whole
error. Two per cent. It looks like nothing." Then the sentence that sets up the
next slide: "it looks like nothing because you are looking at one iteration."

The phrase to leave them with is on the dark bar: a delay is a minimum, never a
period. HAL_Delay guarantees at least ten milliseconds and promises nothing
about the loop.

If someone asks about interrupt latency and jitter — yes, and it makes the real
case worse, not better. Two slides from now, that is the fix.
""")


# ───────────────────────────────────────────────────────── 33  the 12.1 seconds
s = S()
heading(s, "What 203 microseconds does to ten minutes", rule=RED)
rows = [["", "You believe", "Reality"],
        ["Sample interval", "10.000 ms", "10.203 ms"],
        ["Sample rate", "100 Hz", "98.0 Hz"],
        ["A real 20 Hz tone is reported at", "20 Hz", "20.41 Hz"],
        ["After 60 000 samples the log says", "600.0 s", "612.1 s"],
        ["Every event is stamped", "when it happened", "12.1 s too early"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.44, 0.28, 0.28], size=16,
          row_h=Inches(0.55), head_size=16, mono_cols=(1, 2))
for i in (4, 5):
    c = t.cell(i, 2)
    c.fill.solid(); c.fill.fore_color.rgb = RED_L
    c.text_frame.paragraphs[0].runs[0].font.bold = True
box(s, M, Inches(5.60), CONTENT_W, Inches(1.05),
    "Worse than a constant scaling error: the loop period depends on which branches "
    "ran, whether an interrupt arrived, and what the bus was doing.\n"
    "You can bound this error. You cannot invert it.",
    fill=RED_L, edge=RED, size=18.5, bold=True)
D.notes(s, """
TIMING: 01:02–01:03. Read the last two rows and then stop talking for a moment.

The 20.41 Hz row is the one that will show up in somebody's project: a two per
cent frequency error is enough to misidentify a machine order or a resonance,
and it is far too small to look like a bug.

The 12.1 s row is the one that matters. Ask the question that makes it real:
"what were you going to do with this log?" Correlate it — against a second
sensor, an operator's note, a video, another team's file. Twelve seconds of
drift makes every one of those correlations meaningless.

Then the bottom box, and lean on the last sentence. Bounding an error and
inverting it are different operations, and only one of them saves the data.
""")


# ───────────────────────────────────────────────────────── 34  the fix
s = S()
heading(s, "The fix, which is free", "Let the sensor decide when the sample happened")
rows = [["", "Polling with a delay", "Data-ready interrupt"],
        ["Sets the interval", "your software", "the sensor's own timebase"],
        ["Interval error", "loop-dependent, unbounded", "specified in the datasheet"],
        ["Cumulative time error", "grows without limit", "bounded by the timebase tolerance"],
        ["CPU cost", "high — busy waiting", "low"],
        ["Effort to implement", "slightly less", "slightly more"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.28, 0.36, 0.36], size=16,
          row_h=Inches(0.52), head_size=16)
for j, col in ((1, RED_L), (2, TEAL_L)):
    c = t.cell(3, j)
    c.fill.solid(); c.fill.fore_color.rgb = col
    c.text_frame.paragraphs[0].runs[0].font.bold = True
box(s, M, Inches(5.25), CONTENT_W, Inches(0.85),
    "The sensor knows when it sampled. Ask it, rather than guessing.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=25, bold=True)
txt(s, "Timestamp from a hardware timer, not a loop counter: the error becomes a "
       "published tolerance instead of your software's mood. Laboratory 2 asks for "
       "a timing plot for exactly this reason.",
    M, Inches(6.22), CONTENT_W, Inches(0.7), 16, GRAY, line=1.3)
D.notes(s, """
TIMING: 01:03–01:04. This is the single most transferable minute of the lecture.
Say so.

The table is a reference; read only the third row aloud, both columns. Unbounded
against bounded is the whole argument, and it costs one interrupt handler.

Then the teal line, which is the sentence to carry out of the room: the sensor
knows when it sampled — ask it rather than guessing.

Two objections you should welcome. "The interrupt has latency too": yes, and it
is bounded and small, which is the entire point. "This is more work": about
fifteen lines, once, and they will write them in Laboratory 2 in week four.

NEVER CUT THIS SEGMENT, even running late. Cut slide 35 instead.
""")


# ───────────────────────────────────────────────────────── 35  data integrity
s = S()
heading(s, "Knowing that the data is real",
        "Four cheap checks, each catching a failure that otherwise looks like bad data")
checks = [("WHO_AM_I  (0x0F)", TEAL,
           "Read it and compare it with 0x6B.\n\nOne transaction proves the address, "
           "the bus, the pull-ups and the supply, all at once."),
          ("SELF-TEST", TEAL,
           "Deflect the proof mass electrostatically by a known amount.\n\nThe only "
           "check here that tests the mechanics rather than the electronics."),
          ("FIFO OVERRUN", AMBER,
           "If the buffer overflowed, samples were lost and the rest are not evenly "
           "spaced.\n\nA dropped sample is a timing error disguised as data."),
          ("BUS ERROR & RECOVERY", AMBER,
           "I²C can hang with a slave holding the data line low.\n\nA design that "
           "cannot recover stops logging one day and gives no reason.")]
x = M
for name, col, body in checks:
    box(s, x, Inches(2.15), Inches(2.85), Inches(0.62), name, fill=col, edge=col,
        tcolor=CREAM if col == TEAL else DARK, size=14, bold=True)
    txt(s, body, x + Inches(0.10), Inches(2.92), Inches(2.65), Inches(2.4), 14.5,
        INK, line=1.3)
    x += Inches(3.02)
box(s, M, Inches(5.70), CONTENT_W, Inches(0.95),
    "All four are omitted from most first attempts. All four turn “the data looks "
    "strange” into “the sensor was never responding”.",
    fill=GROUND, edge=GRAY, size=19, bold=True)
D.notes(s, """
TIMING: 01:04–01:06. THIS SLIDE IS A DESIGNATED CUT if you are running late.

If you keep it, spend the time on WHO_AM_I, because they did it in Laboratory 1
and it is retrieval: one byte proves four things. Mention the coincidence that
0x6B is both the expected value and one of the part's two I²C addresses — it has
confused a great many people and it will confuse some of them.

FIFO overrun is the one with today's flavour: a silently dropped sample is not
missing data, it is a timing error wearing data's clothes. That is the same
lesson as the last three slides in a fourth costume.

Do not turn this into a checklist to memorise. The point is the last line: these
turn "strange data" into "the sensor was never responding".
""")


# ───────────────────────────────────────────────────────── 36  poll 1 answer
s = poll(D, 1, q1, opts1, minute=66, correct="C", reveal=True)
poll_note(s, "0.72 mg — nearly twelve times the LSB. Your first answer should have "
             "been D: you had not been given the noise density. The right answer "
             "now is C, and you computed it yourselves.", TEAL)
D.notes(s, """
TIMING: 01:06–01:08. Put the minute-7 distribution on the board beside this. The
shift is the lecture's evidence that it worked, and the class should see it.

Say both halves, because this is a professional habit rather than a trick:

"If you chose D at minute seven you were right, and for the best possible
reason: you knew you could not decide. If you chose A you did what most
engineers do, which is read the headline. If you chose B you knew a real formula
and stopped one term too early. And if you now choose C, you can defend it with
arithmetic — which is the only defence that survives a design review."

Then point at the board line you started at minute 14 and finished at minute 56.
It is the whole lecture in one row of chalk.
""")


# ───────────────────────────────────────────────────────── 37  poll 4 transfer
q4 = ("A water-level logger reads a 4–20 mA pressure loop through a 100 Ω sense "
      "resistor and a 12-bit ADC, polling in a while() loop with a 50 ms delay. It "
      "runs for a week.\nAfterwards you discover all four of the following. Which "
      "one can you still fix?")
opts4 = [("A", "the reported level is 40 mm high across the whole week"),
         ("B", "the timestamps drift, ending 90 s behind real time"),
         ("C", "a 9.7 Hz component from the pump has folded into the band"),
         ("D", "the last two ADC bits were always noise")]
s = poll(D, 4, q4, opts4, minute=68)
poll_note(s, "Different measurand, different interface, different failure — the same "
             "question underneath. Vote, then hold your answer: the next slide is the "
             "answer to this one.")
D.notes(s, """
TIMING: 01:08–01:11. TRANSFER ITEM — deliberately a new measurand, so it tests
the principle rather than memory of the accelerometer case. Sixty seconds to
vote, then discussion.

Correct is A: a constant offset is a systematic error against a known reference
— the tank was empty on Tuesday, the level was surveyed on Friday — so it is
removable after the fact.

B is the tempting one, because it LOOKS like a linear correction. It is not: the
loop period depended on branch timing that varied with the data. Bound it; you
cannot invert it. C is the student who has forgotten Poll 3 twenty minutes
later, which is worth catching now rather than in the midterm. D is the student
who thinks averaging recovers resolution — it recovers some, for a stationary
signal, at the cost of bandwidth.

Do not reveal here. The next slide is the answer, in general form.
""")


# ───────────────────────────────────────────────────────── 38  calibratable or gone
s = S()
heading(s, "Calibratable, or gone",
        "The table to keep — and Poll 4's answer is its first row")
rows = [["Error", "Removable afterwards?", "How, or why not"],
        ["Offset", "YES", "one-point calibration against a known reference"],
        ["Scale factor", "YES", "two-point calibration"],
        ["Byte order, sign, units", "YES", "reinterpret the file — the bits are all there"],
        ["Temperature drift", "PARTLY", "only if you logged the temperature. So log it"],
        ["Random noise", "PARTLY", "averaging reduces it by √N, and costs you bandwidth"],
        ["Quantisation", "NO — but negligible here", "0.018 mg against 0.721 mg of noise"],
        ["Aliasing", "NO", "the alias and the signal are the same numbers"],
        ["A lost or wrong timestamp", "NO", "the timing information was never recorded"]]
t = table(s, M, Inches(2.05), CONTENT_W, rows, [0.28, 0.24, 0.48], size=15,
          row_h=Inches(0.43), head_size=15)
for i, col in ((1, TEAL_L), (2, TEAL_L), (3, TEAL_L), (4, AMBER_L), (5, AMBER_L),
               (6, RED_L), (7, RED_L), (8, RED_L)):
    c = t.cell(i, 1)
    c.fill.solid(); c.fill.fore_color.rgb = col
    c.text_frame.paragraphs[0].runs[0].font.bold = True
box(s, M, Inches(6.05), CONTENT_W, Inches(0.80),
    "Everything above is a transformation of data that is still there. Everything "
    "below is missing information.\nNo amount of processing creates information.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=17, bold=True)
D.notes(s, """
TIMING: 01:11–01:13. THIS IS THE ARTEFACT THEY KEEP. Say that: "photograph this
one. You will use it in every remaining laboratory of this course."

Resolve Poll 4 from the first row and move on quickly — A, the offset, and the
other three are all in the bottom half of this table.

Two rows deserve a sentence each. Temperature drift is recoverable if and only
if you logged the temperature; almost every sensor in this course has a
temperature output, most people ignore it, and it costs one column in the file.
Log it. And quantisation: "no" and "negligible" in the same row is not a
contradiction — it cannot be undone and it never mattered.

Then the pattern at the bottom, which is the one law of the subject with no
exceptions: no processing creates information.
""")


# ───────────────────────────────────────────────────────── 39  three anchors
s = S()
heading(s, "Three numbers, one log file",
        "All three were computable before a line of firmware was written")
num_card(s, M, Inches(2.20), cw, "12.4", "bits that carry information",
         "16 − log₂(0.721 / 0.061), from the\nnoise density and your bandwidth.",
         TEAL, h=Inches(2.75))
num_card(s, M + cw + cgap, Inches(2.20), cw, "12 Hz",
         "a signal that does not exist in the world",
         "| 300 − 3 × 104 |. One register\nbit, left at its reset value of 0.",
         RED, h=Inches(2.75))
num_card(s, M + 2 * (cw + cgap), Inches(2.20), cw, "12.1 s",
         "of timestamp error after ten minutes",
         "60 000 × 0.203 ms. One I²C read\nthe loop never accounted for.",
         RED, h=Inches(2.75))
box(s, M, Inches(5.35), CONTENT_W, Inches(0.95),
    "One of the three you can state and live with. Two of them cannot be repaired "
    "afterwards at any price —\nand neither of those two announces itself anywhere "
    "in the file.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=19, bold=True)
txt(s, "The same three numbers you were shown at the start. You now know where "
       "every one of them came from.",
    M, Inches(6.50), CONTENT_W, Inches(0.4), 17, GRAY, italic=True)
D.notes(s, """
TIMING: 01:13–01:15. Go back to the hook explicitly — put slide 4 up beside this
one if your tooling allows, or just say it.

"At minute five these were three assertions. You have now derived all three, and
each one came from a document you already had."

Point at the colours, because the semantic is the course's, not this lecture's:
teal is what you own, red is what you lost. Twelve point four bits is a number
you can write in a report and defend. The other two are damage.

Ask one question and take two answers: "which of the three would you check
first, on a system you inherited?" Any defended answer is a good answer; the
habit is checking before trusting.
""")


# ───────────────────────────────────────────────────────── 40  the four claims
s = S()
heading(s, "The four claims a trustworthy sample makes")
claims = [("01", "What is it?",
           "A value in SI units — with the sensitivity, the sign convention and the "
           "byte order you assumed, stated."),
          ("02", "How much of it is information?",
           "The effective resolution, from the noise density and YOUR bandwidth. "
           "12.4 bits, not 16."),
          ("03", "Which band does it represent?",
           "The measurement bandwidth, and evidence that a filter sat below it, "
           "before the sampler. Not the ODR."),
          ("04", "When did it happen?",
           "A timestamp whose error you can state, from a source you can name.")]
y = Inches(2.05)
for n, t2, sub in claims:
    txt(s, n, M, y, Inches(0.75), Inches(0.5), 24, TEAL_L, bold=True, font=MONO)
    txt(s, t2, M + Inches(0.85), y - Inches(0.02), Inches(11.2), Inches(0.45), 22,
        INK, bold=True)
    txt(s, sub, M + Inches(0.85), y + Inches(0.44), Inches(11.2), Inches(0.45), 17,
        GRAY)
    y += Inches(1.08)
box(s, M, Inches(6.15), CONTENT_W, Inches(0.68),
    "A log file that cannot answer these four is not data. It is a plausible file.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=22, bold=True)
D.notes(s, """
TIMING: 01:15–01:17. Read the four questions only — not the grey lines. Sixty
seconds.

Then make the demand concrete, because as a list it sounds like advice: "all
four are answerable before you write firmware. Not after the run. Before. If you
cannot answer them at the design stage, the run will not tell you."

The last line is the sentence to end the content on, so deliver it and stop. Let
it sit for two seconds before you move to the laboratory bridge.

If you are behind, this is the slide to compress — but not to cut. It is the
lecture's answer to its own title.
""")


# ───────────────────────────────────────────────────────── 41  lab 2 bridge
s = S(bg=DARK)
eyebrow(s, "next", TEAL)
txt(s, "Week 4: Laboratory 2", M, Inches(1.15), Inches(11), Inches(0.8), 38,
    CREAM, bold=True)
txt(s, "Sampling, aliasing and the ADC — with the register bits in your hands",
    M, Inches(2.02), Inches(11.9), Inches(0.5), 23, TEAL, bold=True)
txt(s, "PRE-LAB, before you arrive: compute the effective bits for TWO ODR "
       "settings, exactly as we did today.\nThe bench time is for measuring, not "
       "for deriving — and you will be asked for a timing plot.",
    M, Inches(2.72), Inches(11.9), Inches(1.2), 19, RGBColor(0xB8, 0xC0, 0xC6),
    line=1.4)
box(s, M, Inches(4.20), CONTENT_W, Inches(0.70),
    "Bring one answer with you: which bit do you set so that 52 Hz actually means "
    "52 Hz?",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=20, bold=True)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, Inches(5.15), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "AND THEN LECTURE 4", M, Inches(5.47), Inches(11), Inches(0.35), 14, AMBER,
    bold=True)
txt(s, "MEMS structures, transduction, fabrication and packaging — why the numbers "
       "in the datasheet are\nthe numbers they are, and where drift comes from "
       "before anybody switches anything on.",
    M, Inches(5.87), Inches(11.9), Inches(1.0), 19, CREAM, line=1.4)
D.notes(s, """
TIMING: 01:17–01:18. Be concrete about the pre-lab; vagueness here costs bench
time in week four.

"Two ODR settings, the nine-line calculation, on paper, before you walk in. If
you arrive without it you will spend the first forty minutes deriving instead of
measuring, and the demonstrators will not do it for you."

The question in the teal box has a one-line answer — LPF2_XL_EN — and asking for
it as homework means the whole room arrives having found bit 1 of CTRL1_XL in
the datasheet themselves.

Then the forward link: Lecture 4 explains where the noise density and the drift
came from in the first place. Same datasheet, one level further down.
""")


# ───────────────────────────────────────────────────────── 42  exit ticket
s = S()
heading(s, "Exit ticket", "Ninety seconds · on paper · handed in at the door")
cards = [("1  ·  JUDGEMENT", TEAL, CREAM,
          "A colleague says:\n“we will sample at 1 kHz and filter it down in "
          "software afterwards.”\n\nIn one sentence, what is wrong\nwith that plan?"),
         ("2  ·  RETRIEVAL", AMBER, DARK,
          "Name one error in your Laboratory 1\ndata that you now believe was\n"
          "IRREVERSIBLE.\n\nOne line. No explanation needed.")]
x = M
for title, col, tc, body in cards:
    box(s, x, Inches(2.15), Inches(5.85), Inches(0.68), title, fill=col, edge=col,
        tcolor=tc, size=17, bold=True)
    txt(s, body, x + Inches(0.16), Inches(3.10), Inches(5.5), Inches(2.3), 19,
        INK, line=1.4)
    x += Inches(6.05)
box(s, M, Inches(5.85), CONTENT_W, Inches(0.90),
    "Question 2 is the one that matters. It is the input to Lecture 4's opening "
    "slide, so it will actually be read.",
    fill=GROUND, edge=GRAY, size=19, bold=True)
D.notes(s, """
TIMING: 01:18–01:20. End on time. Hand the slips out while slide 41 is still up.

Q1 key: sampling faster does not remove an alias, it moves it — the filter has
to be in front of the converter, and no software step recovers what the sampler
already merged. Accept any sentence containing that idea.

Q2 is the diagnostic and the reason this ticket exists. Expect roughly a third
to name aliasing, a third the timestamp, and a third to name something that is
in fact calibratable. That last third is precisely the signal you want, and it
is the opening slide of Lecture 4.

READ THEM. This is outcome L3.5 and the spine of Lectures 12–15. If most of the
room names a calibratable error, the synthesis table needs ten minutes of
Lecture 4's opening, not a sentence.
""")


out = "../lecture-03/output/L3-from-physical-quantity-to-trustworthy-samples.pptx"
D.save(out)
print(f"saved {out}  ·  {D.n} slides")
