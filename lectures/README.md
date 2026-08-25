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

## Pilot package (this is what exists so far)

| | Lecture 1 | Lecture 2 | Laboratory 1 |
|---|---|---|---|
| Topic | MEMS, sensors, and the measurement-system architecture | Sensor specifications and datasheet-based selection | Datasheet-to-data bring-up |
| Week | 1 | 2 | 2 |
| Slides | 45 | 33 | — |
| Files | `lecture-01/output/` | `lecture-02/output/` | `lab-01/` |

### Lecture folders contain

- `L*.pptx` — the deck in **English**, speaker notes on every slide (native editable shapes)
- `L*-HY.pptx` — the same deck in **Armenian** (slide text; notes stay English)
- `L*.pdf` — preview, for reading away from a computer
- `lecture-plan.md` — outcomes, authoritative minute-by-minute timeline, cognitive-load audit, reading list
- `activities.md` — every poll with per-distractor diagnostics, peer-instruction scripts, formative quiz with answer key, contingencies

### `lab-01/` contains — **no student programming**

The boards are pre-flashed; students drive the sensor from a serial console and do every
conversion by hand. This uses the semester plan's own "known-good binary" provision (§10).

- `prelab-sheet.md` — **the gate**: datasheet extraction, bit-field construction, a one-page I²C primer, and the console reference
- `lab1-handout.md` — the two claims, staged procedure, three injected faults, troubleshooting table
- `rubric.md` — bench check-off, 21-point submission rubric, metrics to record
- `instructor-notes.md` — answer key, build-and-flash instructions, session choreography ⚠ **verify the register values against your actual part before teaching**
- `console-firmware/` — the register console you build once and flash to every board

## `reader/`

The course reader — the book that covers what no textbook does. **Chapters 1 and 2 are
drafted** (`course-reader-ch1-2.pdf`, 21 pages) as a sample of the format; the remaining
chapters are written one per lecture as each lecture is developed. See
`reader/README.md` for the chapter template and authoring conventions, and
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

Both lectures exist in Armenian as `*-HY.pptx` / `*-HY.pdf`. They are **generated** from
the English decks by `tools/translate_deck.py` using the dictionaries in `tools/i18n/`,
so the two languages cannot drift apart: change a lecture, rebuild it, rerun the
translator.

**Start with `tools/i18n/GLOSSARY-hy.md`** — it lists every technical term chosen, marks
which ones come from the accredited ծրագիր, and flags three that want your judgement
(accuracy/precision/resolution). Correct a term there and the fix propagates to every
slide in both lectures.

## `tools/`

Generation scripts. `deck.py` is the shared design system — palette, type scale, slide
furniture, the measurement-chain diagram. `build_l1.py` / `build_l2.py` produce the
decks; `grid.py` renders thumbnail sheets for visual checking.

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
   Lectures 1–2 and Lab 1 are audit-safe either way. See `instructor-guide.md` §7.1.
2. **The microcontroller prerequisite** — the plan assumes it, never teaches it, then
   assesses it in the capstone. A staged on-ramp and three options are in
   `instructor-guide.md` §9.

## Still to build

Lectures 3–16, Laboratories 2–8, the capstone brief, the assessment bank, and
instructor reference solutions. The pilot's timing data should be reviewed before
Lectures 3–7 are written.
