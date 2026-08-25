# -*- coding: utf-8 -*-
"""Armenian translations, part 3 — Lecture 1: project, synthesis, aliasing, close."""
HY = {
"The semester project": "Կիսամյակային նախագիծը",
"Deliverable 1 is due before Lecture 3": "Առաջին արդյունքը՝ մինչև 3-րդ դասախոսությունը",
"WHAT YOU WILL BUILD": "ԻՆՉ ԿԿԱՌՈՒՑԵՔ",
"A multi-sensor embedded system that": "Բազմատվիչ ներդրված համակարգ, որը",
"measures something real, calibrated,": "չափում է իրական մեծություն՝ ստուգաչափված,",
"filtered, timestamped, validated against": "ֆիլտրված, ժամանականիշով, վալիդացված",
"stated requirements — and honest about": "հայտարարված պահանջների նկատմամբ — և ազնիվ",
"its own limitations.": "իր սահմանափակումների վերաբերյալ։",
"DELIVERABLE 1  ·  ONE PAGE": "ԱՐԴՅՈՒՆՔ 1  ·  ՄԵԿ ԷՋ",
"The seven specification lines, for a": "Յոթ բնութագրային տողերը՝ ձեր ընտրած",
"measurement problem you choose.": "չափման խնդրի համար։",
"No part numbers. No circuit. No code.": "Ոչ մի սարքի կոդ։ Ոչ սխեմա։ Ոչ ծրագիր։",
"Just the seven lines — each with": "Միայն յոթ տողը — յուրաքանչյուրը",
"the reason it has that value.": "իր արժեքի հիմնավորմամբ։",
"Teams of 2–3. Same teams as the laboratory. Choose your measurand this week.":
    "2–3 հոգանոց խմբեր։ Նույն խմբերը, ինչ լաբորատորիայում։ Ընտրե՛ք ձեր չափվող մեծությունը "
    "այս շաբաթ։",

# ── synthesis ────────────────────────────────────────────────────────────────
"Back to the motor": "Վերադառնանք շարժիչին",
"Before I tell you — commit, physically": "Մինչ ասեմ — որոշե՛ք, ֆիզիկապես",
"Put your finger on the box where you now think this failed. Everyone. I am looking.":
    "Մատը դրե՛ք այն վանդակի վրա, որտեղ հիմա կարծում եք՝ սա ձախողվեց։ Բոլորը։ Ես նայում եմ։",
"The three numbers from the post-mortem": "Հետագա քննության երեք թիվը",
"the bearing fault signature": "առանցքակալի վնասվածքի ստորագրությունը",
"the sample rate somebody chose": "նմուշառման հաճախությունը, որ ինչ-որ մեկն ընտրել է",
"none": "ոչ մի",
"anti-alias filter fitted": "տեղադրված հակաալիասինգային ֆիլտր",
"Sampling at 100 Hz, everything above 50 Hz is folded down into the band —":
    "100 Hz նմուշառման դեպքում 50 Hz-ից վեր ամեն ինչ ծալվում է շերտի ներս —",
"and with no filter in front of the ADC, there was nothing to stop it.":
    "և քանի որ ԱԹԿ-ից առաջ ֆիլտր չկար, ոչինչ չէր կանգնեցնում այն։",
"Nyquist: to see 1520 Hz you need to sample above 3040 Hz. They sampled 30 times too "
"slowly.":
    "Նայքվիստ. 1520 Hz տեսնելու համար պետք է նմուշառել 3040 Hz-ից վեր։ Նրանք նմուշառել են "
    "30 անգամ դանդաղ։",
"Where the 20 Hz line came from": "Որտեղից եկավ 20 Hz գիծը",
"Drawn at 19 cycles per 20 samples so you can see it — the motor's ratio was 1520:100, "
"identical arithmetic":
    "Գծված է 19 պարբերություն 20 նմուշի դիմաց, որ տեսանելի լինի — շարժիչի հարաբերությունն "
    "էր 1520:100, նույն թվաբանությունը",
"the real vibration  ·  19 cycles": "իրական թրթռումը  ·  19 պարբերություն",
"what the samples reconstruct  ·  1 cycle":
    "ինչ վերականգնում են նմուշները  ·  1 պարբերություն",
"red dots =": "կարմիր կետերը =",
"the only instants": "միայն այն պահերը,",
"the ADC looked": "երբ ԱԹԿ-ն նայել է",
"The monitor was faithfully displaying the destruction of the bearing - relabelled as "
"a slow load variation.":
    "Հսկիչը ճշգրտորեն ցույց էր տալիս առանցքակալի քայքայումը՝ պիտակավորված որպես բեռի "
    "դանդաղ փոփոխություն։",
"THE VERDICT": "ԴԱՏԱՎՃԻՌԸ",
"Nothing was broken.": "Ոչինչ խափանված չէր։",
"Every part met spec.": "Ամեն մասը համապատասխանում էր բնութագրին։",
"The system was never specified.": "Համակարգը երբեք բնութագրված չէր։",
"Aliasing is permanent. No filter afterwards, no clever software, no machine learning "
"recovers a frequency you failed to sample.":
    "Ալիասինգը անվերադարձ է։ Ոչ մի հետագա ֆիլտր, ոչ խելացի ծրագիր, ոչ մեքենայական "
    "ուսուցում չի վերականգնի հաճախությունը, որը չեք նմուշառել։",
"What was missing": "Ինչը բացակայում էր",
"One line, in one document, that nobody wrote":
    "Մեկ տող, մեկ փաստաթղթում, որը ոչ ոք չգրեց",
"One line. One motor.": "Մեկ տող։ Մեկ շարժիչ։",
"This is also your answer to Poll 4 — option B. And it is the specification line you "
"were asked to write fifteen minutes ago.":
    "Սա նաև ձեր պատասխանն է 4-րդ հարցմանը — տարբերակ Բ։ Եվ սա հենց այն բնութագրային տողն "
    "է, որը ձեզ խնդրեցի գրել տասնհինգ րոպե առաջ։",
"Lecture 3 is about how that line becomes an ADC configuration. Laboratory 2 is where "
"you make aliasing happen with your own hands.":
    "3-րդ դասախոսությունը այն մասին է, թե ինչպես այդ տողը դառնում է ԱԹԿ-ի կարգավորում։ "
    "2-րդ լաբորատորիայում ալիասինգը կստեղծեք ձեր ձեռքերով։",

# ── summary and close ────────────────────────────────────────────────────────
"Four things to keep": "Չորս բան՝ հիշելու",
"A measurement is a chain, and it begins before the sensor.":
    "Չափումը շղթա է, և այն սկսվում է տվիչից առաջ։",
"Bolt, bracket and housing are part of your instrument.":
    "Պտուտակը, ամրակն ու իրանը ձեր չափիչ սարքի մասն են։",
"Some losses are permanent.": "Որոշ կորուստներ անվերադարձ են։",
"Aliasing and a missing timestamp cannot be repaired downstream.":
    "Ալիասինգը և բացակայող ժամանականիշը հետագայում ուղղելի չեն։",
"Shrinking a device is a trade, not an improvement.":
    "Սարքի փոքրացումը փոխզիջում է, ոչ բարելավում։",
"k ∝ L, m ∝ L³, f₀ ∝ 1/L — bandwidth up, noise floor up too.":
    "k ∝ L, m ∝ L³, f₀ ∝ 1/L — թողունակությունը վեր, աղմուկի հատակն էլ վեր։",
"The specification is the deliverable.": "Տեխնիկական բնութագիրն է արդյունքը։",
"Seven lines, each with a reason. Part numbers come afterwards.":
    "Յոթ տող, յուրաքանչյուրը հիմնավորմամբ։ Սարքերի կոդերը գալիս են հետո։",
"Exit ticket": "Ելքի տոմս",
"Anonymous. Hand it in at the door — both halves.":
    "Անանուն։ Հանձնե՛ք դռան մոտ — երկու մասն էլ։",
"1  ·  ONE SPECIFICATION LINE": "1  ·  ՄԵԿ ԲՆՈՒԹԱԳՐԱՅԻՆ ՏՈՂ",
"A drone must hold altitude to ±0.5 m.": "Դրոնը պետք է բարձրությունը պահի ±0.5 մ ճշտությամբ։",
"Write ONE specification line for its": "Գրե՛ք ՄԵԿ բնութագրային տող նրա ճնշման",
"pressure sensor — the line you think": "տվիչի համար — այն տողը, որը կարծում եք",
"matters most, with its number.": "ամենակարևորն է, իր թվով։",
"2  ·  MUDDIEST POINT": "2  ·  ԱՄԵՆԱԱՆՀԱՍԿԱՆԱԼԻ ԿԵՏԸ",
"What is the one thing from today you": "Ո՞րն է այսօրվանից այն մեկ բանը, որում",
"are least sure about?": "ամենաքիչ վստահ եք",
"One sentence. I will answer the three": "Մեկ նախադասություն։ Երեք ամենահաճախ",
"most common at the start of Lecture 2.": "հանդիպողին կպատասխանեմ 2-րդ դասախոսության սկզբում։",
"This is the first time this course has been taught. Your muddiest points genuinely "
"change what happens next week.":
    "Այս դասընթացը դասավանդվում է առաջին անգամ։ Ձեր անհասկանալի կետերը իրապես փոխում են "
    "այն, ինչ տեղի կունենա հաջորդ շաբաթ։",

# ── lab bridge ───────────────────────────────────────────────────────────────
"Week 2: Laboratory 1": "2-րդ շաբաթ. Լաբորատորիա 1",
"Datasheet to data — and yes, it is before the theory":
    "Datasheet-ից տվյալ — և այո, դա տեսությունից առաջ է",
"At the bench you will": "Լաբորատորիայում դուք",
"Which chain stage": "Շղթայի որ փուլը",
"Read supply and logic levels from the datasheet BEFORE applying power":
    "Կկարդաք սնման և տրամաբանական մակարդակները datasheet-ից ՄԻՆՉ լարման միացումը",
"before stage 1": "1-ին փուլից առաջ",
"Wire one I²C sensor to the Nucleo board, with pull-ups":
    "Կմիացնեք մեկ I²C տվիչ Nucleo տախտակին՝ ձգող դիմադրություններով",
"stage 3 → 5": "փուլ 3 → 5",
"Prove the device is the device you think it is  (device-ID register)":
    "Կապացուցեք, որ սարքը հենց այն սարքն է  (սարքի ID ռեգիստր)",
"stage 5": "փուլ 5",
"Configure a full-scale range and an output data rate":
    "Կկարգավորեք չափման տիրույթը և ելքային տվյալների հաճախությունը",
"Convert raw two's-complement codes to SI units — by hand":
    "Կվերածեք չմշակված լրացուցիչ կոդերը ՄՀ միավորների — ձեռքով",
"stage 6": "փուլ 6",
"Prove the number is true: one axis must read ≈ 9.81 m/s² at rest":
    "Կապացուցեք, որ թիվը ճիշտ է. հանգստի վիճակում մեկ առանցքը պետք է ցույց տա ≈ 9.81 m/s²",
"No programming. The boards are already flashed — you drive the sensor from a serial "
"console.":
    "Ոչ մի ծրագրավորում։ Տախտակները արդեն ծրագրավորված են — տվիչը կառավարում եք "
    "սերիական կոնսոլից։",
"The pre-lab sheet is a gate: no signed pre-lab, no power to your board.":
    "Նախալաբորատոր թերթը արգելակ է. առանց ստորագրված նախալաբորատորի՝ լարում չկա։",
"It carries a one-page I²C primer and the console reference — read it before Tuesday.":
    "Այն պարունակում է մեկ էջ I²C ներածություն և կոնսոլի ուղեցույցը — կարդացե՛ք մինչ երեքշաբթի։",
"NEXT": "ՀԱՋՈՐԴԸ",
"Lecture 2": "Դասախոսություն 2",
"Sensor specifications and datasheet-based selection":
    "Տվիչների բնութագրերը և ընտրությունը datasheet-ի հիման վրա",
"Bring a laptop or a printed datasheet. We are going to find a number that decides a "
"design — and it will not be on the front page.":
    "Բերե՛ք նոութբուք կամ տպված datasheet։ Կգտնենք մի թիվ, որը որոշում է նախագիծը — և այն "
    "առաջին էջում չի լինելու։",
"BEFORE NEXT WEEK": "ՄԻՆՉ ՀԱՋՈՐԴ ՇԱԲԱԹ",
"1 ·  Formative quiz (6 questions, ungraded) — posted tonight":
    "1 ·  Ձևավորող թեստ (6 հարց, առանց գնահատականի) — կտեղադրվի այսօր երեկոյան",
"2 ·  Pre-lab sheet for Laboratory 1, including the I²C primer":
    "2 ·  Նախալաբորատոր թերթ Լաբորատորիա 1-ի համար, ներառյալ I²C ներածությունը",
"3 ·  Project deliverable 1: your seven specification lines":
    "3 ·  Նախագծի արդյունք 1. ձեր յոթ բնութագրային տողերը",
"4 ·  Reading: Fraden, Handbook of Modern Sensors — Ch. 1–2":
    "4 ·  Ընթերցանություն. Fraden, Handbook of Modern Sensors — գլ. 1–2",
}
