# Textbook options for the course
Researched 2026-08-25 · for **Microelectromechanical Systems and Sensors** (2026 semester plan)

## The short answer

**No single book matches this syllabus, and this is not a failure of searching.** The
course deliberately spans three separate literatures:

| Literature | Serves | State of the art |
|---|---|---|
| **Measurement science** | Modules A, C — specs, sampling, conditioning, calibration, uncertainty | Mature. Good undergraduate textbooks exist. |
| **MEMS device physics** | Lecture 4, parts of 5–8 | Mature, but written for graduate device *designers*, not integrators. |
| **Embedded sensor integration** | Lectures 13, 15, 16 and every laboratory | **Essentially no textbook literature.** Served by vendor datasheets and application notes. |

Your own semester plan already says this, in §11: it names three different books *and*
lists "manufacturer datasheets, application notes, reference designs, errata and
evaluation-board documentation" as **primary practical sources**. The plan is right. The
question is not which book covers everything — it is which book to adopt for the spine,
and what you must write yourself.

---

## Coverage against the 16 lectures

✓✓ = strong primary source · ✓ = usable · ✗ = not covered

| # | Lecture | Morris & Langari | Fraden | ITMO (free) | Senturia / Kim |
|---|---|---|---|---|---|
| 1 | Measurement-system architecture | **✓✓** Ch1 | ✗ | ✗ | ✗ |
| 2 | Specifications & datasheet selection | **✓✓** Ch2 | ✓ | ✓ §1.3 | ✗ |
| 3 | From quantity to trustworthy samples | **✓✓** Ch6–7 | ✗ | ✗ | ✗ |
| 4 | MEMS structures, transduction, fabrication | ✓ | ✓ | **✓✓** Ch2–3 | **✓✓** |
| 5 | Accelerometers | ✓ | **✓✓** | **✓✓** §2.1 | ✓ |
| 6 | Gyroscopes and six-axis IMUs | ✗ | ✓ | ✓ §2.2 | ✓ |
| 7 | Magnetometers and orientation | ✗ | **✓✓** | ✗ | ✗ |
| 8 | Pressure, force, strain, tactile | ✓ | **✓✓** | **✓✓** §2.3 | ✓ |
| 9 | Temperature, humidity, gas | **✓✓** | **✓✓** | ✗ | ✗ |
| 10 | Optical, proximity, ToF | ✗ | ✓ | ✗ | ✗ |
| 11 | MEMS microphones, acoustic, ultrasonic | ✗ | ✓ | ✗ | ✗ |
| 12 | Analog front ends, signal conditioning | **✓✓** Ch7 | ✓ | ✗ | ✓ |
| 13 | **Digital interfaces, robust acquisition** | ✗ | ✗ | ✗ | ✗ |
| 14 | Calibration, characterisation, uncertainty | **✓✓** Ch3–5 | ✗ | ✓ | ✓ |
| 15 | **Filtering and sensor fusion** | ✗ | ✗ | ✗ | ✗ |
| 16 | **Complete system design and validation** | ✓ | ✗ | ✗ | ✓ |

**Morris & Langari covers the spine — including both pilot lectures.** Fraden covers the
sensor-family middle. Lectures 13, 15 and 16, plus every laboratory, are covered by
nothing.

---

## The candidates, assessed

### 1 · Morris & Langari, *Measurement and Instrumentation*, 3rd ed. — **recommended primary**
Elsevier, September 2020 · 736 pp · ISBN 978-0-12-817141-7

**Why it wins.** It is an *undergraduate textbook*, not a handbook: worked examples and
end-of-chapter problems, which is what students need and what Fraden lacks. Its opening
chapters are almost a chapter-for-lecture match to Module A, and chapters 3–5
(uncertainty, statistics of random error, calibration) are the best treatment of Lecture
14 available anywhere at this level. The 3rd edition expanded its MEMS and smart-sensor
coverage and added material on data acquisition.

Chapter list relevant to us: 1 Fundamentals of Measurement Systems · 2 Instrument Types
and Performance Characteristics · 3 Measurement Uncertainty · 4 Statistical Analysis of
Random Errors · 5 Calibration of Measuring Sensors and Instruments · 6 Data Acquisition
and Signal Processing · 7 Variable Conversion · 8 Measurement Signal Transmission.

**Limits.** No I²C/SPI at register level, no sensor fusion, and it is process-instrument
flavoured rather than embedded. Lectures 6, 7, 10, 11, 13, 15 need other sources.

**Before you buy: check ScienceDirect.** If ANPU holds an Elsevier subscription, this
book is likely already available to your students at no cost. That single check may
settle the whole question.

### 2 · Fraden, *Handbook of Modern Sensors*, 5th ed. — **library reference, not required**
Springer, 2015/2016 · 758 pp · ISBN 978-3-319-19302-1

Outstanding per-family physics and design coverage — the best single source for Lectures
5, 7, 8, 9. But it is a **handbook**: no exercises, no problem sets, no pedagogical
sequence, and it is expensive. Ask for one or two library copies and set specific
sections, which is exactly how the semester plan §11 already proposes using it ("use
selected sections by sensor family").

### 3 · Regtien & Dertien, *Sensors for Mechatronics*, 2nd ed. — **strong alternative**
Elsevier, May 2018 · 394 pp · ISBN 978-0-12-813810-6

Shorter, cheaper, mechatronics-oriented, with commercial-device examples. **One
structural caveat:** it is organised by *physical principle* — resistive, capacitive,
inductive/magnetic, optical, piezoelectric, acoustic — whereas your course is organised
by *measurand*. Every lecture would map to fragments of two or three chapters. Also
Elsevier, so the same ScienceDirect check applies.

### 4 · ITMO, *Микроэлектромеханические системы и датчики* — **free, and already cited**
Университет ИТМО, 2020 · 75 pp · Russian · **free PDF**

This is reference #1 in your accredited 2024 ծրագիր, and the title is an exact match. I
read it: chapters are (1) MEMS sensors and actuators and applications, (2) constructions
and operating principles of micromechanical accelerometers, gyroscopes and pressure
sensors, (3) fabrication technology, (4) analysis methods, (5) CAD/COMSOL modelling.
Each chapter ends with self-check questions.

**Verdict:** genuinely useful for Lecture 4 and the device physics of Lectures 5, 6 and
8, free, and it satisfies the accredited programme's bibliography. But it covers no
measurement science, no datasheets, no interfacing, no calibration workflow and no
fusion — it is silent on both pilot lectures. Written for a *master's* programme in
electronic-means design. Use it as a supplement, not a spine.

### 5 · Kuphaldt, *Lessons in Industrial Instrumentation* — **free and legally reusable**
Creative Commons Attribution 3.0 · very large, continuously revised

Process-industry flavoured (4–20 mA loops, transmitters), so much of it is off-target.
**But the licence is the point:** CC-BY permits copying, modification and redistribution
with attribution, so its calibration, measurement-error and signal-conditioning material
can be **excerpted directly into your own course reader** without a permissions problem.
For a cost-constrained programme that is worth a great deal.

### 6 · Senturia, *Microsystem Design* and Kim, *Fundamentals of MEMS*
Both already in the plan's or the ծրագիր's bibliography. Both are graduate device-design
texts. Set selected sections for Lecture 4 only; the fabrication-heavy chapters are
explicitly out of scope for this course.

---

## What no book will give you

1. **Register-level digital interfacing** (Lecture 13, every lab) — I²C/SPI transactions,
   register maps, reset sequences, endianness, data-ready interrupts, FIFO, bus-error
   recovery, self-test.
2. **The datasheet workflow** (Lecture 2 onward) — reading a conditions block, `typ` vs
   `max`, temperature coefficients, building an error budget, and knowing what the
   datasheet *cannot* tell you.
3. **Undergraduate-level sensor fusion** (Lecture 15) — complementary filters and the
   Kalman *concept* without the full derivation. The literature jumps from nothing
   straight to Groves-level navigation texts.
4. **Your actual kit** — the specific parts, their register maps, their quirks. No
   textbook will ever contain this, and it is a third of the laboratory content.

---

## Recommendation

**Adopt one book, borrow a second, and write the gap.**

| Role | What | Cost |
|---|---|---|
| **Required text** | Morris & Langari 3rd ed. — the spine: Lectures 1, 2, 3, 12, 14 | Check ScienceDirect access first |
| **Library reference** | Fraden 5th ed. — sensor families, selected sections | 1–2 copies |
| **Free supplement** | ITMO 2020 PDF — Lecture 4 device physics, Russian | Free |
| **Reusable source** | Kuphaldt, CC-BY — excerpt into the reader | Free |
| **Written locally** | **Course reader**, ~16 chapters — the gap above | Our work |

### Do not write a full textbook. Write the reader.

Writing a 400-page textbook to replace Morris & Langari would take a year and produce
something worse than the book that already exists. Writing a **150–180 page course
reader** that covers only what no book covers is achievable, and its marginal cost is
close to zero — because the semester plan's §10 *already requires* every lecture package
to contain "learning objectives, annotated diagrams, one commercial datasheet case, one
worked calculation, one integration-failure example, a short formative quiz, reading
list."

**That list is a book chapter.** If each lecture is developed to the plan's own standard,
the reader assembles itself.

### Proposed reader structure — one chapter per lecture, 8–12 pages

1. Learning objectives (already written)
2. The narrative core — the lecture's argument in prose, with the diagrams from the deck
3. One worked calculation, in full (already written)
4. One commercial datasheet case, with the actual pages (already selected)
5. One integration-failure example — the war story (already written)
6. **Reading bridge:** "for the underlying theory, see Morris & Langari §x.y" — so the
   reader complements the adopted book instead of duplicating it
7. Exercises with answers (partly written — the formative quizzes)

Chapters 13, 15 and 16 are the ones that must be written from scratch and carry real
value; the rest are largely assembly.

### Suggested sequence

- **Now:** check ScienceDirect access. It may make the adoption decision for you.
- **Weeks 1–2:** draft reader chapters 1 and 2 from the pilot lectures, as a sample to
  judge the format and the effort before committing.
- **Then:** one chapter per lecture, as each lecture is developed. Never a separate
  project — always a by-product.
- **End of semester:** 16 chapters, tested on a real cohort, with the misconception data
  from the exit tickets folded into the exercises. That is a far better book than one
  written in advance.

## Sources

- Morris & Langari, 3rd ed. — https://shop.elsevier.com/books/measurement-and-instrumentation/morris/978-0-12-817141-7
- Fraden, 5th ed. — https://link.springer.com/book/10.1007/978-3-319-19303-8
- Regtien & Dertien, 2nd ed. — https://shop.elsevier.com/books/sensors-for-mechatronics/regtien/978-0-12-813810-6
- ITMO textbook (free PDF) — https://books.ifmo.ru/file/pdf/2673.pdf
- Kuphaldt, *Lessons in Industrial Instrumentation* (CC-BY) — https://ibiblio.org/kuphaldt/socratic/sinst/book/liii_0v2.pdf
