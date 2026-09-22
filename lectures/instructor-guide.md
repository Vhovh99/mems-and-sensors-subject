# Instructor guide — Module A
**Lecture 1 · Lecture 2 · Lecture 3 · Lecture 4 · Laboratory 1**
Microelectromechanical Systems and Sensors · first offering

Module A of the semester plan is now complete: four lectures and the first laboratory.
Lectures 1–2 and Laboratory 1 were the pilot; Lectures 3–4 were built afterwards, to the
same standard and against the terminology the pilot's Armenian review established.

This is the delivery document. Read it once end to end before Lecture 1, then keep it
open at the lectern for the timing cues and the contingency table.

---

## 1 · What this pilot is for

The semester plan's own production sequence puts this package at step 3: *"Develop
Lecture 1, Lecture 2 and Laboratory 1 as a pilot package and verify the 80-minute
timing."*

So the pilot has **two jobs**, and the second one is easy to forget:

1. Teach three sessions well.
2. **Produce the evidence that decides whether Lectures 3–16 can be built on this
   template.** If the timing does not hold, the fix belongs in the template, not in
   next week's improvisation.

Because this is a first offering there is no prior-year data. Every misconception in
these documents is *predicted* from the measurement-education literature, not observed
in your students. The instrumentation in section 6 is how that changes.

---

## 2 · The narrative spines

Each session has one idea. If you remember nothing else at the lectern, protect these.

| Session | The one thing | Where it resolves |
|---|---|---|
| **Lecture 1** | A measurement is a *chain*, and it begins before the sensor. Some losses are permanent. | Minute 70: the motor's 1520 Hz fault aliased to exactly 20 Hz by a 100 Hz sample rate |
| **Lecture 2** | Selection is arithmetic against a requirement, not a comparison of headlines. | Minute 66: Part A resolves 8× finer and fails, because a 10 mg drift term beats an 8.73 mg measurand — then minute 106 lands it on the real ISM330DHCX, which passes at `typ` and fails at `max` |
| **Lecture 3** | A sample is trustworthy only if you can say what it is, how much is information, which band it represents, and when it happened. | Minute 66: the 16-bit part gives you 12.4 bits — and the 300 Hz pump is sitting in your data at 12 Hz |
| **Lecture 4** | A datasheet describes a die. You buy an assembly. | Minute 70: Lecture 2's unanswerable cross-axis question gets a method — measure the last three links yourself |
| **Laboratory 1** | Two claims: *this is the device I think it is*, and *this number is true*. | The `WHO_AM_I` handshake and the 1 g test |

Both lectures are built as mysteries with withheld answers. **The single most damaging
delivery error is revealing early.** If you resolve the hook at minute 20, the remaining
hour has no destination.

---

## 3 · Delivery notes that matter more than the slides

**Do not open Lecture 1 with administration.** The syllabus, assessment and logistics
come at minute 74. The first 90 seconds are the most valuable of the semester.

**Voting is by hands, then voices.** There is no polling tool and none is needed. The
question stays projected; the room votes by **simultaneous show of hands on a count**
— "hands up for A on my count, three, two, one", then B, C, D, E — and only after the
count do you take two or three spoken answers. Full protocol in
`lecture-01/output/activities.md` §"The voting protocol".

**The one rule: hands before voices.** If a confident student calls out the answer
before the count, the room anchors on it and that poll's data is gone. Cut it off early
and kindly, every time; the class learns the rhythm in about two lectures. This costs
forty seconds per poll and protects the entire exercise.

**This is not a downgrade from clickers.** A show of hands gives you the distribution
*and* the reasoning in the students' own words while the misconception is still live —
which a clicker never could. For a first offering, that commentary is worth more than
the numbers.

**Run peer instruction properly, or do not claim to.** Silent committed vote → *"find
someone who voted differently"* → 90 seconds → re-vote → **announce both percentages
aloud.** Skipping the individual commitment removes the mechanism; skipping the re-vote
removes the evidence. Students who hear "forty per cent, then seventy-five" learn that
the discussion did something.

**Never react to a baseline poll.** No hint, no eyebrow, no "interesting". Say "hold
that thought" and move.

**Write on the physical board and leave it there.** Lecture 1: `k ∝ L¹` and `m ∝ L³`.
Lecture 2: `8.73 mg`. You will point at both repeatedly.

**Blank the screen for the Lecture 1 sketch activity** (press `B` in most presenters).
Unaided recall is the entire mechanism; with the diagram visible it becomes copying.

**Open Lecture 2 with last week's muddiest points.** Slide 2 is a template you must
fill in. Refer to concepts, never to students. Ninety seconds. This does more for
credibility than anything else in the first month — and if you genuinely got no usable
tickets, delete the slide rather than performing a hollow version of it.

**Be honest that this is a first offering.** Both exit-ticket slides say so. Students
give far better diagnostic data when they believe it will be used, and you will be
telling the truth.

---

## 4 · Contingency table

Keep this visible. The rule underneath all of it: **protect the resolution of the
hook.** A lecture that runs out of time before its own ending has taught less than one
that dropped a middle exercise.

### Lecture 1

| Situation | Action |
|---|---|
| A student calls out an answer before the count | "Hands first, reasons after." Re-run the count. An anchored room yields no usable first vote. |
| The room will not raise hands at all (week-1 reticence) | First vote of Lecture 1 only: "eyes closed, hands up for A." Feels theatrical, works, and is almost never needed twice. |
| Projector fails during a poll | Read the stem and the options aloud, twice, and vote on hands as normal. All poll stems are short enough to speak. |
| 6 min late at minute 45 | Cut the pair-sketch to 45 s; drop the second specification exercise (slide 33) to homework. |
| 12 min late | Also move the project brief (slide 36) to a handout and Lecture 2's opening. **Protect:** chain diagram, scaling poll, aliasing reveal, Lab 1 bridge. |
| Poll 3 collapses (<20 % after re-vote) | Stop. Derive `f₀ ∝ 1/L` in three lines on the board. Vote a third time. This concept is load-bearing for Lectures 5, 6 and 11 — four extra minutes is a good trade. |
| Ahead of schedule | Live phone teardown: "name every sensor in the phone in your pocket, and its measurand." |
| Projector fails entirely | The lecture survives on a whiteboard: seven boxes, two exponents, three numbers (1520 / 100 / none). Everything else is commentary. |

### Lecture 2

| Situation | Action |
|---|---|
| No printed datasheets or laptops | Project one page; run the hunt as a whole class, calling on pairs per item. Loses independence, keeps the skill. |
| 8 min late at minute 57 | Drop Part C from the decision table (two candidates, 5 min); set the third as homework. **Never cut Poll 3 or the reveal** — the arithmetic *is* the lecture. |
| 15 min late | Drop the decision table entirely; do the reveal from the front with the class calling out terms. |
| Poll 3 collapses (<25 %) | Write `µg/√Hz × √Hz = µg` on the board with units in full. Unit cancellation is almost always the actual blocker, not the sensing. Re-vote. |
| Ahead of schedule | Hand out a second manufacturer's datasheet for the same measurand: "these two claim the same accuracy — under the same conditions?" (They will not be.) |

### Laboratory 1

| Situation | Action |
|---|---|
| Team arrives without a signed pre-lab | They do not power their board. Give them a datasheet and let them complete it at the bench. Finishing late is the intended consequence — **do not waive the gate**, it is what stands between a 1.8 V I/O part and a 5 V rail. |
| >40 % of teams cannot read the device ID by minute 30 | Stop the room. Demonstrate `scan` and the pull-up voltage check on the projector, once, for everybody. Then continue. |
| A board was not flashed, or lost its firmware | Keep two spare flashed boards and the `.bin` on a USB stick. Reflashing is drag-and-drop onto the ST-LINK drive, about 30 seconds. |
| A sensor dies | Spares are on the bench. Log it in the hardware-failure record — the semester plan asks for that data. |
| Running out of time at minute 70 | Drop check-off question 3, never question 4 (predict the axis before turning). Question 4 is the one that distinguishes understanding from transcription. |
| A team finishes early | Ask them to measure the same axis at ±2 g and ±16 g and explain the raw-code difference; then to estimate their zero-g offset. Note what you gave them — it is a candidate task for next year. |

---

## 5 · The three moments most likely to go wrong

**Lecture 1, the aliasing reveal (minute 70).** The diagram is drawn at 19 cycles per
20 samples so the mechanism is *visible*; the motor's real ratio was 1520:100. Say that
out loud — a sharp student will otherwise notice the ratios differ and conclude you are
hand-waving. Then walk the sum: `15 × 100 = 1500`, `1520 − 1500 = 20`. Then the detail
that explains why nobody caught it: **the shaft turns at 1500 rpm = 25 Hz, so a 20 Hz
line looked entirely plausible.** The wrong answer was believable. That is the lesson.

**Lecture 2, the drift column (minute 57).** Resist explaining all three error terms at
equal weight. Quantisation and offset are set-up; **drift is the point.** Land it as a
single sentence — "the error is larger than the thing being measured, and it appears
after you calibrated" — then ask which of the three columns the front page mentioned.
(None.)

**Laboratory 1, the range-encoding trap.** Several sensor families encode full-scale
range in a non-ascending order, so a student who extrapolates gets a magnitude wrong by
a factor of 2, 4 or 8 — stable, repeatable, and completely wrong. **Do not warn them
beyond what the handout says.** Let it happen, then ask: *"Your reading is stable to a
tenth of a milli-g. Is it right?"* That is worth more than any slide.

---

## 6 · Instrumentation — what to record

This is the pilot's actual deliverable. Four small tables; ten minutes of work per
session.

**A · Poll data.** For Lecture 1 Polls 2, 3, 4 and Lecture 2 Polls 2, 3, 4: first-vote
and post-discussion distribution *across all options*, not just the correct percentage.
A distractor that keeps its share **after** discussion is next year's redesign target.

**B · Timing.** Actual clock time at six marks per lecture (end of hook, end of C1, end
of C2, end of break, end of C3, start of synthesis). Compare against the authoritative
timelines in each `lecture-plan.md`. **If a chunk over-runs in both lectures, the
template is wrong** — fix it before building Lectures 3–16, which is precisely what
this pilot exists to find out.

**C · Muddiest points.** Transcribe every exit ticket into one list per lecture. This is
your misconception inventory, and it is the only source of the semester plan's required
"common misconceptions" review data.

**D · Laboratory metrics.** The four counts at the foot of `lab-01/rubric.md`: pre-lab
completion, teams reading the ID by minute 30, teams struggling with two's complement,
teams hit by the range-encoding trap.

### Decision rules for after the pilot

| Observation | What it means | Action before Lecture 3 |
|---|---|---|
| C2 over-ran in both lectures | 18-minute chunks are too long for this cohort | Redesign the template to 3 chunks of 14 min with an extra state change |
| Poll 3 (L1) above 70 % first vote | Scaling was taught too explicitly | Compress C2; move the freed time to the specification exercise |
| Poll 3 (L2) distractor C dominant | ODR/bandwidth confusion is systemic | Open Lecture 3 with it; it is Lecture 3's core material anyway |
| Poll 4 (L2) options C or D above 25 % | "Calibration fixes everything" survived | Add an explicit hit in Lecture 14; flag for Lab 3 |
| <70 % arrived with a complete pre-lab | Pre-lab too long, or not signposted | Shorten section B to 8 rows; announce the gate again in Lecture 2 |
| Exit-ticket Q1 (L2) below 60 % correct | The noise calculation did not land individually | Re-teach in Lecture 3 with units in full; it is needed for Labs 2, 3, 5, 6 |

---

## 7 · Two open items for your decision

**7.1 · The accredited programme.** The 2024 ծրագիր (1.11.1.17) and the 2026 semester
plan describe different courses. The accredited document is spined on microcontrollers
and digital logic — Theme 4 alone is seven lectures of flip-flops, decoders,
multiplexers and counters — and contains none of the plan's calibration, uncertainty or
fusion content. The plan contains none of Theme 4.

Lectures 1–2 and Lab 1 are audit-safe either way: they map onto official Theme 1.1–1.3
and Լ1. **Before building Lectures 5–16, decide whether the ծրագիր will be formally
revised or an explicit mapping annex produced.** This is a paperwork problem, not a
teaching problem, but it is easier to solve in September than in June.

**7.2 · ~~Verify the Lab 1 answer key~~ — done. Now flash the boards.** The IMU is the
**ST ISM330DHCXTR**, and `lab-01/instructor-notes.md` now carries a fully verified answer
key read from datasheet **DS13012 Rev 6**: register addresses, the `CTRL1_XL` bit layout,
the (non-ascending) full-scale encoding, ODR codes, sensitivities, and the electrical
figures Lecture 2 uses. All arithmetic was checked by computation.

Two small things remain yours:
1. **Confirm the datasheet revision** you hand to students is DS13012 Rev 6.
2. **Confirm the I²C address on your specific breakout** — it depends on how the board
   straps SDO/SA0, and vendors differ. `scan` settles it at the bench in two seconds,
   which is why handout stage 1.4 runs it first.

Then build `lab-01/console-firmware/` once and flash every board. This is on the critical
path for Lab 1 and wants doing a day early, not on the morning.

---

## 8 · Rebuilding the slides

The decks are generated, so edits can be made either way:

- **Small edits** — wording, a number, a colour: open the `.pptx` and edit directly.
  Every diagram is native PowerPoint shapes, so boxes and arrows stay editable.
- **Structural edits** — reordering, new slides, restyling the whole deck: edit
  `tools/build_l1.py` / `build_l2.py` and regenerate:

```bash
cd lectures/tools
.venv/bin/python build_l1.py          # -> lecture-01/output/*.pptx
.venv/bin/python build_l2.py          # -> lecture-02/output/*.pptx
.venv/bin/python grid.py ../lecture-01/output/L1-*.pptx l1 4    # thumbnail sheets
```

`tools/deck.py` holds the palette, type scale and slide furniture — change it there and
both decks follow. The semantic colour rule is worth keeping: **teal = the true signal
path, amber = where error enters, red = the term that kills the design.**


---

## 9 · Teaching in Armenian

All four decks exist in Armenian as `L*-HY.pptx` alongside the English originals. Slide
text is translated; **speaker notes remain in English**, since they are your working
notes rather than student material.

### What changed in September 2026, and why it matters to you

Between 25 August and 8 September you corrected the L1 and L2 Armenian decks **by hand,
inside the `.pptx` files** — about 350 paragraphs. None of that was in the dictionaries,
so the next `translate_deck.py` run would have discarded all of it silently. That has
been fixed in three ways:

1. **Your wording was recovered** — 192 of your sentences now live in
   `tools/i18n/hy_instructor.py`, loaded last so they override everything else.
2. **Your terminology is now enforced**, not merely recorded. `tools/i18n/hy_terms.py`
   holds 155 canonical terms and applies them to every translated string, so a term you
   correct once is correct everywhere, in every lecture, forever. Nine terms in the old
   dictionaries contradicted your reader and now follow it: **լուծաչափ** (not
   լուծունակություն), **չափաբերում** (not ստուգաչափում), **արագաչափ** (not
   աքսելերոմետր), **տվյալների թերթիկ** (not *datasheet*), **դրեյֆ**, **տպասալ**,
   **պատյան**, **ժամանակային դրոշմ**, **ԿՆԲ** (not *LSB*). Units follow too: Hz → Հց,
   kHz → կՀց, Pa → Պա in prose, Latin inside a formula — exactly the distinction you
   made by hand.
3. **The translator will no longer overwrite an existing `-HY.pptx`.** It prints
   `· skipping …`. Sixteen paragraphs on the L1 figure slides could not be recovered
   mechanically, so a blind rebuild would still lose a little; pass `--overwrite`
   deliberately, and diff, when you are ready.

**Read `tools/i18n/GLOSSARY-hy.md` before teaching from the Armenian decks.** It is
generated from the term table, so it cannot drift from what the slides say, and it ends
with five open questions that genuinely need your decision rather than a guess — chiefly
whether *filter* is **զտիչ** (your reader) or **ֆիլտր** (the accredited ծրագիր), which
matters because Lecture 3 uses it on eleven slides.

Every run also writes `tools/i18n/_term_warnings.txt`, listing the places the linter
thinks want your eye. It is short, and it is the file to check after any rebuild.

### Register, not just vocabulary

Your edits were consistently more formal than the generated Armenian, and Lectures 3 and
4 were written to match: declarative rather than rhetorical, nominal rather than verbal,
definitions ending in the definite article, no minute markers on student-facing slides
(*ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1*, not *ՀԱՐՑՈՒՄ 1 · ՐՈՊԵ 7*), and no instructor-facing text on a slide
the students can see. The full list is in the glossary under "Register".

### Practical notes

- Armenian runs 10–25 % longer than English. The translator eases the point size down
  where a string grew; if you lengthen a translation, re-render and check that slide.
- The type is **DejaVu Sans**. Arial and Courier New have no Armenian glyphs at all, and
  Noto Sans Armenian was rejected because it lacks Latin digits and renders every number
  spaced as `0 . 0 6 1`. On a machine without DejaVu Sans — most Windows installs — the
  Armenian still appears but substituted; installing it, free, fixes that.
- The **Armenian reader** now builds separately: `reader/course-reader-hy.pdf`. Until
  September the build mixed the Armenian and English chapters into one PDF, because its
  file glob did not distinguish them. Chapters 3 and 4 have no Armenian version yet.

---

## 10 · The microcontroller on-ramp

### 9.1 · The gap

The semester plan lists **"prior microcontroller experience"** as required entry
background (§3), and Laboratory 8 requires students to submit **source files** for a
working multi-sensor system (§6). Between those two points, the plan contains **no
session that teaches microcontroller use at all** — the first digital-interface lecture
is Lecture 13, in week 13.

For this cohort that entry assumption does not hold. So the plan has an internal gap:
it assumes a skill on the way in, never builds it, and then assesses it on the way out.

Worth knowing: the **accredited 2024 ծրագիր solved this inside the course** — labs
Լ4–Լ10 are LED control, PWM and timers, temperature logging, USART, SPI to an LCD,
stepper and servo control, all on STM32. The skill was taught here, not assumed. The
2026 plan dropped those labs in favour of sensor work without moving the prerequisite
anywhere.

### 9.2 · The principle

**Hand the firmware over one layer at a time, and never let the toolchain be the reason
a measurement lab fails.** Each lab adds exactly one new kind of authorship, and every
lab still ships a known-good binary so a team that loses a build can keep measuring.

### 9.3 · Proposed progression

| Lab | Week | What the student writes | New skill |
|---|---|---|---|
| **1** | 2 | **Nothing.** Console commands; conversions by hand | Register semantics, datasheet-to-value, the bench |
| **2** | 4 | **Change one constant** in supplied firmware and rebuild | Build, flash, serial — the toolchain itself |
| **3** | 6 | **Fill in a driver header** from the datasheet (`imu.h`; `imu.c` supplied) | Owning the values a driver depends on |
| **4** | 8 | **Write one pure function** — roll/pitch from acceleration, or the complementary-filter update | Writing logic, no peripherals involved |
| **5** | 10 | **Write a conversion and calibration function**; add a second sensor to an existing init sequence | Copy-adapt an I²C initialisation |
| **6** | 12 | **Write the acquisition loop**, including invalid-reading rejection | Control flow that drives a driver |
| **7** | 14 | **Write a driver** from the register map, with `imu.c` as the reference to compare against | Authoring a peripheral driver — the plan's own Lab 7 goal |
| **8** | 16 | **Capstone**: integrate, calibrate, validate, submit source | What the plan asks for, now reachable |

The parked driver in `shared/imu-driver-for-later-labs/` is written for steps 3 and 7.

### 9.4 · Where the teaching time comes from

**A one-page "MCU on-ramp" handout issued with Lab 2** — what a build is, what flashing
does, where `main()` lives, how to change a constant, how to open a serial port — plus
**20 minutes of Lab 2's session** spent on a guided build-and-flash with the whole room
doing it together. Lab 2's measurement work (sampling, noise, filtering on a stationary
signal) is light on setup, so it is the one lab that can afford the time.

**This now exists.** `lab-02/mcu-onramp.md` is that page, and stage 1 of
`lab-02/lab2-handout.md` is those twenty minutes, choreographed step by step in
`lab-02/instructor-notes.md`. The constant students change is `LPF2_XL_EN` — Lecture 3's
own register bit — so the toolchain exercise and the measurement lesson are one act
rather than two things sharing a session. Every board also ships a known-good binary, per
§9.2.

Everything after that rides on the plan's existing 0–10 min lab briefing slot.

### 9.5 · The honest risk, and your three options

Twenty minutes plus seven incremental steps is enough to reach a *modest* capstone. It is
**not** equivalent to the seven dedicated microcontroller labs the accredited programme
used to provide. If the cohort truly arrives with zero embedded experience, the realistic
choices are:

1. **Accept a shallower capstone.** Grade Lab 8 on measurement quality, calibration and
   validation — which is what the course is actually about — and treat firmware
   sophistication as a bonus. *Recommended for the first offering.*
2. **Move build work off the bench.** Set the toolchain exercises as homework between
   labs, so contact time stays on measurement. Costs students time and needs them to
   have the toolchain installed; worth surveying in week 1.
3. **Fix the prerequisite at department level.** The cleanest long-term answer: either an
   earlier course carries STM32 basics, or this course formally reclaims some of the
   ծրագիր's Լ4–Լ10 content. This is the same paperwork conversation as §7.1 — raise both
   together.

**Recommendation:** run option 1 this year and gather the evidence — how many teams
managed step 2 in Lab 2, and how many reached step 7 in Lab 14. That data is what makes
the case for option 3 next year, and it costs nothing to collect.
