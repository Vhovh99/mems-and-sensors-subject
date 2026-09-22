# The microcontroller on-ramp — one page, read it once

**Issued with Laboratory 2.** Keep it; every remaining laboratory assumes this page.

This course assumes you have used a microcontroller before. Many of you have not, and
pretending otherwise would waste your time and ours. So Laboratory 2 spends twenty
minutes — once, with the whole room together — turning the toolchain from a source of
fear into a thing you have done. After today you will do it alone, and nobody will
explain it again.

You are not learning to program in Laboratory 2. **You are changing one number and
watching it reach the silicon.** That is the entire skill being built today.

---

## The four words you need

**Source** — text files a human writes. `lab2_config.h` is one. You can read it.

**Compiler** — a program that turns source into machine instructions for one specific
chip. The chip on your board is an Arm Cortex-M0. Your laptop is not, which is why you
cannot simply run the file.

**Build** — running the compiler over all the source and linking the results into one
`.elf` or `.bin` image. A build either succeeds or prints an error with a **file name and
a line number**. Read that line. It is almost always right about where, and often right
about what.

**Flash** — copying the built image into the microcontroller's non-volatile memory, over
the USB cable, through the ST-LINK debugger built into the Nucleo board. After flashing,
the chip resets and starts running your image. Power-cycling does not undo it: flash
survives until you flash something else.

---

## Where things live

```
cubemx-fw/
├─ Core/Src/main.c          the program's entry point. main() is here.
├─ Core/Src/lab2_capture.c  the console. Instructor code. Do not edit.
├─ Core/Inc/lab2_config.h   >>> THE FILE YOU EDIT <<<
└─ Drivers/                 ST's HAL library. Never edit anything in here.
```

`main()` does three things, in this order: initialise the clocks and the peripherals
(code CubeMX generated), call `lab2_init()` once, then call `lab2_poll()` forever. The
`while (1)` loop at the bottom of `main()` never exits. That is normal — an embedded
program has nowhere to return to.

---

## The loop you will run today

1. **Edit.** Open `Core/Inc/lab2_config.h`. Change `0x40` to `0x42`. Save.
2. **Build.** Press the build button, or `make` in a terminal. Wait for `0 errors`.
3. **Flash.** Press the download/run button, or `make flash`. The board's LEDs blink
   during the transfer.
4. **Verify.** Open the serial terminal, 115200 8N1, and press the black RESET button on
   the Nucleo. The banner prints the value that is *actually compiled in*:

   ```
   firmware built with LAB2_CTRL1_XL = 0x42
   ```

   **If it still says `0x40`, the chip is running the old image.** You edited, or built,
   or flashed — but not all three. This is the single most common failure of the day and
   it is not a mistake, it is the normal way of finding out that a build did not happen.

Step 4 is why the banner exists. Never trust that a flash worked; make the firmware tell
you.

---

## Serial, in three lines

The Nucleo presents itself to your laptop as a serial port — `/dev/ttyACM0` on Linux,
`COM<n>` on Windows, `/dev/tty.usbmodem*` on macOS. Settings are **115200 baud, 8 data
bits, no parity, 1 stop bit**, no flow control. Any terminal will do: PuTTY, `screen`,
`minicom`, the built-in terminal in your IDE.

Two things worth knowing before they confuse you. **Only one program may hold the port at
a time** — if the terminal will not open, close the other one. And the board only prints
when it has something to say, so a silent terminal usually means you have not pressed
RESET.

---

## To capture data into a file

You need the CSV in a file to analyse it, and copying it out of a terminal window by hand
does not scale to 2000 rows.

- `screen -L -Logfile capture.csv /dev/ttyACM0 115200` — logs everything to the file.
- PuTTY: Session → Logging → *All session output* → choose a filename, **before** you
  connect.
- Most IDE terminals have a "save output" button. Find it now, not at minute 55.

Afterwards, delete the banner and command echoes from the top of the file so the first
line is `n,t_ms,raw_x,raw_y,raw_z`. Spreadsheets import that directly.

---

## When it goes wrong

| Symptom | Almost always |
|---|---|
| Build fails, red text | read the **first** error, not the last; the rest are its consequences |
| Build succeeds, banner unchanged | you did not flash, or you flashed a different project |
| No serial output at all | wrong port, wrong baud, or you have not pressed RESET |
| Output is mojibake | baud rate is not 115200 |
| Cannot open the port | another terminal already has it |
| `ERROR: no reply from 0x6A` | wiring or pull-ups — a firmware problem this is not |

**If your build breaks and stays broken, say so early and take the known-good binary.**
Every laboratory in this course ships one. The measurement is the assessed work; the
toolchain is a means to it, and losing an afternoon to a build is a bad trade. You will
get another rebuild in Laboratory 3, and another in every lab after that.

---

## What comes next

| Lab | What you will write |
|---|---|
| **2** (today) | one constant, then rebuild |
| 3 | fill in a driver header from the datasheet |
| 4 | one pure function — roll and pitch from acceleration |
| 5 | a conversion and calibration function; add a second sensor to an init sequence |
| 6 | the acquisition loop, including rejecting invalid readings |
| 7 | a driver, from the register map |
| 8 | the capstone: integrate, calibrate, validate, submit source |

One new kind of authorship per laboratory, and a known-good binary every time. By Lab 7
you will write a driver, and it will not feel like a leap, because there will not have
been one.
