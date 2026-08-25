# -*- coding: utf-8 -*-
"""Armenian translations, part 2 — Lecture 1: polls 2–4, scaling, specification."""
HY = {
# ── poll 2 ───────────────────────────────────────────────────────────────────
"POLL 2   ·   MINUTE 24": "ՀԱՐՑՈՒՄ 2   ·   ՐՈՊԵ 24",
"An accelerometer with 0.061 mg resolution is bolted to a motor housing through a 5 mm "
"rubber pad. Which stage has already destroyed the accuracy of the reported number?":
    "0.061 mg լուծունակությամբ աքսելերոմետրը ամրացված է շարժիչի իրանին 5 մմ ռետինե "
    "միջադիրի միջոցով։ Ո՞ր փուլն է արդեն ոչնչացրել հաղորդված թվի ճշտությունը",
"Digitisation — 16 bits cannot support three decimal places":
    "Թվայնացումը — 16 բիթը չի կարող ապահովել երեք տասնորդական նշան",
"Unit conversion — mg was never converted to m/s²":
    "Միավորների ձևափոխումը — mg-ը երբեք չի վերածվել m/s²-ի",
"Mechanical coupling — the rubber pad filters the vibration before any electronics "
"see it":
    "Մեխանիկական կապակցումը — ռետինե միջադիրը ֆիլտրում է թրթռումը, մինչ էլեկտրոնիկան "
    "տեսնի այն",
"No stage — 0.061 mg resolution guarantees the digits are meaningful":
    "Ոչ մի փուլ — 0.061 mg լուծունակությունը երաշխավորում է, որ նշանները իմաստալից են",
"Vote alone first. Then find someone who disagrees with you.":
    "Նախ քվեարկե՛ք ինքնուրույն։ Ապա գտե՛ք մեկին, ով համաձայն չէ ձեզ հետ։",
"POLL 2   ·   MINUTE 24   ·   ANSWER": "ՀԱՐՑՈՒՄ 2   ·   ՐՈՊԵ 24   ·   ՊԱՏԱՍԽԱՆ",
"The measurement chain begins before the sensor. If the mechanical path lies to the "
"proof mass, no downstream precision recovers the truth.":
    "Չափման շղթան սկսվում է տվիչից առաջ։ Եթե մեխանիկական ուղին «ստում է» իներցիոն "
    "զանգվածին, հետագա ոչ մի ճշգրտություն ճշմարտությունը չի վերականգնի։",
"HOLD ON TO THIS": "ՊԱՀԵ՛Ք ՍԱ",
"The chain begins before": "Շղթան սկսվում է",
"the sensor.": "տվիչից առաջ։",
"Your instrument includes the bolt, the bracket and the housing. None of them are in "
"the datasheet, and all of them are yours.":
    "Ձեր չափիչ սարքը ներառում է պտուտակը, ամրակն ու իրանը։ Դրանցից ոչ մեկը datasheet-ում "
    "չկա, և բոլորն էլ ձե՛րն են։",

# ── chunk 2: scaling ─────────────────────────────────────────────────────────
"CHUNK 2  ·  MINUTES 26–44": "ՄԱՍ 2  ·  ՐՈՊԵ 26–44",
"Why micro is different": "Ինչու է միկրոաշխարհը այլ",
"You have spent three years building intuition on machines you can hold.":
    "Երեք տարի ձեռք եք բերել ինտուիցիա մեքենաների վրա, որ կարող եք ձեռքում պահել։",
"At the micrometre scale, half of that intuition inverts. Here is which half.":
    "Միկրոմետրային մասշտաբում այդ ինտուիցիայի կեսը շրջվում է։ Ահա՛ թե որ կեսը։",
"What is actually inside": "Ինչ կա իրականում ներսում",
"A capacitive MEMS accelerometer, in cross-section":
    "Ունակային MEMS աքսելերոմետր՝ լայնական կտրվածքով",
"FIXED PLATE": "ԱՆՇԱՐԺ ԹԻԹԵՂ",
"PROOF MASS  m": "ԻՆԵՐՑԻՈՆ ԶԱՆԳՎԱԾ  m",
"suspension": "առաձգական",
"beams,  k": "հեծաններ,  k",
"gap  d ≈ 1–2 µm": "բացակ  d ≈ 1–2 µm",
"gap  d": "բացակ  d",
"Acceleration moves the mass. Movement changes both gaps — one grows, one shrinks — "
"and the differential capacitance C = εA/d is the signal.":
    "Արագացումը շարժում է զանգվածը։ Շարժումը փոխում է երկու բացակները — մեկը մեծանում է, "
    "մյուսը՝ փոքրանում — և դիֆերենցիալ ունակությունը C = εA/d հանդիսանում է ազդանշանը։",
"That is the whole device — everything in the datasheet is a consequence of m, k and d.":
    "Ահա՛ ամբողջ սարքը — datasheet-ի ամեն ինչ m, k և d-ի հետևանք է։",
"Shrink every dimension by the same factor": "Փոքրացրե՛ք բոլոր չափերը նույն գործակցով",
"Isotropic scaling: length, width, thickness — all by factor s":
    "Իզոտրոպ մասշտաբում. երկարություն, լայնություն, հաստություն — բոլորը s գործակցով",
"mass scales with volume": "զանգվածը մասշտաբվում է ծավալի հետ",
"beam stiffness  k = E·w·t³ / 4L³": "հեծանի կոշտություն  k = E·w·t³ / 4L³",
"They do not scale together.  That single fact is the whole lecture.":
    "Նրանք միասին չեն մասշտաբվում։  Այս մեկ փաստն է ամբողջ դասախոսությունը։",
"Substitute w, t and L all by the same factor s into k = E·w·t³/4L³ and you get "
"s·s³/s³ = s. Stiffness falls linearly. Mass falls cubically.":
    "Տեղադրե՛ք w, t և L-ը նույն s գործակցով k = E·w·t³/4L³ բանաձևում և կստանաք "
    "s·s³/s³ = s։ Կոշտությունը նվազում է գծայնորեն։ Զանգվածը՝ խորանարդորեն։",
"So the resonant frequency rises": "Ուստի ռեզոնանսային հաճախությունը աճում է",
"Shrink the device by 10  →  its resonant frequency rises by 10":
    "Փոքրացրե՛ք սարքը 10 անգամ  →  ռեզոնանսային հաճախությունը աճում է 10 անգամ",
"Device": "Սարք",
"Typical size": "Բնորոշ չափ",
"Resonance": "Ռեզոնանս",
"Bridge span": "Կամրջի թռիչք",
"Tuning fork": "Կարգաբերիչ պատառաքաղ",
"MEMS accelerometer": "MEMS աքսելերոմետր",
"MEMS gyroscope drive": "MEMS գիրոսկոպի շարժիչ",
"MEMS RF resonator": "MEMS ՌՀ ռեզոնատոր",
"This is why MEMS can": "Ահա թե ինչու MEMS-ը",
"measure fast things.": "կարող է չափել արագ երևույթներ։",
"A sensor cannot report": "Տվիչը չի կարող հավաստի",
"signals near its own": "հաղորդել իր սեփական ռեզոնանսին",
"resonance — so a high": "մոտ ազդանշանները — ուստի բարձր",
"f₀ is what buys you": "f₀-ն է, որ ապահովում է",
"bandwidth.": "թողունակությունը։",

# ── poll 3 ───────────────────────────────────────────────────────────────────
"POLL 3   ·   MINUTE 40": "ՀԱՐՑՈՒՄ 3   ·   ՐՈՊԵ 40",
"A MEMS accelerometer's proof mass and suspension beams are all scaled down by a "
"factor of 10. Which statement is true?":
    "MEMS աքսելերոմետրի իներցիոն զանգվածը և առաձգական հեծանները փոքրացվել են 10 անգամ։ "
    "Ո՞ր պնդումը ճիշտ է",
"Resonant frequency rises ×10, and thermomechanical noise gets worse":
    "Ռեզոնանսային հաճախությունը աճում է ×10, և ջերմամեխանիկական աղմուկը վատանում է",
"Resonant frequency falls ×10, and noise improves because it is smaller":
    "Ռեզոնանսային հաճախությունը նվազում է ×10, և աղմուկը լավանում է, քանի որ սարքը փոքր է",
"Resonant frequency is unchanged — mass and stiffness both shrink, so the ratio is "
"constant":
    "Ռեզոնանսային հաճախությունը չի փոխվում — զանգվածն ու կոշտությունը փոքրանում են, "
    "ուստի հարաբերությունը հաստատուն է",
"Resonant frequency rises ×10, and noise improves because there is less material to "
"vibrate":
    "Ռեզոնանսային հաճախությունը աճում է ×10, և աղմուկը լավանում է, քանի որ քիչ նյութ է "
    "թրթռում",
"The hardest question of the lecture. Use the two exponents on the board, not your "
"intuition.":
    "Դասախոսության ամենադժվար հարցը։ Օգտագործե՛ք գրատախտակի երկու ցուցիչները, ոչ թե "
    "ձեր ինտուիցիան։",
"POLL 3   ·   MINUTE 40   ·   ANSWER": "ՀԱՐՑՈՒՄ 3   ·   ՐՈՊԵ 40   ·   ՊԱՏԱՍԽԱՆ",
"Thermomechanical noise ∝ √(4kBT·ω₀ / mQ) — it rises as the proof mass falls. You buy "
"bandwidth and you pay in noise floor.":
    "Ջերմամեխանիկական աղմուկը ∝ √(4kBT·ω₀ / mQ) — աճում է, երբ իներցիոն զանգվածը "
    "նվազում է։ Դուք ձեռք եք բերում թողունակություն և վճարում աղմուկի հատակով։",
"Smaller is not uniformly better": "Փոքրը միանշանակ ավելի լավը չէ",
"The honest ledger of shrinking a device": "Սարքի փոքրացման ազնիվ հաշվեկազմը",
"GETS BETTER": "ԼԱՎԱՆՈՒՄ Է",
"GETS WORSE": "ՎԱՏԱՆՈՒՄ Է",
"▸  Bandwidth — f₀ ∝ 1/L": "▸  Թողունակություն — f₀ ∝ 1/L",
"▸  Thermomechanical noise floor ∝ 1/√m": "▸  Աղմուկի հատակ ∝ 1/√m",
"▸  Response time and thermal settling": "▸  Արձագանքում և ջերմային կայունացում",
"▸  Stiction — surface forces beat body forces":
    "▸  Կպչողություն — մակերևույթն է գերիշխում",
"▸  Power per device": "▸  Հզորություն մեկ սարքի հաշվով",
"▸  Sensitivity to packaging stress": "▸  Զգայունություն փաթեթի լարվածությանը",
"▸  Cost per device at volume": "▸  Արժեք մեկ սարքի հաշվով, մեծ ծավալում",
"▸  Temperature drift and offset stability":
    "▸  Ջերմային շեղում և զրոյի կայունություն",
"▸  Batch fabrication: thousands per wafer":
    "▸  Խմբաքանակ՝ հազարներ մեկ թիթեղից",
"▸  Contamination: a dust speck is fatal": "▸  Աղտոտում. փոշին ճակատագրական է",
"Surface area / volume  ∝  1 / L   —   at small scale the world is all surface.":
    "Մակերես / ծավալ  ∝  1 / L   —   փոքր մասշտաբում աշխարհն ամբողջովին մակերես է։",

# ── state change ─────────────────────────────────────────────────────────────
"MINUTE 44  ·  EVERYBODY STANDS UP": "ՐՈՊԵ 44  ·  ԲՈԼՈՐԸ ՈՏՔԻ",
"Slides off. Paper out.": "Սլայդներն անջատած։ Թուղթը դուրս։",
"Stand up. Actually stand.": "Ոտքի՛ ելեք։ Իսկապես ոտքի։",
"In pairs, one sheet: redraw the measurement chain from memory. Every box, every "
"arrow. 90 seconds.":
    "Զույգերով, մեկ թերթ. վերագծե՛ք չափման շղթան հիշողությամբ։ Ամեն վանդակ, ամեն սլաք։ "
    "90 վայրկյան։",
"Mark an X on every box where the motor's number could have been ruined.":
    "X նշե՛ք ամեն վանդակի վրա, որտեղ շարժիչի թիվը կարող էր փչանալ։",
"Keep this sheet. You will use it at the bench in Week 2.":
    "Պահե՛ք այս թերթը։ Կօգտագործեք լաբորատորիայում 2-րդ շաբաթում։",
"Check your sheet": "Ստուգե՛ք ձեր թերթը",
"Correct in a different colour — do not rewrite it":
    "Ուղղե՛ք այլ գույնով — չվերագրեք",
"Two boxes are forgotten more than any others: mechanical coupling, and timestamping.":
    "Երկու վանդակ ամենից շատ մոռացվում է՝ մեխանիկական կապակցումը և ժամանականիշը։",
"Both are invisible in a datasheet. Both are yours.":
    "Երկուսն էլ datasheet-ում անտեսանելի են։ Երկուսն էլ ձե՛րն են։",

# ── chunk 3: specification ───────────────────────────────────────────────────
"CHUNK 3  ·  MINUTES 48–66": "ՄԱՍ 3  ·  ՐՈՊԵ 48–66",
"From a wish to a specification": "Ցանկությունից՝ տեխնիկական բնութագիր",
"Nobody will ever hand you a specification. They will hand you a sentence":
    "Ոչ ոք ձեզ երբեք տեխնիկական բնութագիր չի տա։ Ձեզ կտան մի նախադասություն՝",
"like the one on the next slide, and expect an instrument at the end of it.":
    "հաջորդ սլայդի նման, և վերջում կսպասեն չափիչ սարք։",
"THE CLIENT SAYS": "ՊԱՏՎԻՐԱՏՈՒՆ ԱՍՈՒՄ Է",
"“Just tell me if the motor": "«Ուղղակի ասե՛ք՝ արդյոք շարժիչը",
"is vibrating too much.”": "չափազանց թրթռում է»։",
"This is what a request actually looks like. It contains no quantity, no range, no "
"bandwidth, no accuracy and no environment. It is not yet an engineering problem.":
    "Ահա՛ իրական պահանջի տեսքը։ Այն չի պարունակում ո՛չ մեծություն, ո՛չ տիրույթ, ո՛չ "
    "թողունակություն, ո՛չ ճշտություն, ո՛չ միջավայր։ Սա դեռ ինժեներական խնդիր չէ։",
"Seven questions that turn a wish into a specification":
    "Յոթ հարց՝ ցանկությունից դեպի բնութագիր",
"What physical variable, in what units?": "Ո՞ր ֆիզիկական մեծությունը, ո՞ր միավորներով",
"RANGE": "ՏԻՐՈՒՅԹ",
"Smallest and largest value that must be reported?":
    "Նվազագույն և առավելագույն արժեքը, որ պետք է հաղորդվի",
"RESOLUTION": "ԼՈՒԾՈՒՆԱԿՈՒԹՅՈՒՆ",
"Smallest change that must be distinguishable?":
    "Նվազագույն փոփոխությունը, որ պետք է տարբերակելի լինի",
"ACCURACY": "ՃՇՏՈՒԹՅՈՒՆ",
"How wrong is a reading allowed to be — and over what temperature?":
    "Որքա՞ն կարող է սխալ լինել ցուցմունքը — և ո՞ր ջերմաստիճաններում",
"BANDWIDTH": "ԹՈՂՈՒՆԱԿՈՒԹՅՈՒՆ",
"How fast does it change? What is the highest frequency that matters?":
    "Որքա՞ն արագ է փոփոխվում։ Ո՞րն է կարևոր առավելագույն հաճախությունը",
"ENVIRONMENT": "ՄԻՋԱՎԱՅՐ",
"Temperature, humidity, vibration, EMI, supply, power budget?":
    "Ջերմաստիճան, խոնավություն, թրթռում, խանգարումներ, սնում, հզորություն",
"OUTPUT": "ԵԼՔ",
"Who consumes the number, in what form, how often, timestamped how?":
    "Ո՞վ, ի՞նչ ձևով, ի՞նչ հաճախությամբ, ի՞նչ ժամանականիշով",
"One of these seven killed the motor. You already know which one.":
    "Այս յոթից մեկը սպանեց շարժիչը։ Դուք արդեն գիտեք՝ որը։",
"The same request, specified": "Նույն պահանջը՝ բնութագրված",
"Now it is something you can order against": "Այժմ սա մի բան է, ըստ որի կարելի է պատվիրել",
"Specification": "Բնութագիր",
"Where the number came from": "Որտեղից է եկել թիվը",
"Quantity": "Մեծություն",
"housing acceleration, m/s² RMS": "իրանի արագացում, m/s² RMS",
"vibration is what a bearing radiates": "առանցքակալը ճառագայթում է հենց թրթռում",
"Range": "Տիրույթ",
"impact transients, not steady vibration":
    "հարվածային անցողիկ պրոցեսներ, ոչ կայուն թրթռում",
"Resolution": "Լուծունակություն",
"earliest detectable fault ≈ 30 mg": "ամենավաղ հայտնաբերելի վնասվածքը ≈ 30 mg",
"Accuracy": "Ճշտություն",
"±5 % of reading, 0–70 °C": "±5 % ցուցմունքից, 0–70 °C",
"trend detection, not absolute metrology":
    "միտումի հայտնաբերում, ոչ բացարձակ չափագիտություն",
"Bandwidth": "Թողունակություն",
"≥ 4 kHz, anti-aliased": "≥ 4 kHz, հակաալիասինգային",
"bearing signature spans 1–4 kHz": "առանցքակալի ստորագրությունը 1–4 kHz տիրույթում է",
"Environment": "Միջավայր",
"0–70 °C, 24 V rail, oily, EMI from a VFD":
    "0–70 °C, 24 V սնում, յուղոտ, էլմագ. խանգարումներ հաճախակարգավորիչից",
"the motor's actual cabinet": "շարժիչի իրական պահարանը",
"Output": "Ելք",
"RMS + spectrum, 1 Hz, timestamped ±1 ms":
    "RMS + սպեկտր, 1 Hz, ժամանականիշ ±1 ms",
"so a frequency can be computed": "որպեսզի հաճախությունը հաշվարկելի լինի",
"Seven lines. This is the deliverable — not a part number.":
    "Յոթ տող։ Ահա՛ արդյունքը — ոչ թե սարքի կոդը։",
"Your turn": "Ձեր հերթն է",
"Four minutes, in pairs — write the seven lines":
    "Չորս րոպե, զույգերով — գրե՛ք յոթ տողը",
"“The drone keeps drifting up and down. Make it hold its altitude properly.”":
    "«Դրոնը շարունակ վեր-վար է գնում։ Արե՛ք, որ բարձրությունը նորմալ պահի»։",
"Start here": "Սկսե՛ք այստեղից",
"What is the physical quantity?": "Ո՞րն է ֆիզիկական մեծությունը",
"It is probably not altitude.": "Հավանաբար բարձրությունը չէ։",
"The hard one": "Դժվարը",
"What bandwidth? How fast does": "Ի՞նչ թողունակություն։ Որքա՞ն արագ",
"a drone's altitude actually change?": "է իրականում փոխվում դրոնի բարձրությունը",
"The trap": "Թակարդը",
"What is the RANGE — and is it the": "Ո՞րն է ՏԻՐՈՒՅԹԸ — և արդյոք նույնն է,",
"same as the RESOLUTION you need?": "ինչ անհրաժեշտ ԼՈՒԾՈՒՆԱԿՈՒԹՅՈՒՆԸ",
"You will not finish all seven lines. Get three right.":
    "Յոթ տողն ամբողջությամբ չեք ավարտի։ Երեքը ճի՛շտ արեք։",

# ── poll 4 ───────────────────────────────────────────────────────────────────
"POLL 4   ·   MINUTE 62": "ՀԱՐՑՈՒՄ 4   ·   ՐՈՊԵ 62",
"Bearing fault energy appears between 1 and 4 kHz. Which single specification line "
"decides whether your system can work at all?":
    "Առանցքակալի վնասվածքի էներգիան հայտնվում է 1–4 kHz տիրույթում։ Բնութագրի ո՞ր մեկ "
    "տողն է որոշում՝ ընդհանրապես կաշխատի՞ ձեր համակարգը",
"Full-scale range ≥ ±16 g": "Չափման լրիվ տիրույթ ≥ ±16 g",
"Bandwidth ≥ 4 kHz, sample rate ≥ 8 kHz, with anti-alias filtering":
    "Թողունակություն ≥ 4 kHz, նմուշառում ≥ 8 kHz, հակաալիասինգային ֆիլտրով",
"Resolution ≤ 0.1 mg": "Լուծունակություն ≤ 0.1 mg",
"Operating temperature up to 85 °C": "Աշխատանքային ջերմաստիճան մինչև 85 °C",
"Every one of these four is a real requirement. Only one of them, if you get it wrong, "
"makes the system incapable rather than merely imperfect.":
    "Այս չորսից ամեն մեկը իրական պահանջ է։ Միայն մեկը, սխալ լինելու դեպքում, համակարգը "
    "դարձնում է անկարող, ոչ պարզապես անկատար։",
"POLL 4   ·   MINUTE 62   ·   ANSWER": "ՀԱՐՑՈՒՄ 4   ·   ՐՈՊԵ 62   ·   ՊԱՏԱՍԽԱՆ",
"A, C and D are all genuine requirements — get them wrong and the system is imperfect. "
"Get B wrong and the system is blind.":
    "Ա, Գ և Դ-ն իրական պահանջներ են — սխալվեք, և համակարգը կլինի անկատար։ Սխալվե՛ք Բ-ում, "
    "և համակարգը կլինի կո՛ւյր։",
}
