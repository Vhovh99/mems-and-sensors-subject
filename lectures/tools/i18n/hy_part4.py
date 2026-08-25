# -*- coding: utf-8 -*-
"""Armenian translations, part 4 — Lecture 2: opening, the four words, datasheets."""
HY = {
"Sensor specifications and": "Տվիչների բնութագրերը և",
"datasheet-based selection": "ընտրությունը datasheet-ի հիման վրա",
"Lecture 2 of 16   ·   80 minutes   ·   Module A: Foundations":
    "Դասախոսություն 2 / 16   ·   80 րոպե   ·   Բաժին Ա. Հիմունքներ",
"Today one number decides a design — and it is not on any front page.":
    "Այսօր մեկ թիվ որոշում է նախագիծը — և այն ոչ մի առաջին էջում չկա։",
"MEMS & Sensors  ·  Lecture 2  ·  Specifications and datasheet-based selection":
    "MEMS և տվիչներ  ·  Դասախոսություն 2",
"Last week's muddiest points": "Անցյալ շաբաթվա անհասկանալի կետերը",
"Your questions, answered before we start": "Ձեր հարցերը՝ պատասխանված մինչ սկսելը",
"INSTRUCTOR: fill these three in from the exit tickets before class.":
    "ԴԱՍԱԽՈՍԻՆ. լրացրե՛ք այս երեքը ելքի տոմսերից մինչ դասը։",
"Refer to concepts, never to students. Ninety seconds total, then move on.":
    "Հղում արե՛ք հասկացություններին, երբեք՝ ուսանողներին։ Ընդամենը իննսուն վայրկյան, ապա "
    "առա՛ջ։",
"Where are we today?": "Որտե՞ղ ենք այսօր",
"Retrieval: last week's chain, this week's box":
    "Վերհիշում. անցյալ շաբաթվա շղթան, այս շաբաթվա վանդակը",
"Everything today happens BEFORE you own any hardware. This is the box you choose — and "
"you choose it with arithmetic.":
    "Այսօրվա ամեն ինչ տեղի ունենում է ՄԻՆՉ սարքավորում ունենալը։ Սա այն վանդակն է, որը "
    "ընտրում եք — և ընտրում եք թվաբանությամբ։",

# ── the hook: two front pages ────────────────────────────────────────────────
"Two front pages": "Երկու առաջին էջ",
"You must order today. Which one?": "Պատվերը պետք է տալ այսօր։ Ո՞րը",
"PART  A": "ՍԱՐՔ  Ա",
"Accelerometer, 3-axis": "Աքսելերոմետր, 3-առանցք",
"16-bit": "16-բիթ",
"Full scale": "Լրիվ տիրույթ",
"Sensitivity": "Զգայունություն",
"Noise density": "Աղմուկի խտություն",
"Unit price": "Միավորի գին",
"“HIGH RESOLUTION · LOW NOISE”": "«ԲԱՐՁՐ ԼՈՒԾՈՒՆԱԿՈՒԹՅՈՒՆ · ՑԱԾՐ ԱՂՄՈՒԿ»",
"PART  B": "ՍԱՐՔ  Բ",
"14-bit": "14-բիթ",
"The job:  report the tilt of a solar-tracker frame to ±0.5°, outdoors, 0 to 40 °C.":
    "Խնդիրը՝  հաղորդել արևահետևիչ շրջանակի թեքությունը ±0.5° ճշտությամբ, բացօթյա, "
    "0-ից 40 °C։",
"POLL 1   ·   MINUTE 7": "ՀԱՐՑՈՒՄ 1   ·   ՐՈՊԵ 7",
"Which part do you specify for a ±0.5° tilt measurement?":
    "Ո՞ր սարքը կնշեք ±0.5° թեքության չափման համար",
"Part A — eight times finer resolution, and cheaper":
    "Սարք Ա — ութ անգամ ավելի բարձր լուծունակություն, և ավելի էժան",
"Part B": "Սարք Բ",
"This cannot be decided from front pages alone":
    "Սա հնարավոր չէ որոշել միայն առաջին էջերից",
"Commit. In seventy minutes I will show you that most of this room just chose a part "
"that cannot meet the requirement — and that its own datasheet said so, on page nine.":
    "Որոշե՛ք։ Յոթանասուն րոպե անց ցույց կտամ, որ այս լսարանի մեծ մասը ընտրեց սարք, որը չի "
    "կարող բավարարել պահանջը — և որ իր datasheet-ը դա ասել էր, իններորդ էջում։",
"First, turn the requirement into a number": "Նախ՝ պահանջը վերածե՛ք թվի",
"You cannot budget an error against an angle":
    "Անկյան դիմաց սխալանքի հաշվեկազմ չեք կազմի",
"8.73 mg is the entire signal we are trying to measure.":
    "8.73 mg-ն ամբողջ ազդանշանն է, որը փորձում ենք չափել։",
"Every error term in this lecture gets compared against those 8.73 mg.":
    "Այս դասախոսության ամեն սխալանքի բաղադրիչ համեմատվում է այդ 8.73 mg-ի հետ։",
"Any term larger than that is fatal. Any term far below it is irrelevant — no matter "
"how good it looks on a front page.":
    "Դրանից մեծ ամեն բաղադրիչ ճակատագրական է։ Դրանից շատ փոքրը՝ անտեղի, ինչքան էլ լավ "
    "երևա առաջին էջում։",

# ── chunk 1: the four words ──────────────────────────────────────────────────
"CHUNK 1  ·  MINUTES 10–28": "ՄԱՍ 1  ·  ՐՈՊԵ 10–28",
"The four words": "Չորս բառ,",
"that get confused": "որոնք շփոթվում են",
"Accuracy. Precision. Resolution. Sensitivity.":
    "Ճշտություն։ Ճշգրտություն։ Լուծունակություն։ Զգայունություն։",
"Most engineering arguments about sensors are really arguments about these.":
    "Տվիչների շուրջ ինժեներական վիճաբանությունների մեծ մասը իրականում սրանց մասին է։",
"Accuracy is not precision": "Ճշտությունը ճշգրտություն չէ",
"Same target, four different instruments": "Նույն թիրախը, չորս տարբեր չափիչ սարք",
"ACCURATE": "ՃԻՇՏ",
"AND PRECISE": "ԵՎ ՃՇԳՐԻՏ",
"PRECISE, NOT": "ՃՇԳՐԻՏ, ԲԱՅՑ",
"ACCURATE, NOT": "ՃԻՇՏ, ԲԱՅՑ",
"PRECISE": "ՈՉ ՃՇԳՐԻՏ",
"NEITHER": "ՈՉ ՄԵԿԸ",
"The centre of the target is the TRUE value. Precision is how tightly the shots group.":
    "Թիրախի կենտրոնը ՃՇՄԱՐԻՏ արժեքն է։ Ճշգրտությունը ցույց է տալիս, թե որքան խիտ են "
    "կուտակված կրակոցները։",
"Accuracy is where the group sits. They are independent — and only one of them is "
"fixable by calibration.":
    "Ճշտությունը ցույց է տալիս, թե որտեղ է գտնվում կուտակումը։ Նրանք անկախ են — և միայն "
    "մեկը շտկելի է ստուգաչափմամբ։",
"POLL 2   ·   MINUTE 18": "ՀԱՐՑՈՒՄ 2   ·   ՐՈՊԵ 18",
"A pressure sensor in a chamber held at a true, constant 1000.0 hPa is read 100 times. "
"Every reading falls between 1012.3 and 1012.5 hPa. The device is:":
    "Ճնշման տվիչը գտնվում է խցիկում, որտեղ ճշմարիտ, հաստատուն ճնշումը 1000.0 hPa է, և "
    "կարդացվում է 100 անգամ։ Բոլոր ցուցմունքները 1012.3–1012.5 hPa միջակայքում են։ Սարքը՝",
"Accurate but not precise": "Ճիշտ է, բայց ոչ ճշգրիտ",
"Precise but not accurate": "Ճշգրիտ է, բայց ոչ ճիշտ",
"Both — the spread is only 0.2 hPa": "Երկուսն էլ — ցրվածությունը ընդամենը 0.2 hPa է",
"Neither, because the resolution is not stated":
    "Ոչ մեկը, քանի որ լուծունակությունը նշված չէ",
"Vote alone, then find someone who disagrees.":
    "Քվեարկե՛ք ինքնուրույն, ապա գտե՛ք մեկին, ով համաձայն չէ։",
"POLL 2   ·   MINUTE 18   ·   ANSWER": "ՀԱՐՑՈՒՄ 2   ·   ՐՈՊԵ 18   ·   ՊԱՏԱՍԽԱՆ",
"12.4 hPa of offset, held to 0.2 hPa of scatter. Superb precision, useless accuracy — "
"until somebody calibrates it.":
    "12.4 hPa զրոյական շեղում, պահված 0.2 hPa ցրվածությամբ։ Հիանալի ճշգրտություն, անպետք "
    "ճշտություն — մինչև որ ինչ-որ մեկը ստուգաչափի։",
"The rule worth memorising": "Կանոնը, որ արժե անգիր անել",
"SYSTEMATIC ERROR": "ՀԱՄԱԿԱՐԳԱՅԻՆ ՍԽԱԼԱՆՔ",
"is a calibration problem": "ստուգաչափման խնդիր է",
"offset, scale factor — measurable, removable":
    "զրոյական շեղում, մասշտաբի գործակից — չափելի, հեռացվող",
"RANDOM ERROR": "ՊԱՏԱՀԱԿԱՆ ՍԽԱԼԱՆՔ",
"is a bandwidth problem": "թողունակության խնդիր է",
"noise — reducible only by averaging, which costs you speed":
    "աղմուկ — նվազեցվում է միայն միջինացմամբ, ինչը արժենում է արագություն",
"DRIFT": "ՇԵՂՈՒՄ",
"is a component-selection problem": "բաղադրիչի ընտրության խնդիր է",
"it moves after you calibrated — so you cannot calibrate it away":
    "շարժվում է ստուգաչափելուց հետո — ուստի չեք կարող ստուգաչափմամբ վերացնել",
"This rule is the spine of Lecture 14 and of Laboratories 3 and 5. You will use it in "
"week six.":
    "Այս կանոնը 14-րդ դասախոսության և 3-րդ, 5-րդ լաբորատորիաների առանցքն է։ Կօգտագործեք "
    "վեցերորդ շաբաթում։",
"The vocabulary, sorted": "Բառապաշարը՝ դասակարգված",
"Static: what it does when nothing is moving. Dynamic: what it does when things change.":
    "Ստատիկ. ինչ է անում, երբ ոչինչ չի շարժվում։ Դինամիկ. ինչ է անում, երբ ամեն ինչ "
    "փոփոխվում է։",
"STATIC CHARACTERISTICS": "ՍՏԱՏԻԿ ԲՆՈՒԹԱԳՐԵՐ",
"DYNAMIC CHARACTERISTICS": "ԴԻՆԱՄԻԿ ԲՆՈՒԹԱԳՐԵՐ",
"smallest to largest measurable value": "նվազագույնից առավելագույն չափելի արժեք",
"highest frequency reported faithfully": "հավաստիորեն հաղորդվող առավելագույն հաճախություն",
"output change per unit of input": "ելքի փոփոխություն մուտքի միավորի հաշվով",
"Response time": "Արձագանքման ժամանակ",
"time to settle after a step": "թռիչքից հետո կայունանալու ժամանակ",
"smallest distinguishable change": "նվազագույն տարբերակելի փոփոխություն",
"ODR": "ODR",
"data rate — NOT bandwidth": "տվյալների հաճախություն — ՈՉ թողունակություն",
"Offset": "Զրոյական շեղում",
"output when the input is zero": "ելքը, երբ մուտքը զրո է",
"noise per √Hz": "աղմուկ √Hz-ի հաշվով",
"Linearity": "Գծայնություն",
"deviation from a straight line": "շեղում ուղիղ գծից",
"Group delay": "Խմբային ուշացում",
"how late the answer arrives": "որքան ուշ է գալիս պատասխանը",
"Hysteresis": "Հիստերեզիս",
"does it matter which way you came?": "կարևո՞ր է, թե որ կողմից եք եկել",
"Cross-sensitivity": "Խաչաձև զգայունություն",
"the axis you did not want": "առանցքը, որը չէիք ուզում",
"Repeatability": "Կրկնելիություն",
"same input, same output, later": "նույն մուտք, նույն ելք, ավելի ուշ",
"Drift": "Շեղում",
"slow change with time and temperature":
    "դանդաղ փոփոխություն ժամանակի և ջերմաստիճանի հետ",

# ── chunk 2: what the datasheet says ─────────────────────────────────────────
"CHUNK 2  ·  MINUTES 28–46": "ՄԱՍ 2  ·  ՐՈՊԵ 28–46",
"What the datasheet": "Ինչ իրականում",
"actually says": "ասում է datasheet-ը",
"A datasheet is a legal document, not a promise.":
    "Datasheet-ը իրավական փաստաթուղթ է, ոչ խոստում։",
"The headline is on page one. The truth is in the conditions.":
    "Վերնագիրը առաջին էջում է։ Ճշմարտությունը՝ պայմաններում։",
"Read the conditions block first": "Նախ կարդացե՛ք պայմանների բլոկը",
"Then, and only then, read the number": "Ապա, և միայն ապա, կարդացե՛ք թիվը",
"Parameter": "Պարամետր",
"Min": "Նվազ.",
"Typ": "Տիպ.",
"Max": "Առավ.",
"Unit": "Միավոր",
"Conditions": "Պայմաններ",
"FS = ±2 g, 25 °C": "FS = ±2 g, 25 °C",
"Zero-g level": "Զրոյական-g մակարդակ",
"25 °C, after soldering": "25 °C, զոդելուց հետո",
"Zero-g temp. coefficient": "Զրոյական-g ջերմ. գործակից",
"−40 to +85 °C": "−40-ից +85 °C",
"ODR = 200 Hz, BW = 50 Hz": "ODR = 200 Hz, BW = 50 Hz",
"Cross-axis sensitivity": "Խաչաձև առանցքային զգայունություն",
"package level, not board level": "փաթեթի մակարդակ, ոչ տախտակի",
"▸  Every number is “typ”.": "▸  Ամեն թիվ «typ» է։",
"No min, no max. You are being told the average of a production run, not a guarantee.":
    "Ոչ նվազագույն, ոչ առավելագույն։ Ձեզ ասում են արտադրական խմբաքանակի միջինը, ոչ "
    "երաշխիք։",
"▸  The conditions differ per row.": "▸  Պայմանները տարբեր են ամեն տողի համար։",
"Sensitivity at 25 °C. Drift over 125 °C. Noise at one specific bandwidth. They are "
"not comparable as printed.":
    "Զգայունությունը 25 °C-ում։ Շեղումը 125 °C տիրույթում։ Աղմուկը մեկ կոնկրետ "
    "թողունակությամբ։ Այնպես, ինչպես տպված են, համեմատելի չեն։",
"The hunt": "Որսը",
"ISM330DHCX datasheet · pairs · 8 minutes · write the page number beside every answer":
    "ISM330DHCX datasheet · զույգերով · 8 րոպե · ամեն պատասխանի կողքին գրե՛ք էջի համարը",
"Supply voltage range — and the separate I/O supply, if there is one":
    "Սնման լարման տիրույթը — և առանձին Ի/Ե սնումը, եթե կա",
"Sensitivity at EACH selectable full-scale range":
    "Զգայունությունը ԱՄԵՆ ընտրելի լրիվ տիրույթի համար",
"Zero-offset level AND its temperature coefficient":
    "Զրոյական շեղման մակարդակը ԵՎ նրա ջերմաստիճանային գործակիցը",
"Noise density — and the bandwidth it was measured at":
    "Աղմուկի խտությունը — և թողունակությունը, որով չափվել է",
"The device-identification register and its expected value":
    "Սարքի նույնականացման ռեգիստրը և նրա սպասվող արժեքը",
"Whether the headline numbers are typ, min or max — and at what temperature":
    "Արդյոք վերնագրային թվերը typ, min թե max են — և ո՞ր ջերմաստիճանում",
"Number 5 is not academic — you need it at the bench next week to prove your sensor is "
"the sensor you think it is.":
    "5-րդը տեսական չէ — ձեզ պետք կգա լաբորատորիայում հաջորդ շաբաթ՝ ապացուցելու, որ ձեր "
    "տվիչը հենց այն տվիչն է։",
"NOW FIND THIS ONE": "ԱՅԺՄ ԳՏԵ՛Ք ՍԱ",
"“What is this device's": "«Ո՞րն է այս սարքի",
"cross-axis sensitivity after it": "խաչաձև առանցքային զգայունությունը",
"has been soldered to my board?”": "իմ տախտակին զոդվելուց հետո»։",
"It is not in the datasheet. It cannot be. The figure is specified for the packaged die "
"— and mounting stress, solder-joint asymmetry and PCB flex all change it.":
    "Այն datasheet-ում չկա։ Չի կարող լինել։ Թիվը նշված է փաթեթավորված բյուրեղի համար — իսկ "
    "ամրացման լարվածությունը, զոդակի անհամաչափությունը և տախտակի ճկումը փոխում են այն։",
"MINUTE 44  ·  STAND UP": "ՐՈՊԵ 44  ·  ՈՏՔԻ",
"Which number was": "Ո՞ր թիվն էր",
"hardest to find?": "ամենադժվար գտնելը",
"Hands up. Then tell me why it was hard —": "Ձեռքե՛րը վեր։ Ապա ասե՛ք ինչու էր դժվար —",
"not what the answer was.": "ոչ թե ինչ էր պատասխանը։",
"The conditions are where the truth lives.": "Ճշմարտությունը բնակվում է պայմաններում։",
}
