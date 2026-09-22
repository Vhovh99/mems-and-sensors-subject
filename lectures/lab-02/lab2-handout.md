# Laboratory 2 — Sampling, noise and filtering
**Week 4** · 80 minutes · teams of two or three · Microelectromechanical Systems and Sensors

> Bring: completed pre-lab sheet, the ISM330DHCX datasheet, a laptop with the toolchain
> and a serial terminal. The pre-lab sheet is a **gate** — section E must be signed
> before you capture.

---

## The three claims you must prove

Lecture 3 asserted three things. Today you measure whether they are true of the part on
your bench.

1. **The noise you get depends on the bandwidth you chose, not on the bits you bought.**
   σ should scale as √ODR, and the bottom bits of every sample should turn out to be
   noise.
2. **A requested sample rate is not an achieved sample rate.** The loop runs slow, always
   in the same direction, and you can say by how much.
3. **Filtering afterwards buys noise back at the price of bandwidth and delay** — and
   sampling fast then averaging lands in exactly the same place as sampling slowly.

Claim 3 is the one worth remembering. If your data supports it, you have measured the
central trade-off of the whole course.

---

## Learning outcomes

| | By the end of this session you can… |
|---|---|
| **Lab2.1** | Change a configuration constant in supplied firmware, rebuild, flash, and **prove from the device itself** that the change reached the silicon |
| **Lab2.2** | Compute mean, standard deviation and effective resolution from a raw capture, and compare them against the datasheet's prediction |
| **Lab2.3** | Demonstrate that σ scales as √bandwidth by measuring it at four or more sample rates |
| **Lab2.4** | Compare a moving average with a first-order low-pass filter on the same data, and state what each costs in bandwidth and delay |
| **Lab2.5** | Measure the achieved sample rate and the accumulated timing error of a polling loop, and justify a sampling and filtering choice for a stated measurement |

---

## Equipment

- STM32 Nucleo with the ISM330DHCX breakout, wired as in Laboratory 1 — **do not rewire**
- USB cable, laptop, toolchain, serial terminal at 115200 8N1
- A stable surface. A bench that someone leans on is a signal source, and today that
  matters
- Optional, for stage 5: anything that vibrates at a fixed rate — a phone with a tone
  generator app resting against the board is ideal

---

## Timetable

| Time | Stage | What happens |
|---|---|---|
| 00–10 | Briefing | Pre-lab check, the three claims, the gate signature |
| 10–30 | **1** | **The toolchain, together** — edit one constant, build, flash, prove it |
| 30–45 | **2** | Noise, standard deviation and effective bits at one rate |
| 45–58 | **3** | The ODR sweep — σ against √bandwidth |
| 58–68 | **4** | Timing: requested rate versus achieved rate |
| 68–76 | **5** | Filtering, and one alias |
| 76–80 | Check-off | Instructor sees your numbers; shutdown |

Stage 1 is twenty minutes and the whole room does it at once. It is the only time this
semester the toolchain gets group attention, so if you are lost, say so **during** it.

---

## Stage 1 (10–30 min) · The toolchain, together

You will do this at the same time as everyone else, step by step, with the instructor.

**1.1** Connect the board. Open the serial terminal. Press the black RESET button. You
should see the banner and `firmware built with LAB2_CTRL1_XL = 0x40`.

**1.2** Type `cfg`. Write down what it reports for `CTRL1_XL`, and confirm it decodes to
104 Hz, ±2 g, `LPF2_XL_EN 0`. **This is the configuration Lecture 3 spent twenty minutes
on** — the one with no anti-alias filter.

**1.3** Capture a baseline now, before you change anything. Put the board flat on the
bench, hands off, and:

```
cap 2000
```

Log it to a file called `baseline_0x40.csv`. Roughly 20 seconds. Do not touch the bench
while it runs.

**1.4** Now the edit. Open `Core/Inc/lab2_config.h`. Change:

```c
#define LAB2_CTRL1_XL   0x40      →      #define LAB2_CTRL1_XL   0x42
```

That single bit is `LPF2_XL_EN`. Save.

**1.5** Build. Wait for zero errors. Flash. Press RESET.

**1.6** **Prove it reached the silicon.** The banner must now say `0x42`, and `cfg` must
report `LPF2_XL_EN 1`. If either still says `0x40`, you have not completed all three of
edit-build-flash — find out which, because that is the actual lesson of stage 1.

**1.7** Capture again, board still flat, hands still off:

```
cap 2000
```

Log it as `filtered_0x42.csv`.

> **Check-off 1 — call the instructor.** Show the banner reading `0x42` and your two CSV
> files. This is the only stage with a hard gate; nothing after it works without both
> captures.

---

## Stage 2 (30–45 min) · What the noise actually is

Work in the spreadsheet. Section G of the pre-lab sheet has every formula you need.

**2.1** For `baseline_0x40.csv`, compute for **each** axis:

| | X | Y | Z |
|---|---|---|---|
| mean, codes | | | |
| mean, mg | | | |
| σ, codes (= σ in LSB) | | | |
| σ, mg | | | |

**2.2** Compare your σ against your pre-lab C2 row for 104 Hz. Agreement to within about
a factor of two is a pass — your part is somewhere between the `typ` and `max` noise
density columns, and finding out where is part of the point.

Where does your part sit, typ or max or between? ____________________

**2.3** **The effective bits.** Using your measured σ:

```
σ in LSB = ______        bits that are noise = log₂(σ in LSB) = ______

effective bits = 16 − ______ = ______
```

Write that number down and say it out loud to your partner: *"this is a 16-bit sensor and
I measured ______ bits."*

**2.4** Now the means. X and Y should read near zero and do not. That offset is the
**zero-g level** from B10 — the same quantity Lecture 4 will spend an hour on. Convert
your X and Y means to mg and check them against the datasheet's ±10 mg typ / ±65 mg max.

X offset: ______ mg   Y offset: ______ mg   Within the max limit? ______

**2.5** Z should read near +1000 mg. What is the magnitude `√(x²+y²+z²)` of your mean
vector? ______ mg. It should be within a few mg of 1000; if it is not, say so at
check-off rather than adjusting anything.

**2.6** Repeat 2.1 and 2.3 for `filtered_0x42.csv`, and compare with your **C5
prediction**.

| | σ (mg) | effective bits |
|---|---|---|
| `0x40`, LPF2 off | | |
| `0x42`, LPF2 on | | |
| ratio | | |

Was your prediction right? ______ Does the ODR differ between the two captures? ______

**That last question is the one to get right.** The sample rate did not change. Only the
bandwidth did. If σ fell, you have measured Lecture 3's central claim with your own
hands, and you caused it by editing one character.

---

## Stage 3 (45–58 min) · σ against √bandwidth

No rebuilding. ODR is settable at runtime — that is why the console has the command.

**3.1** For each rate, set it, capture, and record σ for one axis. Keep the board flat and
still throughout; you are measuring the sensor, not the room.

```
odr 2      (26 Hz)      cap 1500
odr 3      (52 Hz)      cap 1500
odr 4      (104 Hz)     cap 2000
odr 5      (208 Hz)     cap 2000
odr 6      (416 Hz)     cap 3000
```

Set `lpf off` first so all five rows are comparable, and say so in your report.

| ODR (Hz) | BW = ODR/2 | σ measured (mg) | σ predicted from C2 | ratio to previous row |
|---|---|---|---|---|
| 26 | 13 | | | — |
| 52 | 26 | | | |
| 104 | 52 | | | |
| 208 | 104 | | | |
| 416 | 208 | | | |

**3.2** **The law.** Your "ratio to previous row" column should sit near a single number
for every doubling. What is it, and what number did you predict in C2a?

Measured: ______  Predicted: ______

**3.3** **Plot 1 — σ against √BW.** Put √BW on the x-axis and measured σ on the y-axis.
Five points. Add a straight line through the origin. If the points fall on it, noise
density is exactly what the datasheet says it is: a constant, with the bandwidth supplied
by you.

**3.4** From the slope of that line, extract your part's actual noise density in µg/√Hz.

Slope = ______ mg/√Hz = ______ µg/√Hz. Datasheet typ ______ max ______.

---

## Stage 4 (58–68 min) · The rate you asked for, and the rate you got

Every capture already printed the answer. You just have to look at it.

**4.1** Go back to the closing lines of each capture from stage 3 and tabulate:

| ODR set (Hz) | `achieved_rate` reported (Hz) | error (%) | your C4 prediction (%) |
|---|---|---|---|
| 26 | | | |
| 104 | | | |
| 416 | | | |

**4.2** The error is not the same at every rate. Explain why in one sentence, in terms of
the ratio of the I²C read time to the sample period.

______________________________________________________________________

**4.3** **The accumulated error.** Take your 416 Hz capture. If you had assumed the
samples were exactly `1/416` s apart, how far out would the last sample's timestamp be?

```
n samples = ______    assumed duration = n / 416 = ______ s
elapsed_ms reported   = ______ s
error at the end      = ______ s
```

**4.4** In one sentence: is that error calibratable after the fact, or not? Justify from
Chapter 3 §3.12.

______________________________________________________________________

**4.5** **Plot 2 — the interval, sample by sample.** Add a column `t_ms(n) − t_ms(n−1)`
and plot it against `n` for your 416 Hz capture. You will see a staircase, because the
timestamp resolution is 1 ms and the true period is 2.4 ms. **That staircase is the
resolution of the clock, not jitter in the sensor** — say so in your caption. The mean
interval, which the firmware reports in microseconds, is the trustworthy figure.

---

## Stage 5 (68–76 min) · Filtering, and one alias

Use your **416 Hz** capture for all of this. It is the one with the most bandwidth to
give away.

**5.1** In the spreadsheet, add three columns from `raw_x`:

- a **4-sample moving average**
- a **16-sample moving average**
- a **first-order low-pass**, `y ← y + α(x − y)`, with α = 0.25

**5.2** Compute σ for each, and compare against the unfiltered figure:

| | σ (mg) | reduction factor | predicted factor |
|---|---|---|---|
| raw, 416 Hz | | — | — |
| moving average N = 4 | | | √4 = 2 |
| moving average N = 16 | | | √16 = 4 |
| low-pass α = 0.25 | | | ≈ 2.6 |

**5.3** **The comparison that matters.** Put your N = 4 result beside your **native
104 Hz** σ from stage 3:

σ (416 Hz averaged by 4) = ______ mg   σ (native 104 Hz) = ______ mg

Are they the same? ______ Should they be, and why?

______________________________________________________________________

**5.4** **Plot 3 — raw against filtered.** One axis, about 200 samples, three traces:
raw, moving average N = 16, low-pass α = 0.25. Then answer: which of the two filters
responds faster to a change, and which is smoother? You cannot have both.

______________________________________________________________________

**5.5** **The alias, without any extra hardware.** Take the same 416 Hz capture and keep
**every 8th row** — in a spare column, `=INDEX(C:C, (ROW()-1)*8+2)`. You now have the
same physical event sampled at 52 Hz.

Tap the bench rhythmically, or rest a phone playing a steady tone against the board, and
repeat the capture so there is something above 26 Hz to fold. Then:

**Plot 4 — the same event at two sample rates.** Plot the full 416 Hz series and the
decimated 52 Hz series over the same time span. A component that sits above 26 Hz in the
first will appear at a *different, lower* frequency in the second.

A 50 Hz component — and there is often one, from the mains — decimated to 52 Hz appears
at `|50 − 52|` = **2 Hz**. Slow, convincing, and entirely fictitious.

**5.6** In one sentence: could a filter applied to the 52 Hz series remove it?

______________________________________________________________________

---

## Check-off and submission (76–80 min)

> **Bench check-off — the instructor sees these five things and asks one question.**
>
> | | Shown |
> |---|---|
> | 1 | Banner reading `0x42`, and `cfg` reporting `LPF2_XL_EN 1` |
> | 2 | Your stage 2 table: σ and effective bits for `0x40` and `0x42` |
> | 3 | Your stage 3 table with the ratio column filled in |
> | 4 | The `achieved_rate` lines from three captures |
> | 5 | Your stage 5.3 comparison — averaged 416 Hz against native 104 Hz |
>
> The question will be one of: *how many bits did you actually measure?* · *what did
> changing that one bit change, and what did it not change?* · *why are 5.3's two numbers
> the same?*

**Submission, 48 hours, one PDF per team:**

1. **The four plots**, captioned. A caption states what is plotted, at what
   configuration, and what it shows. An uncaptioned plot scores nothing.
2. **The three tables** from stages 2, 3 and 5.
3. **One paragraph, no more than 150 words**, answering this:

   > A colleague must log the tilt of a slow-moving structure to ±0.5°, and asks you what
   > ODR and what filter to use. Give both, with the σ you expect, and say what your
   > choice costs.

   Use your own measured noise density, not the datasheet's. Chapter 2's tilt anchor —
   0.5° is 8.73 mg — is the number to compare against.

4. **One sentence** naming something in today's data that could **not** be fixed
   afterwards.

Item 3 is what the laboratory is for. Items 1 and 2 are evidence that you may answer it.

---

## Troubleshooting — work down the list, in order

| Symptom | Do this |
|---|---|
| Banner still says `0x40` after rebuilding | You edited, built, or flashed — but not all three. Rebuild from scratch, watch for `0 errors`, reflash, press RESET |
| Build fails | Read the **first** error and its line number. If it is in `Drivers/`, you have edited something you should not have — restore it |
| Build stays broken more than 5 minutes | **Take the known-good `0x42` binary and keep measuring.** Note it in your report; it costs you nothing |
| `cap` prints nothing | Wrong port or wrong baud. 115200 8N1 |
| All samples read 0 | The accelerometer is powered down. `odr 4` |
| `ERROR: no reply from 0x6A` | `scan`, then `addr <what it found>`. Wiring, not firmware |
| σ is ten times too large | Someone is touching the bench. Hands off, recapture |
| σ is suspiciously small and identical across rates | You are looking at the same file twice. Check the `# CTRL1_XL=` line at the top of each capture |
| Z reads ≈ 16 400, not ≈ 1000 | Those are codes. Multiply by the sensitivity — that is Lab 1's outcome, retested |
| Magnitude is 970 or 1030, not 1000 | Correct and expected. That is the zero-g offset, and Lecture 4 is about where it comes from |

---

## A note on what you are allowed to conclude

You measured one part, on one bench, on one afternoon. That is enough to establish that
σ scales as √bandwidth, because you saw it do so over a factor of sixteen. It is **not**
enough to establish your part's noise density to three figures, and it says nothing at
all about the next part out of the same reel.

Distinguishing "I have demonstrated a relationship" from "I have measured a value" is a
large part of what separates a laboratory report from a set of numbers. Say which one
each of your conclusions is.
