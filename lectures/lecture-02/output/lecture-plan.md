# Lecture 2 — Lecture plan
**Sensor specifications and datasheet-based selection**
80 minutes · Module A: Foundations · 20–24 students

## Learning outcomes

| | By the end, a student can… | CLO | Assessed by |
|---|---|---|---|
| L2.1 | **Distinguish** accuracy, precision, resolution and sensitivity; sort static from dynamic characteristics | 2 | Poll 2 (min 18) · quiz Q1 |
| L2.2 | **Locate** a number in a real datasheet with its test conditions, and state one limit the datasheet cannot specify | 2 | datasheet hunt (min 33–41) · quiz Q6 |
| L2.3 | **Compute** noise-limited resolution from noise density and bandwidth, and compare it against quantisation | 2, 5 | Poll 3 (min 56) · exit ticket Q1 |
| L2.4 | **Select** among candidates against a requirement using an error budget, and defend the choice on the dominant term | 2, 8 | team decision table · Poll 4 transfer |

## The running case

One requirement carries the whole lecture: **report solar-tracker tilt to ±0.5°,
outdoors, 0–40 °C, calibrated once at 20 °C.**

`0.5° → sin(0.5°) × 1 g = 8.73 mg` — written on the board at minute 12 and never erased.

| Error term | Part A | Part B |
|---|---|---|
| Noise, 100 µg/√Hz × √50 Hz | 0.707 mg | 0.707 mg |
| Quantisation, LSB/√12 | 0.018 mg | 0.141 mg |
| Offset drift, TC × ΔT(±20 °C) | **10.000 mg** | **2.000 mg** |
| **Total (RSS)** | **10.02 mg** → **0.574°** | **2.13 mg** → **0.122°** |
| Against ±0.5° | **FAILS** | passes, 4× margin |

Part A resolves **8× finer** and fails. Part B's 0.488 mg/LSB already resolves 0.028°,
**18× finer than required** — so resolution was never the deciding variable.

All Part A / B / C figures are *representative* commercial values, chosen so the
arithmetic is exact, and are not attributed to a named product.

**Slide 24 then runs the identical budget on the real kit part, the ISM330DHCX**, using
its own published `typ` and `max` columns (DS13012 Rev 6):

| | using typ | using max |
|---|---|---|
| Noise (60 / 100 µg/√Hz × √50 Hz) | 0.424 mg | 0.707 mg |
| Quantisation | 0.018 mg | 0.018 mg |
| Drift (±0.1 / ±0.5 mg/°C × 20 °C) | 2.000 mg | 10.000 mg |
| **Total → angle** | **2.05 mg → 0.117°** | **10.02 mg → 0.574°** |
| Against ±0.5° | passes, 4× margin | **FAILS** |

One part number, one datasheet, and the requirement sits between its two columns. Part A's
figures were essentially this part's worst case and Part B's its typical case — so the
fictional comparison and the real one teach the same lesson, and the real one is harder to
dismiss.

## Authoritative timeline

| Clock | Slides | Segment | Activity |
|---|---|---|---|
| 00:00–00:02 | 1–2 | Open | Last week's muddiest points **(fill this slide in beforehand)** |
| 00:02–00:05 | 3 | Retrieval | Name the seven chain stages, unaided → today's box |
| 00:05–00:07 | 4 | **Hook** | Two front pages |
| 00:07–00:10 | 5 | Poll 1 | Baseline · **answer withheld to min 70** |
| 00:10–00:13 | 6 | Anchor | 0.5° becomes 8.73 mg |
| 00:13–00:18 | 7–8 | **C1a** | Accuracy vs precision: four targets |
| 00:18–00:22 | 9–10 | **Poll 2** | ConcepTest: the 1012.4 hPa sensor |
| 00:22–00:28 | 11–12 | C1b | The rule (systematic / random / drift) · vocabulary sorted |
| 00:28–00:33 | 13–14 | **C2a** | Read the conditions block first |
| 00:33–00:41 | 15 | **C2b** | Datasheet hunt, in pairs — six numbers, page references required |
| 00:41–00:44 | 16 | **C2c** | The question the datasheet cannot answer |
| 00:44–00:46 | 17 | **State change** | Stand · which number was hardest, and why |
| 00:46–00:52 | 18–19 | **C3a** | noise = density × √bandwidth |
| 00:52–00:57 | 20–21 | **Poll 3** | ConcepTest: the calculation · **most diagnostic item** |
| 00:57–01:06 | 22–23 | **C3b** | Quantisation, offset, drift · the full error budget |
| 01:06–01:09 | **24** | **The real part** | **ISM330DHCX: the same budget at `typ` and at `max`** |
| 01:09–01:11 | 25–26 | **Reveal** | Poll 1 answered · the verdict |
| 01:11–01:16 | 27 | C3c | Team decision table (drop Part C if running late) |
| 01:16–01:18 | 28–29 | **Poll 4** | Transfer: outdoor tank level |
| 01:18–01:19 | 30 | Rule | The course's component-selection rule |
| 01:19–01:20 | 31–33 | Close | Summary · exit ticket · Lab 1 tomorrow |

**Attention resets:** 02, 07, 18, 33, 44, 52, 66, 75 min. Longest passive stretch
**9 minutes** (00:57–01:06, the error budget) — and it is arithmetic the students have
just been equipped to follow rather than new concept load.

## Cognitive-load audit

| Segment | Intrinsic load | Managed how |
|---|---|---|
| Vocabulary (12) | **High** — 14 terms | Explicitly declared a *reference page*, not taught; only two entries expanded (ODR ≠ bandwidth, cross-sensitivity); students told it is in the handout so nobody transcribes |
| Datasheet hunt (15) | Moderate | Six *named targets* rather than open reading; pairs; page numbers force location rather than recall |
| Noise arithmetic (19) | Moderate | Units written out in full — unit cancellation, not physics, is the real blocker |
| Error budget (23) | Moderate–high | Four terms introduced one at a time on the previous slide, then assembled; the RSS insight ("largest term dominates") stated explicitly so the table is a confirmation, not a derivation |

**Extraneous load removed:** no GUM uncertainty formalism (Lecture 14 owns it), no
distribution theory behind RMS, no section-by-section reading of a full datasheet, no
multi-vendor catalogue comparison.

## Materials

- `L2-sensor-specifications-and-selection.pptx` — 33 slides, speaker notes on all
- `activities.md` — five polls with per-distractor diagnostics, hunt, decision table
- **Two real datasheets per pair** — printed extracts or laptops. Use the actual lab-kit
  parts so the skill transfers straight into Lab 1
- Handout: the vocabulary reference page · blank decision table · error-budget worksheet
- **Slide 2 must be filled in from Lecture 1's exit tickets before class**

## Reading

- **Set:** Fraden, ch. 2 (characteristics of sensors) — re-read against the datasheet
  you worked on today
- **Set:** the *conditions* pages of your assigned lab-kit datasheet
- **Optional:** a measurement-and-instrumentation text on static/dynamic
  characteristics and error propagation

## Post-lecture actions

1. Record Poll 3's **full distribution**, not just the correct percentage — each
   distractor names a specific procedural error, so the shape tells you what to
   re-teach in Lecture 3.
2. Note whether C or D still attracted votes in Poll 4. If so, the "calibration fixes
   everything" misconception survived Poll 2 and needs a direct hit in Lecture 14.
3. Mark exit-ticket Q1 (the independent noise calculation). Group work can hide an
   individual who cannot do it.
4. Collect muddiest points → opens Lecture 3.
