"""Lecture 4 — MEMS structures, transduction, fabrication and packaging (80 min).

Minute markers stay OFF (deck.SHOW_MINUTES is False). Timings live in the speaker
notes and in lecture-04/output/lecture-plan.md, never on the screen.
"""
import math
from deck import *

D = Deck("MEMS & Sensors  ·  Lecture 4  ·  Structures, transduction, fabrication and packaging")
S = D.slide


# ---------------------------------------------------------------- local furniture
def structure_card(s, x, y, w, title, relation, senses, example, edge=TEAL,
                   h=Inches(2.55), note=None, note_col=AMBER):
    """One of the five canonical structures, as a card."""
    card = box(s, x, y, w, h, "", fill=WHITE, edge=edge, edge_w=2,
               shape=MSO_SHAPE.RECTANGLE)
    box(s, x, y, w, Inches(0.54), title, fill=edge, edge=edge, tcolor=CREAM,
        size=17, bold=True, shape=MSO_SHAPE.RECTANGLE)
    box(s, x + Inches(0.16), y + Inches(0.72), w - Inches(0.32), Inches(0.52),
        relation, fill=GROUND, edge=edge, tcolor=INK, size=15, bold=True,
        font=MONO, shape=MSO_SHAPE.RECTANGLE, edge_w=1)
    yy = y + Inches(1.40)
    for k, v in (("SENSES", senses), ("IN THIS COURSE", example)):
        txt(s, k, x + Inches(0.16), yy, Inches(1.62), Inches(0.28), 11, GRAY,
            bold=True)
        txt(s, v, x + Inches(1.86), yy - Inches(0.04), w - Inches(2.02),
            Inches(0.36), 15, INK)
        yy += Inches(0.42)
    if note:
        box(s, x + Inches(0.16), y + h - Inches(0.60), w - Inches(0.32),
            Inches(0.44), note, fill=note_col, edge=note_col, tcolor=DARK,
            size=12.5, bold=True)
    return card


def principle_card(s, x, y, w, title, static, signal, weakness, explains,
                   edge=TEAL, static_col=TEAL, h=Inches(3.42)):
    """One of the six transduction principles. The static badge is the discriminator."""
    card = box(s, x, y, w, h, "", fill=WHITE, edge=edge, edge_w=2,
               shape=MSO_SHAPE.RECTANGLE)
    box(s, x, y, w, Inches(0.56), title, fill=edge, edge=edge, tcolor=CREAM,
        size=18, bold=True, shape=MSO_SHAPE.RECTANGLE)
    box(s, x + Inches(0.16), y + Inches(0.74), w - Inches(0.32), Inches(0.48),
        "STATIC (DC) RESPONSE:   " + static, fill=static_col, edge=static_col,
        tcolor=DARK if static_col is AMBER else CREAM, size=14, bold=True)
    yy = y + Inches(1.40)
    for k, v in (("SIGNAL", signal), ("MAIN WEAKNESS", weakness),
                 ("EXPLAINS THE DATASHEET LINE", explains)):
        txt(s, k, x + Inches(0.16), yy, w - Inches(0.32), Inches(0.24), 10.5,
            GRAY, bold=True)
        txt(s, v, x + Inches(0.16), yy + Inches(0.24), w - Inches(0.32),
            Inches(0.52), 14.5, INK, line=1.2)
        yy += Inches(0.66)
    return card


# ───────────────────────────────────────────────────────── 1  title
s = S(bg=DARK, footer=False)
b = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.34), H)
b.fill.solid(); b.fill.fore_color.rgb = TEAL
b.line.fill.background(); b.shadow.inherit = False
txt(s, "MICROELECTROMECHANICAL SYSTEMS AND SENSORS", Inches(1.15), Inches(1.5),
    Inches(11), Inches(0.4), 15, TEAL, bold=True)
txt(s, "MEMS structures, transduction,\nfabrication and packaging",
    Inches(1.15), Inches(2.25), Inches(11.3), Inches(2.2), 40, CREAM, bold=True,
    line=1.15)
ln = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.15), Inches(4.72), Inches(1.5), Pt(4))
ln.fill.solid(); ln.fill.fore_color.rgb = AMBER
ln.line.fill.background(); ln.shadow.inherit = False
txt(s, "Lecture 4 of 16   ·   80 minutes   ·   Module A: Foundations",
    Inches(1.15), Inches(5.05), Inches(11), Inches(0.4), 18,
    RGBColor(0xB8, 0xC0, 0xC6))
txt(s, "Two weeks ago a question had no answer. Today you learn why — and what to "
       "do instead.",
    Inches(1.15), Inches(5.75), Inches(11.3), Inches(0.5), 17, GRAY)
D.notes(s, """
TIMING: 0:00. BEFORE THE BELL: have the L3 exit tickets in front of you, the
ISM330DHCX datasheet open at the zero-g level rows with the page number written
on your hand, and the twelve sets of sequencing cards counted out.

Write 8.73 mg on the physical board before anyone arrives and do not erase it.
You will point at it six times today.

Say the hook line out loud rather than reading it: "Lecture 2 ended with a
question I could not answer. That was deliberate. Today we open the box."

Then go straight to the muddiest points. Do not preamble.
""")


# ───────────────────────────────────────────────────────── 2  muddiest points
s = S()
heading(s, "Last week's muddiest points", "From Lecture 3's exit tickets — answered before we start")
for i, t in enumerate(["1", "2", "3"]):
    box(s, M, Inches(2.25) + i * Inches(1.05), Inches(0.62), Inches(0.62), t,
        fill=TEAL, edge=TEAL, tcolor=CREAM, size=22, bold=True, font=MONO)
    box(s, M + Inches(0.95), Inches(2.25) + i * Inches(1.05), Inches(11.0),
        Inches(0.62), "", fill=WHITE, edge=GRAY_L, shape=MSO_SHAPE.RECTANGLE)
txt(s, "INSTRUCTOR: fill these three in from the Lecture 3 exit tickets before class.",
    M + Inches(1.15), Inches(2.42), Inches(10.6), Inches(0.4), 17, GRAY_L,
    italic=True)
box(s, M, Inches(5.7), CONTENT_W, Inches(0.85),
    "Refer to concepts, never to students. Ninety seconds total, then move on.",
    fill=AMBER_L, edge=AMBER, size=18, bold=True)
D.notes(s, """
TIMING: 0:00–0:02. TEMPLATE SLIDE — you must fill it in before class.

Transcribe the three most frequent muddiest points from Lecture 3 and answer each
in about twenty-five seconds. Name the concept, never the student.

If aliasing or anti-alias filtering is still unresolved for a large part of the
room, say one sentence and promise Laboratory 2 — do not re-teach it here, you
have no slack today.

If the tickets were useless, delete this slide rather than improvising. A hollow
ritual is worse than none, and today's opening needs its two minutes back.
""")


# ───────────────────────────────────────────────────────── 3  retrieval: scaling
s = S()
heading(s, "Retrieval, unaided", "Lecture 1's scaling laws — say them before I show them")
laws = [("k ∝ L", "stiffness falls,\nbut only linearly", TEAL),
        ("m ∝ L³", "mass collapses —\nthe cube is the killer", AMBER),
        ("f₀ ∝ 1/L", "resonance climbs:\nthis is why MEMS are fast", TEAL),
        ("A/V ∝ 1/L", "the world becomes\nall surface", AMBER)]
x = M
for rel, why, col in laws:
    box(s, x, Inches(2.30), Inches(2.80), Inches(0.90), rel, fill=WHITE, edge=col,
        tcolor=col, size=25, bold=True, font=MONO, edge_w=2.5)
    txt(s, why, x + Inches(0.06), Inches(3.36), Inches(2.68), Inches(1.0), 16,
        INK, align=PP_ALIGN.CENTER, line=1.3)
    x += Inches(3.03)
box(s, M, Inches(4.70), CONTENT_W, Inches(0.86),
    "Shrink a device and it gets faster and cheaper. It also gets lighter — and "
    "lighter means noisier.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=22, bold=True)
txt(s, "Today those four relations stop being physics and become manufacturing. "
       "Every one of them is a consequence of how the device was made.",
    M, Inches(5.80), CONTENT_W, Inches(0.8), 19, GRAY, line=1.35)
D.notes(s, """
TIMING: 0:02–0:05. RETRIEVAL PRACTICE, not review. Ask before you show.

"Notes down. Four relations from Lecture 1 — mass, stiffness, resonance, surface
to volume. Somebody give me one." Take four students, one relation each, and let
the room correct them. It costs ninety seconds and beats re-explaining.

If they cannot produce m ∝ L³, write it up and leave it up — the honest ledger at
minute 73 collapses without it.

Then the bridge: "You have used these to predict behaviour. Today they turn into
process steps and a stress path."
""")


# ───────────────────────────────────────────────────────── 4  the unpaid debt
s = statement(D, "“What is this device's\ncross-axis sensitivity after it\n"
                 "has been soldered to my board?”",
              "Lecture 2, slide 22. The answer was: it is not in the datasheet, and it "
              "cannot be. I left that unpaid on purpose. Today it gets paid.",
              size=32, eyebrow_text="the debt from lecture 2", accent=RED)
D.notes(s, """
TIMING: 0:05–0:07. Put it up in silence and let them recognise it. Somebody will.

Then say plainly: "Two weeks ago I told you a number could not exist and moved
on. That was a debt. A course that leaves debts like that unpaid teaches students
that engineering has magic in it."

Ask for the reason, take two answers, accept none of them yet: "Hold those. In
three minutes you will vote on it, and I will not tell you the answer until
minute seventy, by which point you will not need me to."

Do not explain. The poll is coming.
""")


# ───────────────────────────────────────────────────────── 5  what you are holding
s = S()
heading(s, "Why no manufacturer can answer it", "Because the specification is not describing a component")
layers = [("1", "A silicon structure a few micrometres thick", TEAL),
          ("2", "Suspended over a sealed cavity, free to move", TEAL),
          ("3", "Glued into a plastic box with an adhesive that cures and shrinks", AMBER),
          ("4", "Soldered to a board that flexes when you tighten a screw", RED)]
y = Inches(2.20)
for n, t, col in layers:
    box(s, M, y, Inches(0.60), Inches(0.60), n, fill=col, edge=col,
        tcolor=CREAM if col is not AMBER else DARK, size=21, bold=True, font=MONO)
    box(s, M + Inches(0.92), y, CONTENT_W - Inches(0.92), Inches(0.60), t,
        fill=WHITE, edge=col, tcolor=INK, size=19, bold=False,
        align=PP_ALIGN.LEFT, shape=MSO_SHAPE.RECTANGLE)
    y += Inches(0.82)
box(s, M, Inches(5.60), CONTENT_W, Inches(0.90),
    "The manufacturer owns line 1 and part of line 3. Lines 3 and 4 are yours — "
    "and they are where the error enters.",
    fill=AMBER_L, edge=AMBER, size=21, bold=True)
D.notes(s, """
TIMING: 0:07–0:08. Sixty seconds, four lines, read them and stop.

Point at line 4 and make it physical: "You will tighten that screw yourself, in
the capstone, with a screwdriver, by feel. That torque is now part of your
instrument."

The sentence to land, in the first person because that is how habits install:
"The datasheet describes a die. I bought an assembly, and I built the rest of it."

Do not go further. This slide only has to make the poll feel answerable rather
than mystical. Go straight to the vote.
""")


# ───────────────────────────────────────────────────────── 6  poll 1 baseline
q1 = ("In Lecture 2 you were asked for a device's cross-axis sensitivity after it "
      "is soldered to your board, and the answer was that the number is not in the "
      "datasheet.\nWhy is it not there?")
opts1 = [("A", "It is proprietary — competitors would learn from it"),
         ("B", "It depends on your board and your assembly, so no manufacturer can "
               "specify it"),
         ("C", "It is in the application note, not the datasheet"),
         ("D", "It is the same as the package-level figure, so printing it twice "
               "would be redundant")]
s = poll(D, 1, q1, opts1, minute=8,
         note="Commit now. I am not telling you the answer until the end of the "
              "lecture — by which point you will have drawn the reason yourselves.")
D.notes(s, """
TIMING: 0:08–0:11. Baseline. DO NOT REVEAL. Record the distribution; you re-show
this slide at minute seventy.

Expect 25–40 % for B. This poll is less about the split than about planting the
question, so do not fish for the answer.

A is the commercial-secrecy instinct — worth thirty seconds of dismantling later:
they publish noise density, which is far more competitively sensitive.

C is the most useful wrong answer, because somebody will go looking during the
break. If they find an app note, that is a gift — read its mounting-stress
mitigation list aloud at minute seventy.

D is misconception M1 in its purest form.
""")


# ───────────────────────────────────────────────────────── 7  the anchor: the rows
s = S()
heading(s, "The packaging tax, in the datasheet you already own",
        "ISM330DHCX · DS13012 Rev 6 · read the conditions column first")
rows = [["Parameter", "Typ", "Max", "Unit", "Conditions"],
        ["Zero-g level", "±10", "±65", "mg", "25 °C, after soldering"],
        ["Zero-g temp. coefficient", "±0.1", "±0.5", "mg/°C", "−40 to +85 °C"],
        ["Cross-axis sensitivity", "±0.5", "—", "%", "25 °C, package level, not board level"]]
t = table(s, M, Inches(2.20), CONTENT_W, rows, [0.25, 0.10, 0.10, 0.10, 0.45],
          size=16, row_h=Inches(0.58), head_size=15, mono_cols=(1, 2))
for j in (1, 2):
    c = t.cell(1, j)
    c.fill.solid(); c.fill.fore_color.rgb = AMBER_L
    c.text_frame.paragraphs[0].runs[0].font.bold = True
box(s, M, Inches(4.60), CONTENT_W, Inches(0.90),
    "“after soldering”  —  the manufacturer is telling you, in the specification "
    "itself, that your assembly is part of the error.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=21, bold=True)
txt(s, "▸  Row 1 is an OFFSET: the output when the input is zero. Row 2 is DRIFT: how "
       "that offset moves.\n"
       "▸  Row 3 is the number Lecture 2 asked for — and its condition line admits "
       "it is not yours.",
    M, Inches(5.72), CONTENT_W, Inches(1.0), 18, INK, line=1.4)
D.notes(s, """
TIMING: 0:11–0:12. These are the real rows, from the real part in their kit. Say
so — after two weeks of representative extracts, that matters.

Read row 1 aloud with its condition, twice: "plus or minus ten milli-g typical,
plus or minus sixty-five maximum, at twenty-five degrees, AFTER SOLDERING."

Then the honesty point: "This is not a manufacturer hiding. This is a
manufacturer telling you exactly where the boundary of their responsibility is,
in five words, and almost nobody reads them."

Hold the arithmetic. The next slide is the punch.
""")


# ───────────────────────────────────────────────────────── 8  the anchor: arithmetic
s = S()
heading(s, "Against Lecture 2's 8.73 mg", "The number on the board since week two")
rich(s, M, Inches(2.12), CONTENT_W, Inches(0.55),
     [[("a 0.5° tilt  =  sin(0.5°) × 1 g  =  ", {"size": 22, "font": MONO}),
       ("8.73 mg", {"size": 27, "font": MONO, "bold": True, "color": TEAL})]],
     align=PP_ALIGN.CENTER)
txt(s, "— the entire signal we are trying to measure", M, Inches(2.72), CONTENT_W,
    Inches(0.34), 17, GRAY, italic=True, align=PP_ALIGN.CENTER)
ratios = [("TYP", "±10 mg", "10 / 8.73", "1.15×", AMBER),
          ("MAX", "±65 mg", "65 / 8.73", "7.45×", RED)]
x = M
for tag, val, calc, ratio, col in ratios:
    box(s, x, Inches(3.15), Inches(5.85), Inches(0.56), tag + "  ZERO-G LEVEL",
        fill=col, edge=col, tcolor=CREAM if col is not AMBER else DARK,
        size=16, bold=True)
    box(s, x, Inches(3.76), Inches(5.85), Inches(1.20),
        val + "   ÷   8.73 mg", fill=WHITE, edge=col, tcolor=INK, size=22,
        bold=True, font=MONO, edge_w=2.5, shape=MSO_SHAPE.RECTANGLE)
    txt(s, ratio, x, Inches(5.06), Inches(5.85), Inches(0.7), 42, col, bold=True,
        font=MONO, align=PP_ALIGN.CENTER)
    x += Inches(6.20)
box(s, M, Inches(5.95), CONTENT_W, Inches(0.86),
    "Even the TYPICAL offset exceeds the whole quantity we are trying to measure. "
    "The maximum is seven and a half times it.",
    fill=RED_L, edge=RED, size=21, bold=True)
D.notes(s, """
TIMING: 0:12–0:14. Do both divisions on the board, out loud. Ten over eight point
seven three is one point one five. Sixty-five over eight point seven three is
seven point four five.

Then stop and let it sit: "The offset of the part in your kit is larger than the
tilt you were asked to measure. Not comparable to it — larger."

Take the obvious objection from the room, because someone will raise it: yes, you
can calibrate an offset out. Say "hold that thought, it is the best question in
the lecture, and it is slide thirty-four." Then move.
""")


# ───────────────────────────────────────────────────────── 9  section C1
s = section(D, "chunk 1", "Five structures\ndo all the work",
            ["Proof mass on a flexure. Cantilever beam. Diaphragm. Resonator. Comb.",
             "Five shapes cover every device in Lectures 5 to 11. Learn the shapes, "
             "not the catalogue."])
D.notes(s, """
TIMING: 0:14. Section marker, fifteen seconds. Read the two lines and move.

Say the promise out loud because it lowers the cognitive load of the whole chunk:
"Five, not fifty. Five fits in your head, and five is genuinely all there is.
Every sensor in the second half of this course is one of these five shapes with a
different transduction bolted onto it."

Do not list them twice. The next slide starts drawing.
""")


# ───────────────────────────────────────────────────────── 10  L1's figure again
s = S()
heading(s, "Structure 1, and you have seen it before",
        "A capacitive MEMS accelerometer, in cross-section — Lecture 1's figure, unchanged")
box(s, Inches(3.4), Inches(2.35), Inches(6.4), Inches(0.42), "FIXED PLATE",
    fill=GRAY_L, edge=GRAY, size=13, bold=True, shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(3.4), Inches(4.62), Inches(6.4), Inches(0.42), "FIXED PLATE",
    fill=GRAY_L, edge=GRAY, size=13, bold=True, shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(4.6), Inches(3.28), Inches(4.0), Inches(0.86), "PROOF MASS  m",
    fill=TEAL_L, edge=TEAL, size=18, bold=True, edge_w=2, shape=MSO_SHAPE.RECTANGLE)
for sx in (Inches(3.55), Inches(8.75)):
    zig = []
    for i in range(9):
        zig.append((Emu(int(sx + (Inches(0.85) if i % 2 else Inches(0.15)))),
                    Emu(int(Inches(3.3) + Inches(0.105) * i))))
    curve(s, zig, TEAL, 2.0)
txt(s, "flexures,  k", Inches(2.40), Inches(3.55), Inches(1.15), Inches(0.4),
    13, TEAL, bold=True, align=PP_ALIGN.RIGHT)
txt(s, "flexures,  k", Inches(9.75), Inches(3.55), Inches(1.2), Inches(0.4),
    13, TEAL, bold=True)
for gy, lbl in ((Inches(2.90), "gap  d ≈ 1–2 µm"), (Inches(4.22), "gap  d")):
    txt(s, lbl, Inches(9.95), gy, Inches(2.6), Inches(0.3), 14, AMBER,
        bold=True, font=MONO)
    a = s.shapes.add_shape(MSO_SHAPE.LEFT_BRACE, Inches(9.72), gy - Inches(0.06),
                           Inches(0.18), Inches(0.36))
    a.fill.background(); a.line.color.rgb = AMBER; a.line.width = Pt(1.25)
    a.shadow.inherit = False
rich(s, M, Inches(5.35), CONTENT_W, Inches(1.4),
     [[("Acceleration moves the mass, one gap grows and the other shrinks, and the "
        "differential ", {"size": 18}),
       ("C = εA/d", {"font": MONO, "bold": True, "size": 18, "color": TEAL}),
       (" is the signal.", {"size": 18})],
      [("In week one this was a drawing. Today it is a thing somebody etched, "
        "released, glued into a box and soldered down — and every one of those "
        "verbs changes ", {"size": 18, "color": GRAY}),
       ("d", {"font": MONO, "bold": True, "size": 18, "color": AMBER}),
       (".", {"size": 18, "color": GRAY})]])
D.notes(s, """
TIMING: 0:14–0:16. Deliberately the SAME picture as Lecture 1. Say that: "I have
not redrawn this. You have seen it. What has changed is what you can now ask
about it."

Point at the one-to-two micrometre gap and name the stake: "C is epsilon A over
d. If assembly stress changes d by one per cent, the capacitance changes by one
per cent, and that appears as an offset. That is the ten milli-g."

That single sentence is the whole lecture in miniature. If you have to cut
something later, do not cut this.
""")


# ───────────────────────────────────────────────────────── 11  the relations
s = S()
heading(s, "Proof mass on a flexure: the three relations",
        "Everything an accelerometer datasheet says is a consequence of m, k and d")
rels = [("F = ma", "the measurand becomes a force —\nthis is the only physics", TEAL),
        ("x = ma / k", "the force becomes a displacement —\nthe flexure sets the sensitivity", TEAL),
        ("f₀ = (1/2π)√(k/m)", "and the same m and k set\nthe usable bandwidth", AMBER)]
x = M
for rel, why, col in rels:
    box(s, x, Inches(2.20), Inches(3.82), Inches(0.88), rel, fill=WHITE, edge=col,
        tcolor=col, size=23, bold=True, font=MONO, edge_w=2.5)
    txt(s, why, x + Inches(0.08), Inches(3.24), Inches(3.66), Inches(0.9), 16,
        INK, align=PP_ALIGN.CENTER, line=1.3)
    x += Inches(4.055)
box(s, M, Inches(4.35), CONTENT_W, Inches(0.86),
    "One structure, one measurand, two specifications you cannot choose "
    "independently: sensitivity and bandwidth share m and k.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=21, bold=True)
txt(s, "This is why the datasheet has selectable full-scale ranges but not selectable "
       "sensitivity at a fixed range: the mass and the springs were fixed by a mask "
       "set, once, for the whole production run. Range is switched in the "
       "electronics. The mechanics are not negotiable.",
    M, Inches(5.45), CONTENT_W, Inches(1.3), 19, GRAY, line=1.4)
D.notes(s, """
TIMING: 0:16–0:18. Three boxes, thirty seconds each, then the grey paragraph.

The trap to name explicitly: students want sensitivity and bandwidth to be
independent knobs. "They are the same two numbers. Make the mass bigger and you
buy sensitivity and lose bandwidth. There is no setting for this — it was decided
by a mask."

That is the first place in the course where a specification is traceable to a
manufacturing decision rather than a design choice, so say the word "mask" and
let it land. It comes back at minute fifty-two.
""")


# ───────────────────────────────────────────────────────── 12  beam and diaphragm
s = S()
heading(s, "Structures 2 and 3", "Cantilever beam · diaphragm over a cavity")
structure_card(s, M, Inches(2.10), Inches(5.85), "CANTILEVER BEAM",
               "k  ∝  E·w·t³ / L³", "force, and it is the flexure above",
               "L8 — force and tactile sensors", edge=TEAL, h=Inches(2.65),
               note="Note the cube on t: thickness is set by DEPOSITION, so a 5 % film "
                    "error is a 16 % stiffness error.")
structure_card(s, M + Inches(6.20), Inches(2.10), Inches(5.85),
               "DIAPHRAGM OVER A CAVITY",
               "deflection  ∝  ΔP·a⁴ / (E·t³)", "pressure, sound",
               "L8 pressure · L11 microphone", edge=TEAL, h=Inches(2.65),
               note="No proof mass anywhere in this device. Remember that at the "
                    "next poll.")
box(s, M, Inches(5.05), CONTENT_W, Inches(0.86),
    "The beam and the flexure are the same object. Structure 2 is not a new idea — "
    "it is structure 1 with the mass taken off the end.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=21, bold=True)
txt(s, "The diaphragm is the first structure that needs a SEALED CAVITY underneath it "
       "— which is why pressure sensors are packaging problems before they are "
       "electronics problems.",
    M, Inches(6.10), CONTENT_W, Inches(0.75), 19, GRAY, line=1.35)
D.notes(s, """
TIMING: 0:18–0:20. Two cards, and one connection they will not make unaided.

Say the connection: "A cantilever is a flexure with nothing on the end. You have
not learned a second structure, you have learned the same one used differently."
That halves the load of this chunk.

The exponents are the teaching point on the beam: t cubed. Do the arithmetic
aloud — five per cent thickness error, sixteen per cent stiffness error — and
promise that deposition at minute fifty-two is where the five per cent comes from.

Plant the diaphragm note deliberately. Poll 2 is four minutes away.
""")


# ───────────────────────────────────────────────────────── 13  resonator and comb
s = S()
heading(s, "Structures 4 and 5", "Resonator · comb — and the comb is the reason gyroscopes exist")
structure_card(s, M, Inches(2.10), Inches(5.85), "RESONATOR",
               "f₀ shifts with mass, stress, T",
               "mass, gas, temperature, time",
               "L9 gas sensing · timing references", edge=TEAL, h=Inches(2.65),
               note="You do not measure an amplitude here. You measure a FREQUENCY — "
                    "which is the cheapest thing to measure well.")
structure_card(s, M + Inches(6.20), Inches(2.10), Inches(5.85), "COMB STRUCTURE",
               "C = n·ε·A/d      F ∝ n·V²",
               "displacement — and it applies force too",
               "L5 · L6 · L10 MEMS mirror", edge=TEAL, h=Inches(2.65),
               note="The only structure that both SENSES and DRIVES.")
box(s, M, Inches(5.05), CONTENT_W, Inches(0.86),
    "A drive comb sustains a vibration. A sense comb reads the Coriolis deflection "
    "of that vibration. That is a gyroscope — and it is why one exists at all.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=20, bold=True)
txt(s, "n is the number of finger pairs. The gap d is set by lithography — so the "
       "smallest feature a fab can print sets the capacitance, and that sets the "
       "noise floor.",
    M, Inches(6.10), CONTENT_W, Inches(0.75), 19, GRAY, line=1.35)
D.notes(s, """
TIMING: 0:20–0:22. Spend your time on the comb, not the resonator.

Say the gyroscope sentence slowly and once: drive comb sustains, sense comb
reads Coriolis. Lecture 6 will thank you, and a student who holds this needs
half as long in week six.

On the resonator, one line only: "the output is a frequency, and frequency is the
one quantity we can measure to nine digits with a cheap counter."

The grey paragraph is the second plant for minute fifty-two — lithography sets d,
d sets C, C sets the noise floor. You will ask for that chain back in the
sequencing activity.
""")


# ───────────────────────────────────────────────────────── 14  the five, in one table
s = S()
heading(s, "The five structures, in one table", "This is the whole of Chunk 1 — it is in the handout")
rows = [["Structure", "Governing relation", "Senses", "In this course"],
        ["Proof mass on a flexure", "x = ma/k,  f₀ = (1/2π)√(k/m)",
         "acceleration, angular rate", "L5 accelerometer, L6 gyroscope"],
        ["Cantilever beam", "k ∝ E·w·t³/L³", "force (it is the flexure above)",
         "L8 force / tactile"],
        ["Diaphragm over a cavity", "deflection ∝ ΔP·a⁴/(E·t³)", "pressure, sound",
         "L8 pressure, L11 microphone"],
        ["Resonator", "f₀ shifts with mass, stress, T",
         "mass, gas, temperature, time", "L9 gas microheater, timing"],
        ["Comb structure", "C = nεA/d,  F ∝ n·V²", "displacement — sense AND drive",
         "L5, L6, L10 MEMS mirror"]]
table(s, M, Inches(2.10), CONTENT_W, rows, [0.22, 0.28, 0.24, 0.26], size=14,
      row_h=Inches(0.62), head_size=14.5, mono_cols=(1,),
      align=[PP_ALIGN.LEFT] * 4)
box(s, M, Inches(5.95), CONTENT_W, Inches(0.86),
    "Five, not a taxonomy. Five is what fits in working memory — and five is "
    "genuinely enough for seven lectures.",
    fill=AMBER_L, edge=AMBER, size=20, bold=True)
D.notes(s, """
TIMING: 0:22. DO NOT READ THIS SLIDE OUT. It is a reference page and it is in the
handout — say both things so nobody transcribes it.

Point at exactly one column: "Senses". "Read down that column and notice that
four different measurands come out of five shapes. You are not learning devices.
You are learning shapes, and then which measurand each shape is good for."

Fifteen seconds, then the poll. If you are running late, this is the slide to
put on screen while you set up Poll 2 rather than a slide to talk about.
""")


# ───────────────────────────────────────────────────────── 15  poll 2
q2 = "Four MEMS devices. Which one does NOT contain a proof mass?"
opts2 = [("A", "a 3-axis accelerometer"),
         ("B", "a vibrating-structure gyroscope"),
         ("C", "a barometric pressure sensor"),
         ("D", "a MEMS microphone")]
s = poll(D, 2, q2, opts2, minute=22,
         note="Vote alone, hands up on my count. Then I am going to tell you something "
              "honest about this question.")
D.notes(s, """
TIMING: 0:22–0:24. Hands up simultaneously on a count. Expect A and B combined at
30–45 % — those are the students who have not yet separated structure from device
category, and they are who this chunk was for.

Expect C at 30–40 % and D at 15–25 %.

This item is deliberately a little unfair, and you are going to say so on the
next slide, so do not pretend otherwise now. Take one spoken reason for A or B
before you reveal — "what is a proof mass FOR?" — because that answer is the
thirty seconds of the chunk that actually teaches.
""")


# ───────────────────────────────────────────────────────── 16  poll 2 answer
s = poll(D, 2, q2, opts2, minute=22, correct="C", reveal=True,
         note="If you voted D you were right about the physics and I asked a bad "
              "question — a microphone is a diaphragm too. Both C and D respond to "
              "pressure across a membrane, not to the inertia of a suspended block.")
D.notes(s, """
TIMING: 0:24–0:26. Reveal, then be honest immediately — the honesty is the lesson.

Say it in these words: "If you voted D, you were right about the physics and I
asked a bad question. Both C and D are diaphragm devices. C is the intended
answer only because a barometer is unambiguously one."

Then to the A and B voters: "Tell me what a proof mass is for." Answer: inertia.
It converts acceleration into force. A pressure sensor has nothing to accelerate.

Modelling a flawed item honestly is worth more than a clean item. Do not skip it.
""")


# ───────────────────────────────────────────────────────── 17  five cover eleven
s = S()
heading(s, "Why five shapes cover seven lectures",
        "Every device in Module B, and the structure underneath it")
rows = [["Lecture", "Device", "Structure", "Transduction"],
        ["L5", "accelerometer", "proof mass on a flexure", "capacitive"],
        ["L6", "gyroscope", "comb drive + proof mass", "capacitive"],
        ["L7", "magnetometer", "none — nothing moves", "electromagnetic"],
        ["L8", "pressure sensor", "diaphragm over a cavity", "piezoresistive"],
        ["L8", "force / tactile", "cantilever beam", "piezoresistive"],
        ["L9", "gas sensor", "resonator / microheater", "thermal"],
        ["L10", "MEMS mirror", "comb", "electrostatic drive"],
        ["L11", "microphone", "diaphragm", "capacitive"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.10, 0.26, 0.36, 0.28], size=14.5,
          row_h=Inches(0.44), head_size=14.5, mono_cols=(0,),
          align=[PP_ALIGN.CENTER, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
for j in (2, 3):
    c = t.cell(3, j)
    c.fill.solid(); c.fill.fore_color.rgb = GRAY_L
box(s, M, Inches(6.10), CONTENT_W, Inches(0.78),
    "Eight devices. Five shapes. One of them needs no moving structure at all — "
    "and knowing which is worth as much as knowing the rest.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=20, bold=True)
D.notes(s, """
TIMING: 0:26–0:29. Walk down the Structure column only. Do not discuss devices —
that is Module B's job and you will run out of clock.

Stop on L7. "The magnetometer has no structure. Nothing moves. It is a solid-state
effect in silicon, and it is in this course because it sits on the same die as
the accelerometer in your kit." Being honest that the pattern has an exception
makes the pattern credible.

Then the payoff: "You now have a reading strategy for seven lectures. Ask what
shape it is before you ask what it measures."
""")


# ───────────────────────────────────────────────────────── 18  the pivot statement
s = statement(D, "You are not about to learn\neleven devices.",
              "You are about to learn five structures and six transduction principles, "
              "and then watch them get recombined seven times. Module B is not a "
              "catalogue. It is one method, applied.",
              size=38, eyebrow_text="the point of chunk 1", accent=TEAL)
D.notes(s, """
TIMING: 0:29–0:30. Read the black line once. Then the grey block once. Then stop
talking for three seconds — this slide works on silence.

Why it is here: the single largest delivery risk in the semester plan is that
Lectures 5 to 11 are experienced as a list of unrelated devices. This slide, the
close at minute seventy-six, and exit-ticket question 2 are the three places you
push against that. Say the same sentence in all three.

If the room looks relieved, you have landed it. Move on briskly.
""")


# ───────────────────────────────────────────────────────── 19  one structure, four jobs
s = S()
heading(s, "One structure, four different sensors",
        "The resonator, to show that the shape is the reusable part")
jobs = [("MASS", "a molecule lands on it;\nf₀ drops", TEAL),
        ("GAS", "a coating adsorbs a species;\nthe mass changes", TEAL),
        ("TEMPERATURE", "Young's modulus changes;\nf₀ tracks it", AMBER),
        ("TIME", "nothing changes;\nf₀ IS the output", TEAL)]
x = M
for name, why, col in jobs:
    box(s, x, Inches(2.30), Inches(2.80), Inches(0.62), name, fill=col, edge=col,
        tcolor=CREAM if col is not AMBER else DARK, size=16, bold=True)
    box(s, x, Inches(3.00), Inches(2.80), Inches(1.30), why, fill=WHITE, edge=col,
        tcolor=INK, size=16, shape=MSO_SHAPE.RECTANGLE, edge_w=1.5)
    x += Inches(3.03)
box(s, M, Inches(4.60), CONTENT_W, Inches(0.86),
    "Same beam. Same equation. Four products — and one of them is a bug in the "
    "other three.",
    fill=AMBER_L, edge=AMBER, size=21, bold=True)
txt(s, "Temperature shifts f₀ whether you asked it to or not: in a gas sensor that is "
       "an error term to compensate, and in a thermometer it is the whole product.",
    M, Inches(5.70), CONTENT_W, Inches(0.8), 19, GRAY, line=1.4)
D.notes(s, """
TIMING: 0:30–0:32. DESIGNATED CUT. If you reached this slide later than minute
thirty-one, put it on the screen, read the amber line, and go.

If you have the time, the amber line is the idea: the same physics is a feature
or a defect depending only on what you claimed to be selling. Ask the room which
of the four is the error term in the other three. They will get it.

This is also where a keen student asks about quartz crystals and temperature
compensation. One sentence, then defer to Lecture 9. Do not follow it.
""")


# ───────────────────────────────────────────────────────── 20  section C2
s = section(D, "chunk 2", "Six principles,\none question that sorts them",
            ["Capacitive · piezoresistive · piezoelectric · thermal · "
             "electromagnetic · optical",
             "The question: can it measure something that is not moving?"])
D.notes(s, """
TIMING: 0:32. Section marker, fifteen seconds — but say the question, because it
is the spine of the next twenty minutes.

"Six principles. I could compare them on ten axes and you would remember none of
it. So we are going to compare them on one axis that actually changes an
engineering decision: static response. Can this thing measure a quantity that is
sitting still?"

Flag the difficulty honestly: "The hardest vote of the lecture is fourteen
minutes away, and it lives on exactly this question."
""")


# ───────────────────────────────────────────────────────── 21  capacitive, piezoresistive
s = S()
heading(s, "The two that carry Module B", "Both answer yes to the static question")
principle_card(s, M, Inches(2.10), Inches(5.85), "CAPACITIVE", "YES",
               "small, high-impedance",
               "needs on-chip electronics; stray capacitance everywhere",
               "why the ISM330DHCX can measure tilt at all",
               edge=TEAL, static_col=TEAL)
principle_card(s, M + Inches(6.20), Inches(2.10), Inches(5.85), "PIEZORESISTIVE",
               "YES", "millivolts from a bridge",
               "a strong temperature coefficient — the bridge drifts",
               "why pressure sensors need temperature compensation",
               edge=TEAL, static_col=TEAL)
box(s, M, Inches(5.75), CONTENT_W, Inches(0.90),
    "Capacitive measures a GAP. Piezoresistive measures a STRAIN. Both hold their "
    "reading when the world stops moving — and that is not a given.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=20, bold=True)
D.notes(s, """
TIMING: 0:32–0:36. Two cards, two minutes each, and one contrast.

Capacitive: "It measures a distance. A distance still exists when nothing is
happening, so the reading survives standing still. The price is that the signal
is tiny and high-impedance, which is why the electronics have to be on the same
die — you cannot run that signal down a track."

Piezoresistive: "Millivolts, robust, easy. The price is on the last line: the
bridge drifts with temperature, so every pressure sensor you meet has a
compensation scheme. Lecture 8."
""")


# ───────────────────────────────────────────────────────── 22  piezoelectric
s = S()
heading(s, "The one that answers no", "Piezoelectric — self-generating, and blind to anything still")
principle_card(s, M, Inches(2.10), Inches(5.85), "PIEZOELECTRIC", "NO",
               "charge, self-generating — no supply needed",
               "no DC response at all; the charge leaks away",
               "why vibration sensors quote a LOW-frequency limit",
               edge=RED, static_col=RED)
# charge-decay picture
txt(s, "TILT  (the input) — stepped to 0.5° and held", Inches(7.10), Inches(2.20),
    Inches(5.5), Inches(0.3), 13, TEAL, bold=True)
axis(s, Inches(7.10), Inches(3.58), Inches(5.20), color=GRAY_L)
curve(s, [(Emu(int(Inches(7.10))), Emu(int(Inches(3.58)))),
          (Emu(int(Inches(8.10))), Emu(int(Inches(3.58)))),
          (Emu(int(Inches(8.10))), Emu(int(Inches(2.80)))),
          (Emu(int(Inches(12.30))), Emu(int(Inches(2.80))))], TEAL, 2.25)
txt(s, "held for years", Inches(10.30), Inches(2.90), Inches(2.0), Inches(0.3),
    12, TEAL, bold=True, font=MONO)
txt(s, "PIEZOELECTRIC OUTPUT — decays with the amplifier's τ",
    Inches(7.10), Inches(4.05), Inches(5.5), Inches(0.3), 13, RED, bold=True)
axis(s, Inches(7.10), Inches(5.42), Inches(5.20), color=GRAY_L)
pts = [(Emu(int(Inches(7.10))), Emu(int(Inches(5.42)))),
       (Emu(int(Inches(8.10))), Emu(int(Inches(5.42)))),
       (Emu(int(Inches(8.10))), Emu(int(Inches(4.64))))]
for i in range(61):
    xx = Inches(8.10) + Inches(4.20) * i / 60.0
    yy = Inches(5.42) - Inches(0.78) * math.exp(-3.4 * i / 60.0)
    pts.append((Emu(int(xx)), Emu(int(yy))))
curve(s, pts, RED, 2.25)
txt(s, "→ 0", Inches(11.55), Inches(5.02), Inches(0.9), Inches(0.3), 15, RED,
    bold=True, font=MONO)
box(s, M, Inches(5.75), CONTENT_W, Inches(0.90),
    "A piezoelectric element responds to a CHANGE in strain. Hold it still and the "
    "output goes to zero — not badly, but exactly to zero.",
    fill=RED_L, edge=RED, size=20, bold=True)
D.notes(s, """
TIMING: 0:36–0:38. This slide exists to make Poll 3 answerable, so build the
picture on the board as well as showing it.

"Charge appears when the strain changes. Nothing generates charge to hold it
there, and the amplifier's input impedance is finite, so the charge leaks. Time
constant: seconds. The frame will be tilted for years."

Then pre-empt distractor D out loud without giving the poll away: "Yes, a better
amplifier lengthens the decay. Lengthens. Not removes."

Do not say the words "it cannot measure tilt". Let them vote first.
""")


# ───────────────────────────────────────────────────────── 23  thermal, electromagnetic
s = S()
heading(s, "Thermal and electromagnetic", "Honestly brief — you meet both again in Module B")
principle_card(s, M, Inches(2.10), Inches(5.85), "THERMAL", "YES, SLOWLY",
               "microvolts, or a resistance change",
               "slow; and it heats itself, so it measures its own power",
               "the warm-up time on a gas sensor",
               edge=TEAL, static_col=AMBER)
principle_card(s, M + Inches(6.20), Inches(2.10), Inches(5.85), "ELECTROMAGNETIC",
               "YES", "large, low-impedance — the easy signal",
               "hard to shrink, and it responds to every magnet nearby",
               "the hard- and soft-iron terms in Lecture 7",
               edge=TEAL, static_col=TEAL)
box(s, M, Inches(5.75), CONTENT_W, Inches(0.90),
    "Thermal is the only principle whose own operation disturbs the measurand. "
    "Electromagnetic is the only one that fights the scaling laws instead of using them.",
    fill=AMBER_L, edge=AMBER, size=19.5, bold=True)
D.notes(s, """
TIMING: 0:38–0:40. DESIGNATED CUT if you are behind — collapse both cards to a
named list and keep Poll 3.

If you have the time, one sentence each is enough. Thermal: "self-heating means
the sensor is part of the thing it measures. That is the warm-up line on every
gas sensor datasheet." Electromagnetic: "big, easy signal — and it does not
shrink, because the useful force needs turns and area, and both die when you
scale down."

The amber line is why these two are on one slide together: both fail in a way the
other four do not.
""")


# ───────────────────────────────────────────────────────── 24  optical
s = S()
heading(s, "Optical", "The last principle, and the one that costs the most package")
principle_card(s, M, Inches(2.10), Inches(5.85), "OPTICAL", "YES",
               "can be very large — sometimes no amplifier at all",
               "needs a window, and the window sees ambient light",
               "the cover-window design in Lecture 10",
               edge=TEAL, static_col=TEAL)
txt(s, "THE THREE BRIEF ONES COME BACK HERE", M + Inches(6.20), Inches(2.15),
    Inches(5.85), Inches(0.3), 12, GRAY, bold=True)
later = [("L7", "electromagnetic", "magnetometers, and why they need calibrating "
          "in situ"),
         ("L9", "thermal", "gas sensing, self-heating and warm-up"),
         ("L10", "optical", "MEMS mirrors, and the window you must design")]
y = Inches(2.60)
for lec, prin, what in later:
    box(s, M + Inches(6.20), y, Inches(0.82), Inches(0.62), lec, fill=TEAL,
        edge=TEAL, tcolor=CREAM, size=17, bold=True, font=MONO)
    txt(s, prin, M + Inches(7.18), y + Inches(0.02), Inches(4.85), Inches(0.3),
        16, TEAL, bold=True)
    txt(s, what, M + Inches(7.18), y + Inches(0.30), Inches(4.85), Inches(0.4),
        14.5, GRAY, line=1.2)
    y += Inches(0.82)
box(s, M + Inches(6.20), Inches(5.10), Inches(5.85), Inches(0.42),
    "Three principles, one slide each. That is proportionate.", fill=GROUND,
    edge=GRAY, size=14, bold=True)
box(s, M, Inches(5.75), CONTENT_W, Inches(0.90),
    "Optical is the only principle where the PACKAGE is part of the transduction: "
    "no window, no measurement.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=20, bold=True)
D.notes(s, """
TIMING: 0:40–0:42. DESIGNATED CUT alongside slide 23.

One idea only: the window. "Every other principle would rather be sealed in the
dark. This one needs a hole in the package, filled with something optically
flat, that survives reflow and does not yellow. That is not a footnote — it is
half the product."

That also sets up Chunk 3 nicely: you are already talking about packaging as
physics, four slides early.

Then straight to Poll 3. Do not summarise the six. The table does that at
minute forty-six.
""")


# ───────────────────────────────────────────────────────── 25  poll 3
q3 = ("A piezoelectric accelerometer — representative industrial vibration type — is "
      "mounted on the solar-tracker frame from Lecture 2 to measure its tilt. The frame "
      "is tilted to 0.5° and held there.\nThirty seconds later, the reported tilt is:")
opts3 = [("A", "0.5°, correctly"),
         ("B", "0°"),
         ("C", "0.5° but very noisy"),
         ("D", "it depends on the amplifier's gain")]
s = poll(D, 3, q3, opts3, minute=46,
         note="Vote. Then in pairs: one of you argues it reads 0.5°, the other argues it "
              "reads zero — then decide. Two minutes.")
D.notes(s, """
TIMING: 0:42–0:44. THE HARDEST VOTE OF THE LECTURE. Target 15–30 % on the first
vote, 55–70 % after pairs.

Full peer instruction, and the prompt matters: assign the positions rather than
letting them discuss freely — one argues 0.5°, one argues zero, then decide.

Expect 40–55 % for A: an accelerometer is an accelerometer. C is misconception M3
— self-generating read as strong. D is the student reaching for electronics, and
it is productive.

If the first vote clears 40 %, someone has met charge amplifiers. Find them and
let them explain it; they will do it better than the slide.
""")


# ───────────────────────────────────────────────────────── 26  poll 3 answer
s = poll(D, 3, q3, opts3, minute=46, correct="B", reveal=True,
         note="Zero. Charge appears when the strain CHANGES; held still, it leaks away "
              "through the amplifier's input impedance in a few seconds. A piezoelectric "
              "accelerometer has no DC response. It cannot measure tilt — not badly, at all.")
D.notes(s, """
TIMING: 0:44–0:46. Reveal, then say why this question is in the lecture.

"This is the only place in Module A where the PRINCIPLE forbids the application.
Every other trade-off you have met was quantitative — better, worse, by how much.
This one is categorical. No specification, no amplifier and no budget fixes it."

Then the follow-up that generalises it, and take the answer from the room: "which
of the six principles COULD measure this tilt?" Answer: all of them except this
one. Capacitive, piezoresistive, thermal, electromagnetic, optical.

Same lesson as Lecture 2, promoted from a number to a principle. Say that.
""")


# ───────────────────────────────────────────────────────── 27  the table, part 1
s = S()
heading(s, "Six principles, sorted by one question", "Can it measure something that is standing still?")
rows = [["Principle", "Static (DC)?", "Signal", "Main weakness"],
        ["Capacitive", "yes", "small, high-impedance",
         "needs on-chip electronics; stray C"],
        ["Piezoresistive", "yes", "mV from a bridge",
         "strong temperature coefficient"],
        ["Piezoelectric", "no", "charge, self-generating",
         "no DC response; the charge leaks"],
        ["Thermal", "yes, slowly", "µV or resistance", "slow; self-heating"],
        ["Electromagnetic", "yes", "large, low-impedance",
         "hard to shrink; magnetically susceptible"],
        ["Optical", "yes", "can be very large", "needs a window; ambient light"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.19, 0.15, 0.28, 0.38], size=15,
          row_h=Inches(0.52), head_size=15,
          align=[PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
for i in range(1, 7):
    c = t.cell(i, 1)
    c.fill.solid()
    c.fill.fore_color.rgb = RED_L if i == 3 else TEAL_L
    r = c.text_frame.paragraphs[0].runs[0]
    r.font.bold = True
    r.font.color.rgb = RED if i == 3 else TEAL
box(s, M, Inches(5.90), CONTENT_W, Inches(0.90),
    "One “no” in the whole column — and it belongs to the principle that looks "
    "most impressive on a front page.",
    fill=RED_L, edge=RED, size=21, bold=True)
D.notes(s, """
TIMING: 0:46–0:49. Read down column two and nothing else. The rest of the table
is a handout page and you should say so.

"Five yeses and one no. If you remember one thing from this chunk, remember which
row is red."

Then the honest qualifier on the thermal row: "yes, slowly" is not a hedge — it
means the principle has DC response but a settling time measured in seconds, and
that is a real engineering constraint rather than a disqualification.

Do not discuss signal levels. The next slide is the one that pays.
""")


# ───────────────────────────────────────────────────────── 28  the table, part 2
s = S()
heading(s, "And what each one explains in a datasheet",
        "The reason this chunk exists: every principle is a specification's cause")
rows = [["Principle", "Static (DC)?", "The datasheet line it explains"],
        ["Capacitive", "yes", "why the ISM330DHCX can measure tilt at all"],
        ["Piezoresistive", "yes", "why pressure sensors need temperature compensation"],
        ["Piezoelectric", "no", "why vibration sensors quote a low-frequency limit"],
        ["Thermal", "yes, slowly", "the warm-up time on a gas sensor"],
        ["Electromagnetic", "yes", "the hard- and soft-iron terms in Lecture 7"],
        ["Optical", "yes", "the cover-window design in Lecture 10"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.21, 0.16, 0.63], size=15.5,
          row_h=Inches(0.52), head_size=15,
          align=[PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.LEFT])
for i in range(1, 7):
    c = t.cell(i, 1)
    c.fill.solid()
    c.fill.fore_color.rgb = RED_L if i == 3 else TEAL_L
    r = c.text_frame.paragraphs[0].runs[0]
    r.font.bold = True
    r.font.color.rgb = RED if i == 3 else TEAL
box(s, M, Inches(5.90), CONTENT_W, Inches(0.90),
    "A specification is never arbitrary. Somewhere behind every line is a "
    "structure, a principle, or a process step.",
    fill=TEAL, edge=TEAL, tcolor=CREAM, size=21, bold=True)
D.notes(s, """
TIMING: 0:49–0:52. This is the slide that justifies Chunk 2 to a sceptical
student, so say the justification.

"You did not learn six principles because six principles are interesting. You
learned them because the right-hand column is the kind of sentence you will need
in a design review, and none of it is memorisation — each line follows from the
physics on the left."

Point at row 3 one last time and connect it to the vote they just lost: "the
low-frequency limit on a vibration sensor is Poll 3, printed as a specification."

Then the section marker. You are on time if this lands at fifty-two.
""")


# ───────────────────────────────────────────────────────── 29  section C3
s = section(D, "chunk 3", "How it is made,\nand what that costs you",
            ["Four process steps. One consequence each. That is the whole treatment.",
             "This is not a fabrication course — fabrication is here because it "
             "explains the datasheet."])
D.notes(s, """
TIMING: 0:52. Section marker, and state the boundary out loud because students
will otherwise expect a process tour.

"Four steps. Not forty. I am not teaching you to fabricate anything, and the
semester plan says so explicitly. Each step is here because it is the reason for
a number you have already met."

If somebody asks a real fabrication question in this chunk: answer it in ONE
sentence, offer the ITMO 2020 text as further reading, and move on. Following
that question is exactly the drift this lecture is designed to resist.
""")


# ───────────────────────────────────────────────────────── 30  four steps
s = S()
heading(s, "Four steps, in order", "One consequence each — and that is the entire treatment")
steps = [("LITHOGRAPHY", "minimum feature size\n→ the comb gap d\n→ the capacitance\n"
          "→ the noise floor", TEAL),
         ("DEPOSITION", "film thickness, and\nRESIDUAL STRESS —\nthe structure is "
          "curved\nbefore you use it", AMBER),
         ("ETCHING", "isotropic or anisotropic\ndecides which shapes\nare possible "
          "at all", TEAL),
         ("RELEASE", "the sacrificial layer goes,\nthe structure is free —\n"
          "and can STICK", AMBER)]
x = M
for i, (name, cons, col) in enumerate(steps):
    box(s, x, Inches(2.15), Inches(2.62), Inches(0.70), name, fill=col, edge=col,
        tcolor=CREAM if col is not AMBER else DARK, size=17, bold=True)
    txt(s, cons, x + Inches(0.06), Inches(3.00), Inches(2.50), Inches(1.5), 15,
        INK, align=PP_ALIGN.CENTER, line=1.35)
    if i < 3:
        arrow(s, x + Inches(2.68), Inches(2.39), Inches(0.35), Inches(0.22),
              color=GRAY)
    x += Inches(3.03)
box(s, M, Inches(4.70), CONTENT_W, Inches(0.80),
    "PAIRS · 3 MINUTES · cards on your desk: put the four steps in order, then match "
    "each one to its consequence.",
    fill=AMBER_L, edge=AMBER, size=19, bold=True)
box(s, M, Inches(5.66), CONTENT_W, Inches(0.90),
    "Then one question: which of the four is the reason a MEMS accelerometer is "
    "noisier than a bench instrument?",
    fill=DARK, edge=DARK, tcolor=CREAM, size=21, bold=True)
D.notes(s, """
TIMING: 0:52–0:56. Hand out the shuffled cards BEFORE you show the steps —
four steps and four consequences, twelve sets. Three minutes, pairs, collect
nothing, walk the room.

Then take the closing question from the room. Answer: LITHOGRAPHY. Minimum
feature size sets how small the structure can be, size sets the mass, and by
Lecture 1's m ∝ L³ less mass means a higher noise floor.

A student who makes that connection unprompted has understood Module A — say so
publicly when it happens. If nobody gets it, draw the chain on the board:
feature → size → mass → noise.
""")


# ───────────────────────────────────────────────────────── 31  bulk vs surface
s = S()
heading(s, "Bulk or surface", "Two ways to build the same shape, and the trade-off is mass")
for xx, name in ((M, "BULK MICROMACHINING"), (M + Inches(6.20), "SURFACE MICROMACHINING")):
    box(s, xx, Inches(2.10), Inches(5.85), Inches(0.62), name, fill=DARK, edge=DARK,
        tcolor=CREAM, size=18, bold=True)
bulk = [("etches INTO the wafer", TEAL),
        ("thick structures, large proof masses", TEAL),
        ("low noise floor", TEAL),
        ("big die, expensive, hard to integrate", AMBER),
        ("pressure sensors, high-grade inertial", GRAY)]
surf = [("builds UP from thin films", TEAL),
        ("micrometres thick, small masses", AMBER),
        ("higher noise floor", AMBER),
        ("cheap, small, on the same die as the electronics", TEAL),
        ("consumer IMUs — the part in your kit", GRAY)]
for i, ((b1, c1), (b2, c2)) in enumerate(zip(bulk, surf)):
    y = Inches(2.92) + i * Inches(0.52)
    txt(s, "▸  " + b1, M + Inches(0.06), y, Inches(5.75), Inches(0.45), 17,
        c1 if c1 is not GRAY else GRAY, bold=(c1 is not GRAY))
    txt(s, "▸  " + b2, M + Inches(6.26), y, Inches(5.75), Inches(0.45), 17,
        c2 if c2 is not GRAY else GRAY, bold=(c2 is not GRAY))
box(s, M, Inches(5.62), CONTENT_W, Inches(0.86),
    "The trade-off is MASS — and by Lecture 1's m ∝ L³ you could already predict "
    "which one is quieter.",
    fill=AMBER_L, edge=AMBER, size=21, bold=True)
txt(s, "Your kit's part is not the quietest accelerometer buildable — only the "
       "quietest that fits beside its own ADC.",
    M, Inches(6.48), CONTENT_W, Inches(0.4), 17, GRAY, line=1.3)
D.notes(s, """
TIMING: 0:56–0:58. ONE comparison slide. Do not add a second.

Ask before you show the bottom line: "Which of these two is quieter, and why?"
They have m ∝ L³ from minute three. Bulk wins, because bulk can afford mass.

Then the reframe in the grey line, which is the honest engineering point: their
part was not chosen to be the best, it was chosen to be integrable and cheap. "A
high-grade bulk-micromachined accelerometer costs a thousand times more and does
not fit on your board."

Amber marks the cost side of each column. Point that out once.
""")


# ───────────────────────────────────────────────────────── 32  release and stiction
s = S()
heading(s, "Release: the step that makes it a machine",
        "The sacrificial layer — and what happens when the beam comes down instead")
panels = [("1 · AS DEPOSITED", "structural film on top of a\nsacrificial layer — nothing "
           "moves yet", TEAL, "sac"),
          ("2 · RELEASED", "the sacrificial layer is etched away.\nThe beam is free. "
           "This is the machine.", TEAL, "free"),
          ("3 · STUCK", "surface forces pull it down and it\nstays down. The device is "
           "dead.", RED, "stuck")]
x = M
for title, cap, col, mode in panels:
    box(s, x, Inches(2.10), Inches(3.82), Inches(0.56), title, fill=col, edge=col,
        tcolor=CREAM, size=16, bold=True)
    px, pw = x + Inches(0.16), Inches(3.50)
    box(s, px, Inches(3.62), pw, Inches(0.50), "SUBSTRATE", fill=GRAY_L, edge=GRAY,
        tcolor=GRAY, size=12, bold=True, shape=MSO_SHAPE.RECTANGLE)
    if mode == "sac":
        box(s, px, Inches(3.27), pw, Inches(0.35), "SACRIFICIAL LAYER", fill=AMBER_L,
            edge=AMBER, tcolor=INK, size=11.5, bold=True, shape=MSO_SHAPE.RECTANGLE)
        box(s, px, Inches(3.05), pw, Inches(0.22), "", fill=TEAL_L, edge=TEAL,
            shape=MSO_SHAPE.RECTANGLE, edge_w=1.5)
    elif mode == "free":
        box(s, px, Inches(3.05), pw, Inches(0.22), "", fill=TEAL_L, edge=TEAL,
            shape=MSO_SHAPE.RECTANGLE, edge_w=1.5)
        txt(s, "free to move", px, Inches(3.30), pw, Inches(0.28), 12, TEAL,
            bold=True, align=PP_ALIGN.CENTER)
    else:
        box(s, px, Inches(3.40), pw, Inches(0.22), "", fill=RED_L, edge=RED,
            shape=MSO_SHAPE.RECTANGLE, edge_w=1.5)
        txt(s, "welded shut", px, Inches(3.12), pw, Inches(0.28), 12, RED,
            bold=True, align=PP_ALIGN.CENTER)
    txt(s, cap, px, Inches(4.28), pw, Inches(1.0), 15, INK, line=1.3,
        align=PP_ALIGN.CENTER)
    x += Inches(4.04)
box(s, M, Inches(5.55), CONTENT_W, Inches(0.90),
    "Stiction is Lecture 1's A/V ∝ 1/L arriving as a yield problem: at this scale "
    "surface forces beat the restoring force of the spring.",
    fill=AMBER_L, edge=AMBER, size=20, bold=True)
txt(s, "Stiction is also a field failure: condensation, shock or electrostatics can "
       "bring a beam down later.",
    M, Inches(6.52), CONTENT_W, Inches(0.4), 17, GRAY, line=1.3)
D.notes(s, """
TIMING: 0:58–1:00. Three panels, left to right, thirty seconds each.

Panel 3 is the point. "A restoring force that scales as L competes with a surface
force that scales as area over volume. Shrink far enough and the surface wins, and
the beam welds itself to the substrate. There is no electrical fix."

Connect it to minute three explicitly — A/V ∝ 1/L was an abstraction then and is
a scrapped wafer now.

Then the grey line, because it is the part students never expect: stiction is a
failure mode in the field, not only a yield problem in the fab. That is why it is
in a course about drift and failure.
""")


# ───────────────────────────────────────────────────────── 33  packaging
s = S()
heading(s, "The package is not protection. It is physics.",
        "Cavity · die attach · wire bond · seal · getter")
box(s, Inches(0.90), Inches(2.30), Inches(6.00), Inches(0.26), "LID  ·  HERMETIC SEAL",
    fill=GRAY, edge=GRAY, tcolor=CREAM, size=11, bold=True, shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(0.90), Inches(2.56), Inches(6.00), Inches(2.30), "", fill=GRAY_L,
    edge=GRAY, shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(1.25), Inches(2.85), Inches(5.30), Inches(1.55), "", fill=WHITE,
    edge=GRAY, shape=MSO_SHAPE.RECTANGLE, dash=MSO_LINE_DASH_STYLE.DASH)
txt(s, "CAVITY — sealed, often at reduced pressure", Inches(1.38), Inches(2.95),
    Inches(5.0), Inches(0.3), 12, GRAY, bold=True)
box(s, Inches(3.00), Inches(3.45), Inches(2.20), Inches(0.52), "MEMS DIE",
    fill=TEAL_L, edge=TEAL, tcolor=INK, size=14, bold=True, edge_w=2,
    shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(3.00), Inches(3.97), Inches(2.20), Inches(0.22), "DIE ATTACH",
    fill=AMBER_L, edge=AMBER, tcolor=INK, size=10.5, bold=True,
    shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(1.50), Inches(3.92), Inches(0.95), Inches(0.28), "GETTER",
    fill=AMBER, edge=AMBER, tcolor=DARK, size=10.5, bold=True,
    shape=MSO_SHAPE.RECTANGLE)
for x0, x1 in ((Inches(3.05), Inches(1.90)), (Inches(5.15), Inches(6.30))):
    curve(s, [(Emu(int(x0)), Emu(int(Inches(3.45)))),
              (Emu(int((x0 + x1) / 2)), Emu(int(Inches(3.05)))),
              (Emu(int(x1)), Emu(int(Inches(3.42))))], GRAY, 1.5)
txt(s, "wire bonds", Inches(5.30), Inches(2.72), Inches(1.5), Inches(0.3), 11,
    GRAY, bold=True)
for i in range(3):
    box(s, Inches(1.70) + i * Inches(2.10), Inches(4.86), Inches(0.85),
        Inches(0.18), "", fill=AMBER, edge=AMBER, shape=MSO_SHAPE.RECTANGLE)
box(s, Inches(0.90), Inches(5.04), Inches(6.00), Inches(0.30), "PCB — YOUR BOARD",
    fill=RED_L, edge=RED, tcolor=INK, size=12, bold=True, shape=MSO_SHAPE.RECTANGLE)
txt(s, "WHAT EACH PART IS ACTUALLY FOR", Inches(7.35), Inches(2.20), Inches(5.3),
    Inches(0.3), 12, GRAY, bold=True)
parts = [("CAVITY", "a void at a controlled pressure —\nand that pressure sets the "
          "damping", TEAL),
         ("DIE ATTACH", "an adhesive that cures, shrinks\nand stresses the die on day "
          "one", AMBER),
         ("WIRE BOND", "a mechanical link to a moving\nobject: a spring, and a stress",
          AMBER),
         ("SEAL", "keeps dust out of a 1–2 µm gap\nwhere one speck is fatal", TEAL),
         ("GETTER", "absorbs gas that leaks in, so the\ndamping stays as designed",
          TEAL)]
y = Inches(2.52)
for name, what, col in parts:
    box(s, Inches(7.35), y, Inches(1.62), Inches(0.52), name, fill=col, edge=col,
        tcolor=CREAM if col is not AMBER else DARK, size=12.5, bold=True)
    txt(s, what, Inches(9.12), y - Inches(0.01), Inches(3.50), Inches(0.54), 12.5,
        INK, line=1.2)
    y += Inches(0.61)
box(s, M, Inches(5.60), CONTENT_W, Inches(0.86),
    "Two of the five put the die under stress before you ever power it up. That "
    "stress is the “after soldering” in the conditions column.",
    fill=AMBER_L, edge=AMBER, size=20, bold=True)
txt(s, "Nothing on this slide is optional, and nothing on it is specified for your "
       "board.", M, Inches(6.55), CONTENT_W, Inches(0.4), 18, GRAY, line=1.3)
D.notes(s, """
TIMING: 1:00–1:02. Walk the cross-section left to right, then the list, then the
amber line. Do not linger on the drawing.

Kill misconception M5 explicitly: "Packaging is not a box you put the sensor in
afterwards. The cavity pressure sets the damping, so it sets the bandwidth. The
adhesive puts a preload on the die. The getter maintains the damping for ten
years. These are specifications, not protection."

The one number to say aloud: the gap is one to two micrometres, so a dust speck
is not dirt, it is a mechanical stop.
""")


# ───────────────────────────────────────────────────────── 34  the 10 mg collision
s = S()
heading(s, "Two tens of a milli-g, and they are not the same ten",
        "Name this collision out loud — it is a guaranteed exam misconception otherwise")
rows = [["", "Lecture 2's 10 mg", "Lecture 4's 10 mg"],
        ["What it is", "offset DRIFT over temperature", "zero-g OFFSET after soldering"],
        ["Where it comes from", "the temperature coefficient of the structure",
         "die attach, package and solder stress"],
        ["The arithmetic", "±0.5 mg/°C × 20 °C = 10 mg", "±10 mg typ, ±65 mg max"],
        ["Against the 8.73 mg signal", "1.15×", "1.15× typ,  7.45× max"],
        ["Can you fix it?", "NO — it moves after you calibrate",
         "YES — one-point calibration on your board"],
        ["Cost of the fix", "—", "one measurement, once, per unit"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.24, 0.38, 0.38], size=14.5,
          row_h=Inches(0.50), head_size=15,
          align=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
for j, col in ((1, RED_L), (2, TEAL_L)):
    c = t.cell(5, j)
    c.fill.solid(); c.fill.fore_color.rgb = col
    r = c.text_frame.paragraphs[0].runs[0]
    r.font.bold = True
    r.font.color.rgb = RED if j == 1 else TEAL
box(s, M, Inches(5.66), CONTENT_W, Inches(0.76),
    "Fabrication and packaging hand you a LARGE but REMOVABLE error. The "
    "temperature coefficient hands you a SMALL-LOOKING but IRREMOVABLE one.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=20, bold=True)
txt(s, "That both land on ten is a coincidence. The DIFFERENCE between them is the "
       "thesis of Module A.",
    M, Inches(6.50), CONTENT_W, Inches(0.4), 17, GRAY, line=1.3)
D.notes(s, """
TIMING: 1:02–1:04. THE MOST IMPORTANT TABLE IN THE LECTURE. Do not rush it.

Somebody objected at minute fourteen that you can calibrate an offset out. Name
them — by the objection, not the person — and agree: "You were right. This is
that answer."

Say the collision explicitly: "Two weeks ago ten milli-g ended a design. Today
ten milli-g is an inconvenience you fix with one measurement. Same magnitude,
opposite verdict, because one of them holds still and the other does not."

If you leave this unremarked, half the room will merge the two on the exam.
""")


# ───────────────────────────────────────────────────────── 35  poll 4
q4 = ("You are specifying a pressure sensor for the capstone project. Four numbers "
      "matter. Which one must you measure on your own assembly, because no datasheet "
      "can give it to you?")
opts4 = [("A", "the noise density at your chosen bandwidth"),
         ("B", "the sensitivity at 25 °C"),
         ("C", "the zero-offset shift caused by your enclosure clamping the sensor"),
         ("D", "the total error band over the operating temperature range")]
s = poll(D, 4, q4, opts4, minute=64,
         note="Transfer question. Different measurand, same distinction you have been "
              "building for the last two chunks.")
D.notes(s, """
TIMING: 1:04–1:06. Quick vote, sixty seconds, short discussion. Target 45–65 %
for C — this is a confidence check on outcome L4.5, not a discriminator, so a
high score is a good sign rather than a wasted vote.

A is the student who has not noticed that noise density is published and the
bandwidth is their own choice. One line: "you compute it, you do not measure it."

D is the student over-generalising Lecture 2. Worth a sentence: preferring the
total error band was right then, and it does not make it measurable-only now.

B should be rejected by nearly everyone.
""")


# ───────────────────────────────────────────────────────── 36  poll 4 answer
s = poll(D, 4, q4, opts4, minute=64, correct="C", reveal=True,
         note="A, B and D are all in the datasheet — D is the very figure Lecture 2 "
              "taught you to prefer. C depends on your enclosure, your screw torque and "
              "your gasket, and it exists nowhere but on your own bench.")
D.notes(s, """
TIMING: 1:06–1:08. Reveal, then the bridge, and say it immediately because it is
an assessment announcement.

"This is project deliverable 2 and it is Laboratory 3. Your sensor-selection
matrix has a required section headed 'specifications we must measure ourselves',
and that list starts today. If it is empty, you have not read your datasheet's
conditions column."

Then the generalisation: the test for that list is not "is it important?" but "does
it depend on something we build?" Screw torque, gasket, enclosure, board flex —
all ours. Sensitivity at 25 °C — theirs.
""")


# ───────────────────────────────────────────────────────── 37  the stress chain
s = S()
heading(s, "The stress chain", "Seven links, and only the first is specified by anyone")
txt(s, "THE CHAIN", M, Inches(1.90), Inches(4.20), Inches(0.26), 11, GRAY, bold=True)
txt(s, "WHAT IT CONTRIBUTES", M + Inches(4.40), Inches(1.90), Inches(4.20),
    Inches(0.26), 11, GRAY, bold=True)
txt(s, "SPECIFIED BY ANYONE?", M + Inches(8.85), Inches(1.90), Inches(3.04),
    Inches(0.26), 11, GRAY, bold=True)
links = [("DIE", "the transduction itself", "yes — the datasheet", TEAL),
         ("DIE ATTACH ADHESIVE", "offset shift, hysteresis", "partly — “after soldering”", AMBER),
         ("PACKAGE BODY", "the temperature coefficient", "partly", AMBER),
         ("SOLDER JOINTS", "asymmetric stress → cross-axis error", "NO", RED),
         ("PCB FLEX", "offset and cross-axis, load-dependent", "NO", RED),
         ("MOUNTING SCREW", "offset that changes when it is retightened", "NO", RED),
         ("5 mm RUBBER PAD", "Lecture 1's war story, in one part", "NO", RED)]
y = Inches(2.12)
for i, (name, contrib, spec, col) in enumerate(links):
    box(s, M, y, Inches(4.20), Inches(0.48), name, fill=WHITE, edge=col,
        tcolor=INK, size=15, bold=True, edge_w=2, shape=MSO_SHAPE.RECTANGLE)
    txt(s, contrib, M + Inches(4.40), y + Inches(0.10), Inches(4.30), Inches(0.36),
        14.5, INK)
    box(s, M + Inches(8.85), y, Inches(3.04), Inches(0.48), spec, fill=col,
        edge=col, tcolor=CREAM if col is not AMBER else DARK, size=13, bold=True)
    if i < 6:
        down_arrow(s, M + Inches(2.00), y + Inches(0.49), Inches(0.12),
                   Inches(0.20), color=col)
    y += Inches(0.615)
box(s, M, Inches(6.42), CONTENT_W, Inches(0.45),
    "Lecture 1's story ended on the seventh link. Lecture 4 ends on the same picture.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=17.5, bold=True)
D.notes(s, """
TIMING: 1:08–1:10. NEVER CUT THIS SLIDE. It is what makes Laboratory 3 make sense.

Build it downward, naming each link, and read the right-hand column aloud as you
go: yes, partly, partly, no, no, no, no.

Then stop on link seven and close the loop with week one: "In Lecture 1 a motor
died because somebody measured its vibration through a five-millimetre rubber
pad. That pad is the last link of this chain. The course's first story and its
fourth lecture are the same diagram."

The habit to install: the datasheet describes link one. You built links two to
seven.
""")


# ───────────────────────────────────────────────────────── 38  poll 1 answer
s = poll(D, 1, q1, opts1, minute=70, correct="B", reveal=True,
         note="Not secrecy, and not an application note. The chain you just drew has "
              "seven links and the manufacturer owns one of them. The number cannot "
              "exist — but the METHOD does: measure it on your own assembly.")
D.notes(s, """
TIMING: 1:10–1:13. Show the minute-8 distribution beside this if you recorded it;
the shift is the lecture's evidence that it worked.

Dismantle A in one sentence: "they publish noise density, which is far more
competitively sensitive than a mounting-stress figure."

Dismantle C properly, because it is the useful one: application notes tell you
how to MITIGATE mounting stress — symmetric pads, no vias under the part, keep it
away from the board edge. They do not specify your assembly's number either. If
somebody found an app note in the break, read its list aloud now.

Close: the debt from Lecture 2 is paid — not with a number, with a method.
""")


# ───────────────────────────────────────────────────────── 39  the honest ledger
s = S()
heading(s, "The honest ledger of going small", "Built with you — I ask for each row before I show it")
rows = [["Shrinking the device", "buys you", "costs you"],
        ["m ∝ L³", "—", "less mass → a higher noise floor"],
        ["k ∝ L", "—", "—"],
        ["f₀ ∝ 1/L", "higher bandwidth", "resonance moves into your signal band"],
        ["area / volume ∝ 1/L", "fast thermal response",
         "surface forces dominate → stiction"],
        ["batch fabrication", "unit cost, integration with electronics",
         "tolerances you cannot control"],
        ["packaging", "protection, handling", "stress you cannot specify"]]
t = table(s, M, Inches(2.10), CONTENT_W, rows, [0.24, 0.34, 0.42], size=15.5,
          row_h=Inches(0.52), head_size=15, mono_cols=(0,),
          align=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT])
for i in (1, 4, 6):
    c = t.cell(i, 2)
    c.fill.solid(); c.fill.fore_color.rgb = RED_L
    r = c.text_frame.paragraphs[0].runs[0]
    r.font.bold = True; r.font.color.rgb = RED
for i in (3, 5):
    c = t.cell(i, 1)
    c.fill.solid(); c.fill.fore_color.rgb = TEAL_L
    r = c.text_frame.paragraphs[0].runs[0]
    r.font.bold = True; r.font.color.rgb = TEAL
box(s, M, Inches(5.90), CONTENT_W, Inches(0.90),
    "The datasheet quantifies the middle column. The last two rows of the right-hand "
    "column are yours to measure.",
    fill=AMBER_L, edge=AMBER, size=20, bold=True)
D.notes(s, """
TIMING: 1:13–1:15. Build it with the class — ask for each row before revealing
it. This deliberately mirrors Lecture 1's ledger slide, so say "you have seen
this table's shape before" and let them recognise the form.

Two rows to insist on. k ∝ L gains nothing and costs nothing, which surprises
them and is worth ten seconds. And the bottom two rows are the new material:
batch fabrication and packaging were not on Lecture 1's version, because in week
one you had not met them.

Then the amber line, which is the whole synthesis in one sentence.
""")


# ───────────────────────────────────────────────────────── 40  the trade
s = statement(D, "Micro-scale is a trade,\nnot an improvement.",
              "Everything you gained, you gained by giving something up. The datasheet "
              "quantifies the gains — and the last two rows of that ledger are yours to "
              "measure, on your own board, with your own screwdriver.",
              size=40, eyebrow_text="what this lecture exists to earn", accent=AMBER)
D.notes(s, """
TIMING: 1:15–1:16. Read it once. Then stop for three seconds. Do not elaborate.

This is the answer to misconception M4 — smaller is better — and it is the
sentence a student should be able to quote back in the capstone defence.

If you want one optional line, use this one: "There is no version of this device
that is small, quiet, cheap and unaffected by your board. If a datasheet appears
to offer you all four, you have not read the conditions column."

Then Module A closes. Change your posture; the next slide is a different register.
""")


# ───────────────────────────────────────────────────────── 41  module A closes
s = S()
heading(s, "Module A ends here", "Four lectures. One method. Now watch it get applied seven times.")
txt(s, "You can now draw the chain, turn a request into a specification, read a "
       "datasheet against a requirement, and explain why a device behaves "
       "differently on your own board.",
    M, Inches(2.12), CONTENT_W, Inches(0.8), 19, INK, line=1.35)
txt(s, "LECTURES 5–11 ARE SEVEN INSTANCES OF ONE PATTERN", M, Inches(3.10),
    CONTENT_W, Inches(0.3), 13, AMBER, bold=True)
pattern = ["MEASURAND", "TRANSDUCTION", "STRUCTURE", "OUTPUT",
           "SPECIFICATIONS", "INTERFACE", "CALIBRATION", "FAILURE MODES"]
for i, name in enumerate(pattern):
    row, col = divmod(i, 4)
    x = M + col * (Inches(2.66) + Inches(0.42))
    y = Inches(3.48) + row * Inches(0.98)
    box(s, x, y, Inches(2.66), Inches(0.62), name, fill=TEAL_L, edge=TEAL,
        tcolor=INK, size=14, bold=True)
    txt(s, str(i + 1), x + Inches(0.08), y + Inches(0.03), Inches(0.3),
        Inches(0.25), 10, TEAL, bold=True, font=MONO)
    if col < 3:
        arrow(s, x + Inches(2.72), y + Inches(0.20), Inches(0.30), Inches(0.22),
              color=TEAL)
down_arrow(s, M + 3 * (Inches(2.66) + Inches(0.42)) + Inches(1.27), Inches(4.14),
           Inches(0.26), Inches(0.20), color=TEAL)
box(s, M, Inches(5.55), CONTENT_W, Inches(0.80),
    "Seven devices, one method. If you can state that pattern, the next seven weeks "
    "are one idea applied seven times rather than a list to memorise.",
    fill=DARK, edge=DARK, tcolor=CREAM, size=19, bold=True)
txt(s, "NEXT:  Lecture 5 — the accelerometer in full: structure 1 and principle 1, "
       "down to a register value.",
    M, Inches(6.50), CONTENT_W, Inches(0.4), 17, TEAL, bold=True)
D.notes(s, """
TIMING: 1:16–1:18. This is worth its ninety seconds — say the pattern out loud,
pointing at each box.

Why it matters: the single largest delivery risk in the semester plan is that
Lectures 5 to 11 are experienced as a list of unrelated devices. Naming the
pattern turns seven weeks into one method applied seven times.

Then the project bridge in one sentence: deliverable 2's sensor-selection matrix
uses exactly these eight headings, so today's "specifications we must measure
ourselves" list is the last column of it.

Do not add a summary slide. The exit ticket is the summary.
""")


# ───────────────────────────────────────────────────────── 42  exit ticket
s = S()
heading(s, "Exit ticket", "Two questions · ninety seconds · handed in at the door")
cards = [("1  ·  YOUR PROJECT", TEAL, CREAM,
          "Name one specification of the\nsensor in your capstone project\n"
          "that you will have to measure\nyourself — and say which stress\n"
          "path makes it necessary."),
         ("2  ·  THE PATTERN", AMBER, DARK,
          "Module A is over.\n\nIn one sentence: what is the\npattern that Lectures 5–11\n"
          "will repeat?")]
x = M
for title, col, tc, body in cards:
    box(s, x, Inches(2.15), Inches(5.85), Inches(0.68), title, fill=col, edge=col,
        tcolor=tc, size=17, bold=True)
    txt(s, body, x + Inches(0.14), Inches(3.10), Inches(5.55), Inches(2.2), 19,
        INK, line=1.45)
    x += Inches(6.20)
box(s, M, Inches(5.70), CONTENT_W, Inches(0.85),
    "Question 2 is the one I am grading myself on. If fewer than half of you can "
    "state the pattern, Lecture 5 opens with it and I am not behind.",
    fill=GROUND, edge=GRAY, size=18, bold=True)
txt(s, "Reading: reader chapter 4 — structures and fabrication. Its failure section "
       "is the mounting-screw story.",
    M, Inches(6.62), CONTENT_W, Inches(0.4), 16, GRAY, italic=True)
D.notes(s, """
TIMING: 1:18–1:20. End on time. Slips out before you start talking.

Q1 tests outcome L4.5 individually — group work at minute 104 can hide a student
who cannot do it. Accept any of: cross-axis after soldering, zero-g offset on
their board, clamping offset, mounting repeatability.

Q2 is the diagnostic: measurand → transduction → structure → output →
specifications → interface → calibration → failure modes. If fewer than half get
it, spend the first three minutes of Lecture 5 on it and do not feel behind.

These slips are the input to Lecture 5's opening slide. Transcribe them tonight.
""")


out = "../lecture-04/output/L4-MEMS-structures-transduction-and-packaging.pptx"
D.save(out)
print(f"saved {out}  ·  {len(D.p.slides._sldIdLst)} slides")
