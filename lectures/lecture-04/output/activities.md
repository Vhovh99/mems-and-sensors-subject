# Lecture 4 — Activity Set
**MEMS structures, transduction, fabrication and packaging overview** · 80 min · 20–24 students

Four content polls, one withheld-answer poll spanning the lecture, one sequencing
activity, one closing synthesis. Attention resets at min 11, 22, 32, 46, 56, 68.

**Voting method:** projected question, **simultaneous show of hands on a count**, then
spoken reasoning — hands before voices. Full protocol in
`lecture-01/output/activities.md`.

> **Numbers.** The zero-g level figures (±10 mg typ, ±65 mg max, at 25 °C after
> soldering) and the ±0.5 % cross-axis figure are from the ISM330DHCX datasheet
> DS13012 Rev 6. The 8.73 mg tilt anchor is Lecture 2's. Where a *representative* device
> is used instead of a named part — the piezoelectric accelerometer in Poll 3 — the slide
> says so.

---

## Poll 1 · minute 8 · baseline, answer withheld until minute 70

**Stem**

> In Lecture 2 you were asked for a device's **cross-axis sensitivity after it is
> soldered to your board**, and the answer was that the number is not in the datasheet.
>
> Why is it not there?

**Options**

| | |
|---|---|
| A | It is proprietary — competitors would learn from it |
| B | It depends on your board and your assembly, so no manufacturer can specify it |
| C | It is in the application note, not the datasheet |
| D | It is the same as the package-level figure, so printing it twice would be redundant |

**Correct: B.** Withhold until minute 70, by which point the class has seen the stress
chain and the answer is not a guess but a derivation.

**Distractor diagnosis**

- **A** — the commercial-secrecy instinct. Common and worth dismantling briefly: the
  manufacturer publishes noise density, which is far more competitively sensitive.
- **B** — correct. Expect 25–40 % at minute 8; this poll is less about the split than
  about planting the question.
- **C** — the plausible-sounding wrong answer, and the most useful one, because a
  student will go looking. Application notes describe *how to mitigate* mounting stress;
  they do not specify your assembly's number either. If someone finds an app note during
  the break, that is a gift — read the mitigation list aloud at minute 70.
- **D** — misconception M1 in its purest form: that the datasheet describes the device as
  you will use it. The conditions column already says "package level, not board level".

---

## Poll 2 · minute 22 · ConcepTest, Chunk 1

**Stem**

> Four MEMS devices. Which one does **not** contain a proof mass?

**Options**

| | |
|---|---|
| A | a 3-axis accelerometer |
| B | a vibrating-structure gyroscope |
| C | a barometric pressure sensor |
| D | a MEMS microphone |

**Correct: C** — and **D is nearly right, which is the point.** A pressure sensor and a
microphone both use a **diaphragm**, not a proof mass: they respond to a pressure
difference across a membrane, not to the inertia of a suspended block. The intended
answer is C because a barometer is unambiguously a diaphragm device; a microphone is a
diaphragm too, so a student voting D has the right *structure* concept and mis-read the
question.

**How to run it:** this poll is deliberately a little unfair, so handle it honestly.
After the vote, say: *"If you voted D, you were right about the physics and I asked a bad
question — both C and D are diaphragm devices. Anyone who voted A or B, tell me what a
proof mass is for."* That converts a flawed item into the best thirty seconds of the
chunk, and it models something worth modelling.

- **A / B** — the students who have not yet separated *structure* from *device category*.
  This is the group the chunk is for. Expect 30–45 % combined.
- **C** — intended. Expect 30–40 %.
- **D** — right physics. Expect 15–25 %.

Target 30–70 %: satisfied either way you count it.

---

## Poll 3 · minute 46 · ConcepTest, Chunk 2 — the hardest vote of the lecture

**Stem**

> A **piezoelectric** accelerometer — representative industrial vibration type — is
> mounted on the solar-tracker frame from Lecture 2 to measure its **tilt**. The frame is
> tilted to 0.5° and held there.
>
> Thirty seconds later, the reported tilt is:

**Options**

| | |
|---|---|
| A | 0.5°, correctly |
| B | **0°** |
| C | 0.5° but very noisy |
| D | it depends on the amplifier's gain |

**Correct: B — zero.** A piezoelectric element produces *charge* in response to a
*change* in strain. Held at a constant tilt there is no change, the charge leaks away
through the amplifier's input impedance, and the output decays to zero with a time
constant of seconds. A piezoelectric accelerometer has **no DC response**. It cannot
measure tilt. Not badly — *at all*.

**Why this is the right hardest question for this lecture.** It is the only place in
Module A where the *transduction principle alone* forbids an application, no matter how
good every specification is. Every other trade-off students have met has been
quantitative; this one is categorical. And it lands on Lecture 2's own requirement, so
the failure is concrete rather than abstract.

**Distractor diagnosis**

- **A** — the default assumption that an accelerometer is an accelerometer. Expect
  40–55 % on the first vote.
- **B** — correct. Target 15–30 % first vote, 55–70 % after peer discussion. If the first
  vote clears 40 %, someone has met charge amplifiers before — find them and let them
  explain it, they will do it better than the slide.
- **C** — misconception M3: piezoelectric is "self-generating so it must be strong". It
  *is* strong, for vibration; strength and DC response are unrelated.
- **D** — the student reaching for the electronics. Productive, because the answer is
  that no amplifier can fix it: a higher input impedance lengthens the decay, and the
  frame will be tilted for years.

**Peer instruction protocol.** Vote → 2 min in pairs, prompt: *"one of you argue that it
reads 0.5°, the other that it reads zero — then decide"* → revote → then the explanation.

**The follow-up that generalises it:** *"So which of the six principles could measure
this tilt?"* Answer: capacitive, piezoresistive, thermal, electromagnetic, optical — all
of them except the one that looked most impressive on the front page. Same lesson as
Lecture 2, promoted from a number to a principle.

---

## Sequencing activity · minutes 52–56 · pairs, no slides

Hand out (or project) the four steps **shuffled**, plus the four consequences shuffled
separately. Pairs, three minutes: put the steps in order and match each to its
consequence.

| Step | Consequence to match |
|---|---|
| Lithography | sets the minimum feature size, so it sets the comb gap, the capacitance and the noise floor |
| Deposition | leaves residual stress, so the structure is already curved before it is used |
| Etching | isotropic or anisotropic decides which shapes are possible at all |
| Release | frees the structure — and exposes it to stiction |

Then one question to the room: **"which of the four is the reason a MEMS accelerometer
is noisier than a bench instrument?"** Answer: lithography, via feature size → mass. It
chains back to Lecture 1's `m ∝ L³`, and a student who makes that connection unprompted
has genuinely understood Module A.

Collect nothing. Three minutes, walk the room, move on.

---

## Poll 4 · minute 64 · transfer

**Stem**

> You are specifying a pressure sensor for the capstone project. Four numbers matter.
> Which one must you **measure on your own assembly**, because no datasheet can give it
> to you?

**Options**

| | |
|---|---|
| A | the noise density at your chosen bandwidth |
| B | the sensitivity at 25 °C |
| C | the zero-offset shift caused by your enclosure clamping the sensor |
| D | the total error band over the operating temperature range |

**Correct: C.** A, B and D are all in the datasheet — indeed D is the figure Lecture 2's
Poll 4 taught them to prefer. C depends on the enclosure the team designs, the torque on
its screws and the gasket they choose, and it exists nowhere but on their bench.

**Distractor diagnosis**

- **A** — the student who has not noticed that noise density *is* published and the
  bandwidth is their own choice. A one-line correction: "you compute it, you do not
  measure it."
- **B** — the easy one, correctly rejected by nearly everyone.
- **C** — correct. Target 45–65 %; this poll is a confidence check on outcome L4.5 more
  than a discriminator, and a high score here is a good sign, not a wasted vote.
- **D** — the student over-generalising Lecture 2's lesson. Worth a sentence: preferring
  the total error band was right *then* and does not make it measurable-only *now*.

**The bridge to say immediately after:** this is project deliverable 2 and Laboratory 3.
The list of "specifications we must measure ourselves" is a required section of the
capstone's sensor-selection matrix, and it starts today.

---

## Closing synthesis · minutes 73–76 · the honest ledger

Not a poll. Build the table with the class, asking for each row before revealing it.
This deliberately mirrors Lecture 1's "honest ledger of shrinking a device" slide, so
the class recognises the form.

| Shrinking the device | buys you | costs you |
|---|---|---|
| `m ∝ L³` | — | **less mass → higher noise floor** |
| `k ∝ L` | — | — |
| `f₀ ∝ 1/L` | **higher bandwidth** | resonance moves into your signal band |
| area/volume `∝ 1/L` | fast thermal response | **surface forces dominate → stiction** |
| batch fabrication | **unit cost, integration with electronics** | tolerances you cannot control |
| packaging | protection, handling | **stress you cannot specify** |

Then the sentence the lecture exists to earn:

> Micro-scale is a trade, not an improvement. Everything you gained, you gained by
> giving something up — and the datasheet quantifies the gains, while the last two rows
> are yours to measure.

---

## Poll 5 · minute 78 · exit ticket, on paper

Two questions, ninety seconds, collected at the door. These are the input to Lecture 5's
opening slide.

1. Name one specification of the sensor in your capstone project that you will have to
   **measure yourself**, and say which stress path makes it necessary.
2. Module A is over. In one sentence: what is the pattern that Lectures 5–11 will repeat?

**Question 2 is the diagnostic.** The intended answer is *measurand → transduction →
structure → output → specifications → interface → calibration → failure modes*. Students
who can state it have the map for the next seven weeks; students who cannot will
experience Lectures 5–11 as a list of unrelated devices, which is the single largest
delivery risk in the semester plan. If fewer than half get it, spend the first three
minutes of Lecture 5 on it and do not feel behind.

---

## Backup plans

| If | Then |
|---|---|
| Running 5 min late at min 42 | cut slides 23–24 (thermal, electromagnetic, optical) to a single named list; keep Poll 3 |
| Running 10 min late | also cut the sequencing activity and set it as the reader-chapter exercise |
| Poll 3 first vote > 40 % correct | skip the charge-decay build-up, go to the comparison table, spend the time on the stress chain |
| Poll 3 first vote < 10 % correct | do the decay on the board with a real time constant, revote, and accept losing slide 19 |
| Someone asks a real fabrication question | answer it in one sentence and offer the ITMO 2020 text (books.ifmo.ru/file/pdf/2673.pdf, Russian, 75 pp), which covers device physics and fabrication properly and satisfies the accredited bibliography. Do not follow the question — it is exactly the drift this lecture is designed to resist |
| Projector fails | survivable: five structures sketched, six principles listed, four steps in order, one stress chain. All six are blackboard objects |

## Materials

- ISM330DHCX datasheet (DS13012 Rev 6) — the zero-g level rows and their conditions
  column are the whole hook; have the page number to hand
- Lecture 1's Figure 1.3 (inside a capacitive accelerometer) — reused deliberately at
  minute 14, not redrawn
- Shuffled cards for the sequencing activity: 4 steps + 4 consequences, 12 sets
- Exit-ticket slips, 24
- **No cleanroom photographs.** Lecture 1's content audit cut them for a reason and that
  reason has not changed: they make students believe this is a fabrication course
