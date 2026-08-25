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

> ## ✅ VERIFIED AGAINST THE DATASHEET
> The part is the **ST ISM330DHCXTR** — iNEMO 6-axis IMU, industrial grade, LGA-14L.
> Every register value and electrical figure below was read from
> **datasheet DS13012 Rev 6** on 2026-08-25 and the arithmetic was checked by
> computation.
>
> Two things still want your own eyes before the session:
> 1. **Confirm the datasheet revision** you hand to students matches DS13012 Rev 6
>    (ST revises; the register map is stable but check).
> 2. **Confirm the I²C address on your specific breakout board.** The address depends
>    on how the board straps SDO/SA0, and vendors differ. The console's `scan` command
>    settles it in two seconds at the bench — which is why stage 1.4 of the handout runs
>    `scan` before anything else.

---

## Answer key — ISM330DHCX  *(DS13012 Rev 6)*

### Pre-lab section B

| B | Quantity | Value |
|---|---|---|
| 1 | Supply voltage V_DD | **1.71 – 3.6 V** (1.8 V typ). Use the board's 3V3. |
| 2 | I/O supply V_DDIO | **1.62 – 3.6 V**. Logic thresholds are ratiometric: V_IH = 0.7·V_DDIO, V_IL = 0.3·V_DDIO |
| 3 | Absolute maximum on V_DD | **−0.3 to 4.8 V**; on any input pin, −0.3 V to V_DDIO + 0.3 V |
| 4 | I²C 7-bit address | **`0x6A`** with SDO/SA0 to GND, **`0x6B`** with SDO/SA0 to V_DDIO. Datasheet: SAD = `110101x`b |
| 5 | Device-ID register | **`WHO_AM_I` = `0x0F`**, fixed read-only value **`0x6B`** |
| 6 | Accelerometer control register | **`CTRL1_XL` = `0x10`**, reset default `0x00` (power-down) |
| 7 | Full-scale field | **`FS[1:0]_XL`, bits 3:2** of `CTRL1_XL` — see the encoding below |
| 8 | ODR field | **`ODR_XL[3:0]`, bits 7:4** of `CTRL1_XL` |
| 9 | Sensitivity | ±2 g → **0.061**; ±4 g → **0.122**; ±8 g → **0.244**; ±16 g → **0.488 mg/LSB** |
| 10 | First output register | **`OUTX_L_A` = `0x28`** (through `OUTZ_H_A` = `0x2D`, so six bytes from `0x28`) |
| 11 | Output format | **16-bit two's complement, little-endian** (low byte at the lower address) |

`CTRL1_XL` bit layout, from Table 41:

```
 bit   7        6        5        4        3       3:2      1           0
     ODR_XL3  ODR_XL2  ODR_XL1  ODR_XL0  FS1_XL  FS0_XL  LPF2_XL_EN   0
```

Bit 0 **must be written 0** for correct operation — the datasheet says so explicitly, and
it is a good thing to make a student notice.

### The full-scale encoding — the trap, and it is real

```
FS[1:0]_XL      range      sensitivity
    00          ±2 g       0.061 mg/LSB      <- reset default
    01          ±16 g      0.488 mg/LSB      <- NOT in ascending order
    10          ±4 g       0.122 mg/LSB
    11          ±8 g       0.244 mg/LSB
```

This is quoted verbatim from Table 42 of DS13012 Rev 6. A student who assumes `01` means
±4 g actually configures ±16 g, then applies the ±4 g sensitivity, and reads a magnitude
of about **250 mg** instead of 1000 — stable, repeatable, and completely wrong.

**Do not warn them beyond what the handout already says.** Let it happen, then ask:
*"Your reading is stable to a tenth of a milli-g. Is it right?"*

### ODR encoding (Table 43) and the values for this lab

`ODR_XL[3:0]`: `0000` power-down · `0011` 52 Hz · **`0100` 104 Hz** · `0101` 208 Hz.

| Goal | `CTRL1_XL` | Meaning |
|---|---|---|
| ±2 g, 104 Hz | **`0x40`** | ODR `0100`, FS `00`, LPF2 off, bit 0 = 0 |
| ±16 g, 104 Hz | **`0x44`** | ODR `0100`, FS `01` — for handout step 2.4 |

Reset default is power-down, so **a device that reads its ID correctly but returns
all-zero data has simply not been enabled.** Expect this; it is on the troubleshooting
table.

### Auto-increment — already on

`IF_INC` is **bit 2 of `CTRL3_C` (`0x12`)**, and `CTRL3_C`'s reset default is **`0x04`** —
so auto-increment is **enabled out of reset** on this part. The console's `dump` command
therefore works without any configuration.

This is worth pointing out rather than hiding: it is a case where the sensible default
saved you, and where a different part in the same family might not have.

### Electrical figures students will meet in Lecture 2

| Parameter | Min | **Typ** | Max | Unit |
|---|---|---|---|---|
| Acceleration noise density, high-performance mode | | **60** | 100 | µg/√Hz |
| Zero-g level offset accuracy | −65 | **±10** | +65 | mg |
| Zero-g level change vs. temperature | −0.5 | **±0.1** | +0.5 | mg/°C |
| Linear acceleration sensitivity tolerance | −2 % | | +2 % | |
| Sensitivity change vs. temperature (−40 to +105 °C) | −0.01 | ±0.005 | +0.01 | %/°C |
| Cross-axis sensitivity (**at 25 °C only**) | | ±0.5 | | % |
| Operating temperature range | −40 | | +105 | °C |

Gyroscope, for Labs 3 and 4: ±125/250/500/1000/2000/4000 dps; 4.375 to 140 mdps/LSB;
zero-rate level ±1 dps typ (±3 max); rate noise density 5 mdps/√Hz; angular random walk
0.21 °/√h; bias instability 3 °/h. The FIFO is 9 kB.

**The cross-axis row is the one to notice.** It is specified *at 25 °C, for the packaged
die*. It says nothing about your board after reflow — which is exactly the point Lecture 2
makes at minute 41, and it is now demonstrable on the students' own datasheet.

### Expected values at rest### Expected values at rest, ±2 g, sensor flat with Z up

- `raw_z` ≈ **+16 300 to +16 500** (1000 mg ÷ 0.061 mg/LSB ≈ 16 393)
- `raw_x`, `raw_y`: the datasheet's zero-g offset accuracy is ±10 mg typ, so expect
  roughly **±160 counts typ** and up to **±1070 counts** at the ±65 mg limit. This *is*
  the zero-g offset from Lecture 2, seen for the first time on real silicon
- magnitude **970–1030 mg** for a typical part; a part near the offset limit can sit
  further out and still be in specification — which is itself worth saying aloud

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
