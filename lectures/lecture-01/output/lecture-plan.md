# Lecture 1 — Lecture plan
**MEMS, sensors, and the measurement-system architecture**
80 minutes · Module A: Foundations · 20–24 students · first offering

## Learning outcomes

| | By the end, a student can… | CLO | Assessed by |
|---|---|---|---|
| L1.1 | **Draw** the path from physical measurand to logged SI value, labelling every stage where information is lost | 1, 5 | pair sketch (min 45) · exit ticket |
| L1.2 | **Classify** a device as sensor / transducer / actuator and name its measurand | 1 | 30-second activity (min 12) · Poll 2 |
| L1.3 | **Predict** from scaling laws (m ∝ L³, k ∝ L, f₀ ∝ 1/L, A/V ∝ 1/L) why MEMS are fast — and name one property that worsens | 1, 3 | Poll 3 (min 40) · quiz Q3, Q4 |
| L1.4 | **Convert** a vague request into a measurement specification: quantity, range, resolution, accuracy, bandwidth, environment, output | 2, 8 | worked exercise (min 58) · exit ticket · project deliverable 1 |

Not an outcome: any numerical datasheet work. That is Lecture 2.

## Authoritative timeline

Poll labels on the slides are *nominal* minute markers. This table is the clock.

| Clock | Slides | Segment | Activity |
|---|---|---|---|
| 00:00–00:03 | 1–4 | **Hook** | The motor that died under observation |
| 00:03–00:05 | 5 | Poll 1 | Baseline commitment · **answer withheld** |
| 00:05–00:08 | 6–7 | Frame | What this course is / is not · outcomes |
| 00:08–00:14 | 8–10 | **C1a** | Sensor / transducer / actuator · 30-second classify |
| 00:14–00:22 | 11–14 | **C1b** | The measurement chain, built one box at a time |
| 00:22–00:24 | 15–16 | C1c | Chain with real numbers · where the truth dies |
| 00:24–00:28 | 17–18 | **Poll 2** | ConcepTest: the rubber pad · peer instruction |
| 00:28–00:29 | 19–20 | Pivot | "The chain begins before the sensor" |
| 00:29–00:40 | 21–23 | **C2** | What is inside · scaling exponents · f₀ ∝ 1/L |
| 00:40–00:44 | 24–25 | **Poll 3** | ConcepTest: scaling · **hardest item** |
| 00:44–00:45 | 26 | C2 close | The honest ledger: better / worse |
| 00:45–00:48 | 27–28 | **State change** | Stand · slides off · pair sketch from memory |
| 00:48–00:58 | 29–32 | **C3a** | The wish · seven questions · worked specification |
| 00:58–01:02 | 33 | C3b | Pairs: specify the drone altitude problem |
| 01:02–01:05 | 34–35 | **Poll 4** | Transfer: which spec line decides feasibility |
| 01:05–01:07 | 36 | Admin | Semester project brief |
| 01:07–01:15 | 37–41 | **Synthesis** | Finger on the box · the three numbers · aliasing · the verdict |
| 01:15–01:16 | 42 | Summary | Four things to keep |
| 01:16–01:18 | 43 | Poll 5 | Exit ticket, collected |
| 01:18–01:20 | 44–45 | Bridge | Lab 1 preview · reading · next lecture |

**Attention resets:** 03, 12, 24, 40, 45, 58, 62, 74 min. Longest passive stretch
**11 minutes** (00:29–00:40, the scaling chunk) — the densest material in the lecture,
and deliberately the one immediately followed by the hardest poll.

## Cognitive-load audit

| Segment | Intrinsic load | Managed how |
|---|---|---|
| Chain build (11–14) | Moderate — 7 new labels | Progressive reveal, one box per slide; no box introduced without a "what dies here?" question |
| Scaling (21–23) | **High** — two exponents, one derivation, one counter-intuitive consequence | Only three symbols carried (m, k, d); the algebra is done once on the board and left visible; the counter-intuitive part is isolated into its own poll |
| Seven questions (31) | Moderate — 7 items | Only two expanded verbally; the rest are a reference handout, stated as such |
| Aliasing (39) | **High** — the hardest idea in the lecture | Deferred to minute 70, after three separate plants; drawn at a 19:20 ratio so the mechanism is visible rather than asserted |

**Extraneous load removed:** no cleanroom photography (it would install the very
misconception the course design rejects), no MEMS history timeline, no market-size
charts, no device taxonomy, no spring-mass transfer function.

## Materials

- `L1-MEMS-measurement-system-architecture.pptx` — 45 slides, speaker notes on all
- `activities.md` — five polls with distractor diagnostics, protocols, contingencies
- Handouts: seven-question specification template · project brief · pre-lab sheet
- Paper for the sketch activity (one sheet per pair) · index cards for exit tickets
- Physical whiteboard for `k ∝ L¹` / `m ∝ L³` — leave them up all lecture

## Reading

- **Set:** Fraden, *Handbook of Modern Sensors*, ch. 1–2 (sensor classification,
  characteristics)
- **Optional:** Senturia, *Microsystem Design*, ch. 1 and the scaling sections
- **Do not set** fabrication chapters. Lecture 4 owns that, and setting them now
  reinforces misconception M2.

## Post-lecture actions

1. Transcribe exit-ticket muddiest points into one list → fills slide 2 of Lecture 2.
2. Record Poll 2, 3, 4 first-vote and post-discussion percentages.
3. Log actual clock time at: end of hook, end of C1, end of C2, end of break, end of
   C3, start of synthesis. Compare against the table above.
4. Release the formative quiz (6 questions, in `activities.md`).
