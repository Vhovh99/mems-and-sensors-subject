# -*- coding: utf-8 -*-
"""Armenian translations, part 1 — Lecture 1: opening, the chain, scaling.

Keys are the exact English strings as they appear in the built deck.
Edit a value here and rebuild; nothing else needs touching.
"""
HY = {
# ── title and hook ───────────────────────────────────────────────────────────
"MICROELECTROMECHANICAL SYSTEMS AND SENSORS":
    "ՄԻԿՐՈԷԼԵԿՏՐԱՄԵԽԱՆԻԿԱԿԱՆ ՀԱՄԱԿԱՐԳԵՐ ԵՎ ՏՎԻՉՆԵՐ",
"MEMS, sensors, and the": "MEMS, տվիչներ և",
"measurement-system architecture": "չափման համակարգի կառուցվածքը",
"Lecture 1 of 16   ·   80 minutes   ·   Module A: Foundations":
    "Դասախոսություն 1 / 16   ·   80 րոպե   ·   Բաժին Ա. Հիմունքներ",
"Bachelor programme · Electrical Engineering · 7th semester":
    "Բակալավրիատ · Էլեկտրատեխնիկա · 7-րդ կիսամյակ",
"Institute of Energy and Electrical Engineering":
    "Էներգետիկայի և էլեկտրատեխնիկայի ինստիտուտ",
"MEMS & Sensors  ·  Lecture 1  ·  Measurement-system architecture":
    "MEMS և տվիչներ  ·  Դասախոսություն 1",
"MINUTE 0  ·  THE HOOK": "ՐՈՊԵ 0  ·  ԳՐԱՎԻՉ ՍԿԻԶԲ",
"The motor that died": "Շարժիչը, որը փչացավ",
"under observation": "հսկողության ներքո",
"A 1500 rpm induction motor.  A vibration monitor.  Six weeks of data.":
    "1500 պտ/րոպե ասինխրոն շարժիչ։  Թրթռման հսկիչ։  Վեց շաբաթվա տվյալներ։",
"WHAT THE SCREEN SHOWED": "ԻՆՉ ՑՈՒՅՑ ԷՐ ՏԱԼԻՍ ԷԿՐԱՆԸ",
"Six weeks of calm": "Վեց շաբաթ՝ հանգիստ",
"20 Hz  ·  amplitude slowly rising  ·  read as normal load variation":
    "20 Hz  ·  ամպլիտուդը դանդաղ աճում է  ·  ընկալվել է որպես բնականոն բեռ",
"WEEK 7": "7-ՐԴ ՇԱԲԱԹ",
"bearing seized": "առանցքակալը խցանվեց",
"motor destroyed": "շարժիչը փչացավ",
"week 1": "1-ին շաբաթ",
"Nothing failed": "Ոչինչ չի խափանվել",
"The post-mortem checked every component":
    "Հետագա քննությունը ստուգել է բոլոր բաղադրիչները",
"The accelerometer": "Աքսելերոմետրը",
"met every number in its datasheet":
    "համապատասխանում էր datasheet-ի բոլոր թվերին",
"The circuit board": "Տպատախտակը",
"no fault found": "անսարքություն չհայտնաբերվեց",
"The firmware": "Ծրագրային ապահովումը",
"no bug found": "սխալ չհայտնաբերվեց",
"The data logger": "Տվյալների գրանցիչը",
"logged every single sample": "գրանցել է ամեն մի նմուշ",
"The engineer": "Ինժեները",
"looked at the screen every week": "ամեն շաբաթ նայել է էկրանին",

# ── poll 1 ───────────────────────────────────────────────────────────────────
"POLL 1   ·   MINUTE 4": "ՀԱՐՑՈՒՄ 1   ·   ՐՈՊԵ 4",
"Where was the fault?": "Որտե՞ղ էր սխալը",
"The accelerometer was too cheap for industrial use":
    "Աքսելերոմետրը չափազանց էժան էր արդյունաբերական կիրառության համար",
"There was a firmware bug nobody found":
    "Ծրագրում սխալ կար, որը ոչ ոք չգտավ",
"Nobody specified the sample rate against the frequency of the fault":
    "Ոչ ոք չսահմանեց նմուշառման հաճախությունը՝ ելնելով վնասվածքի հաճախությունից",
"Bearing degradation cannot be detected by vibration":
    "Առանցքակալի մաշվածությունը հնարավոր չէ հայտնաբերել թրթռման միջոցով",
"The maintenance team ignored a rising trend":
    "Սպասարկող խումբը անտեսեց աճող միտումը",
"Commit now. No discussion. I will show you the answer in the last ten minutes of "
"this lecture — and I want to see whether you change your mind.":
    "Որոշե՛ք հիմա, առանց քննարկման։ Պատասխանը ցույց կտամ վերջին տասը րոպեին — "
    "և կտեսնեմ՝ կփոխե՞ք կարծիքը։",

# ── course framing ───────────────────────────────────────────────────────────
"What this course is": "Ինչ է այս դասընթացը",
"and, just as importantly, what it is not": "և, նույնքան կարևոր՝ ինչ չէ",
"THIS COURSE IS": "ԱՅՍ ԴԱՍԸՆԹԱՑՆ Է",
"Choosing, interfacing, calibrating and": "Իրական տվիչների ընտրություն,",
"validating real sensors inside": "միացում, ստուգաչափում,",
"real embedded systems.": "վալիդացում իրական համակարգերում։",
"IT IS NOT": "ԱՅՆ ՉԷ",
"A cleanroom fabrication course.": "Մաքուր սենյակի արտադրության դասընթաց։",
"We visit fabrication once, in Lecture 4,": "Արտադրությանն անդրադառնում ենք մեկ",
"only as deep as packaging and drift require.":
    "անգամ՝ 4-րդ դասախոսությունում, միայն\nփաթեթավորման և շեղման չափով։",
"The design principle of all sixteen lectures:  understand the measurand → select the "
"sensor → interface it → acquire valid data → calibrate it → process or fuse it → "
"validate it in a system.":
    "Դասընթացի սկզբունքը՝  չափվող մեծությունը → տվիչի ընտրություն → միացում → "
    "վստահելի տվյալներ → ստուգաչափում → մշակում կամ միավորում → վալիդացում։",

# ── outcomes ─────────────────────────────────────────────────────────────────
"By the end of today you can…": "Այսօրվա վերջում դուք կկարողանաք…",
"DRAW": "ԳԾԵԼ",
"the path from a physical quantity to a logged number, and say where information dies":
    "ուղին ֆիզիկական մեծությունից մինչև գրանցված թիվ, և ասել՝ որտեղ է կորչում տեղեկույթը",
"CLASSIFY": "ԴԱՍԵԼ",
"an unfamiliar device: sensor, transducer or actuator — and name its measurand":
    "անծանոթ սարքը՝ տվիչ, փոխակերպիչ թե ակտուատոր — և անվանել չափվող մեծությունը",
"PREDICT": "ԳՈՒՇԱԿԵԼ",
"from scaling laws why MEMS devices are fast — and what gets worse when they shrink":
    "մասշտաբման օրենքներից՝ ինչու են MEMS սարքերն արագ — և ինչը վատանում է փոքրացման դեպքում",
"CONVERT": "ՎԵՐԱԾԵԼ",
"a vague request into a measurement specification you could order against":
    "անորոշ պահանջը չափման բնութագրի, ըստ որի կարելի է պատվեր տալ",
"Notice that all four are verbs. None of them is “know about”.":
    "Ուշադրություն. չորսն էլ բայեր են։ Ոչ մեկը «իմանալ մասին» չէ։",

# ── chunk 1 ──────────────────────────────────────────────────────────────────
"CHUNK 1  ·  MINUTES 8–26": "ՄԱՍ 1  ·  ՐՈՊԵ 8–26",
"The chain": "Շղթան",
"A measurement is not a component. It is a path — and a path is only as":
    "Չափումը բաղադրիչ չէ։ Այն ուղի է — իսկ ուղին ճշմարիտ է այնքան,",
"truthful as its worst link. We are going to build that path one box at a time.":
    "որքան իր ամենաթույլ օղակը։ Այս ուղին կկառուցենք քայլ առ քայլ։",
"Three words we will use precisely": "Երեք բառ, որ կօգտագործենք ճշգրիտ",
"because from here on the difference matters":
    "որովհետև այսուհետ տարբերությունը կարևոր է",
"SENSOR": "ՏՎԻՉ",
"Converts a physical quantity": "Ֆիզիկական մեծությունը վերածում է",
"into a signal you can read.": "ազդանշանի, որը կարող եք կարդալ։",
"MEMS microphone": "MEMS խոսափող",
"sound pressure → voltage": "ձայնային ճնշում → լարում",
"TRANSDUCER": "ՓՈԽԱԿԵՐՊԻՉ",
"Converts energy from one form": "Էներգիան վերածում է մի տեսակից",
"to another. A sensor is one kind.": "մյուսի։ Տվիչը դրա տեսակներից է։",
"loudspeaker, strain gauge,": "բարձրախոս, դեֆորմացիայի տվիչ,",
"piezo disc — either direction": "պիեզո սկավառակ — երկու ուղղությամբ",
"ACTUATOR": "ԱԿՏՈՒԱՏՈՐ",
"Converts a signal into a": "Ազդանշանը վերածում է",
"physical action on the world.": "ֆիզիկական ազդեցության աշխարհի վրա։",
"MEMS mirror": "MEMS հայելի",
"voltage → beam deflection": "լարում → ճառագայթի շեղում",
"Every actuator in this course is also a measurement problem: you only know it acted "
"if you sense the result.":
    "Այս դասընթացում ամեն ակտուատոր նաև չափման խնդիր է. դուք գիտեք, որ այն գործել է, "
    "միայն եթե զգում եք արդյունքը։",
"Thirty seconds": "Երեսուն վայրկյան",
"Sensor, transducer or actuator? And what is the measurand?":
    "Տվիչ, փոխակերպիչ թե ակտուատոր։ Իսկ ո՞րն է չափվող մեծությունը",
"MEMS": "MEMS",
"microphone": "խոսափող",
"?": "?",
"Piezo": "Պիեզո",
"buzzer": "ազդանշանիչ",
"Strain": "Դեֆորմացիայի",
"gauge": "տվիչ",
"mirror": "հայելի",
"Turn to your neighbour. Four devices, thirty seconds. Say the measurand out loud.":
    "Դարձե՛ք հարևանին։ Չորս սարք, երեսուն վայրկյան։ Չափվող մեծությունը բարձրաձայն ասե՛ք։",
"One of these four is passive — it changes a resistance and needs an excitation "
"current before it says anything at all. Which one, and why does that matter?":
    "Այս չորսից մեկը պասիվ է — փոխում է դիմադրությունը և կարիք ունի սնման հոսանքի, "
    "որպեսզի ընդհանրապես ինչ-որ բան «ասի»։ Ո՞րը, և ինչու՞ է դա կարևոր",

# ── the chain diagram ────────────────────────────────────────────────────────
"The measurand": "Չափվող մեծությունը",
"PHYSICAL": "ՖԻԶԻԿԱԿԱՆ",
"QUANTITY": "ՄԵԾՈՒԹՅՈՒՆ",
"MECHANICAL": "ՄԵԽԱՆԻԿԱԿԱՆ",
"COUPLING": "ԿԱՊԱԿՑՈՒՄ",
"TRANSDUCTION": "ՓՈԽԱԿԵՐՊՈՒՄ",
"ANALOG": "ԱՆԱԼՈԳԱՅԻՆ",
"CONDITIONING": "ՄՇԱԿՈՒՄ",
"SAMPLING &": "ՆՄՈՒՇԱՌՈՒՄ ԵՎ",
"QUANTISATION": "ՔՎԱՆՏԱՑՈՒՄ",
"CODES → SI": "ԿՈԴԵՐ → ՄՀ",
"UNITS": "ՄԻԱՎՈՐՆԵՐ",
"TIMESTAMP,": "ԺԱՄԱՆԱԿԱՆԻՇ,",
"LOG, DECIDE": "ԳՐԱՆՑՈՒՄ, ՈՐՈՇՈՒՄ",
"It does not start at the sensor": "Այն չի սկսվում տվիչից",
"The measurement chain": "Չափման շղթան",
"Through the electronics": "Էլեկտրոնիկայի միջով",
"The full chain": "Ամբողջական շղթան",
"The same chain, with real numbers": "Նույն շղթան՝ իրական թվերով",
"One 0.9 mg vibration, all the way to a decision":
    "Մեկ 0.9 mg թրթռում՝ ամբողջ ճանապարհը մինչև որոշում",
"Notice stage 2: the mechanical path already lost a third of the signal — before a "
"single electron moved.":
    "Ուշադրություն 2-րդ փուլին. մեխանիկական ուղին արդեն կորցրել է ազդանշանի մեկ երրորդը — "
    "դեռ ոչ մի էլեկտրոն չի շարժվել։",

# ── where the truth dies ─────────────────────────────────────────────────────
"Where the truth dies": "Որտեղ է կորչում ճշմարտությունը",
"and whether you can ever get it back": "և արդյոք երբևէ կարող եք վերականգնել այն",
"Stage": "Փուլ",
"What is lost": "Ինչ է կորչում",
"Recoverable later?": "Վերականգնելի՞ է հետո",
"2  Mechanical coupling": "2  Մեխանիկական կապակցում",
"amplitude and phase, frequency-dependent": "ամպլիտուդ և փուլ, հաճախությունից կախված",
"No — measure it yourself": "Ոչ — չափե՛ք ինքներդ",
"3  Transduction": "3  Փոխակերպում",
"cross-axis leakage, nonlinearity, temperature drift":
    "առանցքային խաչաձև ազդեցություն, ոչ գծայնություն, ջերմային շեղում",
"Partly — by calibration": "Մասամբ — ստուգաչափմամբ",
"4  Conditioning": "4  Մշակում",
"saturation clips peaks; wrong filter kills the signal":
    "հագեցումը կտրում է գագաթները. սխալ ֆիլտրը սպանում է ազդանշանը",
"No": "Ոչ",
"5  Sampling": "5  Նմուշառում",
"everything above half the sample rate, aliased in":
    "ամեն ինչ նմուշառման հաճախության կիսից վեր՝ ալիասինգով ներս է ընկնում",
"Never": "Երբեք",
"5  Quantisation": "5  Քվանտացում",
"detail below one LSB": "մանրամասնություն մեկ LSB-ից ցածր",
"Partly — averaging": "Մասամբ — միջինացմամբ",
"6  Scaling to units": "6  Միավորների բերում",
"accuracy, if the sensitivity constant is wrong":
    "ճշտություն, եթե զգայունության հաստատունը սխալ է",
"Yes — recompute": "Այո — վերահաշվե՛ք",
"7  Timestamping": "7  Ժամանականիշ",
"the time axis, and therefore all frequency content":
    "ժամանակի առանցքը, հետևաբար՝ ամբողջ հաճախային պարունակությունը",
"Three of these are permanent. Design decisions, not calibration problems.":
    "Սրանցից երեքը անվերադարձ են։ Նախագծման որոշումներ են, ոչ ստուգաչափման խնդիրներ։",
}
