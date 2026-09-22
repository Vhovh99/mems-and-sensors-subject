# -*- coding: utf-8 -*-
"""Write GLOSSARY-hy.md from hy_terms.TERMS, so the two cannot disagree.

    cd lectures/tools && .venv/bin/python i18n/build_glossary.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from i18n import hy_terms

# TERMS is ordered by lecture, so a section is just the slice between two keys.
SECTIONS = [
    ("Measurement chain (Lecture 1)", "sensor", "stiction"),
    ("Specifications (Lecture 2)", "accuracy", "trade-off"),
    ("Acquisition and interfaces (Lecture 3)", "analog signal", "self-test"),
    ("Structures, transduction, fabrication (Lecture 4)", "MEMS", "yield"),
    ("Classroom furniture and register", "poll", "component / term of a sum"),
    ("Laboratory vocabulary", "board (the Nucleo)", "build (a binary)"),
]
keys = list(hy_terms.TERMS)
SRC = {"ծրագիր": "✔ ծրագիր", "reader": "reader", "deck": "deck",
       "ծրագիր+reader": "✔ ծրագիր", "new": "**new**", "lab": "lab-01 (yours)"}

rows = []
for title, first, last in SECTIONS:
    i, j = keys.index(first), keys.index(last)
    rows.append(f"\n### {title}\n")
    rows.append("| English | Armenian | Established by |\n|---|---|---|")
    for k in keys[i:j + 1]:
        hy, src = hy_terms.TERMS[k]
        rows.append(f"| {k} | **{hy}** | {SRC.get(src, src)} |")
TABLE = "\n".join(rows)

BODY = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "GLOSSARY-hy.template.md"), encoding="utf-8").read()
out = BODY.replace("{{TABLE}}", TABLE) \
          .replace("{{NTERMS}}", str(len(hy_terms.TERMS))) \
          .replace("{{NFIX}}", str(len(hy_terms.FIX)))
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GLOSSARY-hy.md")
open(path, "w", encoding="utf-8").write(out)
print(f"wrote {path}  ({len(hy_terms.TERMS)} terms)")
