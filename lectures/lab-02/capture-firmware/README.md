# Laboratory 2 — capture firmware

The firmware students build, flash and drive in Laboratory 2. It extends the Laboratory 1
console idiom rather than replacing it: **raw codes and milliseconds out, never
engineering units, and no statistics at all.** Converting codes and computing σ are the
learning outcomes; if the firmware did either, the lab would teach nothing.

| File | What it is |
|---|---|
| `lab2_config.h` | **the file the student edits** — one constant, `LAB2_CTRL1_XL` |
| `lab2_capture.c` / `.h` | the console: `cap`, `odr`, `lpf`, `cfg`, `scan`, `addr` |
| `test/` | a host build against a simulated sensor, so the firmware can be checked without a board |

## The one constant, and why only one

`instructor-guide.md` §9.3 puts Lab 2 at exactly one rung of the on-ramp: **change one
constant in supplied firmware and rebuild.** So `lab2_config.h` exposes precisely one:

```c
#define LAB2_CTRL1_XL   0x40      /* -> students change this to 0x42 */
```

`0x40` is 104 Hz, ±2 g, **LPF2 off** — the reset-default configuration Lecture 3 spent
twenty minutes on. `0x42` is the same with `LPF2_XL_EN` set. Students capture stationary
data before and after, and watch σ fall because they narrowed the bandwidth without
touching the sample rate. That is Lecture 3's thesis, measured by the student, as a direct
consequence of the one line they edited.

**ODR and LPF2 are also settable at runtime** (`odr 6`, `lpf on`). That is deliberate:
the ODR sweep in stage 3 would otherwise cost four rebuilds and twenty minutes of bench
time to teach nothing the first rebuild did not. One rebuild for the toolchain, runtime
commands for the measurement.

## Commands

```
cap [n]        capture n samples as CSV (default 2000)
odr <code>     0 off · 1 12.5 · 2 26 · 3 52 · 4 104 · 5 208 · 6 416 Hz
lpf on|off     LPF2_XL_EN — the second low-pass filter
cfg            WHO_AM_I, CTRL1_XL decoded field by field, CTRL8_XL, CTRL3_C
scan           list every device answering on the bus
addr <a>       talk to 7-bit address <a>
```

A capture streams as it is taken and buffers nothing, so any length works. Each one is
self-describing — it opens with `# CTRL1_XL=0x.. n=..` and closes with the elapsed time,
the mean interval in microseconds, and the achieved rate:

```
# CTRL1_XL=0x40 n=2000
n,t_ms,raw_x,raw_y,raw_z
1,9,-5,2,16395
...
# elapsed_ms=19640 samples=2000 mean_interval_us=9824
# achieved_rate=101.791 Hz  <- compare with the ODR you set
```

That achieved-rate line is the **only** arithmetic the firmware performs, and it is there
because a stopwatch cannot resolve it and stage 4 depends on it.

## Timing: 1 ms ticks, on purpose

Timestamps come from `HAL_GetTick()`, which is 1 ms. That is too coarse to resolve the
jitter of an individual sample, and entirely sufficient for what the lab asks — the
**mean** interval over a long capture. 2000 samples across ~20 s pins the mean to about
0.5 µs, so a 2 % rate error is unmissable.

A 1 MHz free-running timer would give per-sample jitter, and would need a CubeMX change
plus hardware the students cannot see. If you want it later, add a TIM at 1 MHz and swap
`now_ms()` — nothing else in the file depends on the resolution.

## Building and flashing

Same CubeMX project as Laboratory 1 (`lab-01/cubemx-fw/`, STM32F070xB). Add
`lab2_capture.c` to the build, put `lab2_capture.h` and `lab2_config.h` where the
includes can find them, and call the two entry points:

```c
#include "lab2_capture.h"

int main(void)
{
    /* ... CubeMX init: HAL_Init(), clocks, MX_GPIO_Init(),
           MX_I2C1_Init(), MX_USART2_UART_Init() ... */
    lab2_init();
    while (1) {
        lab2_poll();
    }
}
```

It expects `hi2c1` and `huart2`, exactly as the Lab 1 console does. Serial is 115200 8N1
over the Nucleo's ST-LINK virtual COM port.

**Flash every board with `0x40` before the session** and keep a known-good `0x42` binary
to hand. A team whose build breaks must still be able to finish the measurement — that is
the on-ramp's standing rule (§9.2) and it is the whole reason the toolchain exercise is
safe to run on bench time.

## Testing without hardware

```bash
cd test && make check
```

`test/` builds the real `lab2_capture.c` for the host against a stubbed HAL and a
simulated ISM330DHCX whose noise scales as √bandwidth. It is not a toy: it is what
verified that this lab's conclusions actually emerge from this firmware. See
`test/README.md` for what it checks and what it found.
