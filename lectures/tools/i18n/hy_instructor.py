# -*- coding: utf-8 -*-
"""Sentence-level Armenian recovered from the instructor's hand-edited decks.

RECOVERED, NOT WRITTEN. Between 2026-08-25 and 2026-09-08 the instructor edited
the L1 and L2 `-HY.pptx` files directly (commits c772767, dd2ea8e, 630bb58).
About 350 paragraphs were rewritten and none of it existed in the dictionaries,
so the next `translate_deck.py` run would have discarded all of it.

This file is that work, extracted by aligning each slide's English paragraph
sequence against its Armenian one and keeping only the pairs the alignment could
confirm. It is loaded LAST by `translate_deck.py`, so it overrides
`hy_part1..5.py` wherever the two disagree. Sixteen pairs that turned out to be
alignment slips inside grouped diagram shapes were dropped rather than guessed
at; those slides' Armenian still lives only in the .pptx, which is why the
existing -HY files must not be regenerated blind — see GLOSSARY-hy.md.

Beyond preserving L1 and L2, this is also the register model for Lectures 3-16:
formal, declarative, nominal, no minute markers and no instructor-facing text on
a student-facing slide.
"""

HY = {
    '0.061 mg/LSB':
        '0.061 mg/ԿՆԲ',
    '0.488 mg/LSB':
        '0.488 mg/ԿՆԲ',
    '0.5° became 8.73 mg, and 8.73 mg decided everything that followed.':
        '0.5°-ը վերածվեց 8.73 mg-ի, որն էլ որոշեց հետագա ամբողջ վերլուծությունը։',
    '10 mg and 0.7 mg combine to 10.02 mg. The small term never mattered.':
        '10 mg և 0.7 mg բաղադրիչների RSS-ը 10.02 mg է․ փոքր բաղադրիչը գրեթե չի փոխում արդյունքը։',
    '100 µg/√Hz':
        '100 µg/√Հց',
    '12.4 hPa of offset, held to 0.2 hPa of scatter. Superb precision, useless accuracy — until somebody calibrates it.':
        'Զրոյական շեղումը 12.4 hPa է, իսկ ցրվածքը՝ ընդամենը 0.2 hPa։ Բարձր ճշգրտություն, անբավարար ճշտություն՝ մինչև չափաբերումը։',
    '20 Hz  ·  amplitude slowly rising  ·  read as normal load variation':
        '20 Հց  ·  ամպլիտուդը դանդաղ աճում է  ·  ընկալվել է որպես բնականոն բեռ',
    '8.73 mg is the entire signal we are trying to measure.':
        '8.73 mg-ը մեր ամբողջ օգտակար ազդանշանն է։',
    'A datasheet is a legal document, not a promise.':
        'Տվյալների թերթիկը պայմաններով սահմանված բնութագրերի փաստաթուղթ է, ոչ թե անվերապահ խոստում։',
    'A number without its conditions is not a number.':
        'Առանց չափման պայմանների թիվը իմաստ չունի։',
    'A pressure sensor in a chamber held at a true, constant 1000.0 hPa is read 100 times. Every reading falls between 1012.3 and 1012.5 hPa. The device is:':
        'Խցիկում ճնշումը հաստատուն է, իսկ իրական արժեքը՝ 1000.0 hPa։ Տվիչով կատարում են 100 չափում, և բոլոր արդյունքները 1012.3–1012.5 hPa միջակայքում են։ Տվիչը՝',
    'AGAINST ±0.5°':
        'ՊԱՀԱՆՋ՝ ±0.5°',
    'ANALOG':
        'ԱՆԱԼՈԳԱՅԻՆ ԱԶԴԱՆՇԱՆԻ',
    'AS A TILT ANGLE':
        'ԹԵՔՈՒԹՅԱՆ ԱՆԿՅԱՄԲ',
    'Accuracy. Precision. Resolution. Sensitivity.':
        'Ճշտություն։ Ճշգրտություն։ Լուծաչափ։ Զգայունություն։',
    'All values in mg unless stated. Bandwidth 50 Hz, calibrated at 20 °C, used over 0–40 °C.':
        'Բոլոր արժեքները՝ mg-ով։ BW = 50 Hz, չափաբերումը՝ 20 °C, աշխատանքային տիրույթը՝ 0–40 °C։',
    'An accelerometer with 0.061 mg resolution is bolted to a motor housing through a 5 mm rubber pad. Which stage has already destroyed the accuracy of the reported number?':
        '0.061 mg կետայնությամբ աքսելերոմետրը ամրացված է շարժիչի իրանին 5 մմ ռետինե միջադիրի միջոցով։ Ո՞ր փուլն է արդեն ոչնչացրել հաղորդված թվի ճշտությունը',
    'Any term larger than that is fatal. Any term far below it is irrelevant — no matter how good it looks on a front page.':
        'Դրանից մեծ արժեքն անթույլատրելի է, իսկ անհամեմատ փոքրը՝ ոչ էական՝ անկախ առաջին էջում դրա գրավչությունից։',
    'At the end of this you will know which part you should have chosen.':
        'Վերջում կկարողանաք հաշվարկով հիմնավորել, թե որ սարքն է պետք ընտրել։',
    'Bandwidth':
        'Թողունակություն (BW)',
    'Both utterly negligible against 8.73 mg.':
        'Երկու արժեքներն էլ աննշան են 8.73 mg-ի համեմատ։',
    'Both — the spread is only 0.2 hPa':
        'Ե՛վ ճիշտ է, և՛ ճշգրիտ. ցրվածքը ընդամենը 0.2 hPa է',
    'By the end of today you can…':
        'Դասընթացի վերջում դուք կկարողանաք…',
    'CHUNK 1  ·  MINUTES 10–28':
        'ԲԱԺԻՆ 1',
    'CHUNK 1  ·  MINUTES 8–26':
        'ՄԱՍ 1',
    'CHUNK 2  ·  MINUTES 28–46':
        'ԲԱԺԻՆ 2',
    'CHUNK 3  ·  MINUTES 46–70':
        'ԲԱԺԻՆ 3',
    'CLASSIFY':
        'ՏԱՐԲԵՐԱԿԵԼ',
    'CODES → SI':
        'ԹՎԱՅԻՆ ԿՈԴԵՐ → ՄՄ',
    'Calibrated at 20 °C, used 0–40 °C, so ΔT = ±20 °C.':
        'Չափաբերվել է 20 °C-ում, աշխատում է 0–40 °C-ում, ուստի ΔT = ±20 °C։',
    'Choosing, interfacing, calibrating and':
        'տվիչների ընտրություն,',
    'Commit. In seventy minutes I will show you that most of this room just chose a part that cannot meet the requirement — and that its own datasheet said so, on page nine.':
        'Ընտրությունը հիմնավորեք միայն առաջին էջում ներկայացված տվյալներով։ Պատասխանը կվերանայենք հաշվարկից հետո։',
    'Cross-axis sensitivity':
        'Միջառանցք. զգայունություն',
    'Cross-sensitivity':
        'Միջառանցք. զգայունություն',
    'Current draw':
        'Սպառվող հոսանք',
    'DRIFT':
        'ԴՐԵՅՖ',
    'Drift':
        'Դրեյֆ',
    'Every actuator in this course is also a measurement problem: you only know it acted if you sense the result.':
        'Ամեն ակտուատոր նաև չափման խնդիր է լուծում։ Այն գործել է, եթե տեսնում\xa0ենք դրա արդյունքը։',
    'Every error term in this lecture gets compared against those 8.73 mg.':
        'Սխալի յուրաքանչյուր բաղադրիչ համեմատելու ենք 8.73 mg-ի հետ։',
    'Everything today happens BEFORE you own any hardware. This is the box you choose — and you choose it with arithmetic.':
        'Այսօրվա աշխատանքը կատարվում է մինչև սարքավորումը ձեռք բերելը․ բաղադրիչն ընտրում ենք հաշվարկի հիման վրա։',
    'FIFO where relevant':
        'FIFO՝ ըստ անհրաժեշտության',
    'Find the dominant term. Everything else is decoration.':
        'Գտեք գերակշռող սխալի բաղադրիչը․ մնացածը երկրորդական է։',
    'First, turn the requirement into a number':
        'Պահանջը նախ արտահայտեք թվով',
    'Four terms. One requirement. Twenty minutes.':
        'Չորս բաղադրիչ, մեկ պահանջ։',
    'Four things to keep':
        'Հիշելու չորս դրույթ',
    'Group delay':
        'Խմբային հապաղում',
    'HOLD ON TO THIS':
        'ՀԻՇԵ՛Ք ՈՐ',
    'Hands up. Then tell me why it was hard —':
        'Ձեռք բարձրացրեք և բացատրեք՝ ինչո՞ւ էր դժվար։',
    'ISM330DHCX datasheet · pairs · 8 minutes · write the page number beside every answer':
        'ISM330DHCX տվյալների թերթիկ · զույգերով · պատասխանի մոտ նշեք էջը',
    'ISM330DHCX · the same budget, run twice from its own datasheet':
        'ISM330DHCX · նույն հաշվեկշիռը՝ տվյալների թերթիկի typ. և max. արժեքներով',
    'IT IS NOT':
        'ԱՅՆ ՉԻ ՎԵՐԱԲԵՐՈՒՄ',
    'MINUTE 44  ·  STAND UP':
        'ՔՆՆԱՐԿՈՒՄ',
    'Meets ±0.5° over 0–40 °C':
        'Բավարարում է ±0.5° պահանջը 0–40 °C-ում',
    'Most engineering arguments about sensors are really arguments about these.':
        'Տվիչների վերաբերյալ ճարտարագիտական վեճերի մեծ մասը ծագում է այս հասկացությունների շփոթից։',
    'Neither, because the resolution is not stated':
        'Ո՛չ մեկը, քանի որ լուծաչափը նշված չէ',
    'No min, no max. You are being told the average of a production run, not a guarantee.':
        'Նվազագույն կամ առավելագույն սահման չկա․ դրանք բնորոշ, ոչ երաշխավորված արժեքներ են։',
    'Noise density':
        'Աղմուկի խտություն (ASD)',
    'Noise density — and the bandwidth it was measured at':
        'Աղմուկի սպեկտրային խտությունը և դրա նշման հաճախականային թողունակությունը',
    'Now compute it':
        'Այժմ՝ հաշվարկը',
    'Now the part on your bench':
        'Այժմ գնահատենք լաբորատոր սարքը',
    'Number 5 is not academic — you need it at the bench next week to prove your sensor is the sensor you think it is.':
        '5-րդ կետը կօգտագործեք հաջորդ լաբորատոր աշխատանքում՝ տվիչի ինքնությունը հաստատելու համար։',
    'Offset':
        'Զրոյի շեղում',
    'Offset drift  (TC × ΔT)':
        'Զրոյի շեղման դրեյֆ  (TC × ΔT)',
    'One part number. One datasheet. Two columns — and the requirement sits between them.':
        'Նույն սարքը, նույն պահանջը, բայց հրապարակված երկու սյունակները տալիս են տարբեր եզրակացություններ։',
    'One term dominates. It was on page nine, and it was not on either front page.':
        'Գերակշռում է մեկ բաղադրիչ, որը նշված էր միայն տվյալների թերթիկի խորքում։',
    'POLL 1   ·   MINUTE 4':
        'ՀԱՐՑՈՒՄ 1',
    'POLL 1   ·   MINUTE 7':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1',
    'POLL 1   ·   MINUTE 70   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1 · ՊԱՏԱՍԽԱՆ',
    'POLL 2   ·   MINUTE 18':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 2',
    'POLL 2   ·   MINUTE 18   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 2 · ՊԱՏԱՍԽԱՆ',
    'POLL 2   ·   MINUTE 24':
        'ՀԱՐՑՈՒՄ 2',
    'POLL 2   ·   MINUTE 24   ·   ANSWER':
        'ՀԱՐՑՈՒՄ 2   ·  \xa0ՊԱՏԱՍԽԱՆ',
    'POLL 3   ·   MINUTE 40':
        'ՀԱՐՑՈՒՄ 3',
    'Part A drifts by 10 mg. The entire quantity we are trying to measure is 8.73 mg.':
        'Սարք Ա-ի զրոյական շեղման դրեյֆը 10 mg է, իսկ ամբողջ ազդանշանը՝ 8.73 mg։',
    'Part A had a library. Part A cannot do the job.':
        'Սարք Ա-ի համար գրադարան կար, բայց այն չէր բավարարում պահանջին։',
    'Part A resolves eight times finer':
        'Սարք Ա-ն ունի ութ անգամ ավելի բարձր լուծաչափ,',
    'Part A — eight times finer resolution, and cheaper':
        'Սարք Ա — ութ անգամ ավելի բարձր լուծաչափ և ավելի ցածր գին',
    'Part B resolves 0.028° of tilt: eighteen times finer than the ±0.5° we need. Resolution was never the deciding variable. It only looked like it was, because it was the number on the front page.':
        'Սարք Բ-ի 0.028° լուծաչափը պահանջվող 0.5°-ից 18 անգամ մանր է։ Ուստի լուծաչափը որոշիչ չէր․ վճռորոշը ջերմաստիճանային դրեյֆն էր։',
    'Part C is the trap in the other direction: technically the best part, six times the price, and it buys no capability the requirement asks for. Over-specifying is also an engineering failure.':
        'Սարք C-ն ավելի թանկ է, բայց պահանջից ավելի օգտակար հնարավորություն չի ապահովում․ սա ավելորդ ծախս է։',
    'QUANTISATION':
        'ՔՎԱՆՏԱՑՄԱՆ ՍԽԱԼ',
    'Quantisation  (LSB/√12)':
        'Քվանտացման աղմուկ  (LSB/√12)',
    'RANDOM ERROR':
        'ՊԱՏԱՀԱԿԱՆ ՍԽԱԼ',
    'Read the conditions block first':
        'Նախ կարդացե՛ք չափման պայմանները',
    'Resolution':
        'Լուծաչափ',
    'Resolution is not accuracy, and neither is precision.':
        'Լուծաչափը, ճշտությունը և ճշգրտությունը տարբեր բնութագրեր են։',
    "Retrieval: last week's chain, this week's box":
        'Վերհիշում․ անցյալ դասախոսության շղթան և այսօրվա օղակը',
    'Root-sum-square, because the terms are independent':
        'Անկախ բաղադրիչները համակցվում են քառակուսիների գումարի քառակուսի արմատով (RSS)',
    'SYSTEMATIC ERROR':
        'ՀԱՄԱԿԱՐԳԱՅԻՆ ՍԽԱԼ',
    'Same target, four different instruments':
        'Նույն թիրախը՝ չորս տարբեր չափման արդյունք',
    'Sensitivity at 25 °C. Drift over 125 °C. Noise at one specific bandwidth. They are not comparable as printed.':
        'Տողերի պայմանները տարբեր են՝ 25 °C, 125 °C միջակայք և սահմանված BW։ Առանց պայմանների թվերը համադրելի չեն։',
    'Sensitivity at EACH selectable full-scale range':
        'Զգայունությունը՝ յուրաքանչյուր ընտրվող լրիվ տիրույթի համար',
    'Static: what it does when nothing is moving. Dynamic: what it does when things change.':
        'Ստատիկ՝ անփոփոխ մուտքի դեպքում։ Դինամիկ՝ փոփոխվող մուտքի դեպքում։',
    'Supply voltage range — and the separate I/O supply, if there is one':
        'Սնման լարումների տիրույթները, ներառյալ առանձին I/O սնուցումը, եթե այն նախատեսված է',
    'Systematic → calibration. Random → bandwidth. Drift → component choice.':
        'Համակարգային սխալ → չափաբերում։ Պատահական սխալ → BW։ Դրեյֆ → բաղադրիչի ընտրություն։',
    'THE VERDICT':
        'ԵԶՐԱԿԱՑՈՒԹՅՈՒՆ',
    'THIS COURSE IS':
        'ԱՅՍ ԴԱՍԸՆԹԱՑՆ ՎԵՐԱԲԵՐՈՒՄ Է',
    'TIMESTAMP,':
        'ԺԱՄԱՆԱԿԱՅԻՆ ԴՐՈՇՄ,',
    'Teams of three · 8 minutes · commit to one':
        'Երեք հոգանոց խմբեր · ընտրեք մեկ սարք',
    'Term':
        'Սխալանքի բաղադրիչ',
    'That is the whole device — everything in the datasheet is a consequence of m, k and d.':
        'datasheet-ի ամեն ինչ m, k և d-ի հետևանք է։',
    'The conditions are where the truth lives.':
        'Թվերի իմաստը չափման պայմաններում է։',
    "The course's selection rule":
        'Բաղադրիչի ընտրության կանոնը',
    'The design principle of all sixteen lectures:  understand the measurand → select the sensor → interface it → acquire valid data → calibrate it → process or fuse it → validate it in a system.':
        'Դասընթացի սկզբունքը՝  չափվող մեծությունը → տվիչի ընտրություն → միացում → հավաստի  տվյալներ → ստուգաչափում → մշակում կամ միավորում → ինտեգրում։',
    'The device-identification register and its expected value':
        'Նույնականացման ռեգիստրը և սպասվող արժեքը',
    'The error budget':
        'Սխալների հաշվեկշիռը',
    'The four words':
        'Չորս հասկացություն,',
    'The headline is on page one. The truth is in the conditions.':
        'Գովազդային ցուցանիշը առաջին էջում է, իսկ իրական իմաստը՝ չափման պայմաններում։',
    'The hunt':
        'Տվյալների որոնում',
    'The job:  report the tilt of a solar-tracker frame to ±0.5°, outdoors, 0 to 40 °C.':
        'Խնդիր՝ բացօթյա պայմաններում, 0–40 °C-ում, արևին հետևող շրջանակի թեքությունը չափել ±0.5° ճշտությամբ։',
    'The right FIRST answer was C — you did not have enough information. The right SECOND answer, after twelve minutes of arithmetic, is B.':
        'Սկզբում ճիշտ պատասխանը C-ն էր, քանի որ տեղեկությունը բավարար չէր։ Հաշվարկից հետո ճիշտ է B-ն։',
    'The vocabulary, sorted':
        'Տերմինները՝ ըստ խմբերի',
    'Then, and only then, read the number':
        'Միայն դրանից հետո՝ թվային արժեքը',
    'This cannot be decided from front pages alone':
        'Միայն առաջին էջի տվյալներով որոշել հնարավոր չէ',
    'This rule is the spine of Lecture 14 and of Laboratories 3 and 5. You will use it in week six.':
        'Այս կանոնը 14-րդ դասախոսության և 3-րդ ու 5-րդ լաբորատոր աշխատանքների հիմքն է։ Այն կիրառելու եք 6-րդ շաբաթում։',
    'Three more terms, and one of them is not small':
        'Եվս երեք բաղադրիչ․ դրանցից մեկն էական է',
    'Three words we will use precisely':
        'Երեք տերմին, որոնք կօգտագործենք ճշգրիտ',
    'Today one number decides a design — and it is not on any front page.':
        'Այսօր մեկ թիվ է որոշելու նախագծային ընտրությունը, և այդ թիվը առաջին էջում չկա։',
    'Total error as an angle':
        'Ընդհանուր սխալանքը՝ անկյան միավորով',
    'Turn the requirement into a number before you read any datasheet.':
        'Պահանջը նախ վերածեք թվի, ապա կարդացեք տվյալների թերթիկը։',
    'Two front pages':
        'Երկու սարք՝ առաջին էջի տվյալներով',
    'Typ':
        'Բն.',
    'Unit price at 500 off':
        'Միավորի գինը՝ 500 հատ պատվիրելիս',
    'Vote alone, then find someone who disagrees.':
        'Քվեարկեք ինքնուրույն, ապա քննարկեք ձեր ընտրությունը մեկ այլ ուսանողի հետ։',
    'WHAT THE SCREEN SHOWED':
        'Ի՞ՆՉ ԷՐ ՑՈՒՅՑ ՏԱԼԻՍ ԷԿՐԱՆԸ',
    'What the datasheet':
        'Ի՞նչ է իրականում',
    'What this course is':
        'Որն է այս դասընթացի նպատակը',
    'What to choose on instead — parts that expose the engineering:':
        'Ընտրության հիմքը ճարտարագիտական գնահատման տվյալներն են․',
    'Where are we today?':
        'Որտե՞ղ է այսօրվա թեման',
    'Whether the headline numbers are typ, min or max — and at what temperature':
        'Թվերի կարգավիճակը (typ./min./max.) և չափման ջերմաստիճանը',
    'Which number was':
        'Ո՞ր ցուցանիշն էր',
    'Which part do you specify for a ±0.5° tilt measurement?':
        'Ո՞ր սարքը կընտրեք ±0.5° ճշտությամբ թեքություն չափելու համար։',
    'Write one sentence:   “We specify Part ___ because ___”   — naming the DOMINANT ERROR TERM, not the headline.':
        'Գրեք մեկ նախադասություն․ «Ընտրում ենք Սարք ___-ը, որովհետև ___»՝ նշելով գերակշռող սխալի բաղադրիչը, ոչ թե առաջին էջի ցուցանիշը։',
    'You cannot budget an error against an angle':
        'Սխալների հաշվեկշիռը հնարավոր չէ ուղղակիորեն համեմատել անկյան հետ',
    'You must order today. Which one?':
        'Պատվերը պետք է ձևակերպել այսօր։ Ո՞րը կընտրեք։',
    'Your turn: three candidates':
        'Աշխատանք խմբերով. երեք թեկնածու',
    'Zero-offset level AND its temperature coefficient':
        'Զրոյական g-ի շեղումը և դրա ջերմաստիճանային գործակիցը',
    'a complete datasheet':
        'ամբողջական տվյալների թերթիկ',
    'actually says':
        'ասում տվյալների թերթիկը',
    'an accessible register map':
        'հասանելի ռեգիստրային քարտեզ',
    'an unfamiliar device: sensor, transducer or actuator — and name its measurand':
        'անծանոթ սարքը՝ տվիչ, փոխակերպիչ թե ակտուատոր — և որոշել չափվող\xa0մեծությունը',
    'and, just as importantly, what it is not':
        'և, նույնքան կարևոր՝ որն չէ',
    'because from here on the difference matters':
        'այսուհետ տարբերությունը կարևոր է',
    'calibrated out':
        'չափաբերվում է',
    'data rate — NOT bandwidth':
        'ելքային տվյալների հաճախություն՝ ոչ հաճախականային թողունակություն',
    'data-ready interrupt':
        'տվյալների պատրաստ լինելու ընդհատում',
    'datasheet × your bandwidth':
        'տվյալների թերթիկ × ընտրված BW',
    'datasheet-based selection':
        'ընտրությունը տվյալների թերթիկի միջոցով',
    'deviation from a straight line':
        'փոխանցման իրական բնութագրի շեղումը ուղիղ գծից',
    'documented bandwidth and noise':
        'փաստաթղթավորված BW և աղմուկ',
    'does it matter which way you came?':
        'ելքը կախվա՞ծ է մոտեցման ուղղությունից',
    'from scaling laws why MEMS devices are fast — and what gets worse when they shrink':
        'մասշտաբման օրենքներից՝ ինչու են MEMS սարքերն արագ — և թե որ պարամետրն է վատանում չափսերի փոքրացման արդյունքում',
    'hardest to find?':
        'ամենադժվարը գտնել',
    'highest frequency reported faithfully':
        'առավելագույն հաճախականությունը, որը փոխանցվում է սահմանված ճշտությամբ',
    'how late the answer arrives':
        'ելքային արձագանքի ժամանակային հապաղումը',
    'is a bandwidth problem':
        'հաճախականային թողունակության խնդիր է',
    'is a calibration problem':
        'չափաբերման խնդիր է',
    'it moves after you calibrated — so you cannot calibrate it away':
        'փոխվում է չափաբերումից հետո, ուստի մեկանգամյա չափաբերմամբ չի վերացվում',
    'noise per √Hz':
        'աղմուկը՝ √Հց-ի հաշվով',
    'noise — reducible only by averaging, which costs you speed':
        'աղմուկը նվազում է միջինացմամբ, սակայն նվազում է նաև արագագործությունը',
    'not what the answer was.':
        'Պատասխանը դեռ մի՛ ասեք։',
    'offset, scale factor — measurable, removable':
        'զրոյական շեղում, մասշտաբային գործակից՝ չափելի և ուղղելի',
    'only as deep as packaging and drift require.':
        'անգամ՝ 4-րդ դասախոսությունում։',
    'output change per unit of input':
        'մուտքի մեկ միավոր փոփոխությանը համապատասխանող ելքի փոփոխությունը',
    'output when the input is zero':
        'մուտքի զրոյական արժեքին համապատասխանող ելքը',
    'package level, not board level':
        'պատյան, ոչ տպասալ',
    'pass/fail':
        'պարտ.',
    'passes, 4× margin':
        'բավարարում է՝ 4× պաշարով',
    'real embedded systems.':
        'ինտեգրում իրական համակարգերում։',
    'resolution and full scale':
        'լուծաչափ և չափման լրիվ տիրույթ',
    'same input, same output, later':
        'նույն մուտքի դեպքում նույն արդյունքը՝ կրկնակի չափելիս',
    'selectable range and ODR':
        'ընտրելի չափման տիրույթ և ODR',
    'self-test':
        'ինքնաստուգման գործառույթ',
    'slow change with time and temperature':
        'ելքի դանդաղ փոփոխությունը ժամանակի և ջերմաստիճանի ազդեցությամբ',
    'smallest distinguishable change':
        'տարբերակելի ամենափոքր փոփոխությունը',
    'smallest to largest measurable value':
        'չափելի արժեքների նվազագույնից մինչև առավելագույն միջակայքը',
    'students must still see the underlying configuration and data path.”':
        'Ուսումնասիրեք նաև դրա կարգավորումն ու տվյալների ուղին»։',
    'temp. coefficient × 20 °C':
        'ջերմաստիճանային գործակից × 20 °C',
    'than Part B — and cannot do the job.':
        'սակայն չի բավարարում պահանջը։',
    'that get confused':
        'որոնք հաճախ շփոթում են',
    'the axis you did not want':
        'անցանկալի առանցքի ազդեցությունը',
    'the path from a physical quantity to a logged number, and say where information dies':
        'ֆիզիկական մեծությունից մինչև գրանցված թիվ ուղին, և ասել՝ որտեղ է կորչում տեղեկույթը։',
    'the requirement':
        'պահանջ',
    'tilt of 0.5°  →  sin(0.5°) × 1 g  =  8.73 mg':
        '0.5° թեքություն  →  sin(0.5°) × 1 g  =  8.73 mg',
    'time to settle after a step':
        'աստիճանաձև մուտքից հետո հաստատման ժամանակը',
    'typ at 25 °C is not a guarantee, and an unspecified coefficient is unbounded.':
        '25 °C-ում տրված typ. արժեքը երաշխիք չէ, իսկ չնշված գործակցի սահմաններն անհայտ են։',
    'using MAX':
        'ըստ max.',
    'using TYP':
        'ըստ typ.',
    '“Avoid selecting a part only because an Arduino library exists;':
        '«Սարքը մի՛ ընտրեք միայն Arduino գրադարանի առկայությամբ։',
    '“HIGH RESOLUTION · LOW NOISE”':
        '«ԲԱՐՁՐ ԼՈՒԾԱՉԱՓ · ՑԱԾՐ ԱՂՄՈՒԿ»',
    '√(sum of squares)':
        '√(քառակուսիների գումարի)',
    '▸  Every number is “typ”.':
        '▸ Բոլորը բնորոշ (typ.) արժեքներ են։',
    '▸  The conditions differ per row.':
        '▸  Տողերի պայմանները տարբեր են։',
}
