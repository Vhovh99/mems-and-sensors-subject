#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate lab2-template.xlsx — the student spreadsheet for Laboratory 2.

    python3 make_template.py

Needs openpyxl. Regenerate whenever the handout's tables change, so the sheet and
the handout cannot drift apart.

One compatibility note, learned the hard way: use STDEVP, not STDEV.P. openpyxl
writes the modern name without the `_xlfn.` prefix Excel expects, and LibreOffice
then shows #NAME? in every cell that depends on it. STDEVP is the legacy spelling
and both Excel and LibreOffice accept it. It computes the population standard
deviation, which is what a whole capture calls for.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROWS = 2000                     # data rows the formulas cover

BOLD  = Font(bold=True)
ITAL  = Font(italic=True)
HEAD  = Font(bold=True, color="FFFFFF")
INK   = PatternFill("solid", fgColor="1A1F24")
TEAL  = PatternFill("solid", fgColor="DCEDEF")
AMBER = PatternFill("solid", fgColor="FAECD8")
thin  = Side(style="thin", color="BBBBBB")
BOX   = Border(left=thin, right=thin, top=thin, bottom=thin)

LAST = ROWS + 1                 # last spreadsheet row holding data

wb = Workbook()

# ------------------------------------------------------------- READ ME FIRST
ws = wb.active
ws.title = "READ ME FIRST"
ws.column_dimensions["A"].width = 100
for i, (t, f) in enumerate([
 ("MEMS & Sensors — Laboratory 2 spreadsheet template", BOLD),
 ("", None),
 ("This does the arithmetic the handout asks for. You still have to take the data,", None),
 ("read the sensitivity off the datasheet, and interpret the result — those are the", None),
 ("assessed parts. This sheet only saves you from retyping formulas.", None),
 ("", None),
 ("HOW TO USE IT", BOLD),
 ("1. Capture with the console, logging the terminal to a .csv file.", None),
 ("2. Open the .csv and delete everything above the line starting  n,t_ms,raw_x...", None),
 ("3. Copy the five data columns into the 'capture' sheet, starting at A2.", None),
 ("4. Fill in the yellow configuration cells on 'capture' (M2:N6).", None),
 ("5. Read the answers off 'results'. Copy them into your pre-lab tables.", None),
 ("6. Use a FRESH COPY of this file for every capture you take.", None),
 ("", None),
 ("THE TWO TRAPS", BOLD),
 ("· Population standard deviation, not sample. You have the whole capture. This", None),
 ("  sheet uses STDEVP; with 2000 points the difference is 0.03 % either way, but", None),
 ("  say in your report which you used.", None),
 ("· A code IS an LSB. Sigma in codes is already sigma in LSB — multiply by the", None),
 ("  sensitivity ONCE to get milli-g. Teams multiply twice every year and get an", None),
 ("  answer finer than one code, which is impossible. If your sigma is below", None),
 ("  0.061 mg at +/-2 g, that is what you have done.", None),
 ("", None),
 ("WHAT THIS SHEET DELIBERATELY DOES NOT DO", BOLD),
 ("It does not plot anything. The four plots are yours to make and to caption, and", None),
 ("a caption that does not say what is plotted and at what configuration scores", None),
 ("nothing. It also does not choose your ODR or your filter — that is the paragraph", None),
 ("the whole laboratory exists to make you write.", None),
], start=1):
    c = ws.cell(row=i, column=1, value=t)
    if f:
        c.font = f

# ------------------------------------------------------------------- capture
ws = wb.create_sheet("capture")
headers = [("n", 6), ("t_ms", 9), ("raw_x", 9), ("raw_y", 9), ("raw_z", 9),
           ("", 3), ("x (mg)", 10), ("MA N=4", 10), ("MA N=16", 10),
           ("LP alpha", 11), ("dt (ms)", 9)]
for col, (h, w) in enumerate(headers, start=1):
    c = ws.cell(row=1, column=col, value=h)
    if h:
        c.font = HEAD
        c.fill = INK
    ws.column_dimensions[get_column_letter(col)].width = w

ws["M1"] = "YOUR CONFIGURATION — fill these in"
ws["M1"].font = BOLD
for i, (label, val) in enumerate([
        ("CTRL1_XL (from the # line)", "0x40"),
        ("ODR set (Hz)", 104),
        ("LPF2_XL_EN (0 or 1)", 0),
        ("sensitivity (mg/LSB)", 0.061),
        ("alpha for the low-pass", 0.25)], start=2):
    ws.cell(row=i, column=13, value=label)
    c = ws.cell(row=i, column=14, value=val)
    c.fill, c.border, c.font = AMBER, BOX, BOLD
ws.column_dimensions["M"].width = 34
ws.column_dimensions["N"].width = 10
ws["M8"] = "Paste the capture into A2:E… — n, t_ms, raw_x, raw_y, raw_z"
ws["M9"] = "The columns right of the gap fill themselves."
ws["M9"].font = ITAL

for r in range(2, LAST + 1):
    ws.cell(row=r, column=7, value=f'=IF(C{r}="","",C{r}*$N$5)')
    if r >= 5:
        ws.cell(row=r, column=8, value=f'=IF(C{r}="","",AVERAGE(C{r-3}:C{r})*$N$5)')
    if r >= 17:
        ws.cell(row=r, column=9, value=f'=IF(C{r}="","",AVERAGE(C{r-15}:C{r})*$N$5)')
    ws.cell(row=r, column=10,
            value=(f'=IF(C{r}="","",C{r}*$N$5)' if r == 2 else
                   f'=IF(C{r}="","",J{r-1}+$N$6*(C{r}*$N$5-J{r-1}))'))
    if r >= 3:
        ws.cell(row=r, column=11, value=f'=IF(B{r}="","",B{r}-B{r-1})')

# ------------------------------------------------------------------- results
ws = wb.create_sheet("results")
ws.column_dimensions["A"].width = 42
for c, w in (("B", 14), ("C", 14), ("D", 14), ("E", 34)):
    ws.column_dimensions[c].width = w


def block(row, title):
    c = ws.cell(row=row, column=1, value=title)
    c.font, c.fill = BOLD, TEAL


def hilite(ref, note=None):
    ws[ref].font, ws[ref].fill, ws[ref].border = BOLD, AMBER, BOX
    if note:
        ws[f"E{ref[1:]}"] = note


N = f"COUNT(capture!C2:C{LAST})"

block(1, "STAGE 2 — noise, offset and effective bits")
for col, ax in zip("BCD", "XYZ"):
    ws[f"{col}2"] = ax
    ws[f"{col}2"].font = BOLD
for i, (label, f) in enumerate([
        ("mean, codes",                    "=AVERAGE(capture!{c}2:{c}%d)" % LAST),
        ("mean, mg",                       "=AVERAGE(capture!{c}2:{c}%d)*capture!$N$5" % LAST),
        ("sigma, codes (= sigma in LSB)",  "=STDEVP(capture!{c}2:{c}%d)" % LAST),
        ("sigma, mg",                      "=STDEVP(capture!{c}2:{c}%d)*capture!$N$5" % LAST),
], start=3):
    ws.cell(row=i, column=1, value=label)
    for j, col in enumerate("CDE"):          # raw_x/y/z live in C, D, E
        ws.cell(row=i, column=2 + j, value=f.format(c=col))

ws["A8"], ws["B8"] = "samples in the capture", f"={N}"
ws["A9"], ws["B9"] = "mean vector magnitude, mg", "=SQRT(B4^2+C4^2+D4^2)"
ws["E9"] = "expect ~1000 mg with the board flat"
ws["A10"], ws["B10"] = "zero-g offset X, mg", "=B4"
ws["A11"], ws["B11"] = "zero-g offset Y, mg", "=C4"
ws["E10"] = "datasheet +/-10 mg typ, +/-65 mg max"
ws["A12"], ws["B12"] = "bits that are noise = LOG(sigma_LSB,2)", "=LOG(B5,2)"
ws["A13"], ws["B13"] = "EFFECTIVE BITS = 16 - the above", "=16-B12"
hilite("B13", "say this number out loud")

block(15, "STAGE 3 — is sigma what the datasheet predicts?")
ws["A16"], ws["B16"] = "bandwidth = ODR/2, Hz", "=capture!$N$3/2"
ws["A17"], ws["B17"] = "predicted sigma, typ 60 ug/rtHz, mg", "=60*SQRT(B16)/1000"
ws["A18"], ws["B18"] = "predicted sigma, max 100 ug/rtHz, mg", "=100*SQRT(B16)/1000"
ws["A19"], ws["B19"] = "measured / predicted (max)", "=B6/B18"
ws["A20"], ws["B20"] = "YOUR PART's noise density, ug/rtHz", "=B6/SQRT(B16)*1000"
hilite("B20", "carry this into your stage 3.4 answer")

block(22, "STAGE 4 — the rate you actually got")
ws["A23"] = "mean interval, ms"
ws["B23"] = f"=(INDEX(capture!B:B,{N}+1)-capture!B2)/({N}-1)"
ws["A24"], ws["B24"] = "achieved rate, Hz", "=1000/B23"
ws["A25"], ws["B25"] = "ODR you set, Hz", "=capture!$N$3"
ws["A26"], ws["B26"] = "error, %", "=(B24-B25)/B25*100"
ws["A27"], ws["B27"] = "capture duration, s", "=B23*(B8-1)/1000"
ws["A28"], ws["B28"] = "duration if spacing were 1/ODR, s", "=B8/B25"
ws["A29"], ws["B29"] = "TIMING ERROR AT THE END, s", "=B27-B28"
hilite("B29", "is this calibratable afterwards?")

block(31, "STAGE 5 — what filtering bought, and what it cost")
for col, h in zip("BCD", ("sigma (mg)", "reduction", "predicted")):
    ws[f"{col}32"] = h
    ws[f"{col}32"].font = BOLD
for i, (label, s, red, pred) in enumerate([
        ("raw",                 f"=STDEVP(capture!G2:G{LAST})",  None,          None),
        ("moving average N=4",  f"=STDEVP(capture!H5:H{LAST})",  "=$B$33/B34",  "=SQRT(4)"),
        ("moving average N=16", f"=STDEVP(capture!I17:I{LAST})", "=$B$33/B35",  "=SQRT(16)"),
        ("low-pass alpha",      f"=STDEVP(capture!J2:J{LAST})",  "=$B$33/B36",
         "=SQRT((2-capture!$N$6)/capture!$N$6)")], start=33):
    ws.cell(row=i, column=1, value=label)
    ws.cell(row=i, column=2, value=s)
    if red:
        ws.cell(row=i, column=3, value=red)
    if pred:
        ws.cell(row=i, column=4, value=pred)

ws["A38"], ws["B38"] = "bandwidth after MA N=4, Hz", "=B16/4"
ws["A39"], ws["B39"] = "group delay of MA N=4, ms", "=1.5/capture!$N$3*1000"
ws["E38"] = "which native ODR has this bandwidth?"

block(41, "THE COMPARISON THAT MATTERS — stage 5.3")
ws["A42"], ws["B42"] = "sigma of THIS capture averaged by 4, mg", "=B34"
ws["A43"] = "sigma you measured natively at that bandwidth"
ws["B43"] = 0
hilite("B43", "type it in from your stage 3 table")
ws["A44"] = "ratio"
ws["B44"] = '=IF(B43=0,"fill in B43",B42/B43)'
ws["E44"] = "should be ~1.00 — and 5.3 asks you why"

for s in wb.worksheets:
    s.sheet_view.showGridLines = (s.title == "capture")

wb.save("lab2-template.xlsx")
print(f"wrote lab2-template.xlsx  ({ROWS} data rows)")
