# Laboratory 1 — PRE-LAB SHEET
**Datasheet to data** · Week 2 · Microelectromechanical Systems and Sensors

> **NO PROGRAMMING IN THIS LABORATORY.**
> The boards are pre-flashed. You will drive the sensor from a serial console by
> typing register addresses and values that **you** take from the datasheet, and you
> will convert the raw codes to engineering units **yourself**, on paper or in a
> spreadsheet. There is no toolchain to fight and nothing to compile.
>
> You will begin writing firmware later in the semester, once the microcontroller
> sessions have run.

> **THIS SHEET IS A GATE.**
> Bring it completed, on paper, in your own handwriting. The instructor signs section
> D at the bench. **No signature, no power to your board.** A wrong supply or logic
> level destroys the part in less time than it takes to notice.

Name(s): ______________________________  Team: ______  Date: __________

---

## A · Required reading

1. This sheet, including the I²C primer (F) and the console reference (G).
2. The datasheet for your assigned sensor — **the sections you need**: pin
   description, electrical characteristics (supply and logic levels), register map,
   and the sensitivity table.
3. Your board's user manual pinout page — which physical pins carry I²C1.

You have not been taught I²C in a lecture yet; that is Lecture 3, with the full
treatment in Lecture 13. Section F gives you everything this lab needs.

---

## B · Datasheet extraction  *(from the datasheet — page numbers required)*

This table is the real work of the pre-lab. Every value you write here is a value you
will type into the console at the bench.

| # | Quantity | Your answer | Page |
|---|---|---|---|
| 1 | Supply voltage V_DD, min–max | | |
| 2 | I/O supply V_DDIO, min–max (if separate) | | |
| 3 | Absolute maximum voltage on any pin | | |
| 4 | I²C 7-bit device address, and the pin that selects it | | |
| 5 | Device-ID register: **address** and **expected value** | | |
| 6 | Accelerometer control register: address | | |
| 7 | Bit field that sets full-scale range, and its **encoding** | | |
| 8 | Bit field that sets output data rate, and its encoding | | |
| 9 | Sensitivity (mg/LSB) at **every** selectable range | | |
| 10 | First accelerometer output-data register address | | |
| 11 | Output format: bits, signedness, byte order | | |

**Question 7 deserves a warning.** Do not assume the range encoding counts upwards in
the order you would expect. Read the table. Guessing here is the most common way to
spend an hour on a reading that is stable, repeatable and wrong.

---

## C · Pre-lab calculations

**C1.** Your board's I/O runs at 3.3 V. Your sensor's V_DDIO maximum is your answer to
B2. If you connected this sensor to a 5 V logic board, what would happen, and at which
pin first?

<br><br>

**C2.** You will configure the **±2 g** range. Using your answer to B9, state the value
of one LSB in mg, and the full 16-bit span in g.

<br><br>

**C3.** Build the byte you will write to the accelerometer control register (B6) to get
**±2 g** and an output data rate of about **100 Hz**. Show the bit fields.

```
    bit   7   6   5   4   3   2   1   0
        ┌───┬───┬───┬───┬───┬───┬───┬───┐
        │   │   │   │   │   │   │   │   │      =  0x______
        └───┴───┴───┴───┴───┴───┴───┴───┘
          └──── ODR ────┘ └─FS─┘
```

You will type this value at the bench as `w <reg> <val>`. If it is wrong, nothing
protects you — the sensor will accept it and report confident nonsense.

**C4.** The sensor sits flat on the bench, Z axis up, not moving.
Predict the raw integer you expect from each axis at ±2 g. Show the arithmetic.

  Z: ____________   X: ____________   Y: ____________

**C5.** The console prints these six bytes, low byte first, in this order X, Y, Z:

```
  bytes : 00 00   30 FC   00 40
```

Assemble the three signed 16-bit values and convert all three to **mg** at ±2 g.
State the total magnitude. Is this plausible for a stationary sensor?

  X = ________ = ________ mg    Y = ________ = ________ mg
  Z = ________ = ________ mg    magnitude = ________ mg    plausible? ______

**C6.** Choose the output data rate you will use, and justify it in one sentence. You
are measuring a static orientation, not motion.

  ODR: __________  Because: ________________________________________

---

## D · Bench gate  *(instructor signs before you apply power)*

| Check | Student states aloud | ✓ |
|---|---|---|
| Supply voltage you will connect | | |
| Logic level of your board's I²C pins | | |
| The two lines that need pull-up resistors, and to which rail | | |
| The first register you will read, and its expected value | | |
| What you will do if that read fails | | |

Instructor signature: ______________________  Time: ________

---

## E · Wiring plan  *(draw it — do not wire from memory)*

```
        ┌──────────────────┐                    ┌──────────────────┐
        │   Nucleo board   │                    │  sensor breakout │
        │  3V3 ........... │────────────────────│ VDD              │
        │  GND ........... │────────────────────│ GND              │
        │  I2C1_SDA (D14)  │────────────────────│ SDA              │
        │  I2C1_SCL (D15)  │────────────────────│ SCL              │
        └──────────────────┘                    └──────────────────┘
                                    pull-ups: ______ kΩ to ______
```

**Verify the D14/D15 mapping against your own board's user manual.** It is the standard
Nucleo-64 Arduino-header assignment, but variants differ, and "it worked for the other
team" is not verification.

Most breakouts already carry pull-ups. Check before adding more — two sets in parallel
halves the resistance and can stop the bus working. What did you find?
_______________________________________

---

## F · I²C in one page  *(everything this lab needs)*

**Two wires, many devices.** `SCL` is the clock, always driven by the controller (your
Nucleo). `SDA` carries data both ways. Every device shares the same pair.

**Open-drain, so pull-ups are mandatory.** Devices can only pull a line *low*; nothing
drives it high. A resistor to V_DDIO does that — typically 4.7 kΩ at 100 kHz. **With no
pull-up the bus sits low and nothing works at all.** This is the most common first-day
failure, and the console's `scan` command will show you an empty bus when it happens.

**Addressing.** Each device has a 7-bit address; one pin on the sensor usually selects
between two values, so two identical parts can share a bus. You will type the 7-bit
address. (The console prints the 8-bit form too, because the software libraries you
meet later want the address shifted left by one. Not your problem this week.)

**Reading a register** is two transactions: write the register address, then read the
data back. The console does this for you with `r`.

**Burst reads.** Reading six output bytes one at a time lets the X value come from one
sample and the Z value from the next — a torn reading that looks perfectly fine. The
console's `dump` command reads all six in **one** transaction, from one sample.

**Assembling a 16-bit signed value.** Each axis takes two 8-bit registers, low byte
first on this family, and the result is **two's complement**:

```
    value = (high_byte × 256) + low_byte
    if value ≥ 32768:  value = value − 65536      ← this is what makes it negative
```

Miss that last line and a downward tilt reads as roughly +64000 instead of −1500.
The console does this assembly for you and prints both the bytes and the signed
integer — so you can check your own arithmetic against it in C5.

**Codes are not physics.** The signed integer is not an acceleration. Multiply it by the
sensitivity from the datasheet — and only the row for the range you actually configured:

```
    a [mg] = raw × sensitivity [mg/LSB]
```

The console **will not** do this for you. That is the point of the lab.

---

## G · Console reference  *(the boards are already flashed)*

Serial terminal: **115200 8N1**, over the same USB cable that powers the board.
Values in hex unless noted.

| Command | What it does |
|---|---|
| `help` | list the commands |
| `scan` | list every device that answers on the bus — **your first diagnostic** |
| `addr 6B` | talk to a different 7-bit address |
| `r 0F` | read one register: hex, decimal and binary |
| `r 10 4` | read 4 consecutive registers (count in decimal) |
| `w 10 40` | write `0x40` to register `0x10`, then read it back to confirm |
| `dump 28` | read 6 bytes from `0x28`, assemble three signed 16-bit values |
| `log 28 200 50` | stream 200 samples every 50 ms as CSV — copy this into a spreadsheet |

The console prints **raw codes only**. It never prints mg or m/s². Every engineering
value in your submission is one you computed.

---

## H · What you will hand in

1. Annotated connection diagram (section E, corrected to what you actually built).
2. Register table: every register you wrote, the value, and **why**.
3. A short data log: raw codes **and** your converted SI values, with units.
4. Evidence of the 1 g plausibility test.
5. One sentence: which stage of Lecture 1's measurement chain did you just build?
