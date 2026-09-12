# 3 · From a physical quantity to trustworthy samples

## What you should be able to do after this chapter

1. **Convert** a raw two's-complement register pair into a value in SI units, stating the sensitivity, the sign convention and the byte order you assumed.
2. **Distinguish** output data rate, measurement bandwidth and anti-alias cut-off frequency, and say which of the three, if set wrongly, produces an error that cannot be undone.
3. **Compute** the noise-limited effective resolution of an acquisition chain, and state how many of the bits your datasheet advertises actually carry information.
4. **Choose** between polling and a data-ready interrupt for a stated measurement, and justify the choice in terms of timestamp error rather than convenience.
5. **Classify** the errors in an acquisition chain as calibratable or irreversible.

---

## 3.1 One log file, and three numbers

Chapter 2 ended with a part chosen and defended. This chapter begins with that part on the bench.

You have configured it. The register map is open, the sensitivity is written on a sticky note, and a `while()` loop is filling a CSV file with numbers. The measurement looks finished — the difficult judgement was the selection, and that is behind you.

Here is the configuration, and it is the one Laboratory 2 will use:

> An **ISM330DHCX** accelerometer, configured for **±2 g full scale, 16-bit output, ODR = 104 Hz**. Its datasheet gives the sensitivity as **0.061 mg/LSB**. You log for ten minutes by calling `HAL_Delay(10)` in a loop and reading six bytes over I²C each time.

Now the question this chapter exists to answer:

> **How much of what you logged is true?**

Not "is the sensor good" — Chapter 2 settled that. The sensor is fine. The question is what survived the journey from the silicon to the file, and the answer is three numbers:

| | |
|---|---|
| **12.4** | the number of bits, out of sixteen, that carry information |
| **12 Hz** | the frequency of a signal in your data that does not exist in the world |
| **12.1 s** | how wrong your timestamps are by the end of the log |

Every one of those three was computable before a line of firmware was written, from the same datasheet you already had open. None of the three announces itself in the data. And two of the three cannot be repaired afterwards at any price.

That is the shape of this chapter: acquisition does not fail loudly. It fails by handing you a file full of plausible numbers.

---

## 3.2 What comes out of a sensor

Two kinds of thing, and the boundary between them is where this chapter lives.

**An analog output** is a continuous electrical quantity proportional to the measurand. It comes in three common forms:

- **Voltage.** The simplest and the most fragile. A thermocouple gives tens of microvolts per degree; a bridge gives a few millivolts. Both are small enough that the wire between the sensor and the amplifier is part of the measurement.
- **Current, usually 4–20 mA.** An industrial convention worth understanding, because it solves two problems at once. Current is unchanged by the resistance of a long cable, so the reading does not depend on how far away the sensor is; and because the *zero* of the scale is 4 mA rather than 0 mA, a broken wire reads 0 mA and is therefore distinguishable from a genuine zero. That is a designed-in fault detection, and it is the reason the convention has outlived the technology that prompted it.
- **A bridge.** Four resistive elements in a diamond, excited by a voltage, producing a difference voltage proportional to the imbalance. Strain gauges, piezoresistive pressure sensors and many load cells are bridges. Section 3.3 is about a property of bridges that most people discover by accident.

**A digital output** means the analog-to-digital conversion has already happened, inside the sensor's own package, and what you receive is a number over I²C or SPI. Almost every MEMS sensor you will meet in this course is of this kind.

It is tempting to conclude that a digital output removes the problems of an analog one. It does not. It **moves them inside the package, where you cannot see them and cannot change them** — and it adds two new ones of its own, which are the byte order of the result and the question of *when* the conversion happened. The rest of this chapter is largely about those two.

---

## 3.3 The reference you forgot

Every analog-to-digital converter answers one question: *what fraction of my reference voltage is this input?* The count it returns is

$$ \text{count} = \frac{V_{in}}{V_{ref}} \times 2^{N} $$

Read that formula for what it says. The count does not depend on the input. It depends on the **ratio** of the input to the reference. An ADC has no idea what a volt is.

This has a consequence that decides whether an entire class of measurement works.

Consider a strain-gauge bridge excited from the microcontroller's 3.3 V rail, read by an ADC that uses **the same rail** as its reference. Under load the rail sags to 3.2 V — a 3 % drop. What happens to the reported strain?

Nothing. The bridge output is proportional to its excitation, so it falls by 3 %. The ADC's counts are proportional to $1/V_{ref}$, so they rise by 3 %. The two cancel exactly, because the quantity the code computes was a ratio all along. This is a **ratiometric measurement**, and it is free.

Now change one wire. Give the ADC a precision 2.500 V reference and leave the bridge on the rail. The sag no longer cancels: it becomes a 3 % error in the reported strain, it varies with the load on the rail, and **no calibration can remove it**, because it is not a constant — it is a function of whatever else the board is doing.

Same components. Same cost. One wire's difference between a measurement that is immune to supply variation and one that is at its mercy.

The rule is short enough to remember: **excite the sensor and reference the converter from the same thing, or from two things that are both stable.** Mixing one stable and one unstable is the only combination that fails, and it is the one that looks most sophisticated on a schematic.

---

## 3.4 Quantisation: the error that does not matter here

The converter has a finite number of codes, so it must round. For our accelerometer:

$$ \text{LSB} = \frac{\text{full scale}}{2^{N}} = \frac{4000\ \text{mg}}{65\,536} = 0.061\ \text{mg} $$

which is exactly what the datasheet prints. Rounding to the nearest code introduces an error uniformly distributed over one LSB, whose RMS value is

$$ \sigma_{q} = \frac{\text{LSB}}{\sqrt{12}} = \frac{0.061}{3.464} = 0.018\ \text{mg} $$

The $\sqrt{12}$ is the standard deviation of a uniform distribution of unit width; it is worth knowing where it comes from, and it is not worth deriving twice.

Hold on to 0.018 mg. In Section 3.7 we will compare it with the sensor's own noise and find it smaller by a factor of forty. **Almost every argument you will hear about the last bit of an ADC is, in a real sensor system, an argument about nothing.** Quantisation is the error engineers discuss because it is easy to calculate, and it is very rarely the error that decides anything.

---

## 3.5 Output data rate is not bandwidth

Here are three numbers that students, datasheets and marketing material routinely conflate. They have three different jobs.

| | What it is | Who sets it |
|---|---|---|
| **ODR** — output data rate | how often a new number appears at the output | you, by register |
| **Measurement bandwidth** | the highest signal frequency the device reports faithfully | you, by register — but often a *different* register |
| **Anti-alias cut-off** | the frequency above which the filter *before the sampler* attenuates | the designer of the analog path — sometimes you, sometimes nobody |

The Nyquist–Shannon sampling theorem says a signal is recoverable only if it is sampled at more than twice its highest frequency component. Chapter 1 showed what happens when it is violated: a 1520 Hz bearing tone, sampled at 100 Hz, appeared as a perfectly convincing 20 Hz oscillation.

Chapter 1 presented that as a discovery. This chapter presents it as a **design rule with a register bit attached**, which is a different thing entirely.

### The ordering that cannot be repaired

The anti-alias filter must sit **before** the sampler. Not after. There is no software equivalent.

The reason is arithmetic rather than engineering. Once a 300 Hz component has been sampled at 104 Hz, it is represented in the data by exactly the same sequence of numbers as a genuine 12 Hz component. They are not similar; they are *identical*. No filter, no transform, no amount of computation can separate two things that are the same. The information was destroyed at the instant of sampling, and it was destroyed by the *absence* of a component costing a few cents.

This is the only ordering constraint in the whole measurement chain with that property. Everything else — a wrong gain, a missing offset correction, a sign error, a unit muddle — can be fixed on a laptop a week later, by someone who was not there. This one cannot.

![Aliasing](figures/fig1-4-aliasing.png)

**Figure 3.1** — The mechanism, from Chapter 1. The samples are entirely correct; their *interpretation* is not. Reproduced here because this chapter is where it becomes a register setting rather than a cautionary tale.

### The register bit that catches everybody

The ISM330DHCX's `CTRL1_XL` register holds the ODR selection in bits 7:4, the full-scale selection in bits 3:2, and in bit 1 a flag named `LPF2_XL_EN`.

**After reset, that bit is 0.** The second low-pass filter is disabled.

So the natural sequence of events is this. A student sets ODR = 104 Hz, reasons correctly that the Nyquist limit is 52 Hz, concludes that the measurement bandwidth is 52 Hz, and writes it in the report. The device, meanwhile, is sampling a much wider analog band with no anti-alias filtering, and everything above 52 Hz is folding back into the data.

Suppose a pump on the same frame runs at 300 Hz:

$$ f_{alias} = |300 - 3 \times 104| = |300 - 312| = 12\ \text{Hz} $$

Twelve hertz. Squarely inside the band that a tilt or vibration measurement cares about, comfortably slow enough to look like real mechanical behaviour, and permanent.

It gets worse if the numbers are rounder. At an ODR of 100 Hz:

$$ f_{alias} = |300 - 3 \times 100| = 0\ \text{Hz} $$

The pump becomes a **DC offset**. Somebody will now spend a productive week calibrating it out, and will succeed — at that one pump speed. The calibration will be wrong at every other speed, and the failure will be blamed on the sensor.

And Chapter 1's bearing, at this ODR:

$$ f_{alias} = |1520 - 15 \times 104| = 40\ \text{Hz} $$

Same story, different number. The lesson is not that 104 Hz is a bad choice. It is that **the sample rate alone tells you nothing about what is in your data.**

---

## 3.6 From raw codes to a physical quantity

Four steps, each with a way to get it wrong that produces a plausible answer.

Suppose a burst read of the X-axis returns two bytes:

```
OUTX_L_A (0x28) = 0x2C
OUTX_H_A (0x29) = 0xFF
```

**Step 1 — assemble the word, in the right order.** The device is little-endian: the low byte comes from the lower address. So the 16-bit word is `0xFF2C`, not `0x2CFF`.

**Step 2 — interpret the sign.** The value is 16-bit two's complement. Bit 15 is set, so the number is negative:

$$ 0\text{xFF2C} = 65\,324 \quad \rightarrow \quad 65\,324 - 65\,536 = -212\ \text{counts} $$

**Step 3 — apply the sensitivity.**

$$ a = -212 \times 0.061\ \text{mg} = -12.9\ \text{mg} $$

**Step 4 — convert to SI.**

$$ a = -0.0129\ g \times 9.80665 = -0.127\ \text{m/s}^2 $$

Now the four failures, all of which appear in real laboratory submissions:

- **Wrong byte order.** Reading high-then-low gives `0x2CFF` = 11 519 counts = **+703 mg**. Not obviously absurd. A wrong answer of a believable magnitude is far more dangerous than one that is obviously broken.
- **Sign ignored.** Treating the word as unsigned gives 65 324 counts = **+3985 mg**: a stationary device reporting nearly 4 g. This one at least announces itself, provided somebody looks.
- **Auto-increment misunderstood.** A burst read of six consecutive registers requires the address pointer to advance, controlled by `IF_INC` in `CTRL3_C`. That register resets to `0x04`, so **auto-increment is already enabled** and a burst read works out of the box. The failure mode is the diligent student who writes `0x00` to `CTRL3_C` to "start from a clean state", and then reads the same byte six times.
- **Units left implicit.** mg, g and m/s² all appear in the same laboratory. Put the unit in the column header, once, and check plausibility against the one reference every student has: at rest, one axis should read about 9.81 m/s², and the vector sum of all three should be 1 g whatever the orientation.

That last check is worth more than it looks. It is the only step in this whole chain that tests the *entire* chain at once, against a physical constant you cannot misconfigure.

---

## 3.7 Worked calculation: the bits you own

We can now answer the first of the chapter's three numbers, and we do it entirely from figures already in hand.

**Given.** ±2 g full scale, 16-bit output, ODR = 104 Hz with `LPF2_XL_EN` set so that the measurement bandwidth is ODR/2. Noise density 100 µg/√Hz — the datasheet's *max* column.

**Step 1 — the quantisation step.**

$$ \text{LSB} = \frac{4000\ \text{mg}}{65\,536} = 0.061\ \text{mg} $$

**Step 2 — the quantisation noise.**

$$ \sigma_{q} = \frac{0.061}{\sqrt{12}} = 0.018\ \text{mg} $$

**Step 3 — the bandwidth.**

$$ BW = \frac{ODR}{2} = \frac{104}{2} = 52\ \text{Hz} $$

**Step 4 — the sensor noise in that bandwidth.**

$$ \sigma_{n} = 100\ \mu g/\sqrt{\text{Hz}} \times \sqrt{52\ \text{Hz}} = 100 \times 7.211 = 721\ \mu g = 0.721\ \text{mg} $$

**Step 5 — combine them.** They are independent, so root-sum-square:

$$ \sigma_{total} = \sqrt{0.721^2 + 0.018^2} = 0.721\ \text{mg} $$

The quantisation term has changed the answer in the fourth decimal place. This is the promised comparison from Section 3.4: **the sensor noise is forty times the quantisation noise.** The converter is not the limitation and never was.

**Step 6 — express the noise in codes.**

$$ \frac{0.721\ \text{mg}}{0.061\ \text{mg/LSB}} = 11.8\ \text{LSB} $$

**Step 7 — count the bits.** A noise floor of 11.8 codes means the bottom

$$ \log_{2}(11.8) = 3.6\ \text{bits} $$

of every sample are noise. Therefore

$$ \text{effective bits} = 16 - 3.6 = \mathbf{12.4} $$

**The verdict.** You bought a 16-bit number wrapped around a 12.4-bit measurement. The smallest acceleration change you can actually distinguish in a single sample is not 0.061 mg but **0.72 mg**, twelve times larger.

And the datasheet did not lie to you. It printed the noise density on the same page as the resolution. It simply did not do the multiplication, because the bandwidth was your choice, not theirs.

**Now run it again with the other column.** With the `typ` noise density of 60 µg/√Hz:

$$ \sigma_{n} = 60 \times \sqrt{52} = 433\ \mu g = 0.433\ \text{mg} = 7.1\ \text{LSB} \quad \rightarrow \quad 2.8\ \text{bits} \quad \rightarrow \quad \mathbf{13.2\ bits} $$

The datasheet's own two columns move the answer by 0.8 bits. That is Chapter 2's lesson — *a number without its conditions is not a number* — restated in a different quantity, and it will recur in every remaining chapter.

### A note on names

Three quantities in this area have similar names and different definitions, and a reader who meets them elsewhere should not be confused:

- **Effective resolution**, computed above, compares the total noise with the LSB. It answers "how many bits mean anything?"
- **ENOB** (effective number of bits), as datasheets for standalone ADCs use it, compares the total noise with the *ideal quantisation* noise: $16 - \log_2(0.721/0.018) = 10.7$ bits here. It answers "how much worse than a perfect converter of this width is this one?"
- **Noise-free resolution** uses a peak-to-peak noise figure, conventionally 6.6σ, and comes out lower again.

All three are defensible; none is interchangeable. Whenever you quote one, name it. This chapter uses effective resolution throughout because it is the one that answers a design question.

---

## 3.8 When did it happen?

The third of the chapter's numbers, and the one most often discovered too late.

You called `HAL_Delay(10)`, so the samples are 10 ms apart and the rate is 100 Hz. Except that the loop also has to read the sensor. A six-byte burst read over I²C at 400 kHz is about 81 bit-times of protocol:

$$ t_{I^{2}C} = \frac{81}{400\,000} = 202\ \mu s $$

So the loop period is not 10.000 ms. It is

$$ T = 10.000 + 0.202 = 10.203\ \text{ms} \quad \rightarrow \quad f = 98.0\ \text{Hz} $$

Two consequences, both quantitative.

**Frequencies come out wrong.** A genuine 20 Hz vibration advances $20 \times 10.203\ \text{ms} = 0.2041$ of a cycle per sample. Analysed on the assumption of 10.000 ms spacing, that reads as

$$ \frac{0.2041\ \text{cycles}}{0.010\ \text{s}} = 20.41\ \text{Hz} $$

a 2 % error, which is enough to misidentify a machine order or a resonance.

**Time itself comes out wrong, and cumulatively.** After 60 000 samples your timestamps, generated as $n \times 10$ ms, say that 600.0 s have elapsed. In reality

$$ 60\,000 \times 10.203\ \text{ms} = 612.1\ \text{s} $$

have passed. **Every event in the last part of that log is stamped 12.1 seconds earlier than it happened.** Correlate that log against anything else — a second sensor, an operator's note, a video, another team's data — and the correlation is meaningless.

It is worse than a constant scaling error, because the loop period is not actually constant: it depends on which branches ran, whether an interrupt arrived, and what the bus was doing. You can *bound* the error. You cannot invert it.

### The fix, which is free

Configure the sensor's **data-ready interrupt**. Read the sample in response to it, and timestamp it from a hardware timer rather than from a loop counter. The sample interval is then set by the sensor's own internal timebase, and your timestamp error becomes that timebase's tolerance — a specified quantity, in the datasheet, typically a fraction of a percent — instead of a property of your software's mood.

Many devices, the ISM330DHCX among them, go further and offer a timestamp register and a FIFO, so that samples are stamped at the source and read in batches. If you take one habit from this chapter into the laboratory, take this one: **the sensor knows when it sampled; ask it, rather than guessing.**

| | Polling with a delay | Data-ready interrupt |
|---|---|---|
| Sets the interval | your software | the sensor's timebase |
| Interval error | loop-dependent, unbounded | datasheet-specified |
| Cumulative time error | grows without limit | bounded by the timebase tolerance |
| CPU cost | high — busy waiting | low |
| Effort to implement | slightly less | slightly more |

---

## 3.9 Knowing that the data is real

Four cheap checks, each of which catches a failure that otherwise presents as bad data rather than as an error.

- **Device identity.** Read the `WHO_AM_I` register and compare it against the expected constant — `0x6B` for the ISM330DHCX. This confirms the address, the bus, the pull-ups and the power supply in one transaction. Note in passing that the expected value `0x6B` is also one of the part's two I²C addresses, which has confused a great many people; they are unrelated coincidences of numbering.
- **Self-test.** Most MEMS sensors can electrostatically deflect their own proof mass by a known amount. The output should change by a specified range. This tests the mechanical structure, not just the electronics — the only check in this list that does.
- **FIFO overrun.** If the buffer overflowed, samples were lost, and the ones you have are not evenly spaced. A silently dropped sample is a timing error disguised as data. Read the status flag; do not assume.
- **Bus error and recovery.** I²C can hang with a slave holding the data line low. A design that cannot recover — by clocking the bus until it releases, or by cycling power — will one day stop logging and give no reason.

None of these is difficult. All four are omitted from most first attempts, and all four turn "the data looks strange" into "the sensor was never responding".

---

## 3.10 A datasheet case: two registers decide the chapter

Everything in Sections 3.5 to 3.8 comes down to bits in two registers of the part on your bench.

**`CTRL1_XL` (0x10)**

| Bits | Field | What it decides |
|---|---|---|
| 7:4 | `ODR_XL` | the output data rate — `0100` is 104 Hz |
| 3:2 | `FS_XL` | full scale, and therefore the LSB and the noise in mg |
| 1 | `LPF2_XL_EN` | **whether there is an anti-alias filter at all** — 0 after reset |
| 0 | — | must be written 0 |

Two things are worth noticing. First, the full-scale encoding is **not in ascending order**: `00` = ±2 g, `01` = ±16 g, `10` = ±4 g, `11` = ±8 g. A student who assumes the obvious mapping selects ±16 g while believing they selected ±16 g's neighbour, and every subsequent number is wrong by a factor of two or four. Read the table; do not infer it.

Second, `0x40` gives ±2 g at 104 Hz — and leaves bit 1 clear, which is the configuration discussed at length in Section 3.5.

**`CTRL3_C` (0x12)** resets to `0x04`, which means `IF_INC` is already set. Burst reads work by default. This is the register the diligent student breaks.

The whole of this chapter, then, is contained in about twelve bits. That is characteristic of embedded sensing, and it is why the course insists on register-level configuration rather than a library call: the library sets those bits too, but it does not tell you which ones it chose.

---

## 3.11 An integration failure: the log that was thrown away

A team instrumented a test rig with two sensors: an accelerometer on the frame at 104 Hz, and a pressure transducer on the hydraulic line read by the microcontroller's own ADC at "the same rate". Both logged to the same file, one row per loop iteration, with a single timestamp column generated from a loop counter.

The purpose was to find out whether a pressure spike preceded or followed a mechanical shock. That is a question about ordering, at millisecond resolution.

Three problems, none of which produced an error message:

1. The accelerometer was read over I²C and the pressure transducer through the internal ADC, so the two readings in each row were taken about 200 µs apart. Nothing in the file recorded that.
2. The loop period was 10.2 ms, not 10.0 ms, so the timestamps drifted — by twelve seconds over a ten-minute run.
3. The pressure transducer's analog path had no anti-alias filter, and the pump ran at 300 Hz.

The team's conclusion — that pressure spikes followed the shocks by about 15 ms — was arithmetic on all three errors at once. The 15 ms was neither measured nor measurable with that setup. The rig was rebuilt, and the second attempt used the accelerometer's data-ready interrupt to trigger both readings, timestamped from a hardware timer, with an RC filter on the pressure input. The answer changed sign.

The lesson is not that they were careless. Every individual decision was reasonable, and the file looked perfect: no gaps, no outliers, plausible magnitudes, a monotonic timestamp column. **A log file cannot tell you that it is wrong.** The only defence is to compute what the acquisition chain can and cannot resolve *before* trusting what comes out of it, which is the entire content of this chapter.

---

## 3.12 Calibratable, or gone

The table to keep. Everything in the acquisition chain belongs in one of these two columns, and knowing which is the difference between a problem and a disaster.

| Error | Removable afterwards? | How, or why not |
|---|---|---|
| Offset | **yes** | one-point calibration against a known reference |
| Scale factor | **yes** | two-point calibration |
| Non-linearity | **yes**, with effort | a fitted correction, if you characterise it |
| Wrong byte order | **yes** | reinterpret the file; the bits are all there |
| Sign error | **yes** | reinterpret the file |
| Unit muddle | **yes** | a multiplication |
| Quantisation | **no** — but negligible here | 0.018 mg against 0.72 mg of noise |
| Random noise | **partly** | averaging reduces it by √N, and costs bandwidth |
| Temperature drift | **partly** | only if temperature was logged too — so log it |
| **Aliasing** | **NO** | the alias and the signal are the same numbers |
| **A lost or wrong timestamp** | **NO** | the timing information was never recorded |
| **Saturation / clipping** | **NO** | the value was outside the range; nothing was stored |

Notice the pattern. Everything in the top group is a *transformation* of data that is still present. Everything in the bottom group is *missing information*. No amount of processing creates information, and this is the one law of the subject with no exceptions and no workarounds.

Notice also the third row from the bottom: temperature drift is recoverable *if and only if* you logged the temperature. Almost every sensor in this course has a temperature output, most people ignore it, and it costs one extra column in the file. Log it.

---

## 3.13 The four claims a trustworthy sample makes

A sample you can defend answers four questions, and you should be able to answer all four before writing firmware:

1. **What is it?** A value in SI units, with the sensitivity, sign convention and byte order you assumed stated explicitly.
2. **How much of it is information?** The effective resolution, computed from the noise density and *your* bandwidth — 12.4 bits, not 16.
3. **What band does it represent?** The measurement bandwidth, and evidence that an anti-alias filter was present below it. Not the ODR.
4. **When did it happen?** A timestamp whose error you can state, from a source you can name.

A log file that cannot answer these four is not data. It is a plausible file.

---

## 3.14 Reading

This chapter is the one place in Module A where the adopted textbook covers the ground more thoroughly than we can in eighty minutes, and you should read it.

- **Morris & Langari, *Measurement and Instrumentation*, 3rd ed., Chapter 6 — "Data Acquisition and Signal Processing".** Sampling, aliasing, ADC architectures and quantisation, at more depth and with more mathematics than we have used. Read it after this chapter, not before: it is a better second pass than first.
- **Morris & Langari, Chapter 3 — "Measurement Uncertainty".** Where the root-sum-square combination of Section 3.7 comes from, properly justified.
- **Kuphaldt, *Lessons in Industrial Instrumentation*** (freely licensed, CC-BY) has the best practical treatment of 4–20 mA current loops in print, including why the convention exists and how it fails. Recommended if Section 3.2 interested you.
- **ISM330DHCX datasheet DS13012 Rev 6**, the `CTRL1_XL`, `CTRL3_C` and `WHO_AM_I` register descriptions, and the accelerometer noise table. This is not background reading; it is the working document for Laboratory 2.

What the textbooks will *not* give you is Section 3.8. The relationship between a polling loop and a timestamp is embedded-systems practice rather than instrumentation theory, it is where a great deal of real sensor data goes wrong, and as far as we can find it is not treated at undergraduate level anywhere. That gap is the reason this reader exists.

---

## 3.15 Exercises

**3.1** An ADC has a 12-bit output and a 3.300 V reference. What is its LSB in millivolts, and what is its quantisation noise in millivolts RMS?

**3.2** The same ADC reads a sensor whose output noise is 4 mV RMS. How many of the twelve bits carry information?

**3.3** A sensor is sampled at 200 Hz. An interfering tone exists at 750 Hz. At what frequency does it appear in the data? At what frequency would it appear if the sample rate were changed to 250 Hz?

**3.4** A bridge is excited from a 5.000 V precision reference. The ADC reading it uses the 3.3 V rail as its reference, and the rail sags by 2 %. By how much, and in which direction, does the reported value change? Is the error calibratable?

**3.5** A 16-bit accelerometer at ±4 g has a noise density of 90 µg/√Hz. You need a measurement bandwidth of 10 Hz. Compute the LSB, the noise in mg, the effective resolution in bits, and state which of quantisation or noise dominates.

**3.6** A logger polls a sensor every 20 ms using a delay call. Each read takes 350 µs. Over an eight-hour run, how far out is the final timestamp? Express it in seconds and as a percentage.

**3.7** For each of the following, say whether it can be corrected after the data has been logged, and in one sentence why: (a) a 3 % scale-factor error; (b) a 40 Hz component that was really at 360 Hz sampled at 100 Hz; (c) readings that saturated at full scale for 200 ms; (d) an axis whose sign was inverted; (e) 0.5 mg of random noise.

**3.8** You must measure a vibration whose highest component of interest is 40 Hz, using a sensor with a selectable ODR of 26, 52, 104, 208 or 416 Hz and a selectable low-pass filter. Choose the ODR and the filter cut-off, and justify both. State what you would do if the filter could not be enabled.

---

## Answers

**3.1** $\text{LSB} = 3.300/4096 = 0.806$ mV. $\sigma_q = 0.806/\sqrt{12} = 0.233$ mV RMS.

**3.2** The noise is $4/0.806 = 4.96$ LSB, so $\log_2 4.96 = 2.3$ bits are noise and $12 - 2.3 = 9.7$ bits carry information. Note that the sensor noise is seventeen times the quantisation noise: a 10-bit converter would have measured this sensor essentially as well.

**3.3** At 200 Hz: the nearest multiple is $4 \times 200 = 800$, so $|750 - 800| = 50$ Hz. At 250 Hz: $3 \times 250 = 750$, so $|750 - 750| = 0$ Hz — the tone becomes a DC offset, which is the more dangerous of the two outcomes because it is easy to "calibrate away" and thereby make permanent.

**3.4** The bridge output is unchanged, since its excitation is stable. The ADC's reference falls by 2 %, so the counts rise by 2 % and the reported value reads **2 % high**. It is not calibratable, because the sag depends on the load on the rail and therefore varies during operation. The fix is to reference the ADC from the same 5.000 V source, or to make the rail stable.

**3.5** $\text{LSB} = 8000/65\,536 = 0.122$ mg; $\sigma_q = 0.122/\sqrt{12} = 0.035$ mg; $\sigma_n = 90 \times \sqrt{10} = 285\ \mu g = 0.285$ mg. Noise is $0.285/0.122 = 2.3$ LSB $\rightarrow 1.2$ bits, so **14.8 effective bits**. Noise still dominates, but only by a factor of eight rather than forty — at 10 Hz of bandwidth the converter is beginning to be relevant, which is exactly the regime where a narrow bandwidth is worth buying.

**3.6** Loop period $= 20.350$ ms against an assumed 20.000 ms. Eight hours is 28 800 s of intended time, i.e. $28\,800/0.020 = 1\,440\,000$ samples, whose real duration is $1\,440\,000 \times 0.020350 = 29\,304$ s. The final timestamp is **504 s — over eight minutes — early**, an error of **1.75 %**.

**3.7** (a) Yes: a multiplication, once you have a two-point calibration. (b) No: the alias is arithmetically identical to a genuine 40 Hz signal. (c) No: the values were never stored, so the information does not exist. (d) Yes: reinterpret the file, the magnitudes are correct. (e) Partly: averaging N samples reduces it by √N, at the cost of bandwidth — so it is removable only to the extent that you did not need the bandwidth.

**3.8** Choose **ODR = 104 Hz** with the low-pass cut-off at or just above 40 Hz. Justification: 104 Hz gives a Nyquist limit of 52 Hz, comfortably above the 40 Hz of interest with margin for the filter's finite roll-off; 52 Hz would put Nyquist at 26 Hz, below the signal, and 208 Hz doubles the noise-bandwidth product for nothing (noise rises as √BW). If the filter cannot be enabled, an external RC filter must be fitted **before** the sensor's own sampling — which for a digital sensor is impossible, so the correct answer is to raise the ODR to 416 Hz so that the un-filtered analog bandwidth is a smaller multiple of Nyquist, digitally low-pass filter, and decimate to 104 Hz in software. Note carefully that this reduces the problem and does not solve it: anything above 208 Hz still folds. Choosing a sensor whose anti-alias filter you can enable is the real answer, and it is a selection criterion, which puts it back in Chapter 2.
