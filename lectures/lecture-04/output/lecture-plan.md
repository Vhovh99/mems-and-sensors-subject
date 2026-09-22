# Lecture 4 — Lecture plan
**MEMS structures, transduction, fabrication and packaging overview**
80 minutes · Module A: Foundations · 20–24 students

Semester-plan coverage: proof masses, beams, diaphragms, resonators, comb structures;
capacitive, piezoresistive, piezoelectric, thermal, electromagnetic and optical
transduction; lithography, deposition, etching, bulk/surface micromachining; packaging
and stress.

**The design constraint that governs this lecture.** The semester plan says fabrication
is covered "only to the depth needed to understand structures, limitations, packaging,
drift and failure mechanisms", and §12 says explicitly that this is *not* a cleanroom
fabrication course. Lecture 1's content audit went further and cut fab photographs from
L1 because they reinforce that misconception. So L4 has one job and it is not a process
tour: **fabrication is taught here because it explains the datasheet.** Every process
step earns its slide by being the reason for a specification the students have already
met.

**Accredited-programme mapping.** Covers ծրագիր Theme 1.2 (տվիչներ և ակտուատորներ),
1.3 (դասակարգումը՝ ունակային, ինդուկտիվ, մագնիսական, օպտիկական — the transduction
families of Chunk 2, essentially one-for-one) and 1.4 (արագաչափերի և գիրոսկոպի
աշխատանքի սկզբունքը). Audit-safe.

## Learning outcomes

| | By the end, a student can… | CLO | Assessed by |
|---|---|---|---|
| L4.1 | **Identify** which of five canonical structures a given MEMS sensor uses, and name the relation that governs it | 1 | Poll 2 (min 22) · quiz |
| L4.2 | **Predict** from the transduction principle whether a device can measure a *static* measurand, and justify it | 1, 3 | Poll 3 (min 42) — the hardest vote |
| L4.3 | **Order** the four fabrication steps and state, for each, one device limitation it imposes | 3 | sequencing activity (min 52) |
| L4.4 | **Explain** why a packaged sensor performs differently on your board than in its datasheet, naming three stress paths | 3, 8 | synthesis (min 70) · exit ticket |
| L4.5 | **Decide** which specifications must be measured on the final assembly rather than taken from the datasheet | 2, 8 | Poll 4 (min 64) · project deliverable 2 |

**Not an outcome of L4:** designing a process flow, computing residual stress, or
reproducing a mask set. Students should leave able to *read* a device, not fabricate one.

## The running case — and the debt this lecture repays

Lecture 2 put a question on the screen that had no answer:

> *"What is this device's cross-axis sensitivity after it is soldered to my board?"*
> — L2 slide 22. The answer given was: **it is not in the datasheet, and it cannot be.**

That was left deliberately unpaid. L4 pays it. The reason no manufacturer can supply
that number is the entire content of this lecture: a MEMS sensor is not a component, it
is a **mechanical structure a few micrometres thick, mounted inside a cavity, soldered
to a board that bends.**

### The anchor: the packaging tax

From the same ISM330DHCX datasheet the class has had open for two weeks (DS13012 Rev 6):

| | value | condition |
|---|---|---|
| Zero-g level, typ | ±10 mg | **25 °C, after soldering** |
| Zero-g level, max | ±65 mg | **25 °C, after soldering** |

Against Lecture 2's anchor — a 0.5° tilt is **8.73 mg** of signal:

| | | |
|---|---|---|
| typ offset ÷ signal | 10 / 8.73 | **1.15×** |
| max offset ÷ signal | 65 / 8.73 | **7.45×** |

**Even the typical value exceeds the entire quantity being measured.** The maximum is
seven and a half times it. And the condition line says *after soldering* — the
manufacturer is telling you, in the specification itself, that assembly is part of the
error.

**One inconsistency to be aware of.** Lecture 2's candidate-comparison table quotes a
cross-axis sensitivity of **±1 %**, because Parts A/B/C there are *representative*
figures chosen to make the arithmetic exact, and the slide says so. Lecture 4 quotes the
real ISM330DHCX figure, **±0.5 % at 25 °C, package level**. A student holding both
handouts will notice. The L4 slides label their source explicitly; if you would rather
remove the collision entirely, change L2's representative value rather than L4's real
one.

### The twist that makes the lecture worth 80 minutes

Lecture 2's killer term was also **10 mg** — the offset *drift*, ±0.5 mg/°C × 20 °C. The
same number appears twice in Module A for two completely different reasons, and the
difference is the whole point:

| | L2's 10 mg | L4's 10 mg |
|---|---|---|
| What it is | offset **drift** over temperature | zero-g **offset** after soldering |
| Where it comes from | the temperature coefficient of the structure | die attach, package and solder stress |
| Size vs the 8.73 mg signal | 1.15× | 1.15× (typ), 7.45× (max) |
| Fix | **none** — it moves after you calibrate | **one-point calibration on your board** |
| Cost of the fix | — | one measurement, once, per unit |

So fabrication and packaging hand you a **large but removable** error, while the
temperature coefficient hands you a **small-looking but irremovable** one. Students who
leave with that distinction have the thesis of Module A and the reason Lecture 14 and
Laboratory 3 exist.

That the two numbers collide at 10 mg is a coincidence of this part. Name it explicitly
on slide 34 — an unremarked collision is a guaranteed exam misconception.

## Narrative arc

> **AND** — You can read a datasheet, budget its errors, and acquire a sample you trust.
> Every number you have used came from a table, and every table had a conditions column
> you now read first.
>
> **BUT** — Two weeks ago one of those conditions said *"after soldering"*, and one
> question had no answer at all. You cannot look up how your own board changes the
> device, and no manufacturer can tell you, however good the datasheet is.
>
> **THEREFORE** — Because the specification is not describing a component. It is
> describing a silicon structure two micrometres thick, suspended over a sealed cavity,
> glued into a plastic box and soldered to a board that flexes when you tighten a screw.
> Today we open the box — as deep as the drift, the stress and the failure modes require
> and not one slide deeper — and by the end the unanswerable question has a *method*
> instead of an answer.

## Chunk map

| Chunk | Minutes | Core concept | Cognitive load |
|---|---|---|---|
| Hook + frame | 0–14 | The unpaid debt from L2; the packaging tax; ±65 mg vs 8.73 mg | low, retrieval-heavy |
| **C1** | 14–32 | Five structures do all the work: proof mass + flexure, beam, diaphragm, resonator, comb | medium — new vocabulary, familiar physics |
| **C2** | 32–52 | Six transduction principles, and the static/dynamic discriminator | **highest — Poll 3 lives here** |
| **C3** | 52–70 | How it is made, and what that costs: lithography → deposition → etching → release; bulk vs surface; the stress chain | medium |
| Synthesis | 70–80 | Answering L2's question; the honest ledger; project bridge; exit ticket | low |

## Authoritative timeline

| Clock | Slides | Segment | Activity |
|---|---|---|---|
| 00:00–00:02 | 1–2 | Open | Last week's muddiest points **(from L3 exit tickets)** |
| 00:02–00:05 | 3 | Retrieval | L1's scaling laws, unaided: `k ∝ L`, `m ∝ L³`, `f₀ ∝ 1/L` |
| 00:05–00:08 | 4–5 | **Hook** | The question from Lecture 2 that had no answer |
| 00:08–00:11 | 6 | Poll 1 | Baseline · **answer withheld to min 70** |
| 00:11–00:14 | 7–8 | Anchor | ±10 / ±65 mg, "after soldering", against 8.73 mg |
| 00:14–00:18 | 9–11 | **C1a** | Proof mass + flexure: `C = εA/d`, and L1's figure again |
| 00:18–00:22 | 12–14 | **C1b** | Beam, diaphragm, resonator, comb — one relation each |
| 00:22–00:26 | 15–16 | Poll 2 | ConcepTest · which device has no proof mass |
| 00:26–00:32 | 17–19 | **C1c** | Why five structures cover eleven lectures' worth of sensors |
| 00:32–00:38 | 20–22 | **C2a** | Capacitive, piezoresistive, piezoelectric — the three that matter most |
| 00:38–00:42 | 23–24 | **C2b** | Thermal, electromagnetic, optical — one slide each, honestly brief |
| 00:42–00:46 | 25–26 | Poll 3 | ConcepTest · **hardest** · a piezoelectric device measuring tilt |
| 00:46–00:52 | 27–28 | **C2c** | The comparison table: static response, signal level, drift, power, and the datasheet line each one explains |
| 00:52–00:56 | 29–30 | **C3a** | Four steps, in order · sequencing activity |
| 00:56–00:60 | 31–32 | **C3b** | Bulk vs surface micromachining; the sacrificial layer; stiction |
| 00:60–00:64 | 33–34 | **C3c** | Packaging: cavity, die attach, wire bond, seal, getter — and the 10 mg collision |
| 00:64–00:68 | 35–36 | Poll 4 | Transfer · which spec must you measure yourself |
| 00:68–00:70 | 37 | **C3d** | The stress chain: die → adhesive → package → solder → PCB → screw |
| 00:70–00:73 | 38 | Poll 1 answer | The withheld answer lands; L2's question gets its method |
| 00:73–00:76 | 39–40 | Synthesis | The honest ledger: what micro-scale buys, what it costs |
| 00:76–00:78 | 41 | Close | Module A ends · what Lectures 5–11 now are · project bridge |
| 00:78–00:80 | 42 | Exit ticket | Two questions, on paper |

Slack: slides 23–24 (thermal/electromagnetic/optical) and slide 19 are the designated
cuts. Never cut Poll 3 or the stress chain — the first is the lecture's only genuinely
hard idea, the second is what makes Laboratory 3 make sense.

## The five structures, and the relation for each

Taught as five, not as a taxonomy, because five is the number that fits in working
memory and covers Lectures 5–11 completely.

| Structure | Governing relation | Senses | Course example |
|---|---|---|---|
| Proof mass on a flexure | `F = ma`, `x = ma/k`, `f₀ = (1/2π)√(k/m)` | acceleration, angular rate | L5 accelerometer, L6 gyroscope |
| Cantilever beam | `k ∝ Ewt³/L³` | force, and it is the flexure above | L8 force/tactile |
| Diaphragm over a cavity | deflection `∝ ΔP·a⁴/(E·t³)` | pressure, sound | L8 pressure, L11 microphone |
| Resonator | `f₀` shifts with mass, stress or temperature | mass, gas, temperature, time | L9 gas microheater, timing |
| Comb structure | `C = nεA/d`, `F ∝ n·V²` | displacement — sense *and* drive | L5, L6, L10 MEMS mirror |

Note for delivery: the comb structure is the only one that both senses and actuates, and
that is why gyroscopes are possible at all — the drive comb sustains the vibration whose
Coriolis deflection the sense comb reads. Say it here; Lecture 6 will thank you.

## The six transduction principles

The discriminator that carries the chunk is **static response**, because it is the one
that changes an engineering decision and the one Poll 3 tests.

| Principle | Static (DC)? | Signal | Main weakness | Datasheet line it explains |
|---|---|---|---|---|
| Capacitive | **yes** | small, high-impedance | needs on-chip electronics; stray capacitance | why the ISM330DHCX can measure tilt at all |
| Piezoresistive | **yes** | mV from a bridge | strong temperature coefficient | why pressure sensors need compensation |
| Piezoelectric | **no** | charge, self-generating | no DC response; charge leaks | why vibration sensors quote a low-frequency limit |
| Thermal | yes, slowly | µV or resistance | slow; self-heating | warm-up time on a gas sensor |
| Electromagnetic | yes | large, low-impedance | hard to shrink; magnetically susceptible | hard/soft-iron terms in L7 |
| Optical | yes | can be very large | needs a window; ambient light | cover-window design in L10 |

## Fabrication, in four steps and no more

| Step | Armenian term | The limitation it imposes |
|---|---|---|
| Lithography | վիմագրություն | minimum feature size → sets the comb gap → sets the capacitance → sets the noise floor |
| Deposition | նստեցում | film thickness and **residual stress** → the structure is curved before it is used |
| Etching | փորագրում | isotropic vs anisotropic sets which shapes are possible at all |
| Release | ազատում | the sacrificial layer leaves the structure free — and vulnerable to **stiction** |

Four steps, one consequence each. That is the whole treatment, and it is deliberate: any
more and this becomes a fabrication course, which the semester plan forbids.

**Bulk vs surface micromachining** gets one comparison slide: bulk etches into the wafer
(thick structures, large masses, low noise — pressure sensors), surface builds up from
thin films (small, cheap, integrated with electronics — consumer IMUs). The trade-off is
mass, and by Lecture 1's scaling argument the class can already predict which one is
quieter.

## The stress chain — the lecture's closing diagram

Six links, and only the first is in the datasheet:

`die → die attach adhesive → package body → solder joints → PCB → mounting screw`

| Link | Contributes | Specified by anyone? |
|---|---|---|
| die | the transduction itself | yes — the datasheet |
| die attach | offset shift, hysteresis | partly — "after soldering" |
| package body | temperature coefficient | partly |
| solder joints | asymmetric stress → **cross-axis error** | **no** |
| PCB flex | offset and cross-axis, load-dependent | **no** |
| mounting screw | offset that changes when it is retightened | **no** |

Lecture 1's war story ended at a 5 mm rubber pad — the seventh link, outside the board
entirely. Draw the chain, then put the rubber pad on the end of it, and the course's
first story and its fourth lecture close on the same diagram.

## Misconceptions this lecture is built to catch

| # | Predicted misconception | Where it is caught |
|---|---|---|
| M1 | The datasheet describes the device as you will use it | Poll 1, resolved min 70 |
| M2 | Any accelerometer can measure tilt | **Poll 3** — a piezoelectric one reads zero |
| M3 | Piezoelectric means "better", because it is self-generating | Poll 3 and the comparison table |
| M4 | Smaller is better | slides 39–40, the honest ledger — smaller means less mass means more noise |
| M5 | Packaging is protection, not physics | slides 33–34, 37 |
| M6 | Every structure needs a proof mass | Poll 2 — the pressure sensor does not |
| M7 | Fabrication tolerances are the manufacturer's problem | Poll 4, and Lab 3 |

## Reader chapter

`reader/ch04-structures-and-fabrication.md`, same seven-part shape as Chapters 1–3. Its
integration-failure section is the mounting-screw story, which is the one students meet
again in the capstone.

## Module A closes here

Slide 41 should say so out loud. After four lectures a student can: draw the chain,
specify a measurement, read a datasheet against a requirement, acquire a sample they can
defend, and explain why a device behaves differently on their own board. Lectures 5–11
are then **seven instances of one pattern** — measurand → transduction → structure →
output → specifications → interface → calibration → failure modes — and the pattern is
the thing Module A just built. Saying this explicitly is worth ninety seconds: it turns
the next seven weeks from a list of devices into a method applied seven times.
