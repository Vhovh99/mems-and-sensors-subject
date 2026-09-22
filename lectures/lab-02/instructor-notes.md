# Laboratory 2 — Instructor notes
**Sampling, noise and filtering** · Week 4 · 80 minutes

> ⚠ **Verify the register values and the noise figures in this key against your actual
> part and datasheet revision before teaching.** Everything below is from ISM330DHCX
> DS13012 Rev 6, which is the revision the pilot was built against. This carries the same
> standing caveat as Laboratory 1's key.

---

## What this laboratory is, and what it is not

It is **two labs in one session**, and they are both load-bearing:

1. **A toolchain lab.** Per `instructor-guide.md` §9.3–9.4, Lab 2 is where the whole room
   builds and flashes firmware together, once, for twenty minutes. The cohort is not
   assumed to have done it before, and this is the only group attention it gets. If stage
   1 goes badly, the rest of the on-ramp goes badly.
2. **A measurement lab.** Sampling, noise, effective resolution, filtering — the direct
   bench continuation of Lecture 3.

Lab 2 was chosen for the toolchain because its measurement work is light on setup: the
board is already wired from Lab 1, and a stationary capture needs no fixture. It is the
only lab in the semester that can afford the twenty minutes.

**The single constant students change is `LAB2_CTRL1_XL`, `0x40` → `0x42`.** That is
`LPF2_XL_EN`, the bit Lecture 3 built a poll around. So the toolchain exercise and the
measurement lesson are the same act — they narrow a bandwidth by editing one character
and then measure that σ fell. Do not substitute a different constant; the coupling is the
design.

---

## Answer key — ISM330DHCX *(DS13012 Rev 6)*

### Pre-lab section B

| # | Value | Note |
|---|---|---|
| B1 | 60 µg/√Hz **typ** | high-performance mode |
| B2 | 100 µg/√Hz **max** | the figure to design against |
| B3 | high-performance mode | if the part drops to low-power mode the figures change |
| B4 | 0.061 mg/LSB at ±2 g | 4000 mg / 65 536 |
| B5 | `CTRL1_XL` = `0x10` | |
| B6 | `ODR_XL` = bits 7:4; 104 Hz = `0100` | |
| B7 | `FS_XL` = bits 3:2; ±2 g = `00` | **not ascending**: `01` is ±16 g |
| B8 | `LPF2_XL_EN` = bit 1; **0 after reset** | the bit of the day |
| B9 | `CTRL8_XL` = `0x17`; `HPCF_XL` selects the LPF2 corner | ⚠ verify the field name and the bandwidth table against your revision — see "the one soft number" below |
| B10 | ±10 mg typ, ±65 mg max, **at 25 °C after soldering** | Lecture 4's anchor |

### `CTRL1_XL` bytes for this lab, ±2 g

| Goal | Byte | ODR / FS / LPF2 |
|---|---|---|
| 26 Hz, LPF2 off | `0x20` | `0010` / `00` / 0 |
| 52 Hz, LPF2 off | `0x30` | `0011` / `00` / 0 |
| **104 Hz, LPF2 off — ships on the boards** | **`0x40`** | `0100` / `00` / 0 |
| **104 Hz, LPF2 on — what students build** | **`0x42`** | `0100` / `00` / **1** |
| 208 Hz, LPF2 off | `0x50` | `0101` / `00` / 0 |
| 416 Hz, LPF2 off | `0x60` | `0110` / `00` / 0 |

### Pre-lab C1 — quantisation

```
span = 4000 mg      LSB = 4000 / 65 536 = 0.0610 mg      σ_q = LSB/√12 = 0.0176 mg
```

### Pre-lab C2 — the table, using the max density (100 µg/√Hz)

| ODR | `CTRL1_XL` | BW | σ | σ in LSB | bits lost | effective bits |
|---|---|---|---|---|---|---|
| 26 | `0x20` | 13 Hz | **0.361 mg** | 5.9 | 2.56 | **13.4** |
| 52 | `0x30` | 26 Hz | **0.510 mg** | 8.4 | 3.06 | **12.9** |
| 104 | `0x40` | 52 Hz | **0.721 mg** | 11.8 | 3.56 | **12.4** |
| 208 | `0x50` | 104 Hz | **1.020 mg** | 16.7 | 4.06 | **11.9** |
| 416 | `0x60` | 208 Hz | **1.442 mg** | 23.6 | 4.56 | **11.4** |

With the **typ** density (60 µg/√Hz) every σ scales by 0.6: 0.216 / 0.306 / 0.433 /
0.612 / 0.865 mg. A real part usually lands between the two columns, and locating it is
stage 3.4.

- **C2a** — √2 per doubling. Exactly, and it is worth insisting on the word *exactly*:
  σ ∝ √BW ∝ √ODR, so doubling ODR multiplies σ by √2 = 1.414.
- **C2b** — at 26 Hz, σ = 0.361 mg against σ_q = 0.0176 mg: sensor noise dominates by
  **20×**.
- **C2c** — **none of them.** Quantisation never gets within a factor of ten at any rate
  in this lab. That is the answer, and students find it unsatisfying, which is the point:
  the error everyone wants to discuss is irrelevant here.

### Pre-lab C3 — the filter

- **C3a** — 1.442 / √4 = **0.721 mg**
- **C3b** — it is **identical to the native 104 Hz row**. This is the intended
  discovery and the headline of the lab.
- **C3c** — sampling at 416 Hz and averaging four samples gives the same noise as
  sampling at 104 Hz, because both end up with the same bandwidth. Noise is set by
  bandwidth, and where in the chain you impose the bandwidth is a free choice.
- **C3d** — bandwidth 208/4 = **52 Hz**; group delay (4−1)/2 = 1.5 samples at 416 Hz =
  **3.6 ms**.

### Pre-lab C4 — the achieved rate

| ODR | period | + 202 µs read | achieved | error |
|---|---|---|---|---|
| 416 Hz | 2.404 ms | 2.606 ms | **383.7 Hz** | **−8.4 %** |
| 104 Hz | 9.615 ms | 9.817 ms | **101.9 Hz** | **−2.1 %** |
| 26 Hz | 38.46 ms | 38.66 ms | **25.9 Hz** | **−0.5 %** |

- **C4d** — the error is the read time as a fraction of the sample period, so it grows as
  the period shrinks. At 416 Hz the read is 8 % of the budget; at 26 Hz it is 0.5 %.
  Students who answer "because 416 is faster" have not answered.

### Pre-lab C5 — the prediction

There is **no single right answer**, and that is deliberate. LPF2 narrows the bandwidth,
so σ must fall; by how much depends on the `CTRL8_XL` corner setting. A student who
predicts "σ falls, by somewhere between √2 and 2, because the bandwidth roughly halves"
has reasoned correctly. Grade the reasoning, not the ratio.

### Expected measurements at rest, ±2 g, flat, Z up

- `raw_z` ≈ **+16 300 to +16 500** (1000 mg / 0.061 ≈ 16 393)
- `raw_x`, `raw_y` means: ±160 counts typ, up to ±1070 at the ±65 mg limit — the
  **zero-g offset**, and the direct hand-off to Lecture 4
- mean magnitude **970–1030 mg** for a typical part
- σ at 104 Hz, LPF2 off: expect **0.4 to 0.75 mg** (7 to 12 codes) depending on where the
  part sits between typ and max

---

## The one soft number in this lab

**`CTRL8_XL` and the exact LPF2 bandwidth.** Everything else in this key is verified
arithmetic on published figures. The LPF2 corner is selected by a field in `CTRL8_XL`
whose encoding you should read off your own revision, and the σ ratio students measure in
stage 2.6 depends on it.

This does not weaken the lab. The **direction** is certain — enabling a low-pass filter
at fixed ODR must reduce σ — and that is what stage 2.6 asks them to confirm and what
C5 asks them to predict. If a student demands the exact expected ratio, the honest answer
is: *read `CTRL8_XL` in the datasheet, tell me the corner frequency it selects, and then
you can predict it.* That is a better use of five minutes than any number this key could
supply.

Before the session: run one capture at `0x40` and one at `0x42` yourself, and **write your
measured ratio in the margin here.** After that, this note is resolved for your kit.

Measured on my part: σ(off) = ________ mg, σ(on) = ________ mg, ratio = ________

---

## Preparation checklist

- [ ] Verify and correct the answer key above against your actual part
- [ ] Flash **every** board with `LAB2_CTRL1_XL = 0x40` — the shipped default
- [ ] Build and keep a **known-good `0x42` binary** on a USB stick, one per bench
- [ ] Run the whole lab yourself once, end to end, and fill in the margin above
- [ ] Confirm every laptop can build and flash **before** the session — a survey in
      week 3 is worth more than twenty minutes of debugging in week 4
- [ ] Confirm every laptop has a serial terminal that can **log to a file**. Teams who
      cannot log will try to retype 2000 rows
- [ ] Check `mcu-onramp.md` was issued and read; the stage 1 briefing assumes it
- [ ] Have a spreadsheet template ready to hand out if a team's spreadsheet skills stall
      — `analysis/` has one
- [ ] Optional: a phone with a tone-generator app, for the stage 5.5 alias
- [ ] Ask the class not to lean on the benches during captures. Say it twice

---

## Running the session

### 00–10 · Briefing

Collect the pre-lab sheets and sign section E as you go. **Do not sign a sheet with C2
blank** — a team without C2 has nothing to compare their measurements against and will
produce numbers with no meaning.

Say the three claims out loud and write them on the board. Leave them there.

### 10–30 · Stage 1, the toolchain, together

**Run this from the front, one step at a time, and wait for the whole room at each step.**
The temptation is to let fast teams run ahead; resist it, because the students who need
this are the ones who will not ask.

Choreography that works:

1. Everyone connects, opens a terminal, presses RESET, and **reads the banner aloud**.
   Nobody proceeds until every bench has seen `0x40`.
2. Everyone runs `cfg` and finds `LPF2_XL_EN 0`. Ask: *"what did Lecture 3 say about this
   bit?"*
3. Everyone captures the baseline. Twenty seconds of silence, hands off benches. This is
   also a good moment to spot who cannot log to a file.
4. Now the edit — and here, slow down. Show the file on the projector. Change the
   character. Save. Build. **Say the words "zero errors" and wait until every bench has
   them.**
5. Flash, RESET, read the banner. **Expect a third of the room to still see `0x40`.**
   This is the most valuable moment of the day. Do not fix it for them; ask "which of the
   three steps did not happen?" and let them find it.
6. Second capture.

If a team is still broken at minute 28, hand them the known-good binary without ceremony
and move on. §9.2's rule: the toolchain never gets to be the reason a measurement lab
failed.

### 30–58 · Stages 2 and 3, mostly unattended

This is spreadsheet work and it goes quietly. Circulate and ask two questions:

- *"How many bits did you measure?"* — the answer should be near 12, and they should be
  slightly annoyed about it.
- *"What is your ratio column?"* — the answer should be near 1.414, and if it is not, ask
  whether they kept `lpf off` for all five rows. Mixing filtered and unfiltered rows into
  one sweep is the commonest error of the afternoon.

**Watch for the double-multiply.** σ in codes is already σ in LSB; teams multiply by
0.061 twice and get 0.044 mg, which is *below the quantisation floor* and therefore
impossible. That impossibility is a nice thing to point out rather than correct: *"your
answer is smaller than one code. Can a measurement be finer than the smallest change the
number can represent?"*

### 58–68 · Stage 4, timing

Most teams will not have noticed that the answer was printed at the end of every capture
they took. Let them discover it; if a team is stuck at minute 62, tell them to scroll to
the bottom of a capture file.

The staircase plot in 4.5 confuses people. Be ready to say: **that is the 1 ms clock, not
the sensor.** The mean interval in microseconds is the real measurement. It is worth
saying why the firmware reports the mean rather than per-sample times — a 1 ms tick
cannot resolve a 2.4 ms period, but 2000 of them pin the mean to half a microsecond.

### 68–76 · Stage 5, filtering

The moment to be present for is **5.3**. When a team puts "σ of the 416 Hz capture
averaged by 4" beside "σ measured natively at 104 Hz" and finds the same number, ask:
*"why?"* If they can answer, they have the course's central trade-off. If they cannot,
this is the most valuable ninety seconds you will spend today.

The alias in 5.5 is optional and often does not work in a quiet room with nothing
vibrating. **Do not let it eat the check-off.** If nobody gets a clean alias, do it once
at the front with a phone against a board and project the two series.

### 76–80 · Check-off

Five things and one question, listed in the handout. Keep it to two minutes per team by
asking only the question they look least comfortable with.

---

## Frequently asked, with answers

**"Why is my σ different from the datasheet?"**
Because the datasheet gives a `typ` and a `max` and your part is one part. If you are
between 0.4 and 0.75 mg at 104 Hz you are in specification. Stage 3.4 asks you to
extract your own part's density, which is the honest answer to this question.

**"Should I use STDEV or STDEV.P?"**
`STDEV.P`, because you have the whole capture. With 2000 samples they differ by 0.03 %,
so it changes nothing — but say which you used.

**"My effective-bits number is not a whole number."**
It is not supposed to be. 12.4 bits means the noise straddles the twelfth and thirteenth
bit. Bits are only integers when you are counting wires.

**"Can I average away the aliased component?"**
No, and 5.6 is asking exactly that. Once sampled, the alias and a genuine signal at that
frequency are the same numbers. This is Chapter 3 §3.12's bottom group.

**"Why does raising the ODR make the noise worse? Faster should be better."**
It is not worse — it is wider. You are admitting more of the noise spectrum. If you do
not need the bandwidth, do not buy it; if you do need it, you pay for it in noise. Stage
5.3 shows that you can also buy it back afterwards, at the price of delay.

**"The mean of my X axis is not zero. Is my sensor broken?"**
No — that is the zero-g offset, it is in the datasheet at ±10 mg typ, and Lecture 4 is
substantially about where it comes from. Convert it to mg and check it against the limit.

**"Do I need the phone for the alias?"**
No. It is the one optional part of the lab. The decimation in 5.5 works on any capture
that has something above 26 Hz in it, and a rhythmic tap on the bench usually suffices.

---

## After the session — for the course review file

Record, while it is fresh:

- **How many teams saw `0x40` after their first flash?** This is the number that tells
  you whether twenty minutes was enough, and it is the input to the §9.5 decision about
  whether the on-ramp is viable as designed.
- **How many teams needed the known-good binary?** More than a third means the toolchain
  survey in week 3 should become mandatory.
- **How many got stage 5.3 unprompted?** This is the lab's real outcome.
- **Measured σ ratio for LPF2 off/on**, so the answer key above stops being soft.
- **Did the alias demonstration work in the room?** If not, consider a small vibration
  motor in the kit for next year.
- Timing: did stages 2 and 3 fit? They are the most likely to overrun, and the designated
  cut is stage 5.5.
