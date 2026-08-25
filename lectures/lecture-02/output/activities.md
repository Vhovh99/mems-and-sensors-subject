# Lecture 2 — Activity Set
**Sensor specifications and datasheet-based selection** · 80 min · 20–24 students

Five polls, one guided pair activity, one team decision table, two state changes.
Attention resets at min 10, 24, 36, 46, 56, 70.

**Voting method:** projected question, **simultaneous show of hands on a count**, then
spoken reasoning. Full protocol in `lecture-01/output/activities.md` — hands before
voices, every time. Poll 3 below is the most diagnostic vote in the pilot and it only
works if the first vote is un-anchored.

> **All Part A / Part B figures below are *representative* commercial specifications**, chosen
> so the arithmetic is exact and the engineering conclusion is unambiguous. They are typical of
> real consumer and industrial accelerometers but are **not** attributed to a named product.
> Where the class works on a *named* device (the datasheet hunt), students read the actual PDF
> and the instructor verifies against the revision in use. Teaching students not to trust an
> unsourced number, then handing them unsourced numbers, would be self-defeating.

---

## The running case: the solar-tracker tilt sensor

One requirement carries the whole lecture:

> A solar-tracker frame must report its tilt angle to **±0.5°**, outdoors, over an ambient
> range of **0 to 40 °C**. It is calibrated once on the bench at 20 °C. Choose the accelerometer.

The key conversion, put on the board in minute 12 and never erased:

`tilt of 0.5°  →  sin(0.5°) × 1 g  =  8.73 mg of signal`

**Everything else in the lecture is measured against those 8.73 mg.** Any error term larger
than that is fatal; any error term far below it is irrelevant no matter how good it looks on a
front page. This single number turns "which is better?" into arithmetic.

### The two candidates

| | **Part A** — "high resolution" | **Part B** — unremarkable |
|---|---|---|
| Resolution | 16-bit, ±2 g → **0.061 mg/LSB** | 14-bit, ±4 g → **0.488 mg/LSB** |
| Noise density | 100 µg/√Hz | 100 µg/√Hz |
| Zero-g offset | ±40 mg | ±10 mg |
| Offset temp. coefficient | **±0.5 mg/°C** | **±0.1 mg/°C** |
| Unit price | €1.80 | €4.20 |
| Ecosystem | popular Arduino library | datasheet and app note only |

### The resolution (revealed at min 70 — students compute it themselves at min 50)

Error budget at 50 Hz bandwidth, calibrated at 20 °C, ambient 0–40 °C so ΔT = ±20 °C:

| Term | Part A | Part B |
|---|---|---|
| Noise, `100 µg/√Hz × √50 Hz` | 0.707 mg | 0.707 mg |
| Quantisation, `LSB/√12` | 0.018 mg | 0.141 mg |
| Offset drift, `TC × ΔT` | **10.0 mg** | **2.0 mg** |
| **Total (RSS)** | **10.02 mg** | **2.13 mg** |
| **As an angle** | **0.574°** | **0.122°** |
| **Verdict against ±0.5°** | ❌ **FAILS** | ✅ passes, 4× margin |

**The punchline, and the sentence to write on the board:**
> Part A resolves **8× finer** than Part B — and **fails the requirement**. Part B resolves
> 0.028° of tilt, eighteen times finer than the 0.5° we need, so its resolution was never the
> question. The specification was decided by a line neither front page advertised.

You cannot calibrate away drift with a one-time bench calibration. You can only choose a part
that does not drift, or measure temperature and compensate — which is Lecture 14.

---

## Poll 1 — Baseline (min 4) · *answer withheld to min 70*

Show only the two front pages: `16-bit · ±2 g · 0.061 mg/LSB · "high resolution, low noise"`
versus `14-bit · ±4 g · 0.488 mg/LSB`.

> You must order today. The frame must report tilt to ±0.5°. **Which part?**

| | Option | Diagnosis if chosen |
|---|---|---|
| A | Part A — 8× finer resolution | Resolution = accuracy (M1); headline-number selection (M5) |
| B | Part B | Right answer, usually for the wrong reason at this stage |
| C | **Cannot be decided from front pages alone** | The professional answer |

**Expected:** a clear majority for A. **Correct answer is C, and then B** — and say exactly
that at the reveal: "The right first answer was *I don't have enough information yet*. The
right second answer, after twelve minutes of arithmetic, was B."

**Script:** "No discussion. Commit. I am going to show you at the end of the hour that most of
this room just chose a part that cannot meet the requirement — and that the datasheet told us
so on page 9."

---

## Poll 2 — ConcepTest: accuracy vs precision vs resolution (min 24) · outcome L2.1

> A pressure sensor sits in a chamber held at a true, constant **1000.0 hPa**. It is read 100
> times. Every reading falls between **1012.3 and 1012.5 hPa**.
>
> **The device is:**

| | Option | Diagnosis if chosen |
|---|---|---|
| A | Accurate but not precise | Terms swapped |
| B | **Precise but not accurate** | **Correct** |
| C | Both — the spread is only 0.2 hPa | Small spread read as truth (M1) — the main target |
| D | Neither, because the resolution is not stated | Sophisticated-sounding evasion |

**Target:** 45–65 % first vote.

**The follow-up question that does the real teaching** — ask it immediately after the reveal,
show of hands, no device:
> **"Which of these two problems can I fix with a calibration?"**

Answer: the **12.4 hPa offset — yes**, with a single-point calibration against a reference.
The **0.2 hPa spread — no**; random scatter is not removable by calibration, only reducible by
averaging (and averaging costs you bandwidth). Land it as a rule:

> **Systematic error is a calibration problem. Random error is a bandwidth problem.
> Drift is a component-selection problem.**

That rule is the spine of Lecture 14 and of Labs 3 and 5. Repeat it at the end of the lecture.

---

## Guided pair activity — the datasheet hunt (min 28–46)

Pairs, one real datasheet PDF per pair (printed extract or on a laptop). Use the **actual
device in the lab kit** so the skill transfers directly to Lab 1 in Week 2.

**Use the actual part: ST ISM330DHCXTR** (iNEMO 6-axis IMU, datasheet DS13012 Rev 6) —
the IMU in the course kit. Every number the students find here they will type into the
console in Week 2, which is what makes the hunt worth doing.

**Six numbers to find (8 minutes, written down with page numbers):**

| # | Find | What it teaches |
|---|---|---|
| 1 | Supply voltage range, and the **separate** I/O supply if there is one | Lab 1's first gate — get this wrong and you destroy the part |
| 2 | Sensitivity at **each** selectable full-scale range | Sensitivity is a configuration, not a constant |
| 3 | Zero-g / zero-offset level **and** its temperature coefficient | The number that decided our whole lecture |
| 4 | Noise density, **and the bandwidth or ODR it was measured at** | A noise figure without its conditions is meaningless |
| 5 | The device identification register and its **expected value** | Lab 1's `WHO_AM_I` handshake — they will need this in Week 2 |
| 6 | Whether the headline numbers are `typ`, `min` or `max`, **and at what temperature** | Datasheet literacy |

**Then the question with no answer in the document (2 minutes):**
> **"What is this device's cross-axis sensitivity after it has been reflow-soldered onto
> your board?"**

It is not in the datasheet — and it cannot be. Cross-axis sensitivity is specified for the
packaged die, but board-level mounting stress, solder-joint asymmetry and PCB flex change it.
The honest engineering answer is: *the datasheet cannot tell me this; I must measure it on my
own assembled board.* This is the single most important habit in the lecture, and it is why
Lab 3 exists.

**Debrief (min 44–46, standing):** hands up — which of the six was hardest to find, and why?
Usual winner is #4, because the conditions are in a footnote. Name that: **the conditions are
where the truth lives.**

---

## Poll 3 — ConcepTest: the calculation (min 56) · outcome L2.3

> An accelerometer specifies noise density **100 µg/√Hz**. You configure it for an output data
> rate of **200 Hz** and a measurement bandwidth of **50 Hz**.
>
> **Approximately what RMS noise appears in your readings?**

| | Option | The specific error it diagnoses |
|---|---|---|
| A | ≈ 0.1 mg | Ignored bandwidth entirely — read the density as if it were the answer |
| B | **≈ 0.7 mg** | **Correct: `100 µg/√Hz × √50 Hz = 707 µg`** |
| C | ≈ 1.4 mg | Used √ODR instead of √bandwidth — the ODR/bandwidth confusion (M7) |
| D | ≈ 5 mg | Multiplied by bandwidth instead of its square root |

**Target:** 40–60 % first vote. Every distractor is a *specific procedural error*, so the
distribution tells you exactly which step to re-teach — this is the most diagnostic poll in
the pilot.

**After the re-vote, the point that generalises:** noise is not a property of the sensor alone.
It is a property of the sensor **and the bandwidth you chose**. Halve your bandwidth and you
improve noise by √2 — for free, if the signal allows it. Widen it to chase fast events and you
pay in noise. This is the same trade the motor's monitor got wrong in Lecture 1, seen from the
other side.

**Then, immediately, the reframe (60 s):** "We just computed 0.707 mg of noise. Our measurand
is 8.73 mg. Our drift term is 10 mg. **Which term should you have spent your afternoon on?**"

---

## Team decision table (min 60–70) · outcome L2.4

Teams of 3, one sheet, 8 minutes. Three candidates: Part A, Part B, and **Part C** —
`16-bit, ±2 g, 60 µg/√Hz, offset ±5 mg, TC ±0.05 mg/°C, €11.50, 3 mm × 3 mm, 0.9 mA`.

Fill and commit:

| Criterion | Weight | A | B | C | Source of number |
|---|---|---|---|---|---|
| Meets ±0.5° over 0–40 °C | **pass/fail** | | | | computed, not read |
| Total error as an angle | high | | | | your RSS |
| Unit cost at 500 units | medium | | | | |
| Current draw | medium | | | | |
| Ecosystem / library | **low** | | | | |

**Required output:** one sentence beginning *"We specify Part ___ because ___"*, naming the
**dominant error term**, not the headline number. Two teams read theirs aloud.

**Part C is a deliberate trap in the other direction:** it is technically the best part and it
costs 6× Part B while adding no capability the requirement needs. Over-specifying is also an
engineering failure. If a team picks C, ask: "What did the customer get for the extra €3,650?"

**Closing rule (min 70), quoted from the course plan itself:**
> *"Avoid selecting a part only because an Arduino library exists; students must still see the
> underlying configuration and data path."*

Part B had no library. Part A had one. Part A cannot do the job.

---

## Poll 4 — Transfer to a new measurand (min 72) · outcome L2.4

Deliberately **not** the tilt case — transfer is only demonstrated on a problem the
students have not already seen worked.

> Water level in an outdoor tank, **2 m deep** (≈20 kPa full scale), to be reported to
> **±20 mm**. Water temperature swings **5–35 °C**.
> **Sensor P:** total error band **±0.25 % FS over 0–50 °C**.
> **Sensor Q:** **±0.05 % FS at 25 °C**; temperature coefficient **not specified**.
>
> **Which do you specify?**

| | Option | Diagnosis if chosen |
|---|---|---|
| A | Sensor Q — five times better accuracy | Headline selection again (M5), in a new context |
| B | **Sensor P — its error is bounded over the whole temperature range; Q's is specified at one point only** | **Correct** |
| C | Either — the temperature coefficient can be measured later | "Someone else's problem" |
| D | Sensor Q, calibrated at 25 °C before installation | "Calibration fixes everything" (survives from Poll 2) |

**The arithmetic:** P's ±0.25 % of 20 kPa = 50 Pa ≈ **5.1 mm** — comfortably inside ±20 mm,
and *guaranteed across the operating range*. Q's ±0.05 % = 10 Pa ≈ **1.0 mm** at 25 °C and
**unknown at 5 °C**, because the coefficient is not specified at all.

**The point:** you cannot write a defensible error budget for Q. An unspecified coefficient is
not a small error — it is an **unbounded** one. A total error band over the operating range
beats a headline accuracy at one temperature, every time.

**Why this is the right transfer item:** in the tilt case the killer term was drift the
students could *compute*. Here it is drift they cannot compute at all — same lesson, harder
version, different measurand. If C or D still attract votes here after Poll 2's calibration
rule, that is a genuine finding worth recording for next year.

---

## Poll 5 — Exit ticket (min 76) · anonymous, collected

1. **Computed:** "A sensor gives 200 µg/√Hz. You set a 100 Hz bandwidth. State the RMS noise."
   *(Key: `200 × √100 = 2000 µg = 2 mg`. Marks L2.3 independently of the group work.)*
2. **Judgement:** "Name the one specification you will look for first, for the rest of your
   career, before the headline number." *(Looking for: the conditions block — `typ/min/max`,
   temperature, supply — or offset drift. Both are right.)*
3. **Muddiest point:** one sentence.

---

## Formative quiz (post-lecture, 15 min)

**Q1.** Define accuracy, precision, and resolution so that the three definitions cannot be
confused. Give a device that is precise but inaccurate.
*Key:* accuracy = closeness to the true value (systematic); precision = repeatability of
readings about their own mean (random scatter); resolution = smallest change the output can
represent. A sensor with a large uncorrected offset but very low noise.

**Q2.** Which of these can a single-point bench calibration remove: offset, random noise,
temperature drift, quantisation? Explain each.
*Key:* offset — yes, at the calibration temperature. Random noise — no (only averaging reduces
it, at the cost of bandwidth). Temperature drift — no; it needs a temperature measurement and
a compensation model, since a single point captures only one temperature. Quantisation — no,
it is set by the LSB, though dither/averaging can help below one LSB.

**Q3.** A sensor is 150 µg/√Hz. You need 20 Hz of bandwidth. Compute the RMS noise. Then state
what happens if you widen the bandwidth to 80 Hz.
*Key:* `150 × √20 = 671 µg ≈ 0.67 mg`. At 80 Hz: `150 × √80 = 1342 µg ≈ 1.34 mg` — exactly
double, because bandwidth quadrupled.

**Q4.** A datasheet gives offset TC as ±0.3 mg/°C. The device is calibrated at 25 °C and used
from −10 to +60 °C. What is the worst-case offset error from drift alone, and as a tilt angle?
*Key:* worst ΔT = 35 °C (25 → 60). `0.3 × 35 = 10.5 mg` → `asin(0.0105) ≈ 0.60°`.

**Q5.** Your requirement is 8.73 mg of signal. Your candidate has 0.061 mg resolution and
10 mg of drift. In one sentence, what is wrong with calling this a "high-resolution solution"?
*Key:* the resolution is 140× finer than needed while the drift alone exceeds the entire
measurand — the part resolves a number that is wrong. Resolution is not accuracy.

**Q6.** Give one performance-limiting property that a datasheet **cannot** specify for your
finished product, and say who must determine it.
*Key:* board-level effects — cross-axis sensitivity after soldering, package stress from PCB
flex, thermal gradients across the board, mounting compliance. The integrator must measure it
on the assembled unit.

---

## Contingency

| Failure | Response |
|---|---|
| No printed datasheets / laptops unavailable | Project **one** datasheet page and run the hunt as a whole class, calling on pairs for each of the six numbers. Loses independence, keeps the skill. |
| A student calls out an answer before the vote | "Hands first, reasons after." Re-run the count. Poll 3's diagnostic value depends entirely on an un-anchored first vote. |
| Running >8 min late at min 56 | Cut Part C from the decision table (two candidates, 5 min) and set it as homework. **Never cut Poll 3 or the reveal** — the arithmetic *is* the lecture. |
| Running >15 min late | Drop the decision table entirely; do the reveal from the front with the class calling out terms. Assign the table as the take-home. |
| Poll 3 collapses (<25 %) | Work `√Hz` arithmetic on the board with units written out in full: `µg/√Hz × √Hz = µg`. Unit cancellation is usually the actual blocker, not the physics. Re-vote. |
| Ahead of schedule | Hand out a third datasheet from a *different* manufacturer for the same measurand and ask: "these two parts claim the same accuracy — are they claiming it under the same conditions?" (They will not be.) |
