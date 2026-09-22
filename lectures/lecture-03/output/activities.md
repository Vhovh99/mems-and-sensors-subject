# Lecture 3 — Activity Set
**From physical quantity to trustworthy samples** · 80 min · 20–24 students

Four content polls, one withheld-answer poll spanning the lecture, one 60-second state
change, one worked conversion done with the class. Attention resets at min 11, 23, 32,
44, 60, 68.

**Voting method:** projected question, **simultaneous show of hands on a count**, then
spoken reasoning — hands before voices, every time. Full protocol in
`lecture-01/output/activities.md`. There is no polling software and none is needed.

> **Numbers.** Every figure below is from the ISM330DHCX datasheet (DS13012 Rev 6), the
> part in the lab kit, or is arithmetic on those figures. Nothing here is invented. The
> two places where a *representative* value is used instead of a named product — the
> strain-gauge bridge in Poll 2 and the pressure loop in Poll 4 — say so on the slide.

---

## The running case

> The ISM330DHCX is configured for **±2 g, 16-bit, ODR = 104 Hz**. Its datasheet says
> **0.061 mg/LSB**. You log for ten minutes with a `HAL_Delay(10)` polling loop.
> How much of what you logged is true?

The answer has three parts, and each is a chunk: **12.4 bits, 12 Hz, 12.1 seconds.**
Those three numbers are the lecture. If a student remembers only one thing, it should be
that all three were computable before any firmware was written.

---

## Poll 1 · minute 7 · baseline, answer withheld until minute 66

**Stem**

> Your accelerometer is 16-bit, configured for ±2 g, so its datasheet resolution is
> **0.061 mg/LSB**. You configure ODR = 104 Hz and log the output.
>
> What is the smallest change in acceleration your log can actually distinguish?

**Options**

| | |
|---|---|
| A | 0.061 mg — that is what the datasheet says |
| B | 0.018 mg — the quantisation noise, LSB/√12 |
| C | 0.72 mg |
| D | It cannot be determined from what you have been told |

**The right first answer is D.** At minute 7 the class has not been given the noise
density, so D is the only defensible vote — exactly as Poll 1 of Lecture 2 was
answerable only as "not enough information". Students who have internalised Lecture 2
will notice; most will not, and will vote A.

**The right second answer, at minute 66, is C.** With the noise density (100 µg/√Hz max)
and the bandwidth (52 Hz), the noise floor is 0.72 mg — nearly twelve times the LSB.

**Distractor diagnosis**

- **A** — misconception M1, the whole reason the lecture exists. Expect 55–70 % here.
- **B** — the student who knows LSB/√12 and stops. Sophisticated and still wrong: it is
  the *smaller* of two noise terms by a factor of forty. Praise the knowledge, then use
  it: "you found the term that does not matter — which one does?"
- **C** — right for the wrong reason at minute 7. Ask *how* they got it; if they cannot
  say, it was a guess.
- **D** — right. Expect 5–15 %.

**Do not reveal.** Write the vote distribution on the board and leave it. Revealing here
destroys the arc of the lecture, and the minute-66 reveal is where L3.3 is actually
assessed.

---

## Poll 2 · minute 23 · ConcepTest, Chunk 1

**Stem**

> A strain-gauge bridge is excited from the microcontroller's 3.3 V rail. The ADC that
> reads it uses **the same 3.3 V rail as its reference**. Under load, the rail sags to
> 3.2 V.
>
> The reported strain:

**Options**

| | |
|---|---|
| A | reads about 3 % high |
| B | reads about 3 % low |
| C | does not change |
| D | changes by an amount that depends on the gauge factor |

**Correct: C.** The bridge output is proportional to its excitation, and the ADC's
counts are proportional to 1/reference. Both scale with the same rail, so the ratio —
which is what the code actually computes — is unchanged. This is a **ratiometric
measurement**, and it is free if you wire it deliberately and impossible to recover if
you do not.

**Distractor diagnosis**

- **A / B** — the majority, split roughly evenly, which is what makes this a good vote:
  the room disagrees about the *sign* of an error that does not exist. Let the two camps
  argue for ninety seconds before you say anything.
- **C** — correct. Target 30–45 % after peer discussion.
- **D** — the student conflating sensitivity with reference error. Useful: the gauge
  factor sets how many millivolts per microstrain, and cancels out of the ratio entirely.

**The follow-up that makes it stick:** "Now the same bridge, but the ADC reference is a
precision 2.5 V part and the bridge still runs from the rail. What happens?" — a 3 %
error, straight through, uncalibratable, because the two no longer track. Same hardware
cost. One wire's difference.

Target 30–70 % correct: satisfied.

---

## State change · minute 32 · 60 seconds, no talking

> Stand up. Turn your paper over. From memory, draw the last three boxes of the
> measurement chain and write, under each, the one thing that can be lost there.

Physically standing matters — it is the deliberate attention reset before the hardest
chunk. Do not collect these. Walk two rows and look at three sheets so students know
they are seen; that is the whole enforcement mechanism.

Answers worth hearing aloud (pick two, thirty seconds): *sampling → frequencies above
Nyquist*; *codes → units → the sign and the scale factor*; *timestamp → when it
happened*.

---

## Poll 3 · minute 44 · ConcepTest, Chunk 2 — the hardest vote of the lecture

**Stem**

> You configure the accelerometer for **ODR = 104 Hz** and leave `CTRL1_XL` bit
> `LPF2_XL_EN` at its **reset value of 0**. A pump on the same frame vibrates at
> **300 Hz**.
>
> What appears in your logged data?

**Options**

| | |
|---|---|
| A | nothing — 300 Hz is above the sample rate, so it is not sampled |
| B | a 300 Hz component, attenuated |
| C | a **12 Hz** component, indistinguishable from real signal |
| D | broadband noise, raising the noise floor slightly |

**Correct: C.** `|300 − 3 × 104| = 12 Hz`. The pump appears as a slow 12 Hz oscillation
that no later filter can remove, because by the time the data exists the 300 Hz and the
12 Hz are the same numbers.

**Distractor diagnosis**

- **A** — misconception M2, the dominant one. "Above the sample rate" feels like "outside
  the window". Expect 40–55 %. The refutation is the picture from Lecture 1: the samples
  are *correct*, their interpretation is not.
- **B** — the student who assumes some filter is always present. Worth naming as a
  reasonable *design* instinct and a fatal *assumption*: the register bit is 0 by default,
  and they will set it themselves in Lab 2.
- **C** — correct. Target 20–35 % on the first vote, 50–65 % after discussion. If the
  first vote is above 50 %, your Lecture 1 aliasing segment worked better than expected;
  say so, and move faster through slides 25–26.
- **D** — the student who has heard "noise floor" and reaches for it. Distinguish: noise
  is broadband and averages down; an alias is a *tone* and averaging makes it cleaner.

**Peer instruction protocol.** Vote → 2 minutes in pairs, with the instruction "find
someone who voted differently and make them defend it" → revote → *then* the arithmetic.
Do not do the arithmetic before the revote; the revote is the measurement.

**The kicker slide.** Same tone, sampled at 100 Hz instead of 104: `|300 − 3×100| = 0 Hz`.
The pump becomes a **DC offset** — and someone will spend a week calibrating it out and
succeed, which is worse than failing, because the "calibration" is now wrong at every
other pump speed.

---

## Worked conversion · minutes 50–56 · done with the class, not shown finished

On the board, one register read, all the way to SI units. Ask the class for each step
before writing it.

```
OUTX_L_A (0x28) = 0x2C     OUTX_H_A (0x29) = 0xFF
                                   ↓  little-endian: high byte is the second one
raw = 0xFF2C                       = 65324  as unsigned
                                   ↓  16-bit two's complement: bit 15 is set
raw = 0xFF2C − 65536               = −212   counts
                                   ↓  × sensitivity, ±2 g → 0.061 mg/LSB
a   = −212 × 0.061 mg              = −12.9 mg
                                   ↓  → SI
a   = −0.0129 g × 9.80665          = −0.127 m/s²
```

Four places this goes wrong, and all four appear in Lab 2 submissions:

1. **Byte order.** Reading high-then-low gives `0x2CFF` = 11519 counts = +703 mg. Not a
   small error — a wrong answer of the right magnitude, which is the dangerous kind.
2. **The sign.** Skipping the two's-complement step gives +3985 mg. A device at rest
   reporting 4 g.
3. **`IF_INC`.** `CTRL3_C` resets to 0x04, so auto-increment is *already on* and a burst
   read works. Students who reset `CTRL3_C` to 0x00 to "start clean" break it, and get
   six copies of the same byte.
4. **The units.** mg, g and m/s² all appear in the same lab. Insist on one column header
   with a unit in it. The plausibility check is `≈ 9.81 m/s²` on one axis at rest.

---

## The 16 → 12.4 arithmetic · minutes 56–60 · the anchor resolves

Do this in full, out loud, on the board:

```
full scale, ±2 g              4000 mg
codes, 16-bit                 65 536
LSB                           4000 / 65 536        = 0.061 mg
quantisation noise            0.061 / √12          = 0.018 mg
bandwidth, ODR 104 Hz, LPF2   104 / 2              = 52 Hz
sensor noise, 100 µg/√Hz      100 × √52            = 721 µg = 0.721 mg
noise, in LSB                 0.721 / 0.061        = 11.8 LSB
bits that are noise           log₂ 11.8            = 3.6 bits
effective bits                16 − 3.6             = 12.4 bits
```

**Two sentences to say exactly:**

> The quantisation noise is forty times smaller than the sensor noise. Every argument
> about the last bit of an ADC is, in this system, an argument about nothing.

> You did not buy a 16-bit measurement. You bought a 16-bit *number* wrapped around a
> 12.4-bit measurement, and the datasheet was not lying to you — it told you the noise
> density on the same page.

Then the `typ` column: 60 µg/√Hz gives 0.433 mg and **13.2** effective bits. The
datasheet's own two columns move the answer by 0.8 bits. Lecture 2's lesson, restated in
a new quantity — say that out loud, it is the connective tissue of Module A.

---

## Poll 4 · minute 68 · transfer to a new measurand

**Stem**

> A water-level logger reads a **4–20 mA pressure loop** through a 100 Ω sense resistor
> and a 12-bit ADC, polling in a `while()` loop with a 50 ms delay. It runs for a week.
>
> Afterwards you discover all four of the following. Which one can you still fix?

**Options**

| | |
|---|---|
| A | the reported level is 40 mm high across the whole week |
| B | the timestamps drift, ending 90 s behind real time |
| C | a 9.7 Hz component from the pump has folded into the band |
| D | the last two ADC bits were always noise |

**Correct: A.** A constant offset is a systematic error against a known reference — the
tank was empty on Tuesday, the level was surveyed on Friday — so it is removable after
the fact. The other three are not: a lost clock cannot be reconstructed, an alias is
arithmetically identical to real signal, and information that was never resolved cannot
be recovered.

**Distractor diagnosis**

- **B** — tempting, because it *looks* like a linear correction. It is not: the loop
  period depended on branch timing that varied with the data. You can bound the error;
  you cannot invert it.
- **C** — the student who has already forgotten Poll 3's lesson twenty minutes later.
  Worth catching now rather than in the midterm.
- **D** — the student who thinks averaging recovers resolution. It recovers *some*, but
  only for a stationary signal, and only at the cost of bandwidth — which is the L2/L3
  trade restated. A good place to preview Lecture 15.

Different measurand, different interface, different failure — same question underneath.
That is what makes it a transfer item and not a repeat.

---

## Poll 5 · minute 78 · exit ticket, on paper

Two questions, ninety seconds, collected at the door. These are the input to Lecture 4's
opening slide, so they must actually be read.

1. A colleague says "we will sample at 1 kHz and filter it down in software afterwards."
   In one sentence, what is wrong with that plan?
2. Name one error in your Lab 1 data that you now believe was **irreversible**.

**Question 2 is the one that matters.** It forces retrieval across two weeks and it
tells you whether the calibratable/irreversible distinction — outcome L3.5, and the
spine of Lectures 12–15 — actually landed. Expect a third of the class to name aliasing,
a third to name the timestamp, and a third to name something calibratable, which is
precisely the diagnostic you want.

---

## Backup plans

| If | Then |
|---|---|
| Running 5 min late at min 44 | cut the state change and slide 35 (data integrity); keep Poll 3 |
| Running 10 min late | also compress the worked conversion to steps 1 and 2 only, and set steps 3–4 as the Lab 2 pre-lab |
| Poll 3 first vote > 60 % correct | skip slides 25–26's build-up, go straight to the ODR/BW/cut-off table, use the time on the timestamp segment |
| Poll 3 first vote < 15 % correct | do not push on. Re-draw Lecture 1's aliasing figure on the board, revote, and move the timestamp segment to Lab 2's briefing |
| Projector fails | the whole lecture survives on a whiteboard: three numbers, one chain diagram, one register read. Poll options can be read aloud — the vote is hands, not screens |
| Nobody has the datasheet open | pairs of two, one device between them; the page numbers are in the speaker notes |

## Materials

- ISM330DHCX datasheet (DS13012 Rev 6), one per pair — printed or on a laptop
- Whiteboard, three colours if possible: the deck's semantics are **teal = true signal
  path, amber = where error enters, red = the term that kills the design**
- Exit-ticket slips, 24
- No microcontrollers. This is the lecture *before* the bench, deliberately
