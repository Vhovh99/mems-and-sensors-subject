# Laboratory 1 — Check-off checklist and rubric

## Part 1 · Bench gate (0–10 min) — pass/fail, not graded

The instructor signs pre-lab section D only when the student states, aloud and
unprompted:

- [ ] the supply voltage they will connect
- [ ] the logic level of the board's I²C pins
- [ ] which two lines need pull-ups, and to which rail
- [ ] what they will read first, and its expected value
- [ ] what they will do if that first read fails

**A team without a signature does not power their board.** Give them a printed
datasheet and let them complete the pre-lab at the bench; they will finish late and
that is the intended consequence. Do not waive this — the gate is the only thing
standing between a 1.8 V I/O part and a 5 V rail.

---

## Part 2 · Live check-off (70–80 min) — pass/fail per item

Ask at the bench, with the hardware running. All five must pass.

| | Question | A pass looks like |
|---|---|---|
| 1 | Show me the device ID reading | Serial line showing read value **and** expected value |
| 2 | Show me the 1 g test | Mean magnitude within 900–1100 mg, ten samples recorded |
| 3 | Which register sets the range? What happens to sensitivity if I change it? | Names the register **and** says sensitivity changes, so the scale constant must change with it |
| 4 | Turn the board — show me the axis that will change, *before* you turn it | Correct prediction of axis **and** sign |
| 5 | Which stage of Lecture 1's chain did you just build? | Identifies stages 3→6, ideally naming the codes→units step as the one they wrote |

Question 4 is the one that separates understanding from transcription. A team that
copied a working configuration from a neighbour will predict the wrong axis.

---

## Part 3 · Submission rubric — 21 points

Two pages plus the log. Marks are for **evidence**, not for prose.

| Criterion | Outcome | Pts | Full marks | Half marks | Zero |
|---|---|---|---|---|---|
| **Connection diagram** | Lab1.2 | 3 | Matches what was actually built; every pin labelled with board name *and* physical position; pull-ups shown with values | Diagram present but generic, or pin positions missing | Copied from the handout unchanged |
| **Pre-lab datasheet table** | Lab1.1 | 3 | All 11 rows correct **with page numbers** | Values present, page numbers missing | Blank rows, or values inconsistent with the part on the bench |
| **Register table** | Lab1.3 | 4 | Every register, address, value written, and a *reason* per row that refers to the measurement; bit pattern matches the pre-lab C3 diagram | Values right, reasons generic ("to enable it") | No justification column |
| **Range-change comparison (2.4–2.6)** | Lab1.3 | 2 | Raw codes differ, converted values agree, and the one-sentence explanation is correct | Data present, explanation muddled | Missing, or converted values disagree with no comment |
| **Conversion arithmetic** | Lab1.4 | 3 | Two's-complement handling and the sensitivity multiplication shown **in full for one axis**, in the student's own working | Answers correct, working not shown | Console output copied with no conversion |
| **1 g test and SI conversion** | Lab1.4 | 3 | Ten samples converted, mean magnitude, rotation test **with the prediction written before turning**, m/s² conversion, % difference from 9.81 | Some elements missing | No plausibility check performed |
| **Error discussion (3.5)** | Lab1.4 | 2 | Two distinct causes named, correctly split into calibratable and not | One cause, or the split is wrong | Absent, or "sensor error" |
| **Fault exercise (1.6)** | Lab1.2 | 1 | `scan` and ID behaviour recorded for all three faults, **and** the instrument question answered (oscilloscope or logic analyser on SDA/SCL — look for whether the lines idle high) | Symptoms only | Not attempted |
| **Log and statistics (3.7)** | Lab1.5 | 2 | 200 samples with converted columns, mean and standard deviation of magnitude, and a comparison against the Lecture 2 noise figure | Log converted, no statistics | Raw console dump only |

**Deductions**
- −2 any numerical value reported without units, anywhere in the submission
- −2 submission exceeds two pages excluding the log
- −1 raw codes reported without the corresponding converted values

**Units are not a formatting preference in this course.** A number without a unit is
not a measurement, and this deduction applies for all sixteen weeks.

---

## What "good" looks like

A strong submission is short and almost entirely tables. It contains at least one
sentence that says something *went wrong* and what the team did about it — a magnitude
that came out at 4000 mg until they re-read the range encoding, a bus that would not
answer until they found the second set of pull-ups on the breakout.

A weak submission is fluent, longer, and contains no evidence that anything was ever
measured twice.

Say this to the class at the start of the semester, and mean it.

---

## Instructor data to record (first offering)

Log these four numbers. They are what tells you whether Lab 1 works as designed.

| Metric | Value | Interpretation |
|---|---|---|
| Teams arriving with a complete pre-lab | ___ / ___ | <70 % → the pre-lab is too long or was not signposted |
| Teams that read the device ID by minute 30 | ___ / ___ | <60 % → the fault exercise must move to Lab 2 |
| Teams that reached stage 3.7 (the log) | ___ / ___ | <50 % → 80 min is too short even without a build step |
| Teams needing help with two's complement **by hand** | ___ / ___ | high → add a worked byte-assembly example to Lecture 3; this is now done on paper, so the count is a direct measure |
| Teams whose magnitude was off by a factor of 2/4/8 | ___ / ___ | the range-encoding trap, working as intended |
