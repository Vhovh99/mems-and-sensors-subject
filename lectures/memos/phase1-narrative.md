# Phase 1 — Content Audit & Narrative Design
Pilot: Lecture 1, Lecture 2, Laboratory 1 · Status: awaiting instructor review

Design target: the 2026 semester plan only. First offering of the course — no prior-year
student data, so misconceptions below are *predicted* from the measurement-education
literature and instrumented for capture (see §5).

---

## LECTURE 1 — MEMS, sensors, and the measurement-system architecture

### 1.1 Content audit

The plan assigns Lecture 1 seven items: course goals; sensors vs transducers vs actuators;
MEMS definition and scaling intuition; sensor-system block diagram; application survey;
requirements-to-measurement workflow; semester-project introduction. That is more than
80 minutes will hold at teaching depth. Audit:

**ESSENTIAL — expert modelling required (~62 min)**
| Content | Why it survives | Time |
|---|---|---|
| The measurement chain, stage by stage | This block diagram is the spine of all 16 lectures. Every later lecture is one box in it. Must be built live, not shown finished. | 18 min |
| Scaling laws and their consequences | The only piece of physics in L1, and the one that makes MEMS *different* from the machines these students already know | 15 min |
| Requirements → specification workflow | The course's stated design principle; the skill students are assessed on all semester | 16 min |
| Sensor / transducer / actuator | Cheap to teach, needed for precise speech from here on | 4 min |
| Semester project brief | Frames every lab; must land while attention is fresh, not in the last 2 min | 5 min |
| Lab 1 bridge (theory-order mitigation) | Lab 1 precedes its theory — agreed mitigation | 4 min |

**HELPFUL — compress hard (~8 min)**
- *Application survey.* Do **not** run a 20-slide device tour. Four images, all tied to the
  hook's motor: phone IMU, automotive airbag, industrial vibration node, tyre-pressure sensor.
- *MEMS definition and dimensional scale.* One slide, one comparison object (human hair, 70 µm).
- *One sentence of history:* piezoresistive pressure sensing (1960s) → the airbag accelerometer
  as the first mass-market MEMS. Motivates "commercial device", nothing more.

**DECORATIVE — eliminate**
- History timelines and market-size charts — zero contribution to any L1 outcome.
- Exhaustive MEMS taxonomy trees — the plan spends Lectures 5–11 on families; pre-empting them
  here just loads working memory with labels students cannot yet attach to mechanisms.
- Cleanroom and fab-process photographs — actively harmful in L1: they reinforce misconception
  M2 ("this is a fabrication course"), which the plan explicitly designs against. Fabrication
  is Lecture 4's job.
- Full derivation of the spring-mass transfer function — Lecture 5.

### 1.2 Narrative arc (ABT)

> **AND** — You already know circuits and you know electrical machines. Sensing looks like the
> easy part: pick the part, read the number, act on it. Every datasheet number is published;
> nothing is hidden.
>
> **BUT** — A monitoring system built from parts that all met their specifications watched a
> motor destroy itself and reported that everything was fine. No component failed. The sensor
> was not the measurement. And at micro scale, the mechanical intuition you earned on machines
> quietly stops applying.
>
> **THEREFORE** — What you engineer in this course is not a sensor. It is a *path*: measurand →
> transduction → conditioning → digitisation → codes → units → timestamp → decision, specified
> before anything is purchased, and trustworthy at every stage. That path is this lecture's
> block diagram and this semester's syllabus.

### 1.3 The hook (first 90 seconds) — "The motor that died under observation"

Deliberately set in the students' own department (Electrical Machines & Apparatus): a bearing-
fault vibration monitor on an induction motor. The screen showed a calm, slowly-rising 20 Hz
vibration line for weeks. Then the bearing seized and the motor was destroyed.

Post-mortem: the accelerometer met every datasheet number. The board worked. The firmware had
no bug. The logger logged. **Baseline poll (Poll 1): whose fault was it?**

Resolution withheld until min 72: the bearing-fault signature sat at 1520 Hz, the sampling
rate was 100 Hz with no anti-alias filter, and the fault energy aliased to
|1520 − 15×100| = **exactly 20 Hz** — a benign-looking line read as normal load variation
(the shaft itself turns at 1500 rpm = 25 Hz, so 20 Hz looked entirely plausible). The measurement chain was never designed as a chain —
so nobody owned the sampling decision.

Why this hook works: it is a *mystery with a guilty party*, it is set in machines they already
respect, it makes "the sensor is not the measurement" undeniable in 90 seconds, and it seeds
three later lectures (L2 bandwidth, L3 aliasing, L16 validation) plus Lab 2. It also gives the
lecture a genuine ending rather than a summary slide.

### 1.4 Chunk map — 4 chunks, state change every ≤18 min

| Time | Chunk | Content | State change |
|---|---|---|---|
| 00–08 | **Hook** | Motor mystery + Poll 1 (baseline, no right answer revealed) + one-slide course frame | Poll |
| 08–26 | **C1 — The chain** | Sensor/transducer/actuator (4 min), then build the measurement chain live, one box at a time, asking at each box: *what information can die here?* Concrete numbers on every arrow: 0.9 mg → 3.7 mV → code 1204 → 8.8 mg → 0.50° | Poll 2 (ConcepTest, min 24) |
| 26–44 | **C2 — Why micro is different** | Isotropic scaling: m ∝ L³, k ∝ L, f₀ = √(k/m) ∝ 1/L, A/V ∝ 1/L. Consequences derived, not asserted: kHz–MHz resonances → high bandwidth; µg-scale proof mass → fF capacitance changes → thermomechanical noise ∝ 1/m gets *worse*; surface forces beat body forces → stiction. Land on: **smaller is not uniformly better.** | Poll 3 (hardest, min 40) + sketch |
| 44–48 | **Break** | Non-digital: stand, then 60 s pair-sketch of the chain from memory, slides blank | Retrieval sketch |
| 48–66 | **C3 — Requirements → spec** | Live conversion of "tell me if the motor is vibrating too much" into a specification: quantity, range, bandwidth, resolution, environment, output, rate. Then students do a second one in pairs. Semester project brief handed out here. | Poll 4 (transfer, min 62) |
| 66–74 | **Synthesis** | Return to the motor. Students locate the failure on their own chain diagram before the answer is shown. Reveal aliasing. Name the missing specification line. | Whole-class vote |
| 74–80 | **Close** | Exit ticket (Poll 5, muddiest point + one spec line) · Lab 1 bridge: the data path, the `WHO_AM_I` handshake, where the pre-lab sheet is, and the check-off gate | Exit ticket |

Attention resets: min 8, 24, 40, 44, 62, 74 — longest passive stretch 16 min.

---

## LECTURE 2 — Sensor specifications and datasheet-based selection

### 2.1 Content audit

**ESSENTIAL (~64 min)**
| Content | Why it survives | Time |
|---|---|---|
| Accuracy vs precision vs resolution | Misconception M1 is the single most damaging error in this course; everything downstream (Lab 1, Lab 3, L14) breaks if it survives | 12 min |
| Reading conditions: `typ` / `min` / `max`, supply, temperature, test setup | The datasheet-literacy skill the plan requires from L2 onward | 14 min |
| Offset, drift, temperature coefficient — and why they usually dominate | This is where real selections are won and lost | 12 min |
| Noise density → RMS resolution over bandwidth (√Hz arithmetic) | The one calculation students must own; used in Labs 2, 3, 5, 6 | 14 min |
| Selection against a specification: criteria table + defence | CLO2's assessed behaviour | 12 min |

**HELPFUL — name and move on, one line each (~7 min)**
Hysteresis · threshold · cross-axis sensitivity · linearity (%FS vs %reading — one slide, since
the two conventions differ by an order of magnitude at low readings) · response time vs bandwidth.
These get defined and indexed so students recognise them in a datasheet; they get *developed*
later, where they matter (L14 for hysteresis/repeatability, L5 for cross-axis).

**DECORATIVE — eliminate**
- Formal uncertainty framework (GUM, coverage factors, type A/B) — this is Lecture 14's core.
  Introducing it here duplicates and dilutes both lectures.
- Probability-distribution derivations behind RMS and σ.
- Section-by-section reading of a complete 80-page datasheet — the plan wants *targeted*
  extraction, not exhaustive reading. Students hunt for named numbers.
- Vendor-catalogue comparison of many parts. Three candidates is enough to teach the method;
  more is decoration.

### 2.2 Narrative arc (ABT)

> **AND** — Last lecture you learned to write a specification. Thousands of parts exist, every
> number is published, and the datasheets are free. Selection looks like a table lookup.
>
> **BUT** — The datasheet is a legal document, not a promise. The 16-bit part with 0.061 mg
> resolution is the *wrong* choice for measuring 0.5° of tilt — because its untrimmed zero-g
> offset is 40 mg, roughly five times the entire quantity you are trying to measure. The number
> that decides the design is rarely the number on the front page, and sometimes it is not
> printed at all.
>
> **THEREFORE** — Selection is a calculation against your specification: build an error budget
> from the terms that actually dominate, at the temperature and bandwidth you will actually run,
> and choose on the total — not on the headline.

### 2.3 The hook (first 2 minutes) — "Two front pages"

Two real accelerometer front pages, side by side, nothing else on the slide.

- **Part A** — 16-bit, ±2 g, sensitivity 0.061 mg/LSB, "high-resolution", low-noise marketing line
- **Part B** — 14-bit, ±4 g, sensitivity 0.488 mg/LSB, unremarkable front page

Task: *You must measure the tilt of a solar-tracker frame to 0.5°. Which part?* **Poll 1.**
The expected majority answer is A (more bits, finer resolution — misconception M1 + M5).

Resolution at min 70, after the students themselves compute it: 0.5° of tilt is
sin(0.5°) = 8.73 mg of signal. Part A's zero-g offset is ±40 mg with ±0.5 mg/°C drift; Part B's
is ±10 mg with ±0.1 mg/°C. Calibrated at 20 °C and used over 0–40 °C (ΔT = ±20 °C), Part A's
drift term alone is ±10 mg — **0.574° of apparent tilt, which exceeds the entire ±0.5°
requirement**. Part B's is ±2 mg, or 0.115°. Full RSS budgets: **Part A 10.02 mg = 0.574°
(FAILS); Part B 2.13 mg = 0.122° (passes with 4× margin).**
Part A resolves 8× finer than Part B and still cannot do the job — and Part B's 0.488 mg/LSB
already resolves 0.028° of tilt, eighteen times finer than required, so resolution was never
the deciding variable. **You cannot calibrate away what drifts, and resolution is not
accuracy.** All figures verified; see `lecture-02/output/activities.md`.

### 2.4 Chunk map

| Time | Chunk | Content | State change |
|---|---|---|---|
| 00–10 | **Hook** | Two front pages + Poll 1 (vote recorded, answer withheld) · 3-min retrieval of L1's chain: "which box are we in today?" | Poll + retrieval |
| 10–28 | **C1 — The vocabulary that gets confused** | Accuracy vs precision vs resolution on one target diagram, then the static set (range, sensitivity, offset, linearity, hysteresis, repeatability, threshold) and the dynamic set (bandwidth, response time, ODR, noise density) — each anchored on one accelerometer axis, not defined in the abstract | Poll 2 (ConcepTest, min 24) |
| 28–46 | **C2 — What the datasheet actually says** | The conditions block first, headline numbers second. `typ` vs `min`/`max` (and parts that specify only `typ`). Temperature coefficients. Then a **guided hunt in pairs**: six named numbers to find in a real datasheet, plus one question that has no answer in the document — and students must say so | Pair hunt (8 min) |
| 46–50 | **Break** | Stand; hands-up survey of which number was hardest to find and why | Physical + discussion |
| 50–70 | **C3 — The calculation and the choice** | Error-budget arithmetic: noise density × √BW; quantisation LSB/√12; offset TC × ΔT; RSS combination of independent terms. Worked live on the solar tracker. Then teams complete a 3-candidate criteria table and commit to a choice with one sentence of defence | Poll 3 (min 56) + team table |
| 70–76 | **Synthesis** | Reveal the hook. Then the plan's own selection rule as the lecture's closing rule: *never choose a part because a library exists for it* | Whole-class |
| 76–80 | **Close** | Exit ticket (Poll 4: one computed figure + muddiest point) · pre-lab pointer for Lab 1 | Exit ticket |

Attention resets: min 10, 24, 36, 46, 56, 70 — longest passive stretch 14 min.

---

## LABORATORY 1 (Week 2) — Datasheet-to-data bring-up

Not an ABT narrative — a gated procedure with two provable claims:

> **Claim 1: "the device is alive and it is the device I think it is."** Proven by `WHO_AM_I`.
> **Claim 2: "the number on my screen is true."** Proven against gravity — one axis must read
> ≈ 9.81 m/s² at rest, and ≈ 0 when rotated. Nothing else in the lab counts until both hold.

Structure (per the plan's 80-min lab rhythm, with the agreed mitigation):
- **Gate, 0–10 min.** Pre-lab check-off. Supply and logic levels stated from the datasheet in
  the student's own handwriting, *before* power is applied. No signature, no power.
- **10–30.** Wire I²C with pull-ups and grounding; `scan` the bus; read the device-ID
  register; diagnose the deliberate failure modes (swapped SDA/SCL, wrong address, missing
  pull-up) — these are taught, not accidents.
- **30–50.** Configure full-scale range and ODR by register write; each choice justified in the
  configuration table against the intended measurement.
- **50–70.** Read raw two's-complement data; convert to SI with the datasheet sensitivity;
  run the 1 g plausibility test; log.
- **70–80.** Check-off, submission, and one closing question: *which stage of Lecture 1's chain
  did you just build?*

**No student programming** *(revised 2026-08-25)*: boards are pre-flashed with a register
console, so students type register addresses and values from the datasheet and convert
raw codes to SI units by hand. Firmware authoring is staged across Labs 2–7 — see
`instructor-guide.md` §9. Pre-lab sheet carries the one-page I²C primer and the console
reference as required, gated reading.

---

## 5. First-offering instrumentation

No prior-year misconception data exists, so the pilot must generate it:

1. **Record both votes** on every ConcepTest — first vote and post-discussion vote. The delta
   is the evidence that peer instruction is working; the distractor that keeps attracting votes
   *after* discussion is next year's redesign target.
2. **Keep the exit tickets.** The muddiest-point half, transcribed into one list per lecture, is
   the raw material for the plan's §10 "common misconceptions" review data.
3. **Log real clock time at six marks per lecture** (end of hook, end of C1, end of C2, end of
   break, end of C3, start of close). This is the plan's actual step-3 deliverable: verified
   80-minute timing. If C2 runs long in both lectures, the template is wrong, not the lecture —
   and Lectures 3–16 get built on the corrected version.
4. **Log Lab 1 wall-clock per gate** and the number of teams that fail `WHO_AM_I` on first
   attempt. That single number tells you whether the pre-lab is doing its job.
