# Lecture 1 — Activity Set
**MEMS, sensors, and the measurement-system architecture** · 80 min · 20–24 students

Five polls, one peer-instruction cycle per ConcepTest, two non-digital state changes.

**Voting method — no polling tool, and none needed.** Every poll is projected, and the
room votes by **simultaneous show of hands on a count**, one option at a time. Then, and
only then, the instructor takes two or three spoken answers. See the protocol below; it
is the same for all five polls and for both lectures.
Attention resets at min 8, 24, 40, 44, 62, 74 — no passive stretch exceeds 16 minutes.

**Delivery note for a first offering:** record the **first-vote** and **post-discussion**
distribution for Polls 2, 3 and 4. Those six numbers are the pilot's most valuable output.

---

## Poll 1 — Baseline commitment (min 4) · *no answer revealed*

> **The motor that died under observation.**
> A vibration monitor watched a 1500 rpm induction motor for six weeks. The screen showed a
> calm 20 Hz vibration line, slowly rising — read as normal load variation. In week seven the
> bearing seized and the motor was destroyed.
> Post-mortem: the accelerometer met every number in its datasheet. The board was fine. The
> firmware had no bug. The logger logged every sample.
>
> **Where was the fault?**

| | Option |
|---|---|
| A | The accelerometer was too cheap for industrial use |
| B | There was a firmware bug nobody found |
| C | Nobody ever specified the sample rate against the frequency of the fault they were looking for |
| D | Bearing degradation cannot be detected by vibration measurement |
| E | The maintenance team ignored a rising trend |

**Correct: C** — withheld until min 66.
**Purpose:** commitment, not assessment. A student who has voted is invested in the answer.
**Expected distribution:** A and E attract most votes; both blame a *component* or a *person*
rather than the absence of a *system specification*. That is precisely the habit this course
replaces.
**Script:** "Don't discuss yet, don't call it out — just commit. Hands up for A on my count:
three, two, one." Work through B, C, D, E. Then: "Hold that thought." Do **not** comment on
the distribution, and do **not** take spoken answers on this one — Poll 1 is the only poll
where you collect the vote and say nothing at all.

---

## The voting protocol  *(used for every poll in both lectures)*

No clickers, no phones, no cards. The question stays on the screen; the room votes with
hands, and then it talks.

| Step | What you do | Why it matters |
|---|---|---|
| 1 | **Silent commitment.** "Hands up for A on my count — three, two, one." Then B, C, D, E in turn. One raise per student. | Simultaneity is the whole trick. Sequential or voluntary answering lets the first voice set the room's answer. |
| 2 | **Record it.** Estimate to the nearest quarter of the room, in the margin of your notes. | This is the pilot's evidence. Precision is not needed — the *shift* is what you are measuring. |
| 3 | **Now listen.** "Someone who voted B — tell me why." Take two or three, from different options. | This is where you learn *what they were thinking*, which no clicker would ever have told you. |
| 4 | **Peer instruction.** "Find someone who voted differently. Ninety seconds. Convince them." | Requires a committed answer, which step 1 guaranteed. |
| 5 | **Re-vote**, same method, and **say both numbers out loud.** | Students who hear "forty per cent, then seventy-five" learn that the discussion did something. |

**The one rule: hands before voices.** If a confident student announces the answer during
step 1, that poll's data is gone — so cut it off early and kindly, every time, until the
class learns the rhythm. It takes about two lectures.

**Reticent first week?** Ask for eyes closed, on the first vote of Lecture 1 only. It
removes the social cost of being wrong in front of a cohort you have just met, and it is
almost never needed again.

**Why this is not a downgrade from clickers.** A show of hands gives you the distribution
*and* step 3, which a clicker cannot: the reasoning, in the student's own words, while the
misconception is still live in the room. For a first offering that commentary is worth more
than the numbers.

---

## Poll 2 — ConcepTest: where accuracy dies (min 24) · outcomes L1.1, L1.2

> An accelerometer with **0.061 mg resolution** is bolted to a motor housing through a **5 mm
> rubber pad**. The firmware reads the device correctly and logs 16-bit values. The engineer
> reports the vibration amplitude to three decimal places.
>
> **Which stage of the measurement chain has already destroyed the accuracy of that number?**

| | Option | Diagnosis if chosen |
|---|---|---|
| A | Digitisation — 16 bits cannot support three decimal places | Resolution/accuracy confusion (M1) |
| B | Unit conversion — mg was never converted to m/s² | Real error, but changes the *scale*, not the *validity* |
| C | **Mechanical coupling — the rubber pad attenuates and phase-shifts the vibration before any electronics see it** | **Correct** |
| D | No stage — 0.061 mg resolution guarantees the digits are meaningful | Resolution = truth (M1 + M4) |

**Target:** 40–60 % first vote.
**Teaching point:** the measurement chain **begins before the sensor**. If the mechanical path
lies to the proof mass, no amount of downstream precision recovers the truth. This is why
Lecture 5 specifies mounting orientation and Lecture 16 specifies mechanical location — they
are not afterthoughts, they are the first link.
**If >70 % correct:** skip the discussion, take one sentence of justification, move on.
**If <30 % correct:** do not discuss yet. Re-teach with the rubber pad drawn as a low-pass
filter between measurand and proof mass, then re-vote.

---

## Poll 3 — ConcepTest: scaling (min 40) · outcome L1.3 · **hardest item of the lecture**

> A MEMS accelerometer's proof mass and suspension beams are **all** scaled down by a factor
> of 10 (isotropic scaling — every dimension shrinks equally).
>
> **Which statement is true?**

| | Option | Diagnosis if chosen |
|---|---|---|
| A | **Resonant frequency rises ×10, and thermomechanical noise gets worse** | **Correct** |
| B | Resonant frequency falls ×10, and noise improves because the device is smaller | Wrong direction on both |
| C | Resonant frequency is unchanged — mass and stiffness both shrink, so the ratio is constant | The seductive one: assumes k and m scale together |
| D | Resonant frequency rises ×10, and noise improves because there is less material to vibrate | "Smaller is uniformly better" (M3) |

**Target:** 30–50 % first vote. If it lands above 70 %, the scaling chunk was too explicit —
note it for next year and shorten C2.

**Why C is the trap and how to kill it:** stiffness and mass do **not** scale together.
For isotropic scaling by factor *s*: beam stiffness `k = E·w·t³/(4L³) ∝ s`, while
`m ∝ s³`. Therefore `f₀ = (1/2π)√(k/m) ∝ √(s/s³) = 1/s`. Shrink by 10 → **f₀ rises ×10.**
Write the two exponents side by side on the board — `k ∝ L¹`, `m ∝ L³` — and let the students
see that the ratio cannot be constant.

**Why noise gets worse:** thermomechanical (Brownian) noise-equivalent acceleration scales as
`√(4k_BT·ω₀/(m·Q))` — it rises as the proof mass falls. This is the honest answer to "why
don't they just make it smaller": you buy bandwidth and lose noise floor. Same trade appears
in the datasheets of Lecture 2 and in Lab 3's gyro bias.

**Peer-instruction script:** "Find someone who voted differently from you. You have 90 seconds.
Your job is to make them change their answer — using the two exponents, not your intuition."
Re-vote before revealing. Announce both percentages aloud; students should see the shift.

---

## State change — non-digital retrieval sketch (min 44–48)

1. "Stand up." (10 s — genuinely do this; it resets posture and attention.)
2. **Slides blank.** In pairs, one sheet of paper: redraw the measurement chain from memory,
   every box, with an arrow into and out of each. 90 seconds.
3. "Now mark with an X every box where the motor's number could have been ruined."
4. Show the correct chain. Students self-correct in a different colour — they keep the sheet;
   it is the reference page for Lab 1.

**Why this and not a video:** free recall with the slides off is a far stronger memory
intervention than re-reading, and it hands every student a personally-generated artefact
they will actually use at the bench in Week 2.

---

## Poll 4 — Transfer (min 62) · outcome L1.4

> You must detect whether the bearing of a **1500 rpm** motor is degrading. The literature says
> bearing fault energy appears between **1 and 4 kHz**.
>
> **Which single specification line decides whether your system can work at all?**

| | Option | Diagnosis if chosen |
|---|---|---|
| A | Full-scale range ≥ ±16 g | A real constraint — but the wrong one to fail on |
| B | **Bandwidth ≥ 4 kHz, sample rate ≥ 8 kHz, with anti-alias filtering** | **Correct** |
| C | Resolution ≤ 0.1 mg | Resolution again looks like the answer (M1) |
| D | Operating temperature up to 85 °C | Necessary for survival, irrelevant to detection |

**Target:** 55–75 % — this one should be gettable; it is the payoff of C1 and C3 and the bridge
to the hook's reveal.
**Teaching point:** every distractor is a specification line you genuinely need. The engineering
judgement is knowing which line, if wrong, makes the system *incapable* rather than merely
*imperfect*. That is what "requirements → specification" means in practice.
**Bridge:** "Hold that answer for four minutes. We're about to find out what the motor's
monitor actually had."

---

## Synthesis — resolving the hook (min 66–74)

Sequence matters; do not shortcut it.

1. **Before revealing anything:** "On your chain sketch, put your finger on the box where you
   now think this failed." (Physical commitment — every student, visible to you.)
2. Show the real numbers: fault signature ≈ 1.5 kHz · sample rate 100 Hz · no anti-alias filter.
3. Draw the aliasing on the board: 1500 Hz sampled at 100 Hz folds down to
   `1500 − 15×100 = 0` … work the arithmetic live to `|1500 − 1500| = 0`, then show that a
   1520 Hz component appears at 20 Hz. **There is the calm 20 Hz line.** The monitor was
   faithfully displaying the destruction of the bearing, relabelled as a slow load variation.
4. Re-run Poll 1. Show the two distributions side by side.
5. The line to land, and to repeat in Lecture 3: **"Nothing was broken. Every part met spec.
   The system was never specified."**

Then name what was missing — one line in a document:
`Bandwidth: ≥ 4 kHz, anti-aliased; sample rate ≥ 8 kHz.` One line. One motor.

---

## Poll 5 — Exit ticket (min 76) · anonymous, collected

Two prompts, one index card or one form:

1. **Applied:** "A drone must hold altitude to ±0.5 m. Write **one** specification line for its
   pressure sensor." *(Marks L1.4. Expect range/resolution confusion — that is the data you want.)*
2. **Muddiest point:** "What is the one thing from today you are least sure about? One sentence."

**Use of the data:** transcribe every muddiest point into a single list. Open Lecture 2 by
answering the top three in 90 seconds, by name of concept, not name of student. This does more
for credibility than any other two minutes in the course — and for a first offering, that list
*is* your misconception inventory for next year.

---

## Formative quiz (post-lecture, 10 min, ungraded or low-stakes)

Released after class; due before Lecture 2. Required by the plan's lecture-package standard.

**Q1.** Name the stages of a measurement chain from physical quantity to logged value, in order.
*Key:* measurand → mechanical coupling/mounting → transduction → analog conditioning →
anti-alias filtering → ADC (sampling + quantisation) → raw codes → scaling to SI units →
timestamp → storage/decision.

**Q2.** Give one example of information that is lost at the ADC and cannot be recovered later.
*Key:* any frequency content above half the sample rate — it is aliased into the band
irreversibly; also amplitude detail below one LSB. Note "cannot be recovered" is the point.

**Q3.** A MEMS resonator is scaled down ×5 isotropically. What happens to its resonant
frequency, and why?
*Key:* rises ×5. `k ∝ L`, `m ∝ L³`, so `f₀ ∝ 1/L`.

**Q4.** Name one sensor property that gets **worse** as the device gets smaller, and say why.
*Key:* thermomechanical noise floor (smaller proof mass → larger noise-equivalent
acceleration); or stiction/surface forces (A/V ∝ 1/L, so surface forces dominate body forces);
or increased sensitivity to packaging stress and thermal drift.

**Q5.** Classify each of these and name its measurand: (a) MEMS microphone, (b) piezoelectric
buzzer, (c) strain gauge, (d) MEMS mirror.
*Key:* (a) sensor, sound pressure; (b) actuator, electrical → acoustic; (c) sensor, strain
(passive — resistance change, needs excitation); (d) actuator, electrical → angular
displacement of a reflective surface.

**Q6.** In one sentence: why did the motor's monitor show a calm 20 Hz line?
*Key:* the ~1.5 kHz fault energy was aliased by a 100 Hz sample rate with no anti-alias
filter, appearing as a low-frequency component that was misread as load variation.

---

## Contingency

| Failure | Response |
|---|---|
| A student calls out an answer before the vote | Stop, smile, and say "hands first, reasons after." Then vote. An anchored room produces no usable first vote and no measurable shift. |
| The room will not raise hands at all (week 1 reticence) | Vote by closed eyes: "eyes shut, hands up for A." It feels theatrical and it works, and after one lecture it is rarely needed again. |
| Running >6 min late at min 44 | Cut the pair-sketch to 45 s and drop the second requirements example in C3 (students do it as homework instead). **Never cut the synthesis** — the hook must resolve, or the lecture has no ending. |
| Running >12 min late | Also move the semester-project brief to a handout and Lecture 2's opening. Protect: chain diagram, scaling poll, hook resolution, Lab 1 bridge. |
| Poll 3 collapses (<20 % correct after re-vote) | Stop. Put `k ∝ L¹` and `m ∝ L³` on the board, derive `f₀ ∝ 1/L` in three lines, and re-vote a third time. This concept is load-bearing for Lectures 5, 6 and 11 — it is worth 4 extra minutes here. |
| Ahead of schedule | Extend the application survey with a live phone teardown discussion: "name every sensor in the phone in your pocket, and the measurand for each." |
