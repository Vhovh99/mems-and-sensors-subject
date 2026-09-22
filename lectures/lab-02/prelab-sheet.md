# Laboratory 2 — PRE-LAB SHEET
**Sampling, noise and filtering** · Week 4 · Microelectromechanical Systems and Sensors

> **YOU WILL BUILD AND FLASH FIRMWARE IN THIS LABORATORY — ONCE, TOGETHER.**
> You change **one constant** in a supplied file, rebuild, and reflash. You write no
> code. Read `mcu-onramp.md` before you arrive; the first twenty minutes of the session
> assume it, and they are the only twenty minutes of the semester spent on the toolchain
> as a group.

> **THIS SHEET IS A GATE.**
> Bring it completed, on paper, in your own handwriting. The instructor signs section E
> at the bench. **No signature, no capture.** Unlike Laboratory 1 the risk here is not to
> the hardware — it is to your afternoon. Section C is twenty minutes of arithmetic at
> home that replaces an hour of confusion at the bench, and a team that arrives without
> it will not finish.

Name(s): ______________________________  Team: ______  Date: __________

---

## A · Required reading

1. **`mcu-onramp.md`** — one page. Not optional; the session opens on it.
2. **Reader Chapter 3**, *From a physical quantity to trustworthy samples* — especially
   §3.4 (quantisation), §3.5 (ODR is not bandwidth), §3.7 (the worked effective-bits
   calculation) and §3.8 (timestamps).
3. **ISM330DHCX datasheet DS13012 Rev 6** — the accelerometer noise table, `CTRL1_XL`,
   and `CTRL8_XL`. Page numbers required in section B, as in Laboratory 1.
4. Your own Laboratory 1 submission. You will compare today's numbers against it.

---

## B · Datasheet extraction  *(page number required for every row)*

| # | What to find | Value | Units | Page |
|---|---|---|---|---|
| B1 | Acceleration noise density, **typ** | | | |
| B2 | Acceleration noise density, **max** | | | |
| B3 | The operating mode B1/B2 are specified in | | — | |
| B4 | Sensitivity at ±2 g | | | |
| B5 | `CTRL1_XL` address | | — | |
| B6 | `ODR_XL` field position, and the code for 104 Hz | | — | |
| B7 | `FS_XL` field position, and the code for ±2 g | | — | |
| B8 | `LPF2_XL_EN` bit position, **and its value after reset** | | — | |
| B9 | `CTRL8_XL` address, and which field sets the LPF2 bandwidth | | — | |
| B10 | Zero-g level offset, typ and max, **and its condition line** | | | |

**B8 and B10 are the two rows that matter today.** B8 is the bit you will change; B10 is
the reason your X and Y axes will not read zero.

---

## C · Pre-lab calculations

Show your working. A number with no working scores nothing, here or in the report.

### C1 · The quantisation step and its noise

At ±2 g and 16 bits:

```
full-scale span  = ____________ mg          LSB = span / 2^16 = ____________ mg

quantisation noise  σ_q = LSB / √12 = ____________ mg
```

### C2 · The noise you should measure, at five sample rates

Bandwidth is `ODR/2`. Noise is `density × √bandwidth`. Use the **max** density from B2,
because that is the figure your part is guaranteed against.

| ODR (Hz) | `CTRL1_XL` for ±2 g, LPF2 off | BW = ODR/2 (Hz) | σ = density × √BW (mg) | σ in LSB | bits lost = log₂(σ/LSB) | effective bits |
|---|---|---|---|---|---|---|
| 26 | | | | | | |
| 52 | | | | | | |
| 104 | | | | | | |
| 208 | | | | | | |
| 416 | | | | | | |

**C2a** — By what factor does σ change each time the ODR doubles? Predict it from the
formula *before* you compute the rows, then check that your rows agree.

Answer: ______________

**C2b** — Compare σ at 26 Hz with `σ_q` from C1. Which dominates, and by what factor?

Answer: ______________

**C2c** — At which of the five rates, if any, is the quantisation noise within a factor
of ten of the sensor noise?

Answer: ______________

### C3 · The filter you will apply afterwards

An **N-sample moving average** of independent samples reduces random noise by `√N`, and
reduces the bandwidth by roughly the same factor.

**C3a** — You capture at 416 Hz and average N = 4 samples. What σ do you predict?

`σ(416 Hz) / √4` = ____________ mg

**C3b** — Now look up your own C2 row for **104 Hz**. What do you notice?

______________________________________________________________________

**C3c** — State, in one sentence, what that means about the difference between sampling
slowly and sampling fast then averaging.

______________________________________________________________________

**C3d** — What does the moving average cost you? Give both:

- bandwidth after averaging N = 4 at 416 Hz: ____________ Hz
- group delay, `(N−1)/2` samples, in ms: ____________ ms

### C4 · The rate you will actually get

A capture loop reads six bytes over I²C and then waits. From Chapter 3 §3.8, a six-byte
burst read at 400 kHz takes about **202 µs**.

**C4a** — At ODR 416 Hz the sample period is `1/416` = ____________ ms. Add the read
time. What rate does the loop actually achieve? ____________ Hz

**C4b** — Express that as a percentage error. ____________ %

**C4c** — Repeat for ODR 26 Hz. Error: ____________ %

**C4d** — Which is worse, and why? Answer in terms of the ratio of the read time to the
sample period, not in terms of the rates.

______________________________________________________________________

### C5 · One prediction to be wrong about

Before you touch a board, commit to an answer. You will check it in stage 2.

> You will capture stationary data at 104 Hz with `LPF2_XL_EN = 0`, then set it to 1 and
> capture again. **Predict the ratio σ(off) / σ(on).**

Prediction: ______________   Reasoning: ______________________________________

*You are not being graded on being right. You are being graded on having committed.*

---

## D · What you will hand in

Bring nothing to the bench but this sheet, a laptop and your datasheet. The submission is
due **48 hours** after the session and is listed in the handout; it is four plots and one
paragraph, and it is graded on whether the arithmetic in C is consistent with the data
you actually measured.

---

## E · Bench gate  *(instructor signs before you capture)*

| Check | Student initial | Instructor |
|---|---|---|
| `mcu-onramp.md` read; you can say what "flash" means | | |
| Section B complete, with page numbers | | |
| Section C1–C2 complete, arithmetic shown | | |
| Section C3–C4 complete | | |
| C5 prediction written down **before** the session | | |
| You can open a serial terminal at 115200 8N1 unaided | | |
| You know how to log terminal output to a file | | |

**Instructor signature:** ____________________  **Time:** __________

---

## F · Console reference  *(the boards arrive flashed with `0x40`)*

```
cap [n]        capture n samples as CSV (default 2000)
odr <code>     0 off · 1 12.5 · 2 26 · 3 52 · 4 104 · 5 208 · 6 416 Hz
lpf on|off     LPF2_XL_EN — the second low-pass filter
cfg            WHO_AM_I, CTRL1_XL decoded field by field, CTRL8_XL, CTRL3_C
scan           list every device answering on the bus
addr <a>       talk to 7-bit address <a>
help           this list
```

A capture opens with a comment naming the configuration and closes with the timing
summary:

```
# CTRL1_XL=0x40 n=2000
n,t_ms,raw_x,raw_y,raw_z
1,9,-5,2,16395
...
# elapsed_ms=19640 samples=2000 mean_interval_us=9824
# achieved_rate=101.791 Hz  <- compare with the ODR you set
```

**The console prints raw codes and milliseconds. It computes no mean, no standard
deviation and no filter.** Those are section C's arithmetic applied to real data, and
they are the assessed work.

---

## G · Spreadsheet reference  *(everything the analysis needs)*

You need five operations. In LibreOffice, Excel or Google Sheets they are the same. With
`raw_x` in column C from row 2 to row 2001:

| Want | Formula |
|---|---|
| mean, in codes | `=AVERAGE(C2:C2001)` |
| standard deviation, in codes | `=STDEVP(C2:C2001)` — or `STDEV.P`, they are the same |
| either one, in mg | multiply by your B4 sensitivity |
| σ expressed in LSB | `=STDEVP(C2:C2001)` — it is already in LSB, that is what a code is |
| 4-sample moving average | in `F5`: `=AVERAGE(C2:C5)`, then fill down |
| first-order low-pass, α = 0.25 | in `G2`: `=C2`; in `G3`: `=G2+0.25*(C3-G2)`, fill down |
| the actual sample interval | `=(B2001-B2)/1999` — column B is `t_ms` |

Two traps that cost teams an hour every year:

1. **Population, not sample: `STDEVP` (or `STDEV.P`), not `STDEV`.** You have the whole
   capture, not a sample of it. With 2000 points the difference is 0.03 %, so it will not
   change your conclusion — but state which you used.
2. **σ in codes is already σ in LSB.** A code *is* an LSB. Multiply by the sensitivity
   only when you want milli-*g*. Teams routinely multiply twice.
