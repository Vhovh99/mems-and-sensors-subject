# Host test for the Lab 2 firmware

Builds the real `lab2_capture.c` for a PC against a stubbed HAL and a simulated
ISM330DHCX, so the firmware can be exercised without a board.

```bash
make check
```

## Why it exists

Shipping C to a room of twenty students who have never built firmware, on a lab where the
toolchain *is* the lesson, is not a place to guess. This harness answered two questions
before the code left the desk:

1. **Does the firmware work?** Commands parse, `cfg` decodes the CTRL1_XL fields
   correctly, a capture streams valid CSV, and the closing summary arithmetic is right.
2. **Does the lab's physics actually emerge from it?** This is the important one. The
   simulated sensor's noise scales as √bandwidth, exactly as the datasheet says, and
   `check_lab.py` then checks that the conclusions the handout asks students to draw are
   the conclusions the data supports.

## What `check_lab.py` verifies

Running 3000-sample captures at each ODR:

| Check | Result |
|---|---|
| σ scales as √2 per ODR doubling | 1.411, 1.413, 1.415, 1.414 against √2 = 1.414 |
| σ matches 100 µg/√Hz × √(ODR/2) | 0.365 / 0.515 / 0.728 / 1.030 / 1.457 mg against 0.361 / 0.510 / 0.721 / 1.020 / 1.442 predicted |
| Enabling LPF2 lowers σ at fixed ODR | 0.728 → 0.515 mg |
| An N-sample average on a fast capture equals sampling natively slower | N=4 on 416 Hz → 0.724 mg vs native 104 Hz → 0.728 mg |
| The achieved rate is below the ODR | 101.8 Hz at ODR 104; 383.9 Hz at ODR 416 |

The fourth row is the headline result of the whole laboratory, and it holds to within 1 %.

## What the stub is not

The simulated device models WHO_AM_I, CTRL1_XL's three fields, CTRL3_C's reset value, and
an accelerometer with √bandwidth noise. It does **not** model the real LPF2 response — it
simply halves the bandwidth when `LPF2_XL_EN` is set. The actual filter's corner is
selected by `CTRL8_XL` and depends on the datasheet revision, so the *direction* of the
change is verified here and the *magnitude* is on the instructor's bench-verification
list in `../../instructor-notes.md`.
