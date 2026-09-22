# Laboratory 2 — analysis helpers

| File | For whom | What it is |
|---|---|---|
| `lab2-template.xlsx` | **students** | the spreadsheet, with every formula the handout asks for already in place |
| `make_template.py` | instructor | regenerates the .xlsx; edit this, not the workbook |
| `analyse_capture.py` | instructor | checks a team's numbers in ten seconds at the bench |

## The spreadsheet

Three sheets: `READ ME FIRST`, `capture` (paste data, set five configuration cells) and
`results` (everything the handout's tables want, computed).

It deliberately **does not plot anything**. The four plots and their captions are the
assessed work, and a template that drew them would remove the only part of the analysis
that requires judgement. It also does not choose an ODR or a filter — that is the closing
paragraph the whole laboratory exists to produce.

Hand it out only to teams whose spreadsheet skills are stalling. A team that builds the
columns themselves has learned more, and section G of the pre-lab sheet gives them every
formula they need to do so.

### One compatibility trap, found by testing

Use **`STDEVP`**, not `STDEV.P`. openpyxl writes the modern name without the `_xlfn.`
prefix Excel expects, and LibreOffice then shows `#NAME?` in every dependent cell — which
is most of the `results` sheet. `STDEVP` is the legacy spelling; Excel, LibreOffice and
Google Sheets all accept it, and it is the population standard deviation, which is the
right one for a whole capture.

Students typing their own formulas can use either name; both are correct and with 2000
samples they differ by 0.03 %.

## Verification

The template was filled with a real 2000-sample capture and recalculated in LibreOffice,
then checked against `analyse_capture.py` on the same file. They agree:

| | template | reference |
|---|---|---|
| σ, X axis | 0.7367 mg | 0.7367 mg |
| effective bits | 12.41 | 12.41 |
| extracted noise density | 102 µg/√Hz | 102 µg/√Hz |
| achieved rate | 101.86 Hz (−2.06 %) | 101.86 Hz |
| moving average N=4 | 0.3691 mg, ÷1.996 | 0.3691 mg |
| **stage 5.3 ratio** | **0.9992** | — |

That last row is the laboratory's headline result: a 416 Hz capture averaged by four has
the same σ as sampling natively at a quarter the rate. It comes out of the student's own
spreadsheet at 1.00.

## Using the reference script

```bash
./analyse_capture.py baseline_0x40.csv                    # one capture, everything
./analyse_capture.py baseline_0x40.csv filtered_0x42.csv  # LPF2 off/on ratio
./analyse_capture.py sweep_*.csv                          # the stage 3 table
```

It reads the firmware's CSV including the `#` comment lines, so it knows the
configuration without being told. Standard library only — no venv needed.

The `sweep_*` form prints the students' stage 3 table with the ratio column filled in, and
the two-file form prints the LPF2 off/on ratio you need for the margin note in
`../instructor-notes.md`.
