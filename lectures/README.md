# MEMS and Sensors — teaching materials

Course: **Microelectromechanical Systems and Sensors** (Միկրոէլեկտրամեխանիկական
համակարգեր և տվիչներ) · ANPU, Institute of Energy and Electrical Engineering ·
bachelor, 7th semester, 5 credits · 16 lectures × 80 min + 8 labs × 80 min.

Built to the **2026 semester plan**. Slides in English. Hardware: **STM32 Nucleo** plus
the **ST ISM330DHCXTR** 6-axis IMU (datasheet DS13012 Rev 6 — the verified answer key is
in `lab-01/instructor-notes.md`).

## Start here

**`instructor-guide.md`** — read this first. Delivery notes, the contingency table, the
three moments most likely to go wrong, and what to record during the pilot.

## Module A — complete

| | Lecture 1 | Lecture 2 | Lecture 3 | Lecture 4 | Laboratory 1 | Laboratory 2 |
|---|---|---|---|---|---|---|
| Topic | MEMS, sensors, and the measurement-system architecture | Sensor specifications and datasheet-based selection | From physical quantity to trustworthy samples | MEMS structures, transduction, fabrication and packaging | Datasheet-to-data bring-up | Sampling, noise and filtering |
| Week | 1 | 2 | 3 | 4 | 2 | 4 |
| Slides | 45 | 33 | 42 | 42 | — | — |
| Files | `lecture-01/output/` | `lecture-02/output/` | `lecture-03/output/` | `lecture-04/output/` | `lab-01/` | `lab-02/` |

Lectures 1–2 and Laboratory 1 were the pilot. Lectures 3–4 complete Module A and were
built to the same standard, against the terminology the pilot's Armenian review
established.

**The four spines, in order.** L1: a measurement is a chain, and some losses are
permanent. L2: selection is arithmetic against a requirement. L3: a sample is
trustworthy only if you can say what it is, how much is information, which band, and
when. L4: a datasheet describes a die, but you buy an assembly. Each lecture repays
something the previous one deferred — L4's hook is the question L2 put on screen and
refused to answer.

### Lecture folders contain

- `L*.pptx` — the deck in **English**, speaker notes on every slide (native editable shapes)
- `L*-HY.pptx` — the same deck in **Armenian** (slide text; notes stay English)
- `L*.pdf` — preview, for reading away from a computer
- `lecture-plan.md` — outcomes, authoritative minute-by-minute timeline, cognitive-load audit, reading list
- `activities.md` — every poll with per-distractor diagnostics, peer-instruction scripts, formative quiz with answer key, contingencies

### `lab-02/` contains — **one constant, one rebuild**

Laboratory 2 is the bench continuation of Lecture 3 **and** the toolchain rung of the
on-ramp (`instructor-guide.md` §9.3–9.4): the one session where the whole room builds and
flashes firmware together. The constant they change is `LPF2_XL_EN` — Lecture 3's own
register bit — so the toolchain exercise and the measurement lesson are the same act.

- `prelab-sheet.md` / `-HY.md` — **the gate**: the arithmetic that makes the session possible
- `mcu-onramp.md` — one page on builds, flashing and serial. Issued with this lab, assumed by every lab after it
- `lab2-handout.md` — five stages, with the bench check-off folded in
- `instructor-notes.md` — answer key, choreography, and what to record afterwards
- `capture-firmware/` — the firmware, plus a host test against a simulated sensor
- `analysis/` — the student spreadsheet template and a reference script

Its headline result: a 416 Hz capture averaged over four samples has the same σ as
sampling natively at 104 Hz. Students measure that themselves, and it is the course's
central trade-off in one number.

### `lab-01/` contains — **no student programming**

The boards are pre-flashed; students drive the sensor from a serial console and do every
conversion by hand. This uses the semester plan's own "known-good binary" provision (§10).

- `prelab-sheet.md` — **the gate**: datasheet extraction, bit-field construction, a one-page I²C primer, and the console reference
- `lab1-handout.md` — the two claims, staged procedure, three injected faults, troubleshooting table
- `rubric.md` — bench check-off, 21-point submission rubric, metrics to record
- `instructor-notes.md` — answer key, build-and-flash instructions, session choreography ⚠ **verify the register values against your actual part before teaching**
- `console-firmware/` — the register console you build once and flash to every board

## `reader/`

The course reader — the book that covers what no textbook does. **Chapters 1–4 are
written** (`course-reader.pdf`, 51 pages); Chapters 1–3 also exist in Armenian
(`course-reader-hy.pdf`). Remaining chapters are written one per lecture as each lecture
is developed. See `reader/README.md` for the chapter template, and
`memos/textbook-options.md` for why a reader rather than a textbook.

## Design memos

`memos/phase0-context.md` — teaching context, learning outcomes, evidence plan, the
prerequisite-ordering issue and its mitigation.
`memos/phase1-narrative.md` — content audit (what was cut and why), ABT narrative arcs,
hooks, chunk maps, first-offering instrumentation.
`memos/textbook-options.md` — textbook assessment: coverage of all 16 lectures against
four candidate books, what no book covers, and a course-reader proposal.

## `shared/`

`imu-driver-for-later-labs/` — the register driver written for Lab 1 and deliberately
held back. It is the natural fit for Labs 3 and 7 in the microcontroller on-ramp
(`instructor-guide.md` §9).

## Armenian versions

All four lectures exist in Armenian as `*-HY.pptx` / `*-HY.pdf`, **generated** from the
English decks by `tools/translate_deck.py`, so the two languages cannot drift apart:
change a lecture, rebuild it, rerun the translator.

**Start with `tools/i18n/GLOSSARY-hy.md`.** It is generated from `hy_terms.py`, so it
cannot disagree with what the slides actually say. It records all 156 canonical terms,
marks which come from the accredited ծրագիր and which from your reviewed reader, and ends
with five open questions that need your decision rather than a guess.

Two things changed in September 2026 and are worth knowing:

- **The 350 corrections you made by hand inside the L1/L2 `-HY.pptx` files have been
  recovered** — 192 of your sentences are in `tools/i18n/hy_instructor.py`, loaded last so
  they override everything. Your *terminology* is now enforced mechanically on every
  translated string, so a term corrected once is correct in every lecture: **լուծաչափ**,
  **չափաբերում**, **արագաչափ**, **տվյալների թերթիկ**, **դրեյֆ**, **տպասալ**, **պատյան**,
  **ժամանակային դրոշմ**, **ԿՆԲ**.
- **`translate_deck.py` no longer overwrites an existing `-HY.pptx`** — it prints
  `· skipping …`. Pass `--overwrite` deliberately when you want a rebuild.

## `tools/`

Generation scripts. `deck.py` is the shared design system — palette, type scale, slide
furniture, the measurement-chain diagram. `build_l1.py` … `build_l4.py` produce
the decks; `grid.py` renders thumbnail sheets for visual checking.

```bash
cd tools && .venv/bin/python build_l1.py
```

Small edits are easier made directly in PowerPoint. Use the scripts for structural or
whole-deck changes. Semantic colour, kept consistent across both decks:
**teal = the true signal path · amber = where error enters · red = the term that kills
the design.**

## `source/`

The two originating documents: the accredited 2024 Armenian ծրագիր and the 2026
semester plan. **They describe different courses** — see `instructor-guide.md` §7.1.

## Two things to decide

1. **The accredited ծրագիր vs the semester plan** — they describe different courses.
   **All of Module A is audit-safe**, which is better than first assessed: L3 maps onto
   official Themes 2.1, 2.2, 2.5, 3.3, 3.6 and 3.7, and L4 onto Themes 1.2, 1.3 and 1.4.
   Lectures 5–16 are the open question. See `instructor-guide.md` §7.1.
2. **The microcontroller prerequisite** — the plan assumes it, never teaches it, then
   assesses it in the capstone. A staged on-ramp and three options are in
   `instructor-guide.md` §9.

## Still to build

Lectures 5–16, Laboratories 3–8, the capstone brief, the assessment bank, and instructor
reference solutions. Armenian versions of reader Chapters 3 and 4, and of the Lab 2
handout.

**Before Lectures 5–11**, two things are worth doing in order: review the timing data
from actually teaching Module A, and settle the ծրագիր question below. Lectures 5–11 are
seven instances of one pattern, so getting that pattern right once is worth more than
drafting them quickly.
