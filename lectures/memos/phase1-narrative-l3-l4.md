# Phase 1 — Content audit and narrative design: Lectures 3 and 4
Module A completion · Status: awaiting instructor review · Prepared 2026-09-10

Companion to `phase1-narrative.md`, which covers Lectures 1 and 2. Same method: audit
the semester plan's assigned content into essential / helpful / decorative, then build an
ABT arc and a chunk map that fit 80 minutes at teaching depth.

Two constraints shaped both lectures more than anything else:

1. **Lectures 1 and 2 already exist and are taught.** L3 and L4 must not re-teach what
   they established, and must repay what they deferred. Both do: L3 turns Lecture 1's
   aliasing *discovery* into a register setting, and L4 answers the question Lecture 2
   put on screen and refused to answer.
2. **The pilot's numbers are verified and must be reused, not replaced.** The tilt
   anchor (0.5° = 8.73 mg), the noise figures (60 / 100 µg/√Hz) and the drift term
   (±0.5 mg/°C × 20 °C = 10 mg) recur in both lectures. A student who learned them in
   Week 2 should meet them again in Weeks 3 and 4 rather than a fresh set — this is
   deliberate interleaving, and it is nearly free.

---

## LECTURE 3 — From physical quantity to trustworthy samples

### 3.1 Content audit

The plan assigns eight items: analog and digital outputs; bridges and voltage/current
outputs; ADC resolution and reference; sampling and aliasing; quantisation; ODR vs
bandwidth; I²C/SPI overview; raw codes, units, timestamps and data integrity. That is
comfortably more than 80 minutes at teaching depth, and one of the eight is already
taught.

**ESSENTIAL — expert modelling required (~58 min)**

| Content | Why it survives | Time |
|---|---|---|
| ODR vs bandwidth vs anti-alias cut-off | Three numbers students conflate, one register bit decides it, and getting it wrong is irreversible. The hardest idea in the lecture and the most valuable | 16 min |
| Raw codes → SI units | The single most-failed step in real laboratory submissions: byte order, sign, auto-increment, units. Must be done live, digit by digit | 10 min |
| Effective resolution | Turns "16-bit" from a marketing claim into arithmetic; it is the lecture's anchor and it reuses L2's own numbers | 8 min |
| Timestamps and jitter | Not in any textbook at undergraduate level, and it is where a great deal of real sensor data quietly dies | 8 min |
| The reference, and ratiometric measurement | Cheap to teach, decides whether a whole class of bridge measurement works, and the failure is uncalibratable | 8 min |
| Calibratable vs irreversible | The organising idea of Lectures 12–15; L3 is where the table gets built | 5 min |
| Analog outputs: voltage, current loop, bridge | Vocabulary. 4–20 mA earns its slide because of its designed-in fault detection | 3 min |

**HELPFUL — compress hard (~8 min)**

- *Quantisation.* One slide of arithmetic and one sentence of conclusion. It is the error
  everyone wants to discuss and it is forty times smaller than the one that matters here.
  Teaching it at length would actively mislead.
- *I²C and SPI.* **One slide, and only "what can go wrong"** — bus hang, missing
  pull-ups, no recovery. The full treatment is Lecture 13. Resisting the temptation to
  teach the protocols here is the main discipline of this lecture's second half.
- *Data integrity.* `WHO_AM_I`, self-test, FIFO overrun, bus error. A checklist, not a
  topic. Designated as a cut if running late.

**DECORATIVE — eliminate**

- **ADC architectures.** SAR vs sigma-delta vs flash is genuinely interesting and
  contributes nothing to any L3 outcome. Students do not choose an ADC in this course;
  they configure a sensor that contains one. Lecture 12 may mention it in one line when
  selecting a converter is actually the task.
- **Sampling theory as mathematics.** The convolution/impulse-train derivation of
  aliasing. Lecture 1 already produced the result the students need, arithmetically, and
  they believed it. Repeating it with more mathematics buys nothing and costs 12 minutes.
- **Full I²C/SPI timing diagrams.** Lecture 13.
- **Oversampling and noise shaping.** Lecture 15, where filtering is the subject.
- **Fixed-point arithmetic.** Real, and a Lab 2 troubleshooting note rather than a slide.

### 3.2 Narrative arc (ABT)

> **AND** — You can select a sensor and defend it with an error budget. The part is on
> the bench, the register reads back a 16-bit signed integer, and the datasheet gives you
> 0.061 mg per count. The hard part looks finished.
>
> **BUT** — Between the die and the CSV file there are four conversions, and each can
> discard information silently. None announces itself, and three of the four cannot be
> undone afterwards at any price. The number in your log is not the number the sensor
> measured — and the file will look perfect either way.
>
> **THEREFORE** — A sample is trustworthy only when you can state four things about it:
> what it is in SI units, how much of it is information rather than noise, which band it
> represents, and when it happened. Each is a number you compute before writing firmware.

### 3.3 The hook

Sixty seconds, no story needed — the class already has one running. Slide 4 puts a
plausible CSV file on screen: monotonic timestamps, no gaps, no outliers, sensible
magnitudes. Then one line: **"Three of the numbers in this file are wrong, and the file
cannot tell you which."** Poll 1 follows immediately.

This is a deliberate change of register from Lectures 1 and 2, which both opened with a
narrative war story. Doing it a third time would make it a formula, and the students
would start waiting for the twist instead of thinking. The war story in L3 is held back
to minute 66 and appears in the reader as §3.11.

### 3.4 Chunk map

| Chunk | Min | Concept | Peak load |
|---|---|---|---|
| Hook + anchor | 0–14 | The log file lies; 16 bits vs 12.4 | low |
| C1 | 14–32 | Output and reference: analog forms, ratiometric, quantisation | medium |
| C2 | 32–50 | ODR is not bandwidth; the filter goes first | **highest** |
| C3 | 50–70 | Codes → values; effective bits; timestamps; integrity | medium-high |
| Synthesis | 70–80 | Calibratable vs irreversible; four claims; Lab 2 | low |

### 3.5 Instrumentation for a first offering

No prior-year data exists, so misconceptions are predicted and instrumented:

- **Poll 1's distribution is the measurement of M1.** Record the A/B/C/D split at minute 7
  and again at 66. The shift is the lecture's own effect size, and it is the only place in
  Module A where the same question is asked twice to the same room.
- **Poll 3's first-vote fraction measures how well Lecture 1's aliasing segment held**
  three weeks later. Below 15 % means L1 needs rework, not L3.
- **Exit ticket Q2** ("name one error in your Lab 1 data you now believe was
  irreversible") is a retention probe across two weeks and a live audit of L3.5.

---

## LECTURE 4 — MEMS structures, transduction, fabrication and packaging

### 4.1 Content audit

The plan assigns four groups: structures; six transduction principles; four fabrication
process families; packaging and stress. The risk here is not overload — it is **genre
drift**. Every instructor who has taught MEMS wants to teach fabrication, the material is
photogenic, and the semester plan explicitly forbids it: fabrication only "to the depth
needed to understand structures, limitations, packaging, drift and failure mechanisms",
and §12 says this is not a cleanroom fabrication course.

So the audit is unusually severe, and the governing rule is stated on the plan:
**a process step earns its slide only by explaining a specification the students have
already met.**

**ESSENTIAL (~56 min)**

| Content | Why it survives | Time |
|---|---|---|
| Five structures, one relation each | Covers every device in Lectures 5–11. Learning five structures beats learning eleven families | 14 min |
| Six transduction principles, sorted by static response | The static/dynamic discriminator is the only categorical constraint in Module A — it forbids an application outright | 16 min |
| Packaging and the stress chain | The answer to L2's unanswered question, and the reason Lab 3 exists | 12 min |
| The packaging tax: ±10 / ±65 mg against 8.73 mg | The anchor. Also the large-but-removable vs small-but-fatal asymmetry | 8 min |
| Four fabrication steps, one consequence each | The minimum that makes the above intelligible | 6 min |

**HELPFUL — compress hard (~10 min)**

- *Bulk vs surface micromachining.* One comparison slide. Its payoff is that students can
  predict the noise column themselves from Lecture 1's `m ∝ L³`, which is worth more than
  the fact itself.
- *Thermal, electromagnetic, optical transduction.* One slide each, honestly brief, each
  tied to the lecture that will need it (9, 7, 10). Designated cuts.
- *Stiction.* Two sentences, and it retrieves both Lecture 1's area/volume scaling and its
  vocabulary. Cheap and well placed.

**DECORATIVE — eliminate**

- **Cleanroom photography, equipment, process cross-sections.** Lecture 1's audit cut
  these for a specific reason — they reinforce the misconception that this is a
  fabrication course — and the reason has not changed. This is the single most important
  cut in the lecture and it should be defended even when the material is available.
- **Mask design, alignment marks, overlay, yield statistics.** No L4 outcome touches them.
- **Wafer bonding varieties, SOI, DRIE process chemistry.** Interesting; not ours.
- **Full derivations** of plate deflection or comb capacitance. The *scaling* is the
  teaching content; the constants are not.
- **A MEMS history timeline.** Cut from Lecture 1 for the same reason.
- **Materials science of silicon.** One sentence in the piezoresistive slide — the gauge
  factor is 50–200 against metal foil's 2 — carries the entire load.

### 4.2 Narrative arc (ABT)

> **AND** — You can read a datasheet, budget its errors, and acquire a sample you trust.
> Every number came from a table, and every table had a conditions column you now read
> first.
>
> **BUT** — Two weeks ago one of those conditions said *"after soldering"*, and one
> question had no answer at all. You cannot look up how your own board changes the
> device, and no manufacturer can tell you, however good the datasheet is.
>
> **THEREFORE** — Because the specification is not describing a component. It describes a
> silicon structure two micrometres thick, suspended over a sealed cavity, glued into a
> plastic box and soldered to a board that flexes when you tighten a screw. Today we open
> the box — as deep as the drift, the stress and the failure modes require and not one
> slide deeper — and the unanswerable question gets a *method* instead of an answer.

### 4.3 The hook

The strongest hook available to this lecture was written two weeks earlier and left
deliberately unpaid: Lecture 2's slide 22, the cross-axis question with no answer. Slide
4 shows that slide again, unchanged, and slide 5 says: *"Today you find out why, and what
to do instead."*

This is worth more than a new story. It demonstrates to the class that the course has an
architecture — that a question raised in Week 2 is answered in Week 4 because it was
planned that way — and that is a claim best made by doing it rather than by saying it.

### 4.4 Chunk map

| Chunk | Min | Concept | Peak load |
|---|---|---|---|
| Hook + anchor | 0–14 | L2's unpaid debt; ±65 mg against 8.73 mg | low, retrieval-heavy |
| C1 | 14–32 | Five structures | medium — new words, familiar physics |
| C2 | 32–52 | Six principles; the static/dynamic discriminator | **highest** |
| C3 | 52–70 | Fabrication in four steps; packaging; the stress chain | medium |
| Synthesis | 70–80 | L2's question answered; the honest ledger; Module A closes | low |

### 4.5 Why Poll 3 is the right hardest question

A piezoelectric accelerometer measuring tilt reads **zero**. It is the only place in
Module A where the transduction principle alone forbids an application regardless of
every specification on the front page. Every other trade-off students have met has been
quantitative — this one is categorical, and it lands on Lecture 2's own requirement, so
the failure is concrete rather than abstract.

It also inoculates against a misconception that would otherwise survive the whole course:
that "self-generating" and "high sensitivity" imply "better".

### 4.6 A known weakness, disclosed

**Poll 2 is imperfect by construction.** It asks which of four devices has no proof mass;
the intended answer is the pressure sensor, but the MEMS microphone is also a diaphragm
device and a student voting for it has the right physics. The activity set instructs the
instructor to say so out loud and convert it into the best thirty seconds of the chunk.

The alternative — a cleaner question — was drafted and rejected: every clean version was
a vocabulary test, and vocabulary tests are what the poll design guidelines exist to
prevent. A flawed question about mechanisms is worth more than a sound question about
labels, provided the flaw is handled honestly in the room.

---

## What both lectures assume, and what they leave

**Assumed from L1:** the seven-stage chain, the scaling laws, sensor/transducer/actuator,
the aliasing result.
**Assumed from L2:** the tilt anchor, error budgets, RSS combination, conditions columns,
typ vs max.

**Deferred, deliberately:** analog front-end design → L12; I²C/SPI transactions and
register maps in depth → L13; calibration method and uncertainty → L14; filtering and
fusion → L15.

**Left open for the instructor:** whether the accredited ծրագիր is formally revised or a
mapping annex produced before Lectures 5–16. L3 and L4 happen to be strongly mapped — L3
onto Themes 2.1, 2.2, 2.5, 3.3, 3.6, 3.7 and L4 onto Themes 1.2, 1.3, 1.4 — so Module A
is audit-safe end to end. That is a better position than `phase0-context.md` §2 assumed,
and it is worth recording, but it does not resolve the conflict for Lectures 5–16.
