"""Lecture 1 — MEMS, sensors, and the measurement-system architecture (80 min)."""
import math
from deck import *

D = Deck("MEMS & Sensors  ·  Lecture 1  ·  Measurement-system architecture")
S = D.slide


# ───────────────────────────────────────────────────────── 1  title
s = S(bg=DARK, footer=False)
b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.34), H)
b.fill.solid(); b.fill.fore_color.rgb = TEAL
b.line.fill.background(); b.shadow.inherit = False
txt(s, "MICROELECTROMECHANICAL SYSTEMS AND SENSORS", Inches(1.15), Inches(1.5),
    Inches(11), Inches(0.4), 15, TEAL, bold=True)
txt(s, "MEMS, sensors, and the\nmeasurement-system architecture",
    Inches(1.15), Inches(2.25), Inches(11.3), Inches(2.2), 40, CREAM, bold=True,
    line=1.15)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.15), Inches(4.72), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "Lecture 1 of 16   ·   80 minutes   ·   Module A: Foundations",
    Inches(1.15), Inches(5.05), Inches(11), Inches(0.4), 18,
    RGBColor(0xB8, 0xC0, 0xC6))
txt(s, "Bachelor programme · Electrical Engineering · 7th semester\n"
       "Institute of Energy and Electrical Engineering",
    Inches(1.15), Inches(5.75), Inches(11), Inches(0.9), 15, GRAY, line=1.4)
D.notes(s, """
BEFORE THE BELL: have the hook slide ready. Do not open with administration —
the syllabus, assessment and logistics come at minute 74, not now. The first
90 seconds are the most valuable of the semester; spend them on the mystery.

Say: "Before I tell you what this course is, I want to tell you about a motor
that died while somebody was watching it."  Then advance immediately.
""")


# ───────────────────────────────────────────────────────── 2  hook
s = S(bg=DARK)
eyebrow(s, "minute 0  ·  the hook", AMBER)
txt(s, "The motor that died\nunder observation", M, Inches(1.9), Inches(11),
    Inches(2.1), 46, CREAM, bold=True, line=1.12)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, Inches(4.5), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "A 1500 rpm induction motor.  A vibration monitor.  Six weeks of data.",
    M, Inches(4.85), Inches(11.5), Inches(0.6), 21, RGBColor(0xB8, 0xC0, 0xC6))
D.notes(s, """
TIMING: 0:00–0:01. Tell this as a story, not a slide.

"An industrial plant instrumented a motor to catch bearing failure early.
Accelerometer on the housing, microcontroller, data logged every day, a
trend line on a screen that somebody actually looked at."

Do not rush. Let the room settle into narrative mode. Next slide.
""")


# ───────────────────────────────────────────────────────── 3  timeline
s = S(bg=DARK)
eyebrow(s, "what the screen showed", GRAY)
txt(s, "Six weeks of calm", M, Inches(0.78), Inches(11), Inches(0.7), 34,
    CREAM, bold=True)
# trend line: slowly rising then catastrophe
x0, y0, wid = M, Inches(4.15), Inches(9.6)
axis(s, x0, y0, wid + Inches(1.2), GRAY)
pts = [(Emu(int(x0 + wid * i / 60)),
        Emu(int(y0 - Inches(0.42) - Inches(0.30) * (i / 60))))
       for i in range(61)]
# add a little noise so it reads as real data
pts = [(x, Emu(int(y + Inches(0.055) * math.sin(i * 1.7))))
       for i, (x, y) in enumerate(pts)]
curve(s, pts, TEAL, 2.5)
txt(s, "20 Hz  ·  amplitude slowly rising  ·  read as normal load variation",
    M, Inches(4.62), Inches(9.5), Inches(0.5), 16, TEAL, font=MONO)
# the cliff
cx = x0 + wid
curve(s, [(Emu(int(cx)), Emu(int(y0 - Inches(0.72)))),
          (Emu(int(cx + Inches(0.30))), Emu(int(y0 - Inches(2.55)))),
          (Emu(int(cx + Inches(0.62))), Emu(int(y0 - Inches(0.30))))], RED, 3.0)
txt(s, "WEEK 7", cx + Inches(0.78), Inches(1.55), Inches(2.4), Inches(0.3), 14,
    RED, bold=True, font=MONO)
txt(s, "bearing seized\nmotor destroyed", cx + Inches(0.78), Inches(1.90),
    Inches(2.6), Inches(0.9), 17, RED, bold=True, line=1.25)
txt(s, "week 1", x0, y0 + Inches(0.14), Inches(2), Inches(0.3), 14, GRAY, font=MONO)
D.notes(s, """
TIMING: 0:01–0:02.

Point at the flat line: "For six weeks, this. A 20 Hz vibration, slowly rising.
Every maintenance engineer in this room would read that as load variation."

Then the cliff: "Week seven. The bearing seizes. The motor is scrap."

Pause. Then: "Here is what makes this interesting."
""")


# ───────────────────────────────────────────────────────── 4  all met spec
s = S()
heading(s, "Nothing failed", "The post-mortem checked every component")
items = [
    ("The accelerometer", "met every number in its datasheet"),
    ("The circuit board", "no fault found"),
    ("The firmware", "no bug found"),
    ("The data logger", "logged every single sample"),
    ("The engineer", "looked at the screen every week"),
]
y = Inches(2.15)
for a, bb in items:
    box(s, M, y, Inches(4.05), Inches(0.72), a, fill=WHITE, edge=TEAL,
        size=19, bold=True, align=PP_ALIGN.LEFT)
    txt(s, "✓", M + Inches(4.35), y + Inches(0.14), Inches(0.4), Inches(0.4),
        22, TEAL, bold=True)
    txt(s, bb, M + Inches(4.95), y + Inches(0.20), Inches(6.5), Inches(0.5),
        19, GRAY)
    y += Inches(0.86)
D.notes(s, """
TIMING: 0:02–0:03. Read the left column aloud, tick by tick. The rhythm matters —
five ticks in a row builds the paradox.

"Every component met its specification. Nobody was negligent. And the motor
is still scrap."

Then, flatly: "So I want your verdict." Advance to the poll.
""")


# ───────────────────────────────────────────────────────── 5  poll 1
s = poll(D, 1, "Where was the fault?",
         [("A", "The accelerometer was too cheap for industrial use"),
          ("B", "There was a firmware bug nobody found"),
          ("C", "Nobody specified the sample rate against the frequency of the fault"),
          ("D", "Bearing degradation cannot be detected by vibration"),
          ("E", "The maintenance team ignored a rising trend")],
         minute=4,
         note="Commit now. No discussion. I will show you the answer in the last "
              "ten minutes of this lecture — and I want to see whether you change your mind.")
D.notes(s, """
TIMING: 0:03–0:05. Baseline commitment poll — NOT assessment.

HOW TO RUN THE VOTE (no polling tool — this is the standard method all semester):
  Question stays on screen. "Hands up for A on my count — three, two, one."
  Then B, then C, then D, then E. One raise per student.
  Count to the nearest quarter of the room and write it down.
  ONLY THEN take two spoken answers: "A — tell me why."

SILENT VOTE FIRST, ALWAYS. If anyone says an answer aloud before the hands go up,
the room anchors on it and you lose the independent first vote — which is the whole
mechanism. Voting first costs 40 seconds and protects the entire exercise.

CRITICAL: do NOT reveal, hint, or react to the distribution. Say only
"Hold that thought." Any tell here spends the ending you are saving.

WRITE DOWN the distribution. You will re-run this exact poll at minute 70 and
show the two side by side. For a first offering, that pair of numbers is the
most useful evidence you will collect today.

Expected: A and E dominate — both blame a component or a person rather than the
absence of a system specification. That habit is what this course replaces.
""")


# ───────────────────────────────────────────────────────── 6  what this course is
s = S()
heading(s, "What this course is", "and, just as importantly, what it is not")
box(s, M, Inches(2.2), Inches(5.8), Inches(1.15), "THIS COURSE IS", fill=TEAL,
    edge=TEAL, tcolor=CREAM, size=17, bold=True)
txt(s, "Choosing, interfacing, calibrating and\nvalidating real sensors inside\n"
       "real embedded systems.",
    M + Inches(0.1), Inches(3.55), Inches(5.6), Inches(2), 21, INK, line=1.4)
box(s, M + Inches(6.35), Inches(2.2), Inches(5.8), Inches(1.15), "IT IS NOT",
    fill=GRAY_L, edge=GRAY, tcolor=INK, size=17, bold=True)
txt(s, "A cleanroom fabrication course.\nWe visit fabrication once, in Lecture 4,\n"
       "only as deep as packaging and drift require.",
    M + Inches(6.45), Inches(3.55), Inches(5.6), Inches(2), 21, GRAY, line=1.4)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, Inches(5.55), CONTENT_W, Pt(1.5))
ln.fill.solid(); ln.fill.fore_color.rgb = GRAY_L
ln.line.fill.background(); ln.shadow.inherit = False
rich(s, M, Inches(5.85), CONTENT_W, Inches(1),
     [[("The design principle of all sixteen lectures:  ", {"color": GRAY, "size": 17}),
       ("understand the measurand → select the sensor → interface it → acquire "
        "valid data → calibrate it → process or fuse it → validate it in a system.",
        {"bold": True, "size": 17, "color": INK})]])
D.notes(s, """
TIMING: 0:05–0:07. Now — and only now — you may say what the course is.

Point at the right-hand box explicitly: many students arrive expecting silicon
processing and cleanroom photographs. Kill that expectation in one sentence so
they stop waiting for it. (Misconception M2.)

Read the design principle across the bottom slowly. Tell them it is the spine
of the syllabus and that every lab is one arrow in it.
""")


# ───────────────────────────────────────────────────────── 7  outcomes
s = S()
heading(s, "By the end of today you can…")
outs = [
    ("01", "DRAW", "the path from a physical quantity to a logged number, and say where information dies"),
    ("02", "CLASSIFY", "an unfamiliar device: sensor, transducer or actuator — and name its measurand"),
    ("03", "PREDICT", "from scaling laws why MEMS devices are fast — and what gets worse when they shrink"),
    ("04", "CONVERT", "a vague request into a measurement specification you could order against"),
]
y = Inches(2.15)
for num, verb, rest in outs:
    txt(s, num, M, y + Inches(0.04), Inches(0.7), Inches(0.5), 26, TEAL_L,
        bold=True, font=MONO)
    txt(s, verb, M + Inches(0.85), y, Inches(2.0), Inches(0.5), 22, TEAL, bold=True)
    txt(s, rest, M + Inches(2.95), y + Inches(0.03), Inches(8.9), Inches(0.9),
        20, INK, line=1.3)
    y += Inches(1.06)
txt(s, "Notice that all four are verbs. None of them is “know about”.",
    M, Inches(6.5), CONTENT_W, Inches(0.4), 17, GRAY, italic=True)
D.notes(s, """
TIMING: 0:07–0:08. Fast — 60 seconds. Do not read all four aloud word for word.

Say: "Four things, all of them verbs. If at the end of the hour you can't do
these four, tell me on the exit ticket and I will fix it at the start of
Lecture 2." That promise is cheap and it buys you real exit-ticket honesty.
""")


# ───────────────────────────────────────────────────────── 8  section C1
s = section(D, "chunk 1  ·  minutes 8–26", "The chain",
            ["A measurement is not a component. It is a path — and a path is only as",
             "truthful as its worst link. We are going to build that path one box at a time."],
            minute="08:00")
D.notes(s, """
TIMING: 0:08. Section marker — 15 seconds, do not linger.
""")


# ───────────────────────────────────────────────────────── 9  three words
s = S()
heading(s, "Three words we will use precisely", "because from here on the difference matters")
cols = [
    ("SENSOR", TEAL, "Converts a physical quantity\ninto a signal you can read.",
     "MEMS microphone\nsound pressure → voltage"),
    ("TRANSDUCER", TEAL, "Converts energy from one form\nto another. A sensor is one kind.",
     "loudspeaker, strain gauge,\npiezo disc — either direction"),
    ("ACTUATOR", AMBER, "Converts a signal into a\nphysical action on the world.",
     "MEMS mirror\nvoltage → beam deflection"),
]
x = M
cw = Inches(3.85)
for name, col, defn, ex in cols:
    box(s, x, Inches(2.15), cw, Inches(0.82), name, fill=col, edge=col,
        tcolor=CREAM, size=20, bold=True)
    txt(s, defn, x + Inches(0.12), Inches(3.18), cw - Inches(0.24), Inches(1.5),
        18, INK, line=1.35)
    ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x + Inches(0.12), Inches(4.78),
                            Inches(0.8), Pt(3))
    ln.fill.solid(); ln.fill.fore_color.rgb = col
    ln.line.fill.background(); ln.shadow.inherit = False
    txt(s, ex, x + Inches(0.12), Inches(5.03), cw - Inches(0.24), Inches(1.2),
        15, GRAY, line=1.35, font=MONO)
    x += cw + Inches(0.35)
txt(s, "Every actuator in this course is also a measurement problem: you only know "
       "it acted if you sense the result.",
    M, Inches(6.3), CONTENT_W, Inches(0.5), 17, AMBER, italic=True)
D.notes(s, """
TIMING: 0:08–0:12. Four minutes, no more. This is vocabulary, not physics.

The one point worth making: "transducer" is the general term and "sensor" is the
special case that points inward. Most datasheets use them interchangeably; you
should not.

The bottom line is the sentence students remember. Deliver it, then move.
""")


# ───────────────────────────────────────────────────────── 10  classify
s = S()
heading(s, "Thirty seconds", "Sensor, transducer or actuator? And what is the measurand?")
devs = ["MEMS\nmicrophone", "Piezo\nbuzzer", "Strain\ngauge", "MEMS\nmirror"]
x = M
for d in devs:
    box(s, x, Inches(2.4), Inches(2.7), Inches(1.5), d, fill=WHITE, edge=GRAY,
        size=21, bold=True)
    box(s, x, Inches(4.15), Inches(2.7), Inches(0.7), "?", fill=GROUND,
        edge=GRAY_L, tcolor=GRAY, size=24, bold=True,
        dash=MSO_LINE_DASH_STYLE.DASH)
    x += Inches(2.95)
txt(s, "Turn to your neighbour. Four devices, thirty seconds. Say the measurand out loud.",
    M, Inches(5.5), CONTENT_W, Inches(0.5), 20, INK, bold=True)
txt(s, "One of these four is passive — it changes a resistance and needs an excitation "
       "current before it says anything at all. Which one, and why does that matter?",
    M, Inches(6.1), CONTENT_W, Inches(0.8), 17, AMBER, italic=True, line=1.3)
D.notes(s, """
TIMING: 0:12–0:14. First state change of the lecture — get them talking early,
while the cost of speaking is still low.

ANSWERS: microphone = sensor, sound pressure. Buzzer = actuator (and a
transducer). Strain gauge = sensor, strain — PASSIVE, it needs excitation.
MEMS mirror = actuator, angular deflection.

The strain gauge is the point of the exercise: a passive sensor produces
nothing on its own. That is the seed of Lecture 12's bridge excitation.

Take answers from two pairs, 20 seconds each. Do not survey the room.
""")


# ───────────────────────────────────────────────────────── 11–14  chain builds
build_notes = [
    ("The measurand", 1, """
TIMING: 0:14–0:15. Start with nothing but the physical world.

"On the left is the only thing that is actually true: the motor is vibrating.
Everything to the right of this box is a story we tell about it. Our job is to
make the story faithful."
"""),
    ("It does not start at the sensor", 3, """
TIMING: 0:15–0:17. THIS IS THE SLIDE STUDENTS DO NOT EXPECT.

Box 2 first: "Before any electronics exist, the vibration has to travel through
a bolt, a bracket, a housing, maybe a rubber pad. That mechanical path is part of
your instrument. It has a transfer function. Nobody puts it in the error budget."

Then box 3, transduction: "Now, finally, physics becomes electricity —
capacitance, resistance, charge. Lecture 4 is about how; Lectures 5 to 11 are
about which."
"""),
    ("Through the electronics", 5, """
TIMING: 0:17–0:20.

Box 4 — conditioning: amplify, filter, level-shift. Say the words "anti-alias
filter" now and flag it: "Remember this box. We come back to it at the end of
the hour and it will cost somebody a motor."

Box 5 — sampling and quantisation: "Two separate things happen here and students
merge them for years. Sampling chops time. Quantisation chops amplitude. They
fail differently."
"""),
    ("The full chain", 7, """
TIMING: 0:20–0:22. The complete spine of the course.

Box 6 — codes to units: "The sensor never outputs acceleration. It outputs an
integer. Somebody multiplies it by a number from a datasheet. If that number is
wrong, everything downstream is confidently wrong." (Misconception M4.)

Box 7 — timestamp and decision: "An unstamped sample is nearly worthless. If you
cannot say when it was taken, you cannot compute a frequency — and frequency is
what tells you the bearing is dying."

Say plainly: "This diagram is the syllabus. Sixteen lectures, and every one of
them lives in one of these boxes."
"""),
]
for title, upto, note in build_notes:
    s = S()
    heading(s, title, "The measurement chain" if upto > 1 else None)
    chain(s, Inches(2.5), upto=upto)
    D.notes(s, note)


# ───────────────────────────────────────────────────────── 15  chain with numbers
s = S()
heading(s, "The same chain, with real numbers",
        "One 0.9 mg vibration, all the way to a decision")
chain(s, Inches(2.62), upto=7,
      values={1: "0.9 mg", 2: "0.6 mg", 3: "1.4 mV",
              5: "code 8412", 6: "0.61 mg"})
box(s, M, Inches(6.12), CONTENT_W, Inches(0.62),
    "Notice stage 2: the mechanical path already lost a third of the signal — "
    "before a single electron moved.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 0:22–0:23. Walk the numbers left to right, then down and back.

The teaching beat is the 0.9 → 0.6 mg step. Ask: "Which of these numbers would
appear in a datasheet?" Answer: only the ones inside boxes 3 to 6. The 33 % loss
in box 2 is invisible to every datasheet ever written, and it is the integrator's
problem — yours.

Then: "Now hold on to that, because I want to test whether you believe it."
""")


# ───────────────────────────────────────────────────────── 16  where it dies
s = S()
heading(s, "Where the truth dies", "and whether you can ever get it back")
rows = [
    ["Stage", "What is lost", "Recoverable later?"],
    ["2  Mechanical coupling", "amplitude and phase, frequency-dependent", "No — measure it yourself"],
    ["3  Transduction", "cross-axis leakage, nonlinearity, temperature drift", "Partly — by calibration"],
    ["4  Conditioning", "saturation clips peaks; wrong filter kills the signal", "No"],
    ["5  Sampling", "everything above half the sample rate, aliased in", "Never"],
    ["5  Quantisation", "detail below one LSB", "Partly — averaging"],
    ["6  Scaling to units", "accuracy, if the sensitivity constant is wrong", "Yes — recompute"],
    ["7  Timestamping", "the time axis, and therefore all frequency content", "No"],
]
table(s, M, Inches(2.1), CONTENT_W, rows, [0.27, 0.44, 0.29], size=16,
      row_h=Inches(0.52), head_size=16)
txt(s, "Three of these are permanent. Design decisions, not calibration problems.",
    M, Inches(6.5), CONTENT_W, Inches(0.4), 18, RED, bold=True)
D.notes(s, """
TIMING: 0:23–0:24. Do NOT read the whole table. Read the right-hand column only.

The word to land on is "Never" in the sampling row. Circle it with the cursor.
"This is the only 'never' on the slide. Remember which row it is on."

That is the third and last time you plant the aliasing seed before the reveal.
""")


# ───────────────────────────────────────────────────────── 17–18  poll 2
opts2 = [("A", "Digitisation — 16 bits cannot support three decimal places"),
         ("B", "Unit conversion — mg was never converted to m/s²"),
         ("C", "Mechanical coupling — the rubber pad filters the vibration before "
               "any electronics see it"),
         ("D", "No stage — 0.061 mg resolution guarantees the digits are meaningful")]
q2 = ("An accelerometer with 0.061 mg resolution is bolted to a motor housing "
      "through a 5 mm rubber pad. Which stage has already destroyed the accuracy "
      "of the reported number?")
s = poll(D, 2, q2, opts2, minute=24,
         note="Vote alone first. Then find someone who disagrees with you.")
D.notes(s, """
TIMING: 0:24–0:28. First real ConcepTest. TARGET 40–60 % first vote.

PEER INSTRUCTION PROTOCOL — run it properly:
  1. Silent individual vote. 45 s. Everyone commits.
  2. "Find someone with a different answer. 90 seconds. Convince them."
  3. Re-vote. Announce both percentages out loud.

IF >70 % FIRST VOTE: skip discussion, take one justification, move on.
IF <30 %: do not discuss. Redraw the rubber pad as a low-pass filter sitting
between the measurand and the proof mass, then re-vote.

RECORD BOTH NUMBERS.
""")
s = poll(D, 2, q2, opts2, minute=24, correct="C", reveal=True,
         note="The measurement chain begins before the sensor. If the mechanical path "
              "lies to the proof mass, no downstream precision recovers the truth.")
D.notes(s, """
Reveal. Then close the loop on each distractor — 20 seconds each, no longer:

A — confuses resolution with accuracy. 16 bits is plenty; that was never the issue.
B — a real bug, but it changes the SCALE of the answer, not its VALIDITY.
D — the exact misconception this course exists to remove: fine resolution on a
    corrupted signal gives you a precise wrong answer.

Then: "This is why Lecture 5 specifies mounting orientation and Lecture 16
specifies mechanical location. They are not housekeeping. They are link one."
""")


# ───────────────────────────────────────────────────────── 19  statement
s = statement(D, "The chain begins before\nthe sensor.",
              "Your instrument includes the bolt, the bracket and the housing. "
              "None of them are in the datasheet, and all of them are yours.",
              eyebrow_text="hold on to this")
D.notes(s, """
TIMING: 0:28. Five seconds of silence on this slide. Let it land, then move.
""")


# ───────────────────────────────────────────────────────── 20  section C2
s = section(D, "chunk 2  ·  minutes 26–44", "Why micro is different",
            ["You have spent three years building intuition on machines you can hold.",
             "At the micrometre scale, half of that intuition inverts. Here is which half."],
            minute="26:00")
D.notes(s, "TIMING: 0:28–0:29. Section marker, 15 seconds.")


# ───────────────────────────────────────────────────────── 21  what is inside
s = S()
heading(s, "What is actually inside", "A capacitive MEMS accelerometer, in cross-section")
# fixed plates
box(s, Inches(3.4), Inches(2.35), Inches(6.4), Inches(0.42), "FIXED PLATE",
    fill=GRAY_L, edge=GRAY, size=13, bold=True, shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(3.4), Inches(4.62), Inches(6.4), Inches(0.42), "FIXED PLATE",
    fill=GRAY_L, edge=GRAY, size=13, bold=True, shape=MSO_SHAPE.RECTANGLE)
# proof mass
box(s, Inches(4.6), Inches(3.28), Inches(4.0), Inches(0.86), "PROOF MASS  m",
    fill=TEAL_L, edge=TEAL, size=18, bold=True, edge_w=2, shape=MSO_SHAPE.RECTANGLE)
# springs as zigzags
for sx in (Inches(3.55), Inches(8.75)):
    zig = []
    for i in range(9):
        zig.append((Emu(int(sx + (Inches(0.85) if i % 2 else Inches(0.15)))),
                    Emu(int(Inches(3.3) + Inches(0.105) * i))))
    curve(s, zig, TEAL, 2.0)
txt(s, "suspension\nbeams,  k", Inches(2.55), Inches(3.35), Inches(1.0), Inches(0.8),
    13, TEAL, bold=True, align=PP_ALIGN.RIGHT, line=1.2)
txt(s, "suspension\nbeams,  k", Inches(9.75), Inches(3.35), Inches(1.1), Inches(0.8),
    13, TEAL, bold=True, line=1.2)
# gaps
for gy, lbl in ((Inches(2.90), "gap  d ≈ 1–2 µm"), (Inches(4.22), "gap  d")):
    txt(s, lbl, Inches(9.95), gy, Inches(2.6), Inches(0.3), 14, AMBER,
        bold=True, font=MONO)
    a = s.shapes.add_shape(MSO_SHAPE.LEFT_BRACE, Inches(9.72), gy - Inches(0.06),
                           Inches(0.18), Inches(0.36))
    a.fill.background(); a.line.color.rgb = AMBER; a.line.width = Pt(1.25)
    a.shadow.inherit = False
rich(s, M, Inches(5.42), CONTENT_W, Inches(1.4),
     [[("Acceleration moves the mass. Movement changes both gaps — one grows, one "
        "shrinks — and the differential capacitance ", {"size": 18}),
       ("C = εA/d", {"font": MONO, "bold": True, "size": 18, "color": TEAL}),
       (" is the signal.", {"size": 18})],
      [("That is the whole device — everything in the datasheet is a consequence of ",
        {"size": 18, "color": GRAY}),
       ("m", {"font": MONO, "bold": True, "size": 18, "color": GRAY}),
       (", ", {"size": 18, "color": GRAY}),
       ("k", {"font": MONO, "bold": True, "size": 18, "color": GRAY}),
       (" and ", {"size": 18, "color": GRAY}),
       ("d", {"font": MONO, "bold": True, "size": 18, "color": GRAY}),
       (".", {"size": 18, "color": GRAY})]])
D.notes(s, """
TIMING: 0:29–0:33. Draw attention to three symbols only: m, k, d.

"A mass on springs between two plates. That is a MEMS accelerometer. If you
understood the spring-mass system in mechanics, you already understand the
device — what you do not yet have is intuition for what happens when you make
it a thousand times smaller."

The 1–2 µm gap is worth a beat: "That gap is smaller than a red blood cell.
It is also why a speck of dust in the package is a catastrophe, and why
Lecture 4 spends its time on packaging rather than lithography."

Do NOT derive the transfer function. That is Lecture 5.
""")


# ───────────────────────────────────────────────────────── 22  scaling exponents
s = S()
heading(s, "Shrink every dimension by the same factor",
        "Isotropic scaling: length, width, thickness — all by factor s")
pairs = [("m  ∝  L³", "mass scales with volume", TEAL),
         ("k  ∝  L¹", "beam stiffness  k = E·w·t³ / 4L³", AMBER)]
x = M
for expr, sub, col in pairs:
    box(s, x, Inches(2.25), Inches(5.75), Inches(1.35), expr, fill=WHITE,
        edge=col, tcolor=col, size=42, bold=True, font=MONO, edge_w=2.5)
    txt(s, sub, x + Inches(0.1), Inches(3.78), Inches(5.6), Inches(0.6), 18,
        GRAY, font=MONO)
    x += Inches(6.1)
box(s, M, Inches(4.62), CONTENT_W, Inches(1.05),
    "They do not scale together.  That single fact is the whole lecture.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=25, bold=True)
txt(s, "Substitute w, t and L all by the same factor s into k = E·w·t³/4L³ and you get "
       "s·s³/s³ = s. Stiffness falls linearly. Mass falls cubically.",
    M, Inches(5.95), CONTENT_W, Inches(0.9), 17, GRAY, line=1.35)
D.notes(s, """
TIMING: 0:33–0:36. Slow down. This is the load-bearing slide of the lecture.

Do the substitution on the board, out loud, even though it is on the slide:
  k = E·w·t³ / 4L³   →   (s)(s³)/(s³)  =  s

"Mass goes as the cube. Stiffness goes as the first power. Students assume they
cancel. They do not, and the gap between them is where MEMS lives."

Write k ∝ L¹ and m ∝ L³ on the physical board and LEAVE THEM THERE for the
rest of the lecture. You will point at them again during Poll 3.
""")


# ───────────────────────────────────────────────────────── 23  f0
s = S()
heading(s, "So the resonant frequency rises")
rich(s, M, Inches(2.15), CONTENT_W, Inches(1.2),
     [[("f₀  =  (1/2π) · √(k/m)   ∝   √( L¹ / L³ )   =   √( L⁻² )   =   1 / L",
        {"font": MONO, "bold": True, "size": 30, "color": INK})]],
     align=PP_ALIGN.CENTER)
box(s, M, Inches(3.5), CONTENT_W, Inches(0.9),
    "Shrink the device by 10  →  its resonant frequency rises by 10",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=24, bold=True)
rows = [["Device", "Typical size", "Resonance"],
        ["Bridge span", "100 m", "≈ 0.2 Hz"],
        ["Tuning fork", "10 cm", "≈ 440 Hz"],
        ["MEMS accelerometer", "300 µm", "≈ 5 kHz"],
        ["MEMS gyroscope drive", "100 µm", "≈ 20 kHz"],
        ["MEMS RF resonator", "10 µm", "≈ 100 MHz+"]]
table(s, M, Inches(4.65), Inches(7.6), rows, [0.46, 0.27, 0.27], size=16,
      row_h=Inches(0.40), mono_cols=(1, 2))
txt(s, "This is why MEMS can\nmeasure fast things.\n\nA sensor cannot report\nsignals near its own\nresonance — so a high\nf₀ is what buys you\nbandwidth.",
    M + Inches(8.05), Inches(4.68), Inches(3.9), Inches(2.0), 16, INK, line=1.32)
D.notea = None
D.notes(s, """
TIMING: 0:36–0:39.

Walk the algebra once: √(L/L³) = √(L⁻²) = 1/L. Then the table, top to bottom —
five orders of magnitude in size, eight in frequency.

The right-hand column is the engineering payoff and it is what connects to
Lecture 2: bandwidth. "A high resonant frequency is not a curiosity. It is the
reason you can put an accelerometer on a bearing at all."

Then set up the poll: "Now — you have the two exponents. Use them."
""")


# ───────────────────────────────────────────────────────── 24–25  poll 3
opts3 = [("A", "Resonant frequency rises ×10, and thermomechanical noise gets worse"),
         ("B", "Resonant frequency falls ×10, and noise improves because it is smaller"),
         ("C", "Resonant frequency is unchanged — mass and stiffness both shrink, "
               "so the ratio is constant"),
         ("D", "Resonant frequency rises ×10, and noise improves because there is "
               "less material to vibrate")]
q3 = ("A MEMS accelerometer's proof mass and suspension beams are all scaled down "
      "by a factor of 10. Which statement is true?")
s = poll(D, 3, q3, opts3, minute=40,
         note="The hardest question of the lecture. Use the two exponents on the "
              "board, not your intuition.")
D.notes(s, """
TIMING: 0:39–0:43. HARDEST ITEM. TARGET 30–50 % first vote.

Full peer instruction. Script for step 2:
  "Find someone who voted differently. 90 seconds. Convince them using
   k ∝ L and m ∝ L³ — not using your intuition about small things."

C IS THE TRAP and it is a good-faith error: it assumes k and m scale together.
Point at the board. k ∝ L¹, m ∝ L³, so k/m ∝ L⁻², so f₀ ∝ 1/L.

IF <20 % CORRECT AFTER THE RE-VOTE: stop and derive it in three lines on the
board, then vote a third time. This concept is load-bearing for Lectures 5, 6
and 11 — four extra minutes here is a good trade.

RECORD BOTH NUMBERS. If this lands above 70 % first vote, your scaling chunk
was too explicit — note it and compress next year.
""")
s = poll(D, 3, q3, opts3, minute=40, correct="A", reveal=True,
         note="Thermomechanical noise ∝ √(4kBT·ω₀ / mQ) — it rises as the proof mass "
              "falls. You buy bandwidth and you pay in noise floor.")
D.notes(s, """
Reveal, then explain the trade honestly — this is the most intellectually
satisfying two minutes of the lecture:

"Why doesn't everyone just make them smaller? Because the proof mass is what
averages out the thermal buffeting of the gas molecules around it. Smaller mass,
larger Brownian noise-equivalent acceleration. You are trading noise floor for
bandwidth, and the datasheet will make you choose."

Do not write out the full noise formula on the board. The proportionality —
noise up as m goes down — is the whole content.

Then: "So when you read a noise-density figure in Lecture 2, you now know what
it costs to make it smaller."
""")


# ───────────────────────────────────────────────────────── 26  what improves/worsens
s = S()
heading(s, "Smaller is not uniformly better", "The honest ledger of shrinking a device")
box(s, M, Inches(2.1), Inches(5.8), Inches(0.68), "GETS BETTER", fill=TEAL,
    edge=TEAL, tcolor=CREAM, size=18, bold=True)
box(s, M + Inches(6.35), Inches(2.1), Inches(5.8), Inches(0.68), "GETS WORSE",
    fill=RED, edge=RED, tcolor=CREAM, size=18, bold=True)
good = ["Bandwidth — f₀ ∝ 1/L", "Response time and thermal settling",
        "Power per device", "Cost per device at volume",
        "Batch fabrication: thousands per wafer"]
bad = ["Thermomechanical noise floor ∝ 1/√m", "Stiction — surface forces beat body forces",
       "Sensitivity to packaging stress", "Temperature drift and offset stability",
       "Contamination: a dust speck is fatal"]
for i, (g, b2) in enumerate(zip(good, bad)):
    y = Inches(3.0) + i * Inches(0.66)
    txt(s, "▸  " + g, M + Inches(0.05), y, Inches(5.7), Inches(0.6), 18, INK, line=1.25)
    txt(s, "▸  " + b2, M + Inches(6.40), y, Inches(5.7), Inches(0.6), 18, INK, line=1.25)
box(s, M, Inches(6.24), CONTENT_W, Inches(0.58),
    "Surface area / volume  ∝  1 / L   —   at small scale the world is all surface.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True, font=MONO)
D.notes(s, """
TIMING: 0:43–0:44. 60 seconds. Read only the right-hand column aloud.

The A/V line at the bottom is the unifying idea: gravity and inertia are volume
effects, friction and adhesion and surface tension are area effects. Shrink, and
the area effects win. That is stiction, and it is why a MEMS device can weld
itself shut.

"A macroscopic engineer worries about mass. A MEMS engineer worries about
surfaces."
""")


# ───────────────────────────────────────────────────────── 27  state change
s = S(bg=DARK)
eyebrow(s, "minute 44  ·  everybody stands up", AMBER)
txt(s, "Slides off. Paper out.", M, Inches(1.75), Inches(11), Inches(1), 40,
    CREAM, bold=True)
steps = [("1", "Stand up. Actually stand."),
         ("2", "In pairs, one sheet: redraw the measurement chain from memory. "
               "Every box, every arrow. 90 seconds."),
         ("3", "Mark an X on every box where the motor's number could have been ruined.")]
y = Inches(3.1)
for n, t in steps:
    box(s, M, y, Inches(0.62), Inches(0.62), n, fill=AMBER, edge=AMBER,
        tcolor=DARK, size=22, bold=True, font=MONO)
    txt(s, t, M + Inches(0.95), y + Inches(0.06), Inches(10.4), Inches(0.9), 21,
        CREAM, line=1.3)
    y += Inches(1.08)
txt(s, "Keep this sheet. You will use it at the bench in Week 2.",
    M, Inches(6.4), CONTENT_W, Inches(0.4), 18, TEAL, bold=True)
D.notes(s, """
TIMING: 0:44–0:48. DO NOT SKIP THIS AND DO NOT SHORTEN IT BELOW 3 MINUTES.

Genuinely make them stand — posture change is half the effect. Then slides
BLANK (press B in most presenters) so recall is unaided. Free recall with the
screen off is far stronger than any amount of re-reading.

Walk the room. You will see which boxes are missing across the whole cohort —
that is live diagnostic data, and for a first offering it is gold. Note the two
most commonly forgotten boxes.

Then show the next slide and have them self-correct in a different colour.
They keep the sheet; it is their reference page for Lab 1.
""")


# ───────────────────────────────────────────────────────── 28  correct chain
s = S()
heading(s, "Check your sheet", "Correct in a different colour — do not rewrite it")
chain(s, Inches(2.5), upto=7)
txt(s, "Two boxes are forgotten more than any others: mechanical coupling, and "
       "timestamping.\nBoth are invisible in a datasheet. Both are yours.",
    M, Inches(6.18), CONTENT_W, Inches(0.7), 17, AMBER, italic=True, line=1.3)
D.notes(s, """
TIMING: 0:48. 45 seconds. Self-correction in a second colour is the point —
seeing your own gap is what makes it stick.

Name the two commonly missed boxes (adjust to what you actually saw while
walking the room — that is better data than my prediction).
""")


# ───────────────────────────────────────────────────────── 29  section C3
s = section(D, "chunk 3  ·  minutes 48–66", "From a wish to a specification",
            ["Nobody will ever hand you a specification. They will hand you a sentence",
             "like the one on the next slide, and expect an instrument at the end of it."],
            minute="48:00")
D.notes(s, "TIMING: 0:48–0:49. Section marker.")


# ───────────────────────────────────────────────────────── 30  the wish
s = statement(D, "“Just tell me if the motor\nis vibrating too much.”",
              "This is what a request actually looks like. It contains no quantity, "
              "no range, no bandwidth, no accuracy and no environment. "
              "It is not yet an engineering problem.",
              eyebrow_text="the client says", size=38)
D.notes(s, """
TIMING: 0:49–0:50.

Read it in a slightly bored managerial voice. Then: "There is not one number in
that sentence. Until there is, you cannot buy anything, you cannot design
anything, and you certainly cannot be held to anything."

"So here is the interrogation."
""")


# ───────────────────────────────────────────────────────── 31  the seven questions
s = S()
heading(s, "Seven questions that turn a wish into a specification")
qs = [("QUANTITY", "What physical variable, in what units?"),
      ("RANGE", "Smallest and largest value that must be reported?"),
      ("RESOLUTION", "Smallest change that must be distinguishable?"),
      ("ACCURACY", "How wrong is a reading allowed to be — and over what temperature?"),
      ("BANDWIDTH", "How fast does it change? What is the highest frequency that matters?"),
      ("ENVIRONMENT", "Temperature, humidity, vibration, EMI, supply, power budget?"),
      ("OUTPUT", "Who consumes the number, in what form, how often, timestamped how?")]
y = Inches(2.05)
for i, (k, v) in enumerate(qs):
    col = AMBER if k == "BANDWIDTH" else TEAL
    box(s, M, y, Inches(2.75), Inches(0.60), k, fill=col if k == "BANDWIDTH" else WHITE,
        edge=col, tcolor=CREAM if k == "BANDWIDTH" else col, size=16, bold=True)
    txt(s, v, M + Inches(3.05), y + Inches(0.13), Inches(8.9), Inches(0.55), 19,
        INK)
    y += Inches(0.68)
txt(s, "One of these seven killed the motor. You already know which one.",
    M, Inches(6.72), CONTENT_W, Inches(0.4), 16, AMBER, bold=True, italic=True)
D.notes(s, """
TIMING: 0:50–0:54. Four minutes. Do not lecture all seven — read the headings,
expand only on ACCURACY and BANDWIDTH.

ACCURACY: "Notice the second half of the question — 'over what temperature'.
An accuracy figure without a temperature range is marketing, not engineering."
(This is the direct set-up for Lecture 2.)

BANDWIDTH is highlighted deliberately. Do not explain why yet. If a student
asks, say "good instinct — hold it for ten minutes."

Tell them this list is the semester project's first deliverable and that they
will use it in every lab.
""")


# ───────────────────────────────────────────────────────── 32  worked spec
s = S()
heading(s, "The same request, specified", "Now it is something you can order against")
rows = [["", "Specification", "Where the number came from"],
        ["Quantity", "housing acceleration, m/s² RMS", "vibration is what a bearing radiates"],
        ["Range", "±16 g", "impact transients, not steady vibration"],
        ["Resolution", "≤ 5 mg", "earliest detectable fault ≈ 30 mg"],
        ["Accuracy", "±5 % of reading, 0–70 °C", "trend detection, not absolute metrology"],
        ["Bandwidth", "≥ 4 kHz, anti-aliased", "bearing signature spans 1–4 kHz"],
        ["Environment", "0–70 °C, 24 V rail, oily, EMI from a VFD", "the motor's actual cabinet"],
        ["Output", "RMS + spectrum, 1 Hz, timestamped ±1 ms", "so a frequency can be computed"]]
table(s, M, Inches(2.1), CONTENT_W, rows, [0.17, 0.38, 0.45], size=15.5,
      row_h=Inches(0.50), head_size=15.5)
txt(s, "Seven lines. This is the deliverable — not a part number.",
    M, Inches(6.45), CONTENT_W, Inches(0.4), 19, TEAL, bold=True)
D.notes(s, """
TIMING: 0:54–0:58. Build this live if you can — reveal the middle column row by
row and ask the room for each number before showing it.

The third column is the pedagogical point: EVERY specification number has a
justification. A spec line without a reason is a guess wearing a suit.

Note the bandwidth row out loud, then say nothing more about it.

"Notice what is NOT on this slide: a manufacturer, a part number, a price. Those
come after. Lecture 2 is entirely about what happens next."
""")


# ───────────────────────────────────────────────────────── 33  your turn
s = S()
heading(s, "Your turn", "Four minutes, in pairs — write the seven lines")
box(s, M, Inches(2.15), CONTENT_W, Inches(1.25),
    "“The drone keeps drifting up and down. Make it hold its altitude properly.”",
    fill=DARK, edge=DARK, tcolor=CREAM, size=26, bold=True)
cols = [("Start here", "What is the physical quantity?\nIt is probably not altitude."),
        ("The hard one", "What bandwidth? How fast does\na drone's altitude actually change?"),
        ("The trap", "What is the RANGE — and is it the\nsame as the RESOLUTION you need?")]
x = M
for t, b3 in cols:
    box(s, x, Inches(3.75), Inches(3.85), Inches(0.6), t, fill=AMBER, edge=AMBER,
        tcolor=DARK, size=16, bold=True)
    txt(s, b3, x + Inches(0.1), Inches(4.55), Inches(3.7), Inches(1.3), 18, INK,
        line=1.35)
    x += Inches(4.0)
txt(s, "You will not finish all seven lines. Get three right.",
    M, Inches(6.3), CONTENT_W, Inches(0.4), 18, GRAY, italic=True)
D.notes(s, """
TIMING: 0:58–1:02. Pairs, 4 minutes. Circulate; do not answer, redirect.

THE INTENDED INSIGHT: the measurand is not altitude — it is barometric
PRESSURE, and altitude is derived. That reframing is the whole exercise, and it
previews Lab 5 directly.

THE TRAP is range vs resolution: range might be 950–1050 hPa (weather), while
the resolution needed for ±0.5 m is about 0.06 hPa. Four orders of magnitude
apart. Students routinely conflate these two, and the exit ticket will show you
exactly how many still do.

If a pair finishes early: "now tell me what happens to your altitude reading
when a door opens in the room."
""")


# ───────────────────────────────────────────────────────── 34–35  poll 4
opts4 = [("A", "Full-scale range ≥ ±16 g"),
         ("B", "Bandwidth ≥ 4 kHz, sample rate ≥ 8 kHz, with anti-alias filtering"),
         ("C", "Resolution ≤ 0.1 mg"),
         ("D", "Operating temperature up to 85 °C")]
q4 = ("Bearing fault energy appears between 1 and 4 kHz. Which single "
      "specification line decides whether your system can work at all?")
s = poll(D, 4, q4, opts4, minute=62,
         note="Every one of these four is a real requirement. Only one of them, if you "
              "get it wrong, makes the system incapable rather than merely imperfect.")
D.notes(s, """
TIMING: 1:02–1:05. Transfer poll. TARGET 55–75 % — this one should be gettable.

Short peer instruction: 60 seconds, then re-vote.

The framing in the note line is the actual learning objective: engineering
judgement is knowing which specification line is FATAL versus merely
SUBOPTIMAL. All four matter. Only one of them decides feasibility.

Then: "Hold that answer. We are going back to the motor."
""")
s = poll(D, 4, q4, opts4, minute=62, correct="B", reveal=True,
         note="A, C and D are all genuine requirements — get them wrong and the system is "
              "imperfect. Get B wrong and the system is blind.")
D.notes(s, """
Reveal briefly — 45 seconds. Do not over-explain; the next four slides do the
explaining.

"Range too small: you clip the peaks. Resolution too coarse: you miss small
faults. Temperature too low: it dies in the cabinet. All bad. All survivable.
Bandwidth too low: you are not measuring the thing you think you are measuring
at all. Let me show you."
""")


# ───────────────────────────────────────────────────────── 36  project brief
s = S()
heading(s, "The semester project", "Deliverable 1 is due before Lecture 3")
box(s, M, Inches(2.1), Inches(5.85), Inches(0.68), "WHAT YOU WILL BUILD",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=17, bold=True)
txt(s, "A multi-sensor embedded system that\nmeasures something real, calibrated,\n"
       "filtered, timestamped, validated against\nstated requirements — and honest about\nits own limitations.",
    M + Inches(0.08), Inches(3.0), Inches(5.7), Inches(2.2), 19, INK, line=1.4)
box(s, M + Inches(6.35), Inches(2.1), Inches(5.85), Inches(0.68),
    "DELIVERABLE 1  ·  ONE PAGE", fill=AMBER, edge=AMBER, tcolor=DARK,
    size=17, bold=True)
txt(s, "The seven specification lines, for a\nmeasurement problem you choose.\n\n"
       "No part numbers. No circuit. No code.\nJust the seven lines — each with\nthe reason it has that value.",
    M + Inches(6.43), Inches(3.0), Inches(5.7), Inches(2.2), 18, INK, line=1.35)
box(s, M, Inches(5.72), CONTENT_W, Inches(0.75),
    "Teams of 2–3. Same teams as the laboratory. Choose your measurand this week.",
    fill=GROUND, edge=GRAY, size=18, bold=True)
D.notes(s, """
TIMING: 1:05–1:07. Two minutes. Keep it short — the detail is in the handout.

The one thing to emphasise: deliverable 1 contains NO technology. Students will
want to write "STM32 + MPU6050". Refuse it. "If your first page names a part, you
have skipped the only step that cannot be undone later."

Teams are the lab teams — say this explicitly so Week 2 is not chaos.
""")


# ───────────────────────────────────────────────────────── 37  finger on the box
s = S()
heading(s, "Back to the motor", "Before I tell you — commit, physically")
chain(s, Inches(2.35), upto=7)
box(s, M, Inches(6.0), CONTENT_W, Inches(0.8),
    "Put your finger on the box where you now think this failed. Everyone. I am looking.",
    fill=AMBER_L, edge=AMBER, size=21, bold=True)
D.notes(s, """
TIMING: 1:07–1:08. Physical commitment beats a poll here — you can see the whole
room at once, and so can they.

Wait until every hand is on the paper. Genuinely wait. Then look around and
narrate what you see: "Most of you are on box 5. Some on box 2 — and after the
rubber pad question, I understand why."

Then: "Box 5. Sampling. Here are the numbers nobody wrote down."
""")


# ───────────────────────────────────────────────────────── 38  the numbers
s = S()
heading(s, "The three numbers from the post-mortem", rule=RED)
facts = [("1520 Hz", "the bearing fault signature", TEAL),
         ("100 Hz", "the sample rate somebody chose", RED),
         ("none", "anti-alias filter fitted", RED)]
x = M
for big, lab, col in facts:
    box(s, x, Inches(2.3), Inches(3.85), Inches(1.5), big, fill=WHITE, edge=col,
        tcolor=col, size=44, bold=True, font=MONO, edge_w=2.5)
    txt(s, lab, x + Inches(0.1), Inches(3.98), Inches(3.7), Inches(0.7), 18,
        INK, align=PP_ALIGN.CENTER, line=1.25)
    x += Inches(4.0)
box(s, M, Inches(5.0), CONTENT_W, Inches(1.0),
    "Sampling at 100 Hz, everything above 50 Hz is folded down into the band —\n"
    "and with no filter in front of the ADC, there was nothing to stop it.",
    fill=RED_L, edge=RED, size=21, bold=True)
txt(s, "Nyquist: to see 1520 Hz you need to sample above 3040 Hz. They sampled 30 times too slowly.",
    M, Inches(6.3), CONTENT_W, Inches(0.5), 18, INK, italic=True)
D.notes(s, """
TIMING: 1:08–1:10. Let the three numbers sit for a moment before you speak.

"1520 Hz of real, physical, destructive vibration. Sampled 100 times a second.
No filter."

State Nyquist plainly and move to the arithmetic — the next slide is where the
understanding actually happens.
""")


# ───────────────────────────────────────────────────────── 39  aliasing
s = S()
heading(s, "Where the 20 Hz line came from",
        "Drawn at 19 cycles per 20 samples so you can see it — the motor's ratio "
        "was 1520:100, identical arithmetic", rule=RED)
gx, gy, gw = M + Inches(0.15), Inches(3.75), Inches(8.5)
axis(s, gx, gy, gw, GRAY_L)
# the real signal: 19 cycles across the plot
curve(s, sine(gx, gy, gw, Inches(1.05), 19), TEAL, 1.25)
txt(s, "the real vibration  ·  19 cycles", gx, Inches(2.28), Inches(5),
    Inches(0.3), 15, TEAL, bold=True, font=MONO)
# 21 sample instants, evenly spaced: sin(2p*19*i/20) == -sin(2p*i/20) exactly
for i in range(21):
    frac = i / 20.0
    dot(s, Emu(int(gx + gw * frac)),
        Emu(int(gy - Inches(1.05) * math.sin(2 * math.pi * 19 * frac))), color=RED)
# what those samples reconstruct: exactly one inverted cycle
curve(s, sine(gx, gy, gw, Inches(1.05), 1, phase=math.pi), RED, 3.0,
      dash=MSO_LINE_DASH_STYLE.DASH)
txt(s, "what the samples reconstruct  ·  1 cycle", gx, Inches(4.95), Inches(6),
    Inches(0.3), 15, RED, bold=True, font=MONO)
txt(s, "red dots =\nthe only instants\nthe ADC looked",
    M + Inches(9.05), Inches(2.55), Inches(3.0), Inches(1.3), 16, RED, bold=True,
    line=1.3)
box(s, M + Inches(9.05), Inches(3.95), Inches(3.1), Inches(1.15),
    "| 1520 - 15x100 |\n=  20 Hz", fill=WHITE, edge=RED, tcolor=INK, size=19,
    bold=True, font=MONO, edge_w=2)
box(s, M, Inches(5.62), CONTENT_W, Inches(0.88),
    "The monitor was faithfully displaying the destruction of the bearing - "
    "relabelled as a slow load variation.",
    fill=RED_L, edge=RED, size=20, bold=True)
D.notes(s, """
TIMING: 1:10–1:13. THE INTELLECTUAL CENTRE OF THE LECTURE. Do not rush it.

Walk it: "Here is the real signal — fast, teal. Here are the only instants the
ADC ever looked — the red dots. Now: draw the smoothest curve you can through
just the dots." Trace the dashed red line with your hand.

"Twenty hertz. It is not noise, it is not a bug, it is not a broken sensor.
It is the arithmetic of looking too slowly."

Do the sum aloud: 15 × 100 = 1500. 1520 − 1500 = 20.

Then the killer detail — say it slowly: "The shaft turns at 1500 rpm, which is
25 Hz. So a 20 Hz component looked completely plausible to everyone who saw it."

That is why nobody caught it. The wrong answer was believable.
""")


# ───────────────────────────────────────────────────────── 40  the statement
s = statement(D, "Nothing was broken.\nEvery part met spec.\nThe system was never specified.",
              "Aliasing is permanent. No filter afterwards, no clever software, no "
              "machine learning recovers a frequency you failed to sample.",
              size=36, eyebrow_text="the verdict", accent=RED)
D.notes(s, """
TIMING: 1:13–1:14. Silence. Read it once, slowly. Do not add anything.

This is the sentence you want them to still have in Week 14.
""")


# ───────────────────────────────────────────────────────── 41  one line
s = S()
heading(s, "What was missing", "One line, in one document, that nobody wrote")
box(s, M, Inches(2.5), CONTENT_W, Inches(1.35),
    "Bandwidth:  ≥ 4 kHz, anti-aliased.    Sample rate:  ≥ 8 kHz.",
    fill=DARK, edge=TEAL, tcolor=CREAM, size=28, bold=True, font=MONO, edge_w=3)
txt(s, "One line. One motor.", M, Inches(4.15), CONTENT_W, Inches(0.5), 26, RED,
    bold=True)
rich(s, M, Inches(5.0), CONTENT_W, Inches(1.6),
     [[("This is also your answer to Poll 4 — option ", {"size": 20, "color": GRAY}),
       ("B", {"size": 20, "bold": True, "color": TEAL}),
       (". And it is the specification line you were asked to write "
        "fifteen minutes ago.", {"size": 20, "color": GRAY})],
      [("Lecture 3 is about how that line becomes an ADC configuration. "
        "Laboratory 2 is where you make aliasing happen with your own hands.",
        {"size": 20, "color": INK, "bold": True})]])
D.notes(s, """
TIMING: 1:14–1:15. Re-run POLL 1 here if you have 60 seconds — show the original
distribution next to the new one. The shift is the most persuasive thing you can
put on a screen in week one.

Then connect forward: "You will alias a signal deliberately in Lab 2, in week
four. It is much more fun when you do it on purpose."
""")


# ───────────────────────────────────────────────────────── 42  summary
s = S()
heading(s, "Four things to keep")
keeps = [("01", "A measurement is a chain, and it begins before the sensor.",
          "Bolt, bracket and housing are part of your instrument."),
         ("02", "Some losses are permanent.",
          "Aliasing and a missing timestamp cannot be repaired downstream."),
         ("03", "Shrinking a device is a trade, not an improvement.",
          "k ∝ L, m ∝ L³, f₀ ∝ 1/L — bandwidth up, noise floor up too."),
         ("04", "The specification is the deliverable.",
          "Seven lines, each with a reason. Part numbers come afterwards.")]
y = Inches(2.05)
for n, t, sub in keeps:
    txt(s, n, M, y, Inches(0.75), Inches(0.5), 24, TEAL_L, bold=True, font=MONO)
    txt(s, t, M + Inches(0.85), y - Inches(0.02), Inches(11.2), Inches(0.45), 22,
        INK, bold=True)
    txt(s, sub, M + Inches(0.85), y + Inches(0.42), Inches(11.2), Inches(0.4), 18,
        GRAY)
    y += Inches(1.12)
D.notes(s, """
TIMING: 1:15–1:16. Ninety seconds. Read the four bold lines only.
""")


# ───────────────────────────────────────────────────────── 43  exit ticket
s = S()
heading(s, "Exit ticket", "Anonymous. Hand it in at the door — both halves.")
box(s, M, Inches(2.15), Inches(5.85), Inches(0.7), "1  ·  ONE SPECIFICATION LINE",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=17, bold=True)
txt(s, "A drone must hold altitude to ±0.5 m.\n\nWrite ONE specification line for its\n"
       "pressure sensor — the line you think\nmatters most, with its number.",
    M + Inches(0.08), Inches(3.1), Inches(5.7), Inches(2), 20, INK, line=1.4)
box(s, M + Inches(6.35), Inches(2.15), Inches(5.85), Inches(0.7),
    "2  ·  MUDDIEST POINT", fill=AMBER, edge=AMBER, tcolor=DARK, size=17, bold=True)
txt(s, "What is the one thing from today you\nare least sure about?\n\nOne sentence. "
       "I will answer the three\nmost common at the start of Lecture 2.",
    M + Inches(6.43), Inches(3.1), Inches(5.7), Inches(2), 20, INK, line=1.4)
txt(s, "This is the first time this course has been taught. Your muddiest points genuinely "
       "change what happens next week.",
    M, Inches(5.85), CONTENT_W, Inches(0.6), 18, TEAL, bold=True, italic=True)
D.notes(s, """
TIMING: 1:16–1:18.

The bottom line is true and students respond to it — say it out loud. Honesty
about a first offering buys you far better data than pretending to authority.

COLLECT THESE AND KEEP THEM. Transcribe the muddiest points into one list. Open
Lecture 2 by answering the top three in 90 seconds, referring to concepts and
never to students. This single habit does more for your credibility than
anything else in the first month.
""")


# ───────────────────────────────────────────────────────── 44  lab bridge
s = S()
heading(s, "Week 2: Laboratory 1", "Datasheet to data — and yes, it is before the theory")
rows = [["At the bench you will", "Which chain stage"],
        ["Read supply and logic levels from the datasheet BEFORE applying power",
         "before stage 1"],
        ["Wire one I²C sensor to the Nucleo board, with pull-ups", "stage 3 → 5"],
        ["Prove the device is the device you think it is  (device-ID register)", "stage 5"],
        ["Configure a full-scale range and an output data rate", "stage 5"],
        ["Convert raw two's-complement codes to SI units — by hand", "stage 6"],
        ["Prove the number is true: one axis must read ≈ 9.81 m/s² at rest", "stage 6"]]
table(s, M, Inches(2.05), CONTENT_W, rows, [0.72, 0.28], size=16, 
      row_h=Inches(0.455), head_size=16)
box(s, M, Inches(5.40), CONTENT_W, Inches(0.62),
    "No programming. The boards are already flashed — you drive the sensor from a "
    "serial console.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=19, bold=True)
box(s, M, Inches(6.14), CONTENT_W, Inches(0.72),
    "The pre-lab sheet is a gate: no signed pre-lab, no power to your board.\n"
    "It carries a one-page I²C primer and the console reference — read it before Tuesday.",
    fill=AMBER_L, edge=AMBER, size=17, bold=True)
D.notes(s, """
TIMING: 1:18–1:19. THE AGREED MITIGATION for the ordering problem — Lab 1 runs
a week before Lecture 3 teaches digital interfaces. Do not skip this slide.

Be explicit and disarming about it: "You have not been taught I²C yet, and you
have not been taught to program this board yet. Neither is an accident. The
boards are already flashed with a console: you will type register addresses that
YOU took from the datasheet, and you will do the arithmetic yourself. You write
firmware later in the semester."

Say the last part plainly — some students will have been dreading exactly that,
and a few will be disappointed. Both are worth defusing in week one.

Emphasise the gate. It exists to stop somebody putting 5 V on a 1.8 V part.

Point at the right-hand column: every bench action maps to a box in today's
diagram. That is why they keep the sketch.
""")


# ───────────────────────────────────────────────────────── 45  close
s = S(bg=DARK)
eyebrow(s, "next", TEAL)
txt(s, "Lecture 2", M, Inches(1.4), Inches(11), Inches(0.8), 40, CREAM, bold=True)
txt(s, "Sensor specifications and datasheet-based selection",
    M, Inches(2.25), Inches(11), Inches(0.6), 26, TEAL, bold=True)
txt(s, "Bring a laptop or a printed datasheet. We are going to find a number that "
       "decides a design — and it will not be on the front page.",
    M, Inches(3.1), Inches(10.5), Inches(1), 21, RGBColor(0xB8, 0xC0, 0xC6), line=1.35)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, Inches(4.4), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "BEFORE NEXT WEEK", M, Inches(4.72), Inches(11), Inches(0.35), 14, AMBER,
    bold=True)
txt(s, "1 ·  Formative quiz (6 questions, ungraded) — posted tonight\n"
       "2 ·  Pre-lab sheet for Laboratory 1, including the I²C primer\n"
       "3 ·  Project deliverable 1: your seven specification lines\n"
       "4 ·  Reading: Fraden, Handbook of Modern Sensors — Ch. 1–2",
    M, Inches(5.12), Inches(11), Inches(1.7), 18, CREAM, line=1.45)
D.notes(s, """
TIMING: 1:19–1:20. Do not overrun. End on time in week one and they will
believe you for fifteen more weeks.

Last words: "Next week, two datasheets, and most of this room is going to
choose the wrong part. I am looking forward to it."
""")


out = "../lecture-01/output/L1-MEMS-measurement-system-architecture.pptx"
D.save(out)
print(f"saved {out} — {len(D.p.slides.__iter__.__self__._sldIdLst)} slides")
