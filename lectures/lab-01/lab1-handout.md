# Laboratory 1 — Datasheet to data
**Week 2 · 80 minutes · teams of 2–3 · Microelectromechanical Systems and Sensors**

> **No programming this week.** The boards are pre-flashed with a register console.
> You supply every address, every register value and every conversion — from the
> datasheet, by hand. Firmware authoring starts later in the semester.

## The two claims you must prove

Everything here exists to establish two statements. Nothing else counts until both hold.

> **Claim 1 — "The device is alive, and it is the device I think it is."**
> Proven by reading the device-ID register and getting the value the datasheet promises.
>
> **Claim 2 — "The number on my screen is true."**
> Proven against gravity: one axis reads ≈ 9.81 m/s² at rest, and ≈ 0 when turned
> horizontal.

An engineer who cannot prove these two things has not made a measurement. They have
made a number.

## Learning outcomes

| | |
|---|---|
| **Lab1.1** | Verify supply and logic-level compatibility from the datasheet **before** applying power, and state the consequence of getting it wrong |
| **Lab1.2** | Wire an I²C sensor to an STM32 Nucleo with correct pull-ups and grounding, and confirm device identity |
| **Lab1.3** | Configure one operating mode (full-scale range + ODR) by register write, and justify both choices |
| **Lab1.4** | Convert raw two's-complement codes to SI units using datasheet sensitivity, and verify plausibility against a known physical reference |
| **Lab1.5** | Produce an annotated connection diagram, a documented register sequence, and a labelled data log |

## Equipment

- STM32 Nucleo board (**pre-flashed**), USB cable
- **ST ISM330DHCX** 6-axis IMU breakout, assigned per bench
- Breadboard, jumper wires, pull-up resistors if your breakout lacks them
- Multimeter
- Serial terminal at **115200 8N1**, and a spreadsheet
- **Your signed pre-lab sheet**

---

## Timetable

| Time | Stage | What happens |
|---|---|---|
| 0–10 | **GATE** | Pre-lab check-off. Instructor signs section D. No signature → no power. |
| 10–30 | **Claim 1** | Wire the bus. `scan`. Read the device ID. Diagnose three injected faults. |
| 30–50 | **Configure** | Set range and ODR with `w`. Justify both. Compare two ranges. |
| 50–70 | **Claim 2** | `dump`, convert by hand, run the 1 g test, `log` to a spreadsheet. |
| 70–80 | **Check-off** | Instructor sign-off, submission, closing question. |

---

## Stage 1 (10–30 min) · Prove the device is there

**1.1** Power off. Wire V_DD, GND, SDA, SCL per your section E diagram. Confirm pull-ups
are present exactly once — on the breakout or added by you, never both.

**1.2** With the sensor **disconnected** from 3V3, measure the board's 3V3 rail:
__________ V. Within a few percent of 3.3 V, or stop and ask.

**1.3** Connect and power on. Open the serial terminal at 115200 8N1. You should see the
console banner. Press Enter to get a `>` prompt, then type `help`.

**1.4** Type `scan`. Record every address that answers: ______________________

Compare with your pre-lab B4. If the address that answers is not the one you predicted,
find out why **before** going further — the answer is usually a strap pin.

> **A warning that saves an hour.** On this part the device-ID *value* happens to be
> the same number as one of its possible I²C *addresses*. They are unrelated: one is
> the contents of a register, the other is who you are talking to. If you find yourself
> reasoning "the address is right because the ID is right", stop and separate the two.

**1.5** Read the device-ID register (pre-lab B5):

```
> r 0F                     ← use YOUR register address
  0x0F = 0x6C   (108)   01101100
```

Record: register __________  value read __________  expected __________

**Do not continue until these match.** If they do not, work down the troubleshooting
table at the end of this handout — **in order**, not at random.

### 1.6 · Three faults, on purpose

Once the ID reads correctly, break it deliberately. These are the three failures that
would otherwise cost you a day later in the semester, and here there is someone to ask.

For each fault: run `scan` **and** the ID read, record what each one shows, then restore
and confirm the ID reads again.

| | Fault | `scan` shows | `r <id>` shows |
|---|---|---|---|
| **A** | Swap SDA and SCL | | |
| **B** | Point the console at the wrong address (`addr` +1) | | |
| **C** | Remove one pull-up resistor | | |

**Then answer in writing:** faults A and C both produce an empty `scan`. **What single
instrument would tell them apart immediately, and what would you look for on it?**

*(Keep your answer. You will use the instrument itself later in the semester.)*

---

## Stage 2 (30–50 min) · Configure, and justify

**2.1** Write the control byte you built in pre-lab C3 — ±2 g at about 100 Hz:

```
> w 10 40                  ← use YOUR register and YOUR value
  wrote 0x40 to 0x10, reads back 0x40
```

If the read-back differs from what you wrote, that is information, not a failure. Some
bits are read-only or reserved. Record it and say why you think it happened.

**2.2** Read the register back with `r` and confirm the bit pattern matches your C3
diagram, bit for bit.

**2.3** Complete the register table. Every row needs a reason — "the example used it" is
not a reason.

| Register | Address | Value written | What it sets | Why this value |
|---|---|---|---|---|
| | | | | |
| | | | | |

**2.4** `dump` the output registers and record the raw Z code. Now switch to the **±16 g**
range and `dump` again, with the board in the *same physical position*.

- Raw Z at ±2 g: __________   Raw Z at ±16 g: __________
- Converted (your arithmetic, mg): __________   __________

**2.5** The two raw codes differ by roughly a factor of eight. The two converted values
should agree to within a few mg. Explain, in one sentence, why both facts are correct at
the same time.

<br>

**2.6** Return to ±2 g for the rest of the lab, and say in one line why ±2 g is the right
choice for measuring a static orientation.

---

## Stage 3 (50–70 min) · Prove the number is true

**3.1** With the sensor flat, Z up, at rest, run `dump`. Record the bytes and the three
signed integers the console prints.

**3.2** Convert all three to mg **yourself**, using the sensitivity for the range you
configured. Show the arithmetic for one axis in full.

<br>

**3.3 · The 1 g test.** Ten `dump` readings, sensor undisturbed:

| # | raw X | raw Y | raw Z | X (mg) | Y (mg) | Z (mg) | magnitude (mg) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| … | | | | | | | |
| 10 | | | | | | | |

Mean magnitude: __________ mg. It should be close to 1000 mg.

> If your magnitude is near 4000, 2000, 250 or 125 mg, do not adjust anything.
> Go back to pre-lab B7 and read the range encoding table again.

**3.4 · The rotation test.** Turn the board so Z is horizontal. **Before you turn it,
write down which axis you expect to change and in which direction.**

  Predicted: ______________________  Observed: ______________________

**3.5 · Convert to SI.** Express your resting Z axis in m/s² and compare with 9.81.

  Measured: __________ m/s²   Difference: __________ %

**3.6** Your mean magnitude is not exactly 1000 mg. Name **two** distinct reasons from
Lectures 1 and 2, and say which of the two a calibration could remove.

<br>

**3.7** Run `log 28 200 50` — 200 samples, 50 ms apart. Copy the CSV into a spreadsheet,
add columns converting each axis to mg, and compute the mean and standard deviation of
the magnitude.

  mean __________ mg    std dev __________ mg

That standard deviation is the noise you calculated in Lecture 2, measured for the first
time on your own hardware. Compare the two — order of magnitude is enough.

---

## Check-off and submission (70–80 min)

At the bench, the instructor will ask:

1. Show me the device ID reading.
2. Show me the 1 g test.
3. Which register sets the range, and what happens to the sensitivity if I change it?
4. Turn the board — show me the axis you expect to change, **before** you turn it.
5. **Which stage of Lecture 1's measurement chain did you just build?**

**Hand in:** annotated connection diagram · register table with justifications · the
ten-sample table with your conversions · fault-exercise answers including the instrument
question · the 200-sample log with converted columns, mean and standard deviation · one
sentence answering question 5.

Length limit: **two pages plus the log.** You are assessed on evidence, not narrative.

---

## Troubleshooting — work down the list, in order

| Symptom | Most likely cause | Check |
|---|---|---|
| `scan` finds nothing | Missing pull-up, or SDA/SCL swapped, or no power at the sensor | Measure SDA and SCL with the bus idle: both should sit at ≈ 3.3 V. If they are at 0 V, you have no pull-up |
| `scan` finds a device at an address you did not expect | Strap pin state | Check the address-select pin against pre-lab B4 |
| `ERROR: bus busy` | Nearly always a missing pull-up | As above |
| ID reads `0x00` or `0xFF` | Nothing responding at that address | Confirm 3.3 V **at the sensor's own V_DD pin**, not at the board header |
| ID reads a plausible but wrong value | Right bus, wrong register or wrong part | Re-check B5 against the datasheet |
| `dump` returns all zeros, ID is fine | Accelerometer not enabled — ODR field still `0000` | Power-down is the reset default on most parts |
| Downward tilt gives ≈ +64000 | Two's complement not applied in **your** arithmetic | Subtract 65536 when the value is ≥ 32768 |
| Magnitude off by 2, 4 or 8 | Sensitivity does not match the configured range | The range encoding is **not** in ascending order — re-read the table |
| Values wander when you touch the breadboard | Loose jumper or poor common ground | Reseat; confirm one solid ground |
| Console prints nothing at all | Wrong baud, or wrong COM port | 115200 8N1; check which port appeared when you plugged in |

## A note on the range encoding

Several sensor families encode full-scale range in an order that is deliberately not
what you would guess — the pattern for ±16 g may sit numerically between ±2 g and ±4 g.
There is a historical reason and it does not matter. The habit does:

> **Read the table. Do not extrapolate a register encoding.**

If your magnitude is a factor of 2, 4 or 8 away from 1000 mg, this is almost always why.
