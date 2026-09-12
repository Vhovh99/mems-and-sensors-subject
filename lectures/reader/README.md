# Course reader

The book that fills the gap no textbook covers. It **complements** an adopted textbook
rather than replacing it — see `../memos/textbook-options.md` for the assessment behind
that decision.

## What is here

| File | What it is |
|---|---|
| `course-reader.pdf` | **The English deliverable** — Chapters 1–4, 51 pages, A4 |
| `course-reader-hy.pdf` | **The Armenian deliverable** — Chapters 1–2 so far |
| `ch01-the-measurement-chain.md` | Chapter 1 source |
| `ch02-specifications-and-selection.md` | Chapter 2 source |
| `ch03-trustworthy-samples.md` | Chapter 3 source |
| `ch04-structures-and-fabrication.md` | Chapter 4 source |
| `ch0*-hy.md` | the Armenian chapters |
| `figures/` | Figures, cropped automatically from the lecture decks |
| `figures-hy/` | Armenian figure variants |

`course-reader-ch1-2.pdf`, `lecture-1.pdf` and `lecture-2.pdf` are earlier one-off
builds, superseded by the two PDFs above. They can be deleted.

**Chapters 3 and 4 have no Armenian version yet.** They are the next translation job, and
unlike Chapters 1 and 2 they should not need re-terminologising: they were written against
`tools/i18n/GLOSSARY-hy.md`, which is now the course's single source of truth for terms.

## Chapter template

Every chapter follows the same seven-part shape, which is deliberately identical to what
the semester plan §10 already demands of a lecture package:

1. **What you should be able to do after this chapter** — the lecture's learning outcomes, as verbs
2. **The narrative** — the lecture's argument in prose, with its diagrams
3. **One worked calculation**, in full, with the arithmetic shown
4. **One commercial datasheet case**
5. **One integration-failure example** — the war story
6. **Reading** — a bridge to the adopted textbook, so the reader never duplicates it
7. **Exercises, with full answers**

Because each lecture is developed to that standard anyway, a chapter is mostly assembly.
The exceptions are Chapters 13, 15 and 16 (digital interfaces, sensor fusion, system
validation), which no textbook covers and which must be written from scratch.

## Rebuilding

```bash
cd lectures/tools
.venv/bin/python extract_figures.py     # re-crop figures from the decks
.venv/bin/python build_reader.py        # -> course-reader.pdf AND course-reader-hy.pdf
```

`build_reader.py` splits the chapters by language: `chNN-*.md` builds the English PDF and
`chNN-*-hy.md` the Armenian one. They must not be mixed — and until September 2026 they
were, because the glob was simply `ch*.md`. The Armenian build also overrides the type to
DejaVu, since Georgia and Arial carry no Armenian glyphs.

`build_reader.py` picks up every `reader/ch*.md` in filename order, so adding
`ch03-....md` is all that is needed to extend the book. Change the output filename in
that script once more than two chapters exist.

## Conventions for authors

- **Maths is plain Unicode** between `$$ … $$` — `m ∝ L³`, `√(k / m)`, `f₀`. There is no
  TeX engine involved and none is needed. Each line inside the delimiters becomes its
  own centred line, so multi-step derivations stack.
- **Figures** live in `figures/` and are generated, not drawn by hand. Add an entry to
  the `FIGS` list in `extract_figures.py` naming the deck, the slide number and a crop
  box in inches.
- **Captions** are a paragraph beginning `**Figure 1.1** —` or `**Table 1.1** —`
  immediately after the image or table. The build script styles them automatically.
- **Every number gets verified by computation** before it goes in. The figures in these
  two chapters were all checked; keep that up, because the course's central lesson is
  that an unsourced number is not a number.
- **Representative component data** is labelled as such. Parts A, B and C are typical of
  real commercial devices but are not attributed to a named product, so the arithmetic
  can be exact without misrepresenting anybody's silicon.

## Status

Chapters 1 and 2 are a **draft for review** — the format is the thing to judge. If the
shape works, the remaining fourteen chapters are written one per lecture as each lecture
is developed, never as a separate project.
