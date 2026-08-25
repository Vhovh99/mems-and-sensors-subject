# Armenian terminology — please review

The Armenian decks are generated from the English ones by `tools/translate_deck.py`,
using the dictionaries in `tools/i18n/hy_part1.py … hy_part5.py`.

**This glossary is the thing to check first.** Every term below is used consistently
across both lectures. If you disagree with one, change it in the dictionary file and
rerun the translator — the correction propagates everywhere at once. Terms are far more
important to get right than individual sentences, because students will carry them for
sixteen weeks.

## Where the terms come from

Where the accredited 2024 ծրագիր already fixes a term, **its wording was used** — so the
vocabulary matches what your department has already approved. Those rows are marked ✔.

Terms that appear in datasheets are followed by the English in the slide text on first
use, or left in Latin entirely, because students must recognise them in an ST document
next week.

## Core vocabulary

| English | Armenian used | Note |
|---|---|---|
| sensor | **տվիչ** | ✔ ծրագիր |
| actuator | **ակտուատոր** | ✔ ծրագիր |
| transducer | **փոխակերպիչ** | distinguished from տվիչ on slide 9 |
| measurand | **չափվող մեծություն** | |
| measurement chain | **չափման շղթա** | the spine term of Lecture 1 |
| capacitive | **ունակային** | ✔ ծրագիր |
| accelerometer | **աքսելերոմետր** | ✔ ծրագիր |
| gyroscope | **գիրոսկոպ** | ✔ ծրագիր |
| signal | **ազդանշան** | ✔ ծրագիր |
| amplifier | **ուժեղարար** | ✔ ծրագիր |
| filter | **ֆիլտր** | ✔ ծրագիր |
| ADC | **ԱԹԿ** (անալոգաթվային կերպափոխիչ) | ✔ ծրագիր |
| interrupt | **ընդհատում** | ✔ ծրագիր |
| microcontroller | **միկրոկոնտրոլլեր** | ✔ ծրագիր |
| proof mass | **իներցիոն զանգված** | |
| stiffness | **կոշտություն** | |
| resonant frequency | **ռեզոնանսային հաճախություն** | |
| sampling | **նմուշառում** | |
| quantisation | **քվանտացում** | |
| aliasing | **ալիասինգ** | term of art, kept as a loanword |
| bandwidth | **թողունակություն** | |
| accuracy | **ճշտություն** | ⚠ see below |
| precision | **ճշգրտություն** | ⚠ see below |
| resolution | **լուծունակություն** | ⚠ see below |
| sensitivity | **զգայունություն** | |
| offset | **զրոյական շեղում** | |
| drift | **շեղում** / **դրեյֆ** | |
| noise | **աղմուկ** | |
| calibration | **ստուգաչափում** | metrology standard |
| error budget | **սխալանքի հաշվեկազմ** | |
| specification | **տեխնիկական բնութագիր** | |
| datasheet | **datasheet** | left in Latin on purpose — that is what they will search for |
| timestamp | **ժամանականիշ** | |
| stiction | **կպչողություն** | |
| RMS | **RMS** | kept Latin |
| FIFO, ODR, LSB, I²C | kept Latin | register-level terms |

## Three terms worth your specific attention ⚠

1. **ճշտություն (accuracy) vs ճշգրտություն (precision).** Lecture 2 turns entirely on
   this distinction, and Armenian usage in engineering is not always consistent. If your
   department uses the pair the other way round, swap them in `hy_part4.py` — but swap
   **both**, or slide 8 and Poll 2 will contradict each other.
2. **լուծունակություն (resolution).** Also seen as *թույլատրողականություն* or
   *լուծաչափ*. Whichever you prefer, it must stay distinct from ճշտություն, because
   Poll 2 of Lecture 2 exists precisely to separate them.
3. **շեղում** is doing double duty for *drift* and, in *զրոյական շեղում*, for *offset*.
   That is tolerable in prose but if you find students conflating them, consider
   **դրեյֆ** for drift throughout, which the dictionaries already use in a few places.

## Deliberate choices you may want to change

- **MEMS stays "MEMS"**, not ՄԷՄՀ. It is how the field, the datasheets and the search
  engines write it. The full Armenian name appears on the title slide.
- **Numbers, units and register values stay Latin** — `0.061 mg/LSB`, `0x6B`, `µg/√Hz`.
- **Speaker notes are still in English.** They are instructor-facing working notes, not
  student material. Say the word and they can be translated too (~5 800 words).
- **Part A / Part B / Part C** became **Սարք Ա / Սարք Բ / Սարք Գ**, and poll options
  A–E are read as Ա–Ե in the answer slides.

## Fonts — do not change casually

Armenian text is set in **DejaVu Sans** (and DejaVu Sans Mono where the original was
monospaced). This was tested, not guessed:

- **Arial and Courier New have no Armenian glyphs at all.**
- **Noto Sans Armenian was rejected.** It has no Latin digits, so the renderer
  substitutes them one glyph at a time and every number comes out spaced like
  `0 . 0 6 1`. In a course made of numbers that is unusable.
- DejaVu Sans renders Armenian, Latin, digits and `µ √ ± ° ∝` correctly.

If you open the decks on a machine without DejaVu Sans (most Windows installs), the
Armenian will still appear but in a substituted font. Installing DejaVu Sans — it is
free — makes them look as intended everywhere.

## Rebuilding after an edit

```bash
cd lectures/tools
.venv/bin/python translate_deck.py      # rebuilds both -HY.pptx from the English decks
```

The English decks are never modified. If you change a lecture, rebuild it first
(`build_l1.py` / `build_l2.py`) and then rerun the translator so both languages stay in
step. Any string the dictionary does not cover is listed in `i18n/_untranslated.txt`
after each run — currently 43 entries, all of them pure numbers and units that
correctly need no translation.
