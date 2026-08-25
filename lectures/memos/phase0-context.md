# Phase 0 — Context & Learning Outcomes
**Pilot package: Lecture 1, Lecture 2, Laboratory 1**
Course: Microelectromechanical Systems and Sensors (Միկրոէլեկտրամեխանիկական համակարգեր և տվիչներ)
Prepared: 2026-08-24 · Status: awaiting instructor confirmation

---

## 1. Teaching context

| Parameter | Value | Source |
|---|---|---|
| Institution | ANPU — Institute of Energy & Electrical Engineering, Dept. of Electrical Machines & Apparatus | Official ծրագիր 1.11.1.17 |
| Level | Bachelor, 7th semester (3rd–4th year) | Official ծրագիր |
| Programme | Electrical Engineering 071302.02.6 (Էլեկտրատեխնիկա, էլեկտրամեխանիկա, էլեկտրատեխնոլոգիաներ) | Official ծրագիր |
| Credits | 5 | Official ծրագիր |
| Contact format | 16 lectures × 80 min + 8 labs × 80 min = 32 h | Semester plan |
| Class size | 20–24 students, lab teams of 2–3 | Semester plan |
| Platform | **STM32 Nucleo** (single class-wide platform) | Instructor decision |
| Language | **English slides and notes** | Instructor decision |
| Course character | System-oriented sensor integration; fabrication confined to Lecture 4 | Semester plan §12 |

### Assumed prior knowledge
Required: circuit analysis, introductory electronics, C/C++ basics, prior microcontroller exposure.
Course prerequisites listed officially: Էլեկտրատեխնիկա, Էլեկտրոնիկա, Էլեկտրական մեքենաներ և տրանսֆորմատորներ, Էլեկտրական և էլեկտրոնային ապարատներ, Ինֆորմատիկա.

**Design consequence:** students arrive fluent in *circuits* and *machines*, not in *measurement*. They can analyse an RC network but have likely never seen a noise-density figure, a two's-complement register read, or a `typ`/`max` column. Lecture 2 is therefore genuinely new material, not revision — budget accordingly.

---

## 2. Two source documents disagree — resolution needed

| | Official 2024 ծրագիր (accredited) | New semester plan (24 Aug 2026) |
|---|---|---|
| Spine | Microcontrollers + digital logic (triggers, decoders, multiplexers, counters) | Commercial sensor families + integration |
| Sensors | Theme 1 only (6 subtopics) | Modules A–D, 11 of 16 lectures |
| Labs | 10 × Multisim + STM32 | 8 × sensor bring-up/characterisation |
| Digital logic | Theme 4, seven lectures (RS/D/JK/T flip-flops, dividers, clock generators) | **Absent** |
| Fabrication | Absent | Lecture 4 only |

**Working assumption (per your instruction):** design to the **new semester plan**.

**Flag for your decision, not blocking this pilot:** the accredited ծրագիր's Theme 4 (digital logic and trigger circuits, ~7 lectures) has no home in the new plan, and the new plan's calibration/uncertainty/fusion content has no home in the accredited one. If ANPU audits against the accredited document, the new plan needs either a formal ծրագիր revision or an explicit mapping annex. Lectures 1, 2 and Lab 1 are safe either way — they map onto the official Theme 1.1–1.3 and Լ1.

---

## 3. Learning outcomes

Written to be *observable in the room or in the submission*. Each maps to the semester plan's CLOs.

### Lecture 1 — MEMS, sensors, and the measurement-system architecture

| # | By the end of this lecture, a student can… | CLO | Evidence |
|---|---|---|---|
| **L1.1** | **Draw** the signal path of a measurement system from physical measurand to logged, timestamped value in SI units, labelling every stage where information can be lost | 1, 5 | Sketch-on-paper activity (min 22); exit ticket |
| **L1.2** | **Classify** an unfamiliar device as sensor, transducer, or actuator, and name its measurand and transduction mechanism | 1 | ConcepTest poll (min 20); 4 rapid classifications |
| **L1.3** | **Predict**, using scaling arguments (m ∝ L³, k ∝ L, f₀ ∝ 1/L, A/V ∝ 1/L), why MEMS devices are fast and sensitive — and name one property that gets *worse* at micro scale | 1, 3 | ConcepTest poll (min 40) — the hardest concept |
| **L1.4** | **Convert** a vague application request ("detect if the machine is vibrating too much") into a measurement specification: quantity, range, resolution, bandwidth, environment | 2, 8 | Requirement→spec worksheet (min 55); becomes semester-project deliverable 1 |

**Not an outcome of L1:** computing anything numerically from a datasheet — that is L2. L1 buys the vocabulary and the map.

### Lecture 2 — Sensor specifications and datasheet-based selection

| # | By the end of this lecture, a student can… | CLO | Evidence |
|---|---|---|---|
| **L2.1** | **Distinguish** accuracy from precision, resolution from sensitivity, and repeatability from drift, and state which of a given list are static vs dynamic characteristics | 2 | ConcepTest poll (min 18) — targets the #1 misconception |
| **L2.2** | **Locate** a required number in a real datasheet, read its test conditions (supply, temperature, `typ` vs `max`), and state one performance limit the datasheet does **not** specify | 2 | Guided datasheet hunt (min 30) on LSM6DSO32 / BMP390 |
| **L2.3** | **Compute** noise-limited resolution from noise density and bandwidth (µg/√Hz → mg RMS), compare it against LSB/quantisation, and identify which dominates | 2, 5 | Worked calculation (min 48), then one solo variant |
| **L2.4** | **Select** between three candidate devices against a stated requirement using an explicit criteria table, and **defend** the choice on accuracy-over-temperature, power, and cost — not on `typ` sensitivity alone | 2, 8 | Team decision table (min 58); transfer poll (min 68) |

### Laboratory 1 (Week 2) — Datasheet-to-data bring-up

| # | A student can… | CLO | Evidence |
|---|---|---|---|
| **Lab1.1** | Verify supply and logic-level compatibility from the datasheet **before** applying power, and state the consequence of getting it wrong | 3, 4 | Pre-lab check-off (gate: no power until signed) |
| **Lab1.2** | Wire one I²C sensor to an STM32 Nucleo with correct pull-ups and grounding, and confirm device identity via `WHO_AM_I` | 4 | Live read of the ID register at the bench |
| **Lab1.3** | Configure one operating mode (full-scale range + ODR) by register write, and justify both choices against the intended measurement | 4 | Register/configuration table in submission |
| **Lab1.4** | Convert raw two's-complement codes to SI units using datasheet sensitivity, and verify plausibility with a known physical reference (1 g rest test / room temperature) | 5 | Data log showing ≈9.81 m/s² on one axis |
| **Lab1.5** | Produce an annotated connection diagram, documented initialisation sequence, and short labelled data log | 8 | Check-off + submission against rubric |

---

## 4. Prerequisite-ordering risk found in the plan

Lab 1 (Week 2) requires I²C bring-up, register maps, and raw-code conversion. But:
- Lecture 3 (Week 3) is where "I²C/SPI overview, raw codes, units, timestamps" is first taught.
- Lecture 13 (Week 13) is where digital-bus detail properly lands.

So Lab 1 runs **one week before** its own theory. The plan half-anticipates this ("80 minutes is sufficient only when wiring diagrams, starter firmware, required reading and pre-lab calculations are completed before class").

**Mitigation as built** *(revised after instructor review, 2026-08-25)*:
1. Lecture 1 closes with a "what Lab 1 will ask of you" segment — the data path, the device-ID handshake, and where the pre-lab sheet lives. Costs ~5 min of L1, saves 30 min of bench confusion.
2. **Lab 1 requires no programming at all.** Boards are pre-flashed with a register console; students type register addresses and values they took from the datasheet, and convert raw codes to SI units by hand. This uses the plan's own provision for a *"known-good binary or test script"* (§10).
3. Pre-lab sheet carries a one-page I²C primer and the console command reference as required reading — assessed by the pre-lab gate.

Lab 1 stays in Week 2 (instructor decision).

### Second prerequisite gap, found on review

The plan lists *"prior microcontroller experience"* as entry background (§3) but no session teaches it, while Lab 8 requires students to submit **source files** (§6). This cohort does not have that background — so the plan assumes a skill on the way in, never builds it, and then assesses it on the way out.

A staged on-ramp across Labs 1–8, and the three realistic options for closing the gap, are in `instructor-guide.md` §9. Note that the accredited 2024 ծրագիր taught these skills *inside* the course (Լ4–Լ10: LED control, PWM, USART, SPI, motors); the 2026 plan dropped those labs without relocating the prerequisite.

---

## 5. Anticipated student misconceptions (these drive the ConcepTest distractors)

| # | Misconception | Where it dies |
|---|---|---|
| M1 | "More decimal places / more bits = more accurate" — resolution confused with accuracy | L2 poll 1; L2.3 calculation |
| M2 | "MEMS means it was made in a cleanroom, so this is a fabrication course" | L1 hook + framing |
| M3 | "Smaller is uniformly better" — no intuition that stiction, thermal noise, and drift worsen at micro scale | L1 poll 2 (L1.3) |
| M4 | "A sensor outputs the physical quantity" — no model of code → units → calibration | L1.1 sketch; Lab 1.4 |
| M5 | "`typ` is what I'll get" — reads typical column, ignores min/max and temperature coefficient | L2 datasheet hunt |
| M6 | "If an Arduino library exists, the part is fine" — explicitly warned against in the plan's selection rule | L2.4 decision table |
| M7 | "Sampling faster is always better" — no ODR-vs-bandwidth-vs-noise trade-off | L2.3; Lab 2 |

---

## 6. Evidence plan (how we know the pilot worked)

**In-lecture (formative):** 5 polls per lecture, target 30–70 % first-vote correct on ConcepTests. Record first-vote and post-discussion percentages — that delta is the peer-instruction evidence.

**Exit tickets:** L1 — one-sentence spec for a stated application. L2 — one computed resolution figure plus the device chosen and why.

**Lab 1 (summative, low weight):** check-off gate + submission rubric on the five Lab1.x outcomes.

**Pilot-timing verification** (the plan's actual step-3 goal): instructor logs real clock time at four marks per lecture (end of hook, end of chunk 1, end of chunk 2, start of synthesis). Compare against the designed timeline in Phase 1. This is the data that tells you whether Lectures 3–16 can be built on the same template.

**CLO coverage check:** this pilot touches CLO1, 2, 3, 4, 5, 8. CLO6 (calibration/uncertainty) and CLO7 (fusion) are untouched — correct at this stage; they belong to Lectures 14–15 and Labs 3–5.
