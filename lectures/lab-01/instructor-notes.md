# Laboratory 1 — Instructor notes

> ## THIS LAB REQUIRES NO STUDENT PROGRAMMING
> The semester plan lists *"prior microcontroller experience"* as entry background, and
> for the first offering that assumption does not hold. Lab 1 therefore runs on the
> plan's own alternative provision (§10, teaching assets): a **known-good binary**.
>
> You build `console-firmware/` **once** and flash every board before the session.
> Students drive the sensor from a serial terminal, typing register addresses and values
> they took from the datasheet, and convert every code to engineering units by hand or
> in a spreadsheet. No toolchain, no compilation, no IDE.
>
> **Every Lab 1 learning outcome is preserved** — and Lab1.4 is stronger than it was in
> the build-it-yourself version, because the students now do the two's-complement and
> sensitivity arithmetic themselves instead of reading a converted number off a screen.
>
> The register-driver firmware written for later use is parked in
> `../shared/imu-driver-for-later-labs/`. See `../instructor-guide.md` §9 for the
> proposed microcontroller on-ramp across Labs 1–8.

> ## ⚠ VERIFY BEFORE YOU TEACH
> The register values below are for the **LSM6DSO / LSM6DSOX / LSM6DSO32 family**,
> which is the class of part the semester plan's sensing kit specifies. They are
> given so you have a working answer key on the bench.
>
> **Check every one against the datasheet revision for the exact part on your
> benches before the session, and correct this file.** Register maps differ between
> families and occasionally between revisions of the same family.
>
> This is not boilerplate caution. In a course whose central lesson is *"read the
> conditions, do not trust an unsourced number"*, an unverified answer key would be
> the worst possible thing to hand a demonstrator.

---

## Answer key — LSM6DSO-family accelerometer

| Pre-lab | Quantity | Value |
|---|---|---|
| B4 | 7-bit I²C address | `0x6A` with SDO/SA0 tied low; `0x6B` tied high |
| — | HAL address (7-bit ≪ 1) | `0xD4` / `0xD6` |
| B5 | `WHO_AM_I` register | `0x0F`, returns `0x6C` |
| B6 | Accelerometer control | `CTRL1_XL` = `0x10` |
| B7 | Full-scale field | `FS_XL[1:0]`, bits 3:2 of `CTRL1_XL` |
| B8 | ODR field | `ODR_XL[3:0]`, bits 7:4 of `CTRL1_XL` |
| B10 | First output register | `OUTX_L_A` = `0x28` |
| B11 | Data format | 16-bit two's complement, **little-endian** (low byte at the lower address) |
| 2.2 | Auto-increment | `IF_INC`, bit 2 of `CTRL3_C` (`0x12`) — **set by default after reset on this family**, which is worth pointing out |

### The full-scale encoding — the deliberate trap

```
FS_XL[1:0]      range      sensitivity
   00           ±2 g       0.061 mg/LSB
   01           ±16 g      0.488 mg/LSB     <-- not in ascending order
   10           ±4 g       0.122 mg/LSB
   11           ±8 g       0.244 mg/LSB
```

A student who assumes `01` means ±4 g configures ±16 g, then applies the ±4 g
sensitivity, and reads a magnitude of about **250 mg** instead of 1000. The number is
stable, repeatable and completely wrong — which makes it a much better teaching moment
than a crash.

**Do not warn them beyond what the handout already says.** Let it happen, then ask:
"Your reading is stable to a tenth of a milli-g. Is it right?"

### Pre-lab C5 answer key  *(bytes `00 00  30 FC  00 40`, ±2 g, 0.061 mg/LSB)*

| Axis | bytes (lo, hi) | raw int16 | mg |
|---|---|---|---|
| X | `00 00` | 0 | 0.0 |
| Y | `30 FC` | **−976** | **−59.5** |
| Z | `00 40` | 16384 | 999.4 |

Magnitude = **1001.2 mg** → plausible for a stationary sensor.

Y is the whole point of the exercise: `0xFC30` = 64560, and 64560 − 65536 = −976. A
student who skips that subtraction reports +3939 mg on the Y axis and a magnitude of
about 4065 mg, which is impossible for a resting sensor — and that impossibility is
what should make them check.

### Configuration values for this lab

| Goal | `CTRL1_XL` | Meaning |
|---|---|---|
| ±2 g, 104 Hz | `0x40` | `ODR_XL = 0100` (104 Hz), `FS_XL = 00` (±2 g) |
| ±16 g, 104 Hz | `0x44` | `ODR_XL = 0100`, `FS_XL = 01` (±16 g) — for step 2.4 |

Reset default is power-down (`ODR_XL = 0000`), so a device that reads its ID correctly
but returns all-zero data has simply not been enabled. Expect this; it is on the
troubleshooting table.

### Expected values at rest, ±2 g, sensor flat with Z up

- `raw_z` ≈ **+16 300 to +16 500** (1000 mg ÷ 0.061 mg/LSB ≈ 16 393)
- `raw_x`, `raw_y` ≈ **−300 to +300** (uncalibrated offset, tens of mg — this *is* the
  zero-g offset from Lecture 2, seen for the first time on real silicon)
- magnitude **970–1030 mg** typical for an uncalibrated consumer part

If a team gets magnitude within 2 mg of 1000 on the first try, be slightly suspicious
and ask to see the raw codes.

---

## Preparation checklist

- [ ] Verify and correct the answer key above against your actual part
- [ ] **Build `console-firmware/` once and flash every board** (see below). Do this at
      least a day early, and test one board end to end with a real sensor
- [ ] Label each flashed board so a student can tell a flashed one from a spare
- [ ] Keep one board wired and working on your own bench as a known-good comparison
- [ ] Print: pre-lab sheets (one per student), handouts (one per team), datasheet
      extracts (one per team — the pin/electrical/register/sensitivity sections)
- [ ] Pre-strap all breakouts to the **same** address, or label each bench with its own
- [ ] Check which breakouts already carry pull-ups; note it on the bench card
- [ ] Have 2–3 spare sensors and one spare Nucleo. Something will die
- [ ] Confirm a **serial terminal** works on every bench PC (115200 8N1) and that
      students can find the COM/tty port. No toolchain needed on bench PCs
- [ ] Confirm a **spreadsheet** is available on every bench PC — stage 3.7 needs one
- [ ] An oscilloscope or logic analyser on the demonstration bench, for question 1.6

## Building and flashing the console (once, before the session)

1. New STM32CubeMX project for your Nucleo board.
2. Enable **I2C1** (standard mode, 100 kHz — do not start at 400 kHz) and **USART2**
   (115200 8N1). USART2 is wired to the ST-LINK virtual COM port, so the console
   arrives on the student's PC over the same USB cable that powers the board.
3. Add `sensor_console.c` and `sensor_console.h` to the project.
4. In `main.c`: `#include "sensor_console.h"`, call `console_init()` after the
   peripheral init, and call `console_poll()` in the `while (1)` loop. That is the
   whole integration — see `console-firmware/main_console.c`.
5. No `printf` retargeting is required; the console writes through
   `HAL_UART_Transmit` directly, so there is no `_write()` or `syscalls.c` to set up.
6. Build, then flash every board (drag-and-drop the `.bin` onto the ST-LINK mass-storage
   drive is fastest for a class set).

**Keep the `.bin` and the CubeMX project.** You will reflash boards during the semester,
and the same console is a useful debugging aid in every later lab.

### What the console deliberately does not do

It **never prints engineering units.** It prints hex, decimal, binary and assembled
signed integers, and stops there. Converting a code into milli-g using a sensitivity
taken from a datasheet is learning outcome Lab1.4; if the firmware did it, the lab would
teach nothing. Resist the temptation to add a convenience command.

It also **prints the register read-back** after every write, including when the value
differs from what was written. That is not a bug to hide — reserved and read-only bits
are a real datasheet lesson, and the handout asks students to explain it.

## Running the session

**0–10, the gate.** Be strict and be quick — 30 seconds per team. Sign, or send them
back with a datasheet. Announce at the start: "I am signing five things. If you cannot
say them out loud, you are not ready to put voltage on a part that costs more than
your lunch."

**10–30, Claim 1.** Circulate constantly. With the build step gone, the failures now
cluster almost entirely on **wiring and pull-ups** — which is exactly where you want a
week-2 lab to fail, because the students can see and fix the cause.

Teach `scan` as the first move, always. It splits the problem in half in one command: an
empty bus is a physical-layer fault, a populated bus with the wrong address is a
configuration fault. Resist fixing anything yourself — point at the troubleshooting
table and ask which row they are on. Redirect teams who debug by guessing; that habit
is worth more than this lab.

**30–50, configuration.** Watch for copied control-register values — a team can now type
one in three seconds, so copying is easier than before. The justification column and the
pre-lab C3 bit diagram are where you catch it. Ask: "why 104 Hz and not 1660?" and
"show me that bit pattern on your pre-lab sheet."

**50–70, Claim 2.** The 1 g test is the emotional high point of the session — the first
time the course produces a physical truth. Let teams call you over. Then immediately ask
why it is not exactly 1000, and let them discover offset on their own hardware.

Expect the two's-complement arithmetic to be the genuine sticking point now that it is
done by hand. That is a feature: the console prints the assembled signed integer, so a
team can check their own working against it and find their own error. Point them at that
rather than at the answer.

**70–80, check-off.** Question 4 (predict the axis before turning) is the discriminator.
Do not skip it when running late; skip question 3 instead.

## Frequently asked, with answers

**"Can I use the Arduino library instead?"** No — and this is the semester plan's
explicit selection rule, so say why rather than just refusing: you are being taught the
configuration and the data path, which a library exists precisely to hide. You may use
libraries freely in the project, once you can explain what they do.

**"Why 100 kHz and not 400?"** Because a marginal bus fails at 400 kHz and works at
100, and today you are debugging your wiring, not your data rate. Raise it in Lab 7.

**"My magnitude is 996 mg, is that wrong?"** No — it is your first measurement of
zero-g offset and scale-factor error, which is what Lab 3 calibrates. Write it down.

**"Can the console just print milli-g?"** No, and it never will. Turning a code into a
unit using a number whose conditions you have read is the skill this lab exists to
build. Everything downstream in the course assumes you can do it.

**"When do we write our own firmware?"** Later in the semester, once the microcontroller
sessions have run — see the on-ramp in `../instructor-guide.md` §9. The driver you will
eventually write already exists as a reference in
`../shared/imu-driver-for-later-labs/`.

## After the session — for the course review file

Record the four metrics at the foot of `rubric.md`. Also note:

- the single most common blocker, and at what minute it appeared
- whether the 80 minutes was sufficient, and for what fraction of teams
- any team that finished early, and what you gave them (candidate stretch task for
  next year)
- whether the fault exercise (1.5) fitted, or was rushed — if it was rushed twice,
  move it to Lab 2 rather than shortening it
