# Lecture 3 — Lecture plan
**From physical quantity to trustworthy samples**
80 minutes · Module A: Foundations · 20–24 students

Semester-plan coverage: analog and digital outputs; bridges and voltage/current outputs;
ADC resolution and reference; sampling and aliasing; quantisation; ODR vs bandwidth;
I²C/SPI overview; raw codes, units, timestamps and data integrity.

**Accredited-programme mapping.** This is the most audit-safe lecture of the four. It
covers ծրագիր Theme 2.1 (անալոգային/թվային ազդանշաններ), 2.2 (զտիչներ), 2.5
(անալոգաթվային կերպափոխիչներ), and Theme 3.3 (ընդհատումներ), 3.6 (SPI), 3.7 (I²C) — six
official subtopics in one 80-minute lecture. Worth recording in the mapping annex
discussed in `memos/phase0-context.md` §2.

## Learning outcomes

| | By the end, a student can… | CLO | Assessed by |
|---|---|---|---|
| L3.1 | **Convert** a raw two's-complement register pair into SI units, stating sensitivity, sign convention and byte order | 4, 5 | worked conversion (min 50) · Lab 2 pre-lab |
| L3.2 | **Distinguish** ODR, measurement bandwidth and anti-alias cut-off, and say which one, set wrongly, causes an *irreversible* error | 3, 5 | Poll 3 (min 40) · exit ticket Q1 |
| L3.3 | **Compute** the noise-limited effective resolution of an acquisition chain and state how many of the datasheet's bits carry information | 2, 5 | Poll 1 answered at min 66 · quiz |
| L3.4 | **Choose** between polling and a data-ready interrupt for a stated measurement, and justify it in terms of timestamp error | 4 | Poll 4 (min 64) · Lab 2 deliverable |
| L3.5 | **Classify** the errors in an acquisition chain as calibratable or irreversible | 5, 8 | synthesis table (min 70) · exit ticket Q2 |

**Not an outcome of L3:** designing an analog front end. Instrumentation amplifiers,
common-mode range and grounding get one slide each here as *vocabulary*, and their full
treatment is Lecture 12. L3 owns the boundary from conditioned analog signal to logged
number.

## The running case

Lecture 2 ended with a part chosen. Lecture 3 starts with that part on the bench, and
the question Lab 2 will ask in Week 4:

> The ISM330DHCX is configured for **±2 g, 16-bit, ODR = 104 Hz**. Its datasheet says
> **0.061 mg/LSB**. You log for ten minutes with a `HAL_Delay(10)` polling loop.
> **How much of what you logged is true?**

Three numbers answer it, and each one is a chunk of the lecture.

### 1. The bits you own

| | | |
|---|---|---|
| Full scale, ±2 g | 4000 mg over 65 536 codes | **0.061 mg/LSB** |
| Quantisation noise | LSB/√12 | 0.018 mg |
| Bandwidth at ODR 104 Hz | ODR/2, *with LPF2 enabled* | 52 Hz |
| Sensor noise (100 µg/√Hz max) | 100 µg/√Hz × √52 Hz | **0.721 mg** |
| Noise, in LSB | 0.721 / 0.061 | 11.8 LSB |
| **Bits that are noise** | log₂(11.8) | **3.6** |
| **Effective bits** | 16 − 3.6 | **12.4** |

**The anchor of the lecture: you bought 16 bits and you own 12.4.** The bottom 3.6 bits
of every sample are noise, and no amount of averaging in post changes what the log
contains. It goes on the board in two stages — see "Board work" below — because 0.72 mg
is Poll 1's withheld answer and must not appear before minute 56.

With the `typ` noise density (60 µg/√Hz) it is 0.433 mg and 13.2 effective bits — so the
datasheet's own two columns move the answer by nearly a bit. Same lesson as Lecture 2,
different quantity.

### 2. The band you actually sampled

`CTRL1_XL` bit 1 is `LPF2_XL_EN`, and **it is 0 after reset**. Students will therefore
set ODR = 104 Hz, believe they have a 52 Hz measurement, and have no anti-alias filter
at all.

| Interfering tone | Sampled at | Appears at |
|---|---|---|
| 300 Hz (a nearby pump) | 104 Hz | **12 Hz** |
| 1520 Hz (Lecture 1's bearing) | 104 Hz | 40 Hz |
| 300 Hz | 100 Hz | **0 Hz — it looks like an offset** |

`|300 − 3 × 104| = 12 Hz`. Twelve hertz is inside the band a tilt or vibration
measurement cares about, it is indistinguishable from real signal, and it is
**irreversible**. This is Lecture 1's aliasing result again, but now a *register bit* is
responsible for it, which is the difference between a lecture and a laboratory.

### 3. The clock you did not have

A six-byte I²C burst read at 400 kHz is 81 bit-times ≈ 202 µs. So `HAL_Delay(10)` plus
one read is a **10.203 ms** loop:

| | |
|---|---|
| Intended rate | 100 Hz |
| Actual rate | **98.0 Hz** |
| A real 20 Hz tone is reported at | 20 × (10.203/10.000) = **20.41 Hz** |
| After 60 000 samples, the log says | 600.0 s |
| Real elapsed time | **612.1 s** |
| Every event is stamped | **12.1 s too early** |

The fix costs nothing: take the sample on the **data-ready interrupt** and timestamp it
from a hardware timer, and the error becomes the sensor's own timebase tolerance instead
of the software's mood. This is the single most transferable thing in the lecture, and it
is the reason Lab 2 asks for a timing plot.

All three numbers come from the same datasheet the class already has open, and from the
ISM330DHCX facts verified for the pilot (DS13012 Rev 6).

## Narrative arc

> **AND** — You can select a sensor and defend it with an error budget. The part is on
> the bench; the register reads back a 16-bit signed integer; the datasheet gives you
> 0.061 mg per count. The hard part looks finished.
>
> **BUT** — Between the die and the CSV file there are four conversions, and each one can
> discard information silently. Unlike an offset, none of them announces itself, and
> three of the four cannot be undone afterwards at any price. The number in your log is
> not the number the sensor measured.
>
> **THEREFORE** — A sample is trustworthy only when you can state four things about it:
> what it is in SI units, how much of it is information rather than noise, which
> frequency band it represents, and *when* it happened. Each of those four is a number you
> compute before you write a line of firmware — which is what this lecture, and Lab 2,
> are for.

## Chunk map

| Chunk | Minutes | Core concept | Cognitive load |
|---|---|---|---|
| Hook + frame | 0–14 | The number in the log is not the measurement; the 16→12.4 anchor | low, mostly retrieval |
| **C1** | 14–32 | The output and the reference: analog vs digital, bridges, ratiometric measurement, quantisation | medium |
| **C2** | 32–50 | ODR is not bandwidth: sampling, the anti-alias filter's position, decimation | **highest — the lecture's hardest idea** |
| **C3** | 50–70 | Codes to trustworthy values: two's complement, byte order, effective bits, timestamps, interrupts, integrity | medium-high, but arithmetic-led |
| Synthesis | 70–80 | Calibratable vs irreversible; the four claims; Lab 2 bridge; exit ticket | low |

## Authoritative timeline

| Clock | Slides | Segment | Activity |
|---|---|---|---|
| 00:00–00:02 | 1–2 | Open | Last week's muddiest points **(fill in beforehand)** |
| 00:02–00:05 | 3 | Retrieval | Chain stages 5–7, unaided → today's territory |
| 00:05–00:07 | 4 | **Hook** | One log file, three lies |
| 00:07–00:11 | 5 | Poll 1 | Baseline · **answer withheld to min 66** |
| 00:11–00:14 | 6–7 | Anchor | 0.061 mg/LSB, and what it is not |
| 00:14–00:18 | 8–9 | **C1a** | Analog output: voltage, current loop, bridge |
| 00:18–00:23 | 10–11 | **C1b** | The reference: ratiometric vs absolute |
| 00:23–00:26 | 12–13 | Poll 2 | ConcepTest · the sagging rail |
| 00:26–00:32 | 14–16 | **C1c** | Quantisation: LSB, LSB/√12, and why more bits is not more truth |
| 00:32–00:34 | 17 | State change | Stand and sketch the chain from memory (60 s) |
| 00:34–00:40 | 18–20 | **C2a** | Sampling: Nyquist as a design rule, not a discovery |
| 00:40–00:44 | 21–22 | **C2b** | The filter goes **before** the sampler — the one irreversible ordering |
| 00:44–00:48 | 23–24 | Poll 3 | ConcepTest · **hardest** · 300 Hz and `LPF2_XL_EN = 0` |
| 00:48–00:50 | 25–26 | **C2c** | ODR, bandwidth, cut-off: three numbers, three jobs |
| 00:50–00:56 | 27–29 | **C3a** | Raw codes: two's complement, little-endian, `IF_INC`, × sensitivity |
| 00:56–00:60 | 30–31 | **C3b** | The 16 → 12.4 arithmetic, in full |
| 00:60–00:64 | 32–34 | **C3c** | Timestamps: the 12.1 s error, and the interrupt that fixes it |
| 00:64–00:66 | 35 | **C3d** | Data integrity: `WHO_AM_I`, self-test, FIFO overrun, bus error |
| 00:66–00:68 | 36 | Poll 1 answer | The withheld answer lands: 0.72 mg, not 0.061 mg |
| 00:68–00:71 | 37 | Poll 4 | Transfer · a 4–20 mA loop, a different measurand |
| 00:71–00:75 | 38–39 | Synthesis | Calibratable vs irreversible — the table students keep |
| 00:75–00:78 | 40–41 | Close | The four claims a trustworthy sample makes · Lab 2 bridge |
| 00:78–00:80 | 42 | Exit ticket | Two questions, on paper |

Slack: the state change at 00:32 and slide 35 (data integrity) are the designated cuts if
running late. Never cut Poll 3 or the timestamp segment — they are the two things Lab 2
depends on.

## Board work

Three things go on the board and stay there. **Note the split in the first one:** the
full line contains 0.72 mg, which is Poll 1's withheld answer, so it must not appear
before minute 56.

1. At minute 14, write only `0.061 mg/LSB` and, beside it, *"16 bits bought — how many
   owned?"*. Complete the line term by term during the arithmetic at minutes 56–60, so
   it ends as `0.061 mg/LSB · noise 0.72 mg · 11.8 LSB · 3.6 bits · 12.4 effective`.
2. `|300 − 3×104| = 12 Hz` — from minute 44.
3. `ODR ≠ BW ≠ f_cut` — from minute 48, in the instructor's own handwriting, because it
   is the sentence most students will get wrong on the midterm.

## Misconceptions this lecture is built to catch

| # | Predicted misconception | Where it is caught |
|---|---|---|
| M1 | More bits means a better measurement | Poll 1, resolved min 66 |
| M2 | Sampling faster fixes aliasing | Poll 3 — raising ODR moves the alias, it does not remove it |
| M3 | The anti-alias filter can be applied in software afterwards | slides 21–22, explicitly |
| M4 | ODR is the bandwidth | slides 25–26; the `LPF2_XL_EN` default is the evidence |
| M5 | A timestamp is whatever the loop counter says | slides 32–34, the 12.1 s number |
| M6 | A ratiometric error can be calibrated out | Poll 2 — it cancels by construction, or it does not cancel at all |
| M7 | Signed data is a formatting detail | slides 28–29: a missed sign bit reads −1 g as **+2998 mg**, and a swapped byte order reads −12.9 mg as +703 mg |

## Reader chapter

`reader/ch03-trustworthy-samples.md`, same seven-part shape as Chapters 1 and 2. It is
the chapter Lab 2's pre-lab reading points at.

## What the students take away

- The **calibratable-vs-irreversible table** from slide 38. It is the one artefact of this
  lecture they will use in every remaining laboratory.
- The Lab 2 pre-lab calculation: compute effective bits for two ODR settings *before*
  arriving, so the bench time is spent measuring, not deriving.
