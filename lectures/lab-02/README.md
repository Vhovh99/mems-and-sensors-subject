# Laboratory 2 — Sampling, noise and filtering
**Week 4** · 80 minutes · the bench continuation of Lecture 3

| File | For whom | What it is |
|---|---|---|
| `prelab-sheet.md` | students | **the gate.** Datasheet extraction and the arithmetic that makes the session possible |
| `prelab-sheet-HY.md` | students | the same sheet in Armenian |
| `mcu-onramp.md` | students | **one page on the toolchain** — what a build is, what flashing does, how to log serial output |
| `lab2-handout.md` | students | the five stages, with the bench check-off folded in |
| `instructor-notes.md` | instructor | answer key, choreography, preparation checklist, what to record afterwards |
| `capture-firmware/` | instructor | the firmware, and the one constant students edit |
| `analysis/` | both | the student spreadsheet template, and a reference script for checking numbers at the bench |

There is **no `rubric.md`** — the bench check-off and the submission list live in the
handout's closing section instead.

## What makes this laboratory unusual

It is **two labs in one session**, and both are load-bearing:

1. **The toolchain lab.** Per `../instructor-guide.md` §9.3–9.4, this is the one session
   where the whole room builds and flashes firmware together. The cohort is not assumed
   to have done it before, and it gets twenty minutes of group attention here and never
   again. Lab 2 was chosen for it because its measurement work needs no fixture — the
   board is already wired from Lab 1, and a stationary capture needs nothing but a still
   bench.
2. **The measurement lab.** Sampling, noise, effective resolution and filtering.

The two are the same act, not two things sharing a room. The constant students change is
`LAB2_CTRL1_XL`, `0x40` → `0x42`, which is `LPF2_XL_EN` — the register bit Lecture 3
built a poll around. They edit one character, rebuild, and measure that σ fell. Do not
substitute a different constant; that coupling is the design.

## The three claims students test

1. Noise depends on the **bandwidth you chose**, not the bits you bought. σ should scale
   as √ODR.
2. A requested sample rate is not an achieved sample rate.
3. Filtering afterwards buys noise back at the price of bandwidth and delay — and
   sampling fast then averaging lands in exactly the same place as sampling slowly.

**Claim 3 is the laboratory's headline.** A 416 Hz capture averaged over four samples has
the same σ as sampling natively at 104 Hz. Verified end to end against the stubbed
firmware: 0.724 mg against 0.728 mg, and 0.9992 in the student spreadsheet.

## Verified before it shipped

- The firmware compiles clean (`-Wall -Wextra`) and runs against a simulated
  ISM330DHCX — `capture-firmware/test/`, `make check`.
- The lab's own conclusions were checked against that simulation: σ ratios of 1.411,
  1.413, 1.415, 1.414 against √2; the filter equivalence above; achieved rates below the
  ODR at every setting.
- The student spreadsheet was filled with a real capture, recalculated in LibreOffice,
  and cross-checked against the reference script. They agree to four figures.

The one figure **not** verified is the exact σ ratio when LPF2 is enabled, because it
depends on the `CTRL8_XL` bandwidth field and the datasheet revision. Its *direction* is
certain, which is all the lab asks. There is a margin in `instructor-notes.md` to write
the measured value into once, from your own kit.

## Sequence

`mcu-onramp.md` and `prelab-sheet.md` go out **a week ahead**, at the end of Lecture 3 —
that lecture's closing slide already tells students to bring the effective-bits
calculation for two ODR settings, which is pre-lab section C2.
