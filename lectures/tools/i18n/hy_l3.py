# -*- coding: utf-8 -*-
"""Armenian slide text for Lecture 3 — From physical quantity to trustworthy samples.

Terminology follows tools/i18n/GLOSSARY-hy.md, which is the course's single source
of truth; register follows the instructor's own hand corrections recovered in
hy_instructor.py. The companion reader chapter is reader/ch03-trustworthy-samples-hy.md.

Loaded by translate_deck.py before hy_instructor, so any string the instructor has
personally corrected still wins.
"""

HY = {
    'From physical quantity to':
        'Ֆիզիկական մեծությունից մինչև',
    'trustworthy samples':
        'հավաստի նմուշներ',
    'Lecture 3 of 16   ·   80 minutes   ·   Module A: Foundations':
        'Դասախոսություն 3 / 16   ·   80 րոպե   ·   Մոդուլ Ա․ Հիմունքներ',
    'One log file, and three numbers that decide how much of it is true.':
        'Մեկ գրանցամատյան և երեք թիվ, որոնք որոշում են, թե դրանից որքանն է հավաստի։',
    'MEMS & Sensors  ·  Lecture 3  ·  From physical quantity to trustworthy samples':
        'MEMS և տվիչներ  ·  Դասախոսություն 3',
    "INSTRUCTOR: fill these three in from Lecture 2's exit tickets before class.":
        'ԴԱՍԱԽՈՍԻՆ․ լրացրեք այս երեքը 2-րդ դասախոսության ելքի տոմսերից՝ մինչ դասը։',
    'Retrieval: the chain from Lecture 1 — today we live in boxes 5, 6 and 7':
        'Վերհիշում․ 1-ին դասախոսության շղթան — այսօր աշխատում ենք 5-րդ, 6-րդ և 7-րդ օղակներում',
    'Stages 1–4 hand you a conditioned signal. Everything after that is arithmetic on numbers — and three of its errors cannot be undone.':
        '1–4 փուլերը ձեզ տալիս են մշակված ազդանշան։ Դրանից հետո ամեն ինչ թվերի վրա կատարվող թվաբանություն է, և դրա սխալներից երեքն անդառնալի են։',
    'One log file':
        'Մեկ գրանցամատյան',
    'Ten minutes of data. 60 000 rows. No gaps, no outliers, plausible magnitudes.':
        'Տասը րոպե տվյալ։ 60 000 տող։ Բացակայող տողեր չկան, արտանետումներ չկան, մեծությունները ողջամիտ են։',
    'ISM330DHCX  ·  ±2 g  ·  16-bit  ·  ODR = 104 Hz  ·  0.061 mg/LSB  ·  HAL_Delay(10) polling loop  ·  10 minutes':
        'ISM330DHCX  ·  ±2 g  ·  16 բիթ  ·  ODR = 104 Hz  ·  0.061 mg/ԿՆԲ  ·  HAL_Delay(10) հարցախույզի ցիկլ  ·  10 րոպե',
    'BITS OF SIXTEEN THAT CARRY INFORMATION':
        'ԲԻԹ ՏԱՍՆՎԵՑԻՑ, ՈՐՈՆՔ ՏԵՂԵԿՈՒՅԹ ԵՆ ԿՐՈՒՄ',
    'You bought a 16-bit number.':
        'Դուք գնել եք 16-բիթանոց թիվ։',
    'You own rather less than that.':
        'Ձերն է զգալիորեն ավելի քիչը։',
    'A SIGNAL IN YOUR DATA THAT DOES NOT EXIST IN THE WORLD':
        'ԱԶԴԱՆՇԱՆ ՁԵՐ ՏՎՅԱԼՆԵՐՈՒՄ, ՈՐԸ ԻՐԱԿԱՆՈՒՄ ԳՈՅՈՒԹՅՈՒՆ ՉՈՒՆԻ',
    'It is not noise. It is a tone,':
        'Դա աղմուկ չէ։ Դա ազդանշան է,',
    'and it looks entirely real.':
        'և ամբողջովին իրական տեսք ունի։',
    '12.1 s':
        '12.1 վրկ',
    'HOW WRONG YOUR TIMESTAMPS ARE BY THE END':
        'ՈՐՔԱՆՈՎ ԵՆ ՍԽԱԼ ԺԱՄԱՆԱԿԱՅԻՆ ԴՐՈՇՄՆԵՐԸ ՎԵՐՋՈՒՄ',
    'Every event in the last part of':
        'Գրանցման վերջին հատվածի յուրաքանչյուր',
    'the log is stamped too early.':
        'իրադարձություն դրոշմված է չափազանց վաղ։',
    'Every one of these three was computable before a line of firmware was written.':
        'Այս երեքն էլ հաշվարկելի էին նախքան որևէ ծրագրային տող գրելը։',
    'Two of the three cannot be repaired afterwards at any price.':
        'Երեքից երկուսը հետագայում ոչ մի գնով ուղղելի չեն։',
    'POLL 1':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1',
    'Your accelerometer is 16-bit, configured for ±2 g, so its datasheet resolution is 0.061 mg/LSB. You configure ODR = 104 Hz and log the output.':
        'Ձեր արագաչափը 16-բիթանոց է և կարգավորված է ±2 g-ի, ուստի տվյալների թերթիկում լուծաչափը նշված է 0.061 mg/ԿՆԲ։ Սահմանում եք ODR = 104 Հց և գրանցում ելքը։',
    'What is the smallest change in acceleration your log can actually distinguish?':
        'Որքա՞ն է արագացման ամենափոքր փոփոխությունը, որը ձեր գրանցամատյանն իրականում կարող է տարբերակել',
    '0.061 mg — that is what the datasheet says':
        '0.061 mg — այն, ինչ նշված է տվյալների թերթիկում',
    '0.018 mg — the quantisation noise, LSB/√12':
        '0.018 mg — քվանտացման աղմուկը, ԿՆԲ/√12',
    'It cannot be determined from what you have been told':
        'Հնարավոր չէ որոշել տրված տվյալներով',
    'Commit to one. The answer is withheld until the end of the lecture — and by then you will have computed it yourselves.':
        'Ընտրեք մեկը։ Պատասխանը բացվում է դասախոսության վերջում, և այդ պահին դուք ինքներդ արդեն կհաշվարկեք այն։',
    'The number everyone trusts':
        'Թիվը, որին բոլորը վստահում են',
    'Where 0.061 mg/LSB comes from':
        'Որտեղից է գալիս 0.061 mg/ԿՆԲ-ն',
    '4000 mg  ÷  65 536 codes  =  0.061 mg / LSB':
        '4000 mg  ÷  65 536 կոդ  =  0.061 mg / ԿՆԲ',
    'One count of the register is 0.061 mg. That much is simply true.':
        'Ռեգիստրի մեկ միավոր կոդը 0.061 mg է։ Այս մասով ամեն ինչ ճիշտ է։',
    '±2 g is 4000 mg of span. Sixteen bits is 65 536 codes. Divide one by the other and you get the size of one step of the number — which is exactly what the datasheet prints, on the same page as everything else we will use today.':
        '±2 g-ը 4000 mg տիրույթ է։ Տասնվեց բիթը 65 536 կոդ է։ Բաժանեք մեկը մյուսի վրա և կստանաք թվի մեկ աստիճանի չափը, ինչը հենց այն է, ինչ տպագրված է տվյալների թերթիկում՝ այսօր օգտագործվող մնացած ամեն ինչի հետ նույն էջում։',
    '…and three things it is not':
        '…և երեք բան, որ այն չէ',
    'It is not the smallest change you can distinguish.':
        'Այն տարբերակելի ամենափոքր փոփոխությունը չէ։',
    'That is set by the noise — and the noise depends on a bandwidth nobody has chosen yet.':
        'Այն սահմանվում է աղմուկով, իսկ աղմուկը կախված է թողունակությունից, որը դեռ ընտրված չէ։',
    'It is not an accuracy.':
        'Այն ճշտություն չէ։',
    'Offset, scale error and drift are separate numbers on separate rows. Lecture 2 spent an hour on them.':
        'Զրոյական շեղումը, մասշտաբի սխալը և դրեյֆը առանձին տողերի առանձին թվեր են։ 2-րդ դասախոսությունը մեկ ժամ նվիրեց դրանց։',
    'It is not a property of the sensor alone.':
        'Այն միայն տվիչի հատկություն չէ։',
    'Change the full scale and it moves. Change the bandwidth and the measurement changes while it stays put.':
        'Փոխեք չափման լրիվ տիրույթը, և այն կփոխվի։ Փոխեք թողունակությունը, և չափումը կփոխվի, մինչդեռ այն կմնա նույնը։',
    'ON THE BOARD, NOW, AND NOT ERASED:':
        'ԳՐԱՏԱԽՏԱԿԻՆ՝ ԱՅԺՄ ԵՎ ՄԻՆՉ ՎԵՐՋ․',
    'you bought 16 bits — how many of them do you own?':
        'գնել եք 16 բիթ — դրանցից քանի՞սն են ձերը',
    'CHUNK 1':
        'ԲԱԺԻՆ 1',
    'The output and':
        'Ելքը և',
    'the reference':
        'հենային լարումը',
    'What actually comes out of a sensor — and what the converter compares it against.':
        'Ինչ իրականում ստացվում է տվիչի ելքում, և ինչի հետ է կերպափոխիչը համեմատում այն։',
    "One wire's difference between a measurement that survives a sagging rail and one that does not.":
        'Մեկ լարի տարբերություն սնման անկումը գերապրող և չգերապրող չափման միջև։',
    'What comes out of a sensor':
        'Ի՞նչ է ստացվում տվիչի ելքում',
    'Three analog forms — and one where the conversion already happened, where you cannot see it':
        'Երեք անալոգային ձև, և մեկը, որտեղ փոխակերպումն արդեն կատարվել է՝ ձեզ անտեսանելի',
    'VOLTAGE':
        'ԼԱՐՈՒՄ',
    'Tens of µV per °C from a thermocouple; a few mV from a bridge.':
        'Ջերմազույգից՝ աստիճանի հաշվով տասնյակ µV; կամրջակից՝ մի քանի mV։',
    'Small enough that the wire is part of the measurement.':
        'Այնքան փոքր, որ լարն արդեն չափման մաս է կազմում։',
    'CURRENT  ·  4–20 mA':
        'ՀՈՍԱՆՔ  ·  4–20 mA',
    'Unchanged by cable resistance, so distance does not matter.':
        'Կախված չէ մալուխի դիմադրությունից, ուստի հեռավորությունը նշանակություն չունի։',
    '4 mA is a live zero: a broken wire reads 0 mA, and is detectable.':
        '4 mA-ը «կենդանի զրո» է․ խզված լարը տալիս է 0 mA և հայտնաբերելի է։',
    'BRIDGE':
        'ԿԱՄՐՋԱԿ',
    'Four elements in a diamond, excited by a voltage; the output follows the imbalance.':
        'Շեղանկյան տեսքով չորս տարր՝ սնվող լարումով; ելքը հետևում է անհավասարակշռությանը։',
    'Strain gauges, pressure sensors, load cells.':
        'Տենզոտվիչներ, ճնշման տվիչներ, բեռնաչափեր։',
    'DIGITAL  ·  I²C / SPI':
        'ԹՎԱՅԻՆ  ·  I²C / SPI',
    'The ADC is inside the package. You receive a number, not a voltage.':
        'ԱԹԿ-ն պատյանի ներսում է։ Դուք ստանում եք թիվ, ոչ թե լարում։',
    "Almost every MEMS sensor here — and today's case.":
        'Այստեղի գրեթե բոլոր MEMS տվիչները — և այսօրվա դեպքը։',
    'VOCABULARY ONLY TODAY:   instrumentation amplifier   ·   common-mode range   ·   grounding and shielding   →   Lecture 12 in full':
        'ԱՅՍՕՐ՝ ՄԻԱՅՆ ԵԶՐՈՒՅԹՆԵՐԸ․   չափիչ ուժեղարար   ·   համաֆազ լարման տիրույթ   ·   հողանցում և էկրանավորում   →   ամբողջությամբ՝ 12-րդ դասախոսությունում',
    'A digital output does not remove the analog problems — it moves them inside the package, where you can neither see nor change them.':
        'Թվային ելքը չի վերացնում անալոգային խնդիրները․ այն տեղափոխում է դրանք պատյանի ներս, որտեղ դուք ո՛չ տեսնում եք դրանք, ո՛չ էլ կարող եք փոփոխել։',
    'And it adds two of its own: the byte order of the result, and when the conversion happened.':
        'Եվ ավելացնում է ևս երկուսը՝ արդյունքի բայթերի կարգը և այն, թե երբ է կատարվել փոխակերպումը։',
    'What an ADC actually measures':
        'Ի՞նչ է իրականում չափում ԱԹԿ-ն',
    'Not a voltage — a ratio':
        'Ոչ լարում, այլ հարաբերություն',
    'count  =  V_in / V_ref  ×  2^N':
        'կոդ  =  V_in / V_ref  ×  2^N',
    'An ADC has no idea what a volt is.':
        'ԱԹԿ-ն պատկերացում չունի, թե ինչ է վոլտը։',
    '▸  It is a ratio, not a voltage.':
        '▸  Դա հարաբերություն է, ոչ թե լարում։',
    'The count depends on the input compared with the reference. Read the formula again for what it says.':
        'Կոդը կախված է հենային լարման հետ համեմատված մուտքից։ Կարդացեք բանաձևը կրկին՝ հենց այն, ինչ գրված է։',
    '▸  Every V_ref error is a gain error.':
        '▸  V_ref-ի ամեն սխալ ուժեղացման սխալ է։',
    'Not on one reading — on every reading, in the same direction, for as long as the reference is wrong.':
        'Ոչ մեկ ցուցմունքում, այլ բոլորում՝ միևնույն ուղղությամբ, այնքան ժամանակ, քանի դեռ հենային լարումը սխալ է։',
    'The rule: excite the sensor and reference the converter from the same thing, or from two things that are both stable.':
        'Կանոնը․ տվիչի սնումը և կերպափոխիչի հենային լարումը վերցրեք միևնույն աղբյուրից, կամ երկու տարբեր, բայց կայուն աղբյուրներից։',
    'Two wirings, one sagging rail':
        'Երկու միացում, մեկ իջնող սնում',
    'A 3.3 V rail sags to 3.2 V under load. Representative bridge figures, not a named product.':
        '3.3 Վ սնման գիծն իջնում է 3.2 Վ-ի բեռի տակ։ Կամրջակի արժեքները բնորոշ են, ոչ թե անվանական սարքի։',
    'RATIOMETRIC  —  bridge and ADC reference from the SAME rail':
        'ՀԱՐԱԲԵՐԱԿՑԱՅԻՆ  —  կամրջակը և ԱԹԿ-ի հենային լարումը ՄԻԵՎՆՈՒՅՆ գծից',
    'bridge output      ↓ 3 %':
        'կամրջակի ելք      ↓ 3 %',
    'ADC counts         ↑ 3 %':
        'ԱԹԿ-ի կոդեր         ↑ 3 %',
    'reported strain    0 % error':
        'հաղորդվող դեֆորմացիա    0 % սխալ',
    'The code computes a ratio, and both terms moved together, so the ratio never changed. This is free — if you wired it deliberately.':
        'Ծրագիրը հաշվարկում է հարաբերություն, և երկու անդամներն էլ շարժվեցին միասին, ուստի հարաբերությունը չփոխվեց։ Սա անվճար է, եթե միացումը կատարվել է գիտակցաբար։',
    'ABSOLUTE  —  precision 2.5 V reference, bridge still on the rail':
        'ԲԱՑԱՐՁԱԿ  —  ճշգրիտ 2.5 Վ հենային լարում, կամրջակը դեռ սնման գծի վրա',
    'ADC counts         unchanged':
        'ԱԹԿ-ի կոդեր         անփոփոխ',
    'reported strain    3 % LOW':
        'հաղորդվող դեֆորմացիա    3 % ՑԱԾՐ',
    'Nothing cancels. And it is not a constant — it varies with whatever else the board is doing, so no calibration removes it.':
        'Ոչինչ չի կրճատվում։ Եվ սա հաստատուն մեծություն չէ․ այն փոփոխվում է՝ կախված տպասալի վրա կատարվող այլ գործընթացներից, ուստի ոչ մի չափաբերում այն չի վերացնի։',
    "Same components. Same cost. One wire's difference.":
        'Նույն բաղադրիչները։ Նույն արժեքը։ Մեկ լարի տարբերություն։',
    'POLL 2':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 2',
    "A strain-gauge bridge is excited from the microcontroller's 3.3 V rail. The ADC that reads it uses the same 3.3 V rail as its reference. Under load, the rail sags to 3.2 V.":
        'Տենզոկամրջակը սնվում է միկրոկոնտրոլլերի 3.3 Վ սնման գծից։ Այն ընթերցող ԱԹԿ-ն որպես հենային լարում օգտագործում է նույն 3.3 Վ գիծը։ Բեռի տակ լարումն իջնում է մինչև 3.2 Վ։',
    'The reported strain:':
        'Հաղորդվող դեֆորմացիան․',
    'reads about 3 % high':
        'ցույց է տալիս մոտ 3 % ավելի բարձր',
    'reads about 3 % low':
        'ցույց է տալիս մոտ 3 % ավելի ցածր',
    'does not change':
        'չի փոխվում',
    'changes by an amount that depends on the gauge factor':
        'փոխվում է տենզոզգայունության գործակցից կախված մեծությամբ',
    'Vote alone first. Then find someone who voted differently and make them defend it.':
        'Նախ քվեարկեք ինքնուրույն։ Ապա գտեք այլ կերպ քվեարկած մեկին և խնդրեք հիմնավորել իր ընտրությունը։',
    'POLL 2   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 2   ·   ՊԱՏԱՍԽԱՆ',
    'The bridge output is proportional to its excitation; the counts are proportional to 1/reference. Both scale with the same rail, so the ratio the code computes never moved.':
        'Կամրջակի ելքը համեմատական է իր սնման լարմանը, իսկ կոդերը՝ 1/հենային լարմանը։ Երկուսն էլ մասշտաբավորվում են միևնույն գծով, ուստի ծրագրի հաշվարկած հարաբերությունը չի փոխվել։',
    'Quantisation':
        'Քվանտացում',
    'The converter has a finite number of codes, so it must round':
        'Կերպափոխիչն ունի սահմանափակ թվով կոդեր, ուստի ստիպված է կլորացնել',
    'LSB  =  full scale / 2^N  =  4000 mg / 65 536  =  0.061 mg':
        'ԿՆԲ  =  չափման լրիվ տիրույթ / 2^N  =  4000 mg / 65 536  =  0.061 mg',
    'the true value':
        'իրական արժեքը',
    'what the code says':
        'ինչ ասում է կոդը',
    'input  →':
        'մուտք  →',
    'Between two codes there is nothing.':
        'Երկու կոդերի միջև ոչինչ չկա։',
    'The converter reports the nearest step and throws the difference away. The error is uniformly distributed over one LSB, and it is there in every single sample.':
        'Կերպափոխիչը հաղորդում է մոտակա աստիճանը և տարբերությունը դեն է նետում։ Սխալը հավասարաչափ բաշխված է մեկ ԿՆԲ-ի սահմաններում և առկա է յուրաքանչյուր նմուշում։',
    'It is also the only error in this lecture that is perfectly predictable before you switch anything on.':
        'Սա նաև այս դասախոսության միակ սխալն է, որը լիովին կանխատեսելի է դեռ սարքը միացնելուց առաջ։',
    'The quantisation noise':
        'Քվանտացման աղմուկը',
    'Rounding injects a known, computable amount of it':
        'Կլորացումը ներմուծում է դրա հայտնի և հաշվարկելի քանակ',
    'σ_q  =  LSB / √12  =  0.061 / 3.464  =  0.018 mg':
        'σ_q  =  ԿՆԲ / √12  =  0.061 / 3.464  =  0.018 mg',
    '√12 is the standard deviation of a uniform distribution of unit width. Worth knowing where it comes from once; not worth deriving twice.':
        '√12-ը միավոր լայնությամբ հավասարաչափ բաշխման միջին քառակուսային շեղումն է։ Արժե մեկ անգամ իմանալ, թե որտեղից է գալիս; չարժե երկու անգամ արտածել։',
    'Note what this is NOT: it is the resolution of the number, not the resolution of the measurement.':
        'Ուշադրություն դարձրեք, թե սա ինչ ՉԷ․ սա թվի լուծաչափն է, ոչ թե չափման լուծաչափը։',
    'Hold on to 0.018 mg.':
        'Հիշեք 0.018 mg-ը։',
    "Later we put it beside the sensor's own noise — and one of those two terms decides nothing at all.":
        'Այն ավելի ուշ կդնենք տվիչի սեփական աղմուկի կողքին, և այդ երկու անդամներից մեկը ոչինչ չի որոշում։',
    'Why more bits is not more truth':
        'Ինչու՞ ավելի շատ բիթը ավելի շատ ճշմարտություն չէ',
    'the noise floor of the measurement  —  identical in both':
        'չափման աղմուկային հատակը  —  երկուսում նույնական',
    '16-BIT CONVERTER':
        '16-ԲԻԹԱՆՈՑ ԿԵՐՊԱՓՈԽԻՉ',
    'one step = 0.061 mg':
        'մեկ աստիճանը = 0.061 mg',
    '20-BIT CONVERTER':
        '20-ԲԻԹԱՆՈՑ ԿԵՐՊԱՓՈԽԻՉ',
    'one step = sixteen times finer':
        'մեկ աստիճանը՝ տասնվեց անգամ ավելի մանր',
    'Adding bits divides the step. It does not divide the noise.':
        'Բիթեր ավելացնելը բաժանում է աստիճանը։ Այն չի բաժանում աղմուկը։',
    'Bits below the noise floor are extra digits, not extra information.':
        'Աղմուկային հատակից ցածր բիթերը լրացուցիչ նիշեր են, ոչ թե լրացուցիչ տեղեկույթ։',
    'Whether the last bits buy you anything depends on a number that is not on the front page — the noise density — and on a choice that is entirely yours: the bandwidth.':
        'Արդյոք վերջին բիթերը որևէ բան տալիս են, կախված է առաջին էջում չնշված մեծությունից՝ աղմուկի սպեկտրային խտությունից, և ամբողջովին ձեր ընտրությունից՝ թողունակությունից։',
    'STAND UP  ·  60 SECONDS  ·  NO TALKING':
        'ՈՏՔԻ  ·  60 ՎԱՅՐԿՅԱՆ  ·  ԱՌԱՆՑ ԽՈՍԵԼՈՒ',
    'Draw the last three boxes':
        'Հիշողությամբ գծեք շղթայի',
    'of the chain from memory':
        'վերջին երեք օղակները',
    'Under each one, write the single thing that can be lost there.':
        'Յուրաքանչյուրի տակ գրեք այն մեկ բանը, որը կարող է կորչել այնտեղ։',
    'SAMPLING          →          CODES TO UNITS          →          TIMESTAMP':
        'ՆՄՈՒՇԱՌՈՒՄ          →          ԿՈԴԵՐԻՑ ՄԻԱՎՈՐՆԵՐ          →          ԺԱՄԱՆԱԿԱՅԻՆ ԴՐՈՇՄ',
    'Turn your paper over first. Nothing to hand in.':
        'Նախ շրջեք թերթը։ Հանձնելու ոչինչ չկա։',
    'CHUNK 2':
        'ԲԱԺԻՆ 2',
    'Output data rate':
        'Ելքային տվյալների հաճախությունը',
    'is not bandwidth':
        'թողունակություն չէ',
    'The hardest idea in Module A.':
        'Մոդուլ Ա-ի ամենադժվար գաղափարը։',
    'One register bit decides whether your data contains a signal that never existed.':
        'Ռեգիստրի մեկ բիթ որոշում է, արդյոք ձեր տվյալները պարունակում են երբեք գոյություն չունեցած ազդանշան։',
    'Nyquist, as a design rule':
        'Նայքվիստը՝ որպես նախագծման կանոն',
    'Lecture 1 met this as a discovery. Today it is a register setting.':
        '1-ին դասախոսությունում սա բացահայտում էր։ Այսօր ռեգիստրի կարգավորում է։',
    'the real signal  ·  19 cycles':
        'իրական ազդանշանը  ·  19 պարբերություն',
    'The theorem is not the design rule.':
        'Թեորեմը նախագծման կանոն չէ։',
    'The design rule is its contrapositive: you must guarantee that nothing above f_max ever reaches the sampler.':
        'Նախագծման կանոնը դրա հակադիր պնդումն է․ պետք է երաշխավորել, որ f_max-ից վեր ոչինչ երբեք չհասնի նմուշառիչին։',
    'That is a filter. It is not a sample rate.':
        'Դա զտիչ է։ Դա նմուշառման հաճախություն չէ։',
    'The samples are entirely correct. Their interpretation is not.':
        'Նմուշները լիովին ճշգրիտ են։ Դրանց մեկնաբանությունը՝ ոչ։',
    'Where a tone lands after sampling':
        'Ո՞ւր է ընկնում ազդանշանը նմուշառումից հետո',
    'N is whichever integer multiple of the sample rate lies nearest to it':
        'N-ը նմուշառման հաճախության այն ամբողջ բազմապատիկն է, որն ամենամոտն է դրան',
    "Lecture 1's bearing tone, at today's ODR:   | 1520 − 15 × 104 |  =  | 1520 − 1560 |  =  40 Hz":
        '1-ին դասախոսության առանցքակալի ազդանշանը՝ այսօրվա ODR-ի դեպքում․   | 1520 − 15 × 104 |  =  | 1520 − 1560 |  =  40 Hz',
    'folds back into the band you are keeping':
        'ծալվում է ձեր պահած շերտի մեջ',
    '52 Hz — the band you believe you are measuring':
        '52 Հց — շերտը, որը կարծում եք չափում եք',
    'The sample rate alone tells you nothing about what is in your data.':
        'Նմուշառման հաճախությունն ինքնին ոչինչ չի ասում ձեր տվյալների պարունակության մասին։',
    'The one ordering that cannot be repaired':
        'Հերթականությունը, որը հնարավոր չէ ուղղել',
    'CORRECT  —  the filter sits before the sampler':
        'ՃԻՇՏ  —  զտիչը գտնվում է նմուշառիչից առաջ',
    'SIGNAL':
        'ԱԶԴԱՆՇԱՆ',
    'ANTI-ALIAS':
        'ՀԱԿԱԱԼԻԱՍԻՆԳԱՅԻՆ',
    'FILTER':
        'ԶՏԻՉ',
    'SAMPLER':
        'ՆՄՈՒՇԱՌԻՉ',
    'DIGITAL FILTER':
        'ԹՎԱՅԻՆ ԶՏԻՉ',
    '(optional)':
        '(ըստ ցանկության)',
    'Out-of-band energy is removed while it is still separable from the signal. Everything downstream is then a choice, not a repair.':
        'Շերտից դուրս էներգիան հեռացվում է, քանի դեռ այն ազդանշանից տարանջատելի է։ Դրանից հետո ամեն ինչ ընտրություն է, ոչ թե ուղղում։',
    'WRONG  —  “we will filter it in software afterwards”':
        'ՍԽԱԼ  —  «հետո ծրագրային ճանապարհով կզտենք»',
    '(too late)':
        '(արդեն ուշ է)',
    '300 Hz IS NOW':
        '300 ՀՑ-Ն ԱՅԺՄ',
    '12 Hz, FOREVER':
        '12 ՀՑ Է, ԸՆԴՄԻՇՏ',
    'By the time the data exists, a 300 Hz component and a genuine 12 Hz component are the same sequence of numbers. Not similar — identical. Nothing separates two things that are the same.':
        'Երբ տվյալներն արդեն գոյություն ունեն, 300 Հց բաղադրիչը և իրական 12 Հց բաղադրիչը թվերի միևնույն հաջորդականությունն են։ Ոչ նման, այլ նույնական։ Ոչինչ չի տարանջատում երկու նույնական մեծություն։',
    'Everything else in the chain — a wrong gain, a missed sign, a unit muddle — can be fixed on a laptop a week later. This one cannot.':
        'Շղթայի մնացած ամեն ինչ՝ սխալ ուժեղացման գործակից, բաց թողնված նշան, միավորների շփոթ, կարող է ուղղվել մեկ շաբաթ անց՝ նոութբուքի վրա։ Այս մեկը՝ ոչ։',
    'The bit that decides it':
        'Բիթը, որը որոշում է դա',
    'ISM330DHCX  ·  CTRL1_XL (0x10)  ·  reset value 0x00':
        'ISM330DHCX  ·  CTRL1_XL (0x10)  ·  վերագործարկման արժեքը 0x00',
    'bit 7':
        'բիթ 7',
    'bit 6':
        'բիթ 6',
    'bit 5':
        'բիթ 5',
    'bit 4':
        'բիթ 4',
    'bit 3':
        'բիթ 3',
    'bit 2':
        'բիթ 2',
    'bit 1':
        'բիթ 1',
    'bit 0':
        'բիթ 0',
    'output data rate  ·  0100 = 104 Hz':
        'ելքային տվյալների հաճախություն  ·  0100 = 104 Hz',
    'full scale':
        'չափման լրիվ տիրույթ',
    'the filter':
        'զտիչը',
    'LPF2_XL_EN = 0 after reset.  Your part ships with no anti-alias filter.':
        'LPF2_XL_EN = 0 վերագործարկումից հետո։  Ձեր սարքը մատակարարվում է առանց հակաալիասինգային զտիչի։',
    'So the natural sequence of events is this. You set ODR = 104 Hz. You reason, correctly, that the Nyquist limit is 52 Hz. You write “52 Hz measurement bandwidth” in the report.':
        'Ուստի իրադարձությունների բնական հաջորդականությունը հետևյալն է։ Դուք սահմանում եք ODR = 104 Հց։ Ճիշտ եզրակացնում եք, որ Նայքվիստի սահմանը 52 Հց է։ Հաշվետվության մեջ գրում եք «չափման թողունակությունը՝ 52 Հց»։',
    'Meanwhile the device is sampling a far wider analog band with no filter at all, and everything above 52 Hz folds back into your data.':
        'Այդ ընթացքում սարքը նմուշառում է շատ ավելի լայն անալոգային շերտ՝ առանց որևէ զտիչի, և 52 Հց-ից վեր ամեն ինչ ծալվում է ձեր տվյալների մեջ։',
    '0x40 gives ±2 g at 104 Hz — and leaves bit 1 clear. In Laboratory 2 you set it yourself.':
        '0x40-ը տալիս է ±2 g՝ 104 Հց-ում, և թողնում է 1-ին բիթը զրո։ 2-րդ լաբորատոր աշխատանքում այն կսահմանեք ինքներդ։',
    'POLL 3':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 3',
    'You configure the accelerometer for ODR = 104 Hz and leave CTRL1_XL bit LPF2_XL_EN at its reset value of 0. A pump on the same frame vibrates at 300 Hz.':
        'Արագաչափը կարգավորում եք ODR = 104 Հց-ի և CTRL1_XL ռեգիստրի LPF2_XL_EN բիթը թողնում եք վերագործարկման 0 արժեքով։ Նույն շրջանակի վրա տեղակայված պոմպը տատանվում է 300 Հց հաճախությամբ։',
    'What appears in your logged data?':
        'Ի՞նչ է հայտնվում ձեր գրանցված տվյալներում',
    'nothing — 300 Hz is above the sample rate, so it is not sampled':
        'ոչինչ — 300 Հց-ը նմուշառման հաճախությունից բարձր է, ուստի չի նմուշառվում',
    'a 300 Hz component, attenuated':
        '300 Հց բաղադրիչ՝ թուլացված',
    'a 12 Hz component, indistinguishable from real signal':
        '12 Հց բաղադրիչ՝ իրական ազդանշանից չտարբերակվող',
    'broadband noise, raising the noise floor slightly':
        'լայնաշերտ աղմուկ, որը փոքր-ինչ բարձրացնում է աղմուկային հատակը',
    'Vote. Then two minutes in pairs: find someone who voted differently and make them defend it. Then we vote again — and only then do we do the arithmetic.':
        'Քվեարկեք։ Ապա երկու րոպե՝ զույգերով․ գտեք այլ կերպ քվեարկած մեկին և խնդրեք հիմնավորել։ Ապա քվեարկում ենք կրկին, և միայն դրանից հետո անցնում ենք հաշվարկին։',
    'POLL 3   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 3   ·   ՊԱՏԱՍԽԱՆ',
    '| 300 − 3 × 104 |  =  | 300 − 312 |  =  12 Hz.  Squarely inside the band a tilt or vibration measurement cares about, slow enough to look like real mechanical behaviour, and permanent.':
        '| 300 − 3 × 104 |  =  | 300 − 312 |  =  12 Hz։  Հենց այն շերտում, որը կարևոր է թեքության կամ վիբրացիայի չափման համար, բավական դանդաղ՝ իրական մեխանիկական վարքի տեսք ունենալու համար, և մշտական։',
    'Three numbers, three jobs':
        'Երեք թիվ, երեք գործառույթ',
    'The sentence most often got wrong on the midterm':
        'Նախադասությունը, որում միջանկյալ քննության ժամանակ ամենից հաճախ սխալվում են',
    'What it decides':
        'Ի՞նչ է որոշում',
    'Who sets it':
        'Ո՞վ է սահմանում',
    'On your part, today':
        'Ձեր սարքում՝ այսօր',
    'ODR — output data rate':
        'ODR — ելքային տվյալների հաճախություն',
    'how often a new number appears at the output':
        'որքա՞ն հաճախ է ելքում հայտնվում նոր թիվ',
    'you, by register':
        'դուք՝ ռեգիստրով',
    '104 Hz  ·  CTRL1_XL bits 7:4':
        '104 Հց  ·  CTRL1_XL բիթեր 7:4',
    'Measurement bandwidth':
        'Չափման թողունակություն',
    'the highest frequency reported faithfully':
        'հավաստիորեն փոխանցվող առավելագույն հաճախականությունը',
    'you — often by a different register':
        'դուք՝ հաճախ այլ ռեգիստրով',
    '52 Hz  ·  only if LPF2 is on':
        '52 Հց  ·  միայն եթե LPF2-ը միացված է',
    'Anti-alias cut-off':
        'Հակաալիասինգային կտրում',
    'what reaches the sampler at all':
        'ինչն ընդհանրապես հասնում է նմուշառիչին',
    'the analog path — sometimes nobody':
        'անալոգային ուղին՝ երբեմն ոչ ոք',
    'none  ·  LPF2_XL_EN = 0':
        'չկա  ·  LPF2_XL_EN = 0',
    'Set the ODR wrongly and you get more numbers, or fewer, and you waste bus and power.':
        'Սխալ սահմանեք ODR-ը, և կստանաք ավելի շատ կամ ավելի քիչ թվեր՝ վատնելով շինան և հզորությունը։',
    'Set the cut-off wrongly and the data is wrong for ever.':
        'Սխալ սահմանեք կտրման հաճախականությունը, և տվյալները սխալ կլինեն ընդմիշտ։',
    'Sampling faster does not fix it':
        'Ավելի արագ նմուշառելը դա չի ուղղում',
    'Same pump, three configurations':
        'Նույն պոմպը, երեք կարգավորում',
    'Interfering tone':
        'Խանգարող ազդանշան',
    'Sampled at':
        'Նմուշառված',
    'Appears at':
        'Դրսևորվում է',
    '300 Hz — a pump on the same frame':
        '300 Հց — պոմպ նույն շրջանակի վրա',
    'inside your band':
        'ձեր շերտի ներսում',
    "1520 Hz — Lecture 1's bearing":
        '1520 Հց — 1-ին դասախոսության առանցքակալը',
    '300 Hz — the same pump':
        '300 Հց — նույն պոմպը',
    'it looks like an offset':
        'տեսք ունի զրոյական շեղման',
    'At 100 Hz the pump becomes a DC offset. Somebody will spend a productive week calibrating it out — and will succeed, at that one pump speed.':
        '100 Հց-ի դեպքում պոմպը դառնում է հաստատուն շեղում։ Ինչ-որ մեկը մեկ շաբաթ արդյունավետ կաշխատի այն չափաբերմամբ վերացնելու վրա և կհաջողի՝ պոմպի տվյալ պտտման հաճախության դեպքում։',
    'Succeeding is worse than failing: the calibration is then wrong at every other speed, and the sensor gets the blame.':
        'Հաջողելը ձախողվելուց վատ է․ չափաբերումն այդ դեպքում սխալ է մնացած բոլոր հաճախությունների դեպքում, իսկ մեղքը բարդվում է տվիչի վրա։',
    'Raising the sample rate moves the alias. It does not remove it. Choose the band first, then the rate.':
        'Նմուշառման հաճախությունը բարձրացնելը տեղափոխում է կեղծ ազդանշանը։ Չի վերացնում այն։ Նախ ընտրեք շերտը, ապա հաճախությունը։',
    'CHUNK 3':
        'ԲԱԺԻՆ 3',
    'Codes to':
        'Կոդերից՝',
    'trustworthy values':
        'հավաստի արժեքներ',
    'Four conversions between the die and the CSV file.':
        'Չորս փոխակերպում բյուրեղի և CSV ֆայլի միջև։',
    'Each one has a way of going wrong that produces a perfectly plausible answer.':
        'Յուրաքանչյուրն ունի սխալվելու եղանակ, որը տալիս է միանգամայն ընդունելի պատասխան։',
    'One register read, all the way to SI':
        'Մեկ ռեգիստրի ընթերցում՝ մինչև ՄՄ միավորներ',
    'Ask the class for each step before you write it':
        'Յուրաքանչյուր քայլից առաջ հարցրեք լսարանին',
    'OUTX_L_A (0x28) = 0x2C        OUTX_H_A (0x29) = 0xFF':
        'OUTX_L_A (0x28) = 0x2C        OUTX_H_A (0x29) = 0xFF',
    'little-endian: the low byte is at the lower address':
        'կրտսեր բայթն առաջ․ ցածր հասցեում կրտսեր բայթն է',
    'raw  =  0xFF2C  =  65 324   as unsigned':
        'կոդ  =  0xFF2C  =  65 324   որպես աննշան թիվ',
    "16-bit two's complement: bit 15 is set, so it is negative":
        '16 բիթ՝ երկուսի լրացմամբ․ 15-րդ բիթը սահմանված է, ուստի թիվը բացասական է',
    '65 324  −  65 536  =  −212 counts':
        '65 324  −  65 536  =  −212 կոդ',
    '× sensitivity, ±2 g → 0.061 mg/LSB':
        '× զգայունություն, ±2 g → 0.061 mg/ԿՆԲ',
    '−212  ×  0.061 mg  =  −12.9 mg':
        '−212  ×  0.061 mg  =  −12.9 mg',
    '→ SI, × 9.80665':
        '→ ՄՄ, × 9.80665',
    '−0.0129 g  ×  9.80665  =  −0.127 m/s²':
        '−0.0129 g  ×  9.80665  =  −0.127 մ/վրկ²',
    'Four steps.':
        'Չորս քայլ։',
    'Four ways to get an answer that looks entirely reasonable.':
        'Չորս եղանակ՝ ստանալու միանգամայն ողջամիտ թվացող պատասխան։',
    'All four turn up in real laboratory submissions.':
        'Չորսն էլ հանդիպում են իրական լաբորատոր հաշվետվություններում։',
    'The device is very nearly at rest, tilted slightly, on this axis.':
        'Սարքը գտնվում է գրեթե հանգստի վիճակում՝ այս առանցքով փոքր-ինչ թեքված։',
    'Four ways to a plausible wrong answer':
        'Չորս ուղի՝ ընդունելի թվացող սխալ պատասխանին',
    'All four appear in real laboratory submissions':
        'Չորսն էլ հանդիպում են իրական լաբորատոր հաշվետվություններում',
    'The mistake':
        'Սխալը',
    'What you get':
        'Ի՞նչ եք ստանում',
    'Why it is dangerous':
        'Ինչու՞ է վտանգավոր',
    'Byte order — high byte read first':
        'Բայթերի կարգ — ավագ բայթն ընթերցված առաջինը',
    '0x2CFF = 11 519 = +703 mg':
        '0x2CFF = 11 519 = +703 mg',
    'a wrong answer of a believable magnitude, which is the dangerous kind':
        'ընդունելի մեծության սխալ պատասխան, ինչը վտանգավոր տեսակն է',
    'Sign ignored — word read as unsigned':
        'Անտեսված նշան — բառը ընթերցված որպես աննշան թիվ',
    '65 324 = +3985 mg':
        '65 324 = +3985 mg',
    'a device at rest reporting nearly 4 g; at least this one announces itself':
        'հանգստի վիճակում գտնվող սարքը հաղորդում է գրեթե 4 g; գոնե սա ինքն իրեն ի ցույց է դնում',
    'IF_INC — CTRL3_C written 0x00 “to start clean”':
        'IF_INC — CTRL3_C-ում գրված է 0x00 «մաքուր վիճակից սկսելու համար»',
    'six copies of one byte':
        'մեկ բայթի վեց կրկնօրինակ',
    'CTRL3_C resets to 0x04, so auto-increment was already on. You turned it off':
        'CTRL3_C-ը վերագործարկվում է 0x04 արժեքով, ուստի ավտոմատ ինկրեմենտն արդեն միացված էր։ Դուք անջատեցիք այն',
    'Units left implicit':
        'Չնշված միավորներ',
    'mg, g and m/s² in one file':
        'mg, g և մ/վրկ² մեկ ֆայլում',
    'put the unit in the column header, once, and never in the prose':
        'միավորը մեկ անգամ նշեք սյունակի վերնագրում և երբեք՝ տեքստում',
    'The plausibility check that tests the whole chain at once: at rest, one axis reads about 9.81 m/s², and the vector sum of all three is 1 g in any orientation.':
        'Ընդունելիության ստուգումը, որը միանգամից ողջ շղթան է ստուգում․ հանգստի վիճակում մեկ առանցքը ցույց է տալիս մոտ 9.81 մ/վրկ², իսկ երեքի վեկտորական գումարը 1 g է՝ ցանկացած կողմնորոշման դեպքում։',
    'The bits you own':
        'Բիթերը, որոնք ձերն են',
    'Every figure below is already in the datasheet you have open':
        'Ստորև բերված յուրաքանչյուր արժեք արդեն առկա է ձեր բաց տվյալների թերթիկում',
    'Arithmetic':
        'Հաշվարկ',
    'Result':
        'Արդյունք',
    'full scale, ±2 g':
        'չափման լրիվ տիրույթ, ±2 g',
    '4000 mg':
        '4000 mg',
    'codes, 16-bit':
        'կոդեր, 16 բիթ',
    'LSB':
        'ԿՆԲ',
    'quantisation noise':
        'քվանտացման աղմուկ',
    'bandwidth, ODR 104 Hz, LPF2 on':
        'թողունակություն, ODR 104 Հց, LPF2 միացված',
    'sensor noise, 100 µg/√Hz (max)':
        'տվիչի աղմուկ, 100 µg/√Հց (max)',
    'noise, in LSB':
        'աղմուկը՝ ԿՆԲ-ով',
    '11.8 LSB':
        '11.8 ԿՆԲ',
    'bits that are noise':
        'բիթեր, որոնք աղմուկ են',
    '3.6 bits':
        '3.6 բիթ',
    'EFFECTIVE BITS':
        'ԱՐԴՅՈՒՆԱՐԱՐ ԲԻԹԵՐ',
    '12.4 bits':
        '12.4 բիթ',
    'The quantisation noise is forty times smaller than the sensor noise. Every argument about the last bit of an ADC is, in this system, an argument about nothing.':
        'Քվանտացման աղմուկը քառասուն անգամ փոքր է տվիչի աղմուկից։ ԱԹԿ-ի վերջին բիթի շուրջ ամեն վեճ այս համակարգում ոչնչի շուրջ վեճ է։',
    'THE ANCHOR':
        'ԽԱՐԻՍԽԸ',
    'You bought 16 bits.':
        'Դուք գնել եք 16 բիթ։',
    'You own 12.4.':
        'Ձերն է 12.4-ը։',
    "With the datasheet's typ noise density of 60 µg/√Hz the same arithmetic gives 0.433 mg and 13.2 effective bits. The part's own two printed columns move the answer by 0.8 bits — Lecture 2's lesson, restated in a new quantity.":
        'Տվյալների թերթիկի typ. աղմուկի խտության՝ 60 µg/√Հց դեպքում նույն հաշվարկը տալիս է 0.433 mg և 13.2 արդյունարար բիթ։ Սարքի իսկ երկու տպագրված սյունակները պատասխանը փոխում են 0.8 բիթով՝ 2-րդ դասախոսության եզրակացությունը, վերաշարադրված նոր մեծությամբ։',
    'The clock you did not have':
        'Ժամացույցը, որը չունեիք',
    'HAL_Delay(10) is not a 100 Hz sample rate':
        'HAL_Delay(10)-ը 100 Հց նմուշառման հաճախություն չէ',
    'HAL_Delay(10)   ·   10.000 ms':
        'HAL_Delay(10)   ·   10.000 մվրկ',
    'I²C read  ·  202 µs':
        'I²C ընթերցում  ·  202 µs',
    'one loop iteration  —  drawn to scale':
        'ցիկլի մեկ կրկնություն  —  մասշտաբով',
    'six bytes over I²C at 400 kHz':
        'վեց բայթ I²C-ով 400 կՀց հաճախությամբ',
    '81 bit-times  ÷  400 kHz  =  202 µs':
        '81 բիթ-ժամանակ  ÷  400 kHz  =  202 µs',
    '→  98.0 Hz,  not 100 Hz':
        '→  98.0 Հց,  ոչ թե 100 Հց',
    'Two per cent. Always in the same direction. Every single iteration.':
        'Երկու տոկոս։ Միշտ նույն ուղղությամբ։ Յուրաքանչյուր կրկնության մեջ։',
    'Nothing is broken. Nothing reports an error. The loop simply takes longer than you told it to —':
        'Ոչինչ չի խափանվել։ Ոչ մի սխալ չի հաղորդվում։ Ցիկլը պարզապես ավելի երկար է տևում, քան դուք նշել եք,',
    'and a delay is a minimum, never a period.':
        'իսկ ուշացումը նվազագույնն է, ոչ երբեք՝ պարբերությունը։',
    'What 203 microseconds does to ten minutes':
        'Ի՞նչ է անում 203 միկրովայրկյանը տասը րոպեի հետ',
    'You believe':
        'Դուք կարծում եք',
    'Reality':
        'Իրականում',
    'Sample interval':
        'Նմուշառման քայլ',
    '10.000 ms':
        '10.000 մվրկ',
    '10.203 ms':
        '10.203 մվրկ',
    'Sample rate':
        'Նմուշառման հաճախություն',
    'A real 20 Hz tone is reported at':
        'Իրական 20 Հց ազդանշանը հաղորդվում է որպես',
    'After 60 000 samples the log says':
        '60 000 նմուշից հետո գրանցամատյանը ցույց է տալիս',
    '600.0 s':
        '600.0 վրկ',
    '612.1 s':
        '612.1 վրկ',
    'Every event is stamped':
        'Յուրաքանչյուր իրադարձություն դրոշմված է',
    'when it happened':
        'երբ տեղի է ունեցել',
    '12.1 s too early':
        '12.1 վրկ ավելի վաղ',
    'Worse than a constant scaling error: the loop period depends on which branches ran, whether an interrupt arrived, and what the bus was doing.':
        'Ավելի վատ, քան հաստատուն մասշտաբային սխալը․ ցիկլի պարբերությունը կախված է կատարված ճյուղավորումներից, ընդհատման ժամանումից և շինայի վիճակից։',
    'You can bound this error. You cannot invert it.':
        'Այս սխալը կարող եք գնահատել վերևից։ Հնարավոր չէ շրջել այն։',
    'The fix, which is free':
        'Լուծումը, որն անվճար է',
    'Let the sensor decide when the sample happened':
        'Թողեք, որ տվիչն ինքը որոշի, թե երբ է կատարվել նմուշառումը',
    'Polling with a delay':
        'Հարցախույզ ուշացումով',
    'Data-ready interrupt':
        'Տվյալների պատրաստ լինելու ընդհատում',
    'Sets the interval':
        'Սահմանում է քայլը',
    'your software':
        'ձեր ծրագիրը',
    "the sensor's own timebase":
        'տվիչի սեփական ժամանակային բազան',
    'Interval error':
        'Քայլի սխալ',
    'loop-dependent, unbounded':
        'կախված ցիկլից, չսահմանափակված',
    'specified in the datasheet':
        'նշված է տվյալների թերթիկում',
    'Cumulative time error':
        'Կուտակվող ժամանակային սխալ',
    'grows without limit':
        'աճում է անսահմանափակ',
    'bounded by the timebase tolerance':
        'սահմանափակված ժամանակային բազայի շեղումով',
    'CPU cost':
        'Պրոցեսորի բեռ',
    'high — busy waiting':
        'բարձր — սպասում ցիկլում',
    'low':
        'ցածր',
    'Effort to implement':
        'Իրականացման բարդություն',
    'slightly less':
        'փոքր-ինչ ցածր',
    'slightly more':
        'փոքր-ինչ բարձր',
    'The sensor knows when it sampled. Ask it, rather than guessing.':
        'Տվիչը գիտի, թե երբ է նմուշառել։ Հարցրեք նրան՝ գուշակելու փոխարեն։',
    "Timestamp from a hardware timer, not a loop counter: the error becomes a published tolerance instead of your software's mood. Laboratory 2 asks for a timing plot for exactly this reason.":
        'Ժամանակային դրոշմը վերցրեք ապարատային հաշվիչից, ոչ թե ցիկլի հաշվիչից․ սխալը դառնում է հրապարակված շեղում՝ ձեր ծրագրի պատահական վարքի փոխարեն։ 2-րդ լաբորատոր աշխատանքը հենց դրա համար պահանջում է ժամանակային գծապատկեր։',
    'Knowing that the data is real':
        'Ինչպես համոզվել, որ տվյալներն իրական են',
    'Four cheap checks, each catching a failure that otherwise looks like bad data':
        'Չորս էժան ստուգում, որոնցից յուրաքանչյուրը հայտնաբերում է ձախողում, որն այլապես վատ տվյալի տեսք ունի',
    'WHO_AM_I  (0x0F)':
        'WHO_AM_I  (0x0F)',
    'Read it and compare it with 0x6B.':
        'Ընթերցեք և համեմատեք 0x6B-ի հետ։',
    'One transaction proves the address, the bus, the pull-ups and the supply, all at once.':
        'Մեկ գործարքը միանգամից հաստատում է հասցեն, շինան, ձգող դիմադրությունները և սնումը։',
    'SELF-TEST':
        'ԻՆՔՆԱՍՏՈՒԳՈՒՄ',
    'Deflect the proof mass electrostatically by a known amount.':
        'Էլեկտրաստատիկ ուժով շեղեք իներտ զանգվածը հայտնի մեծությամբ։',
    'The only check here that tests the mechanics rather than the electronics.':
        'Այստեղ միակ ստուգումն է, որը ստուգում է մեխանիկան, ոչ թե էլեկտրոնիկան։',
    'FIFO OVERRUN':
        'FIFO-Ի ԳԵՐԲԵՌՆՈՒՄ',
    'If the buffer overflowed, samples were lost and the rest are not evenly spaced.':
        'Եթե բուֆերը լցվել է, նմուշներ կորել են, և մնացածը հավասարաչափ բաշխված չեն։',
    'A dropped sample is a timing error disguised as data.':
        'Կորած նմուշը տվյալի տեսք ընդունած ժամանակային սխալ է։',
    'BUS ERROR & RECOVERY':
        'ՇԻՆԱՅԻ ՍԽԱԼ ԵՎ ՎԵՐԱԿԱՆԳՆՈՒՄ',
    'I²C can hang with a slave holding the data line low.':
        'I²C-ն կարող է կախվել, երբ ստրուկ սարքը տվյալների գիծը պահում է ցածր մակարդակի վրա։',
    'A design that cannot recover stops logging one day and gives no reason.':
        'Այն նախագիծը, որը չի կարող վերականգնվել, մի օր դադարում է գրանցել՝ առանց բացատրության։',
    'All four are omitted from most first attempts. All four turn “the data looks strange” into “the sensor was never responding”.':
        'Չորսն էլ բացակայում են առաջին փորձերի մեծ մասում։ Չորսն էլ «տվյալները տարօրինակ են» վիճակը վերածում են «տվիչն ընդհանրապես չի պատասխանել» վիճակի։',
    'POLL 1   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1   ·   ՊԱՏԱՍԽԱՆ',
    '0.72 mg — nearly twelve times the LSB. Your first answer should have been D: you had not been given the noise density. The right answer now is C, and you computed it yourselves.':
        '0.72 mg — գրեթե տասներկու անգամ ավելի մեծ, քան ԿՆԲ-ն։ Ձեր առաջին պատասխանը պետք էր լիներ D․ աղմուկի սպեկտրային խտությունը ձեզ տրված չէր։ Այժմ ճիշտ պատասխանը C-ն է, և դուք ինքներդ հաշվարկեցիք այն։',
    'POLL 4':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 4',
    'A water-level logger reads a 4–20 mA pressure loop through a 100 Ω sense resistor and a 12-bit ADC, polling in a while() loop with a 50 ms delay. It runs for a week.':
        'Ջրի մակարդակի գրանցիչը 4–20 mA ճնշման օղակը ընթերցում է 100 Ω չափիչ դիմադրության և 12-բիթանոց ԱԹԿ-ի միջոցով՝ հարցախույզով while() ցիկլում, 50 մվրկ ուշացումով։ Աշխատում է մեկ շաբաթ։',
    'Afterwards you discover all four of the following. Which one can you still fix?':
        'Հետո հայտնաբերում եք հետևյալ չորսը։ Դրանցից ո՞րը դեռ կարող եք ուղղել',
    'the reported level is 40 mm high across the whole week':
        'հաղորդվող մակարդակն ամբողջ շաբաթվա ընթացքում 40 mm ավելի բարձր է',
    'the timestamps drift, ending 90 s behind real time':
        'ժամանակային դրոշմները շեղվում են՝ վերջում 90 վրկ հետ ընկնելով իրական ժամանակից',
    'a 9.7 Hz component from the pump has folded into the band':
        'պոմպի 9.7 Հց բաղադրիչը ծալվել է շերտի մեջ',
    'the last two ADC bits were always noise':
        'ԱԹԿ-ի վերջին երկու բիթերը միշտ աղմուկ էին',
    'Different measurand, different interface, different failure — the same question underneath. Vote, then hold your answer: the next slide is the answer to this one.':
        'Այլ չափվող մեծություն, այլ ինտերֆեյս, այլ ձախողում, բայց ներքևում՝ նույն հարցը։ Քվեարկեք, ապա պահեք ձեր պատասխանը․ հաջորդ սլայդը սրա պատասխանն է։',
    'Calibratable, or gone':
        'Չափաբերմամբ ուղղելի, թե՞ կորած',
    "The table to keep — and Poll 4's answer is its first row":
        'Աղյուսակ, որն արժե պահել, և 4-րդ քվեարկության պատասխանը դրա առաջին տողն է',
    'Error':
        'Սխալ',
    'Removable afterwards?':
        'Հետագայում ուղղելի՞ է',
    'How, or why not':
        'Ինչպես, կամ ինչու ոչ',
    'YES':
        'ԱՅՈ',
    'one-point calibration against a known reference':
        'մեկ կետով չափաբերում հայտնի հենակետի նկատմամբ',
    'Scale factor':
        'Մասշտաբային գործակից',
    'two-point calibration':
        'երկու կետով չափաբերում',
    'Byte order, sign, units':
        'Բայթերի կարգ, նշան, միավորներ',
    'reinterpret the file — the bits are all there':
        'վերամեկնաբանել ֆայլը — բիթերը տեղում են',
    'Temperature drift':
        'Ջերմաստիճանային դրեյֆ',
    'PARTLY':
        'ՄԱՍԱՄԲ',
    'only if you logged the temperature. So log it':
        'միայն եթե ջերմաստիճանը գրանցել եք։ Ուստի գրանցե՛ք այն',
    'Random noise':
        'Պատահական աղմուկ',
    'averaging reduces it by √N, and costs you bandwidth':
        'միջինացումը նվազեցնում է √N անգամ և արժենում է թողունակություն',
    'NO — but negligible here':
        'ՈՉ — բայց այստեղ աննշան է',
    '0.018 mg against 0.721 mg of noise':
        '0.018 mg՝ 0.721 mg աղմուկի դիմաց',
    'Aliasing':
        'Ալիասինգ',
    'NO':
        'ՈՉ',
    'the alias and the signal are the same numbers':
        'կեղծ և իրական ազդանշանները նույն թվերն են',
    'A lost or wrong timestamp':
        'Կորած կամ սխալ ժամանակային դրոշմ',
    'the timing information was never recorded':
        'ժամանակի մասին տեղեկույթը երբեք չի արձանագրվել',
    'Everything above is a transformation of data that is still there. Everything below is missing information.':
        'Վերևի ամեն ինչ դեռևս առկա տվյալների ձևափոխություն է։ Ներքևի ամեն ինչ բացակայող տեղեկույթ է։',
    'No amount of processing creates information.':
        'Ոչ մի մշակում տեղեկույթ չի ստեղծում։',
    'Three numbers, one log file':
        'Երեք թիվ, մեկ գրանցամատյան',
    'All three were computable before a line of firmware was written':
        'Այս երեքն էլ հաշվարկելի էին նախքան որևէ ծրագրային տող գրելը',
    'BITS THAT CARRY INFORMATION':
        'ԲԻԹԵՐ, ՈՐՈՆՔ ՏԵՂԵԿՈՒՅԹ ԵՆ ԿՐՈՒՄ',
    '16 − log₂(0.721 / 0.061), from the':
        '16 − log₂(0.721 / 0.061)՝ ելնելով',
    'noise density and your bandwidth.':
        'աղմուկի խտությունից և ձեր թողունակությունից։',
    'A SIGNAL THAT DOES NOT EXIST IN THE WORLD':
        'ԱԶԴԱՆՇԱՆ, ՈՐԸ ԻՐԱԿԱՆՈՒՄ ԳՈՅՈՒԹՅՈՒՆ ՉՈՒՆԻ',
    '| 300 − 3 × 104 |. One register':
        '| 300 − 3 × 104 |։ Ռեգիստրի մեկ',
    'bit, left at its reset value of 0.':
        'բիթ՝ թողնված վերագործարկման 0 արժեքով։',
    'OF TIMESTAMP ERROR AFTER TEN MINUTES':
        'ԺԱՄԱՆԱԿԱՅԻՆ ԴՐՈՇՄԻ ՍԽԱԼ ՏԱՍԸ ՐՈՊԵ ԱՆՑ',
    '60 000 × 0.203 ms. One I²C read':
        '60 000 × 0.203 մվրկ։ Մեկ I²C ընթերցում,',
    'the loop never accounted for.':
        'որը ցիկլը երբեք հաշվի չառավ։',
    'One of the three you can state and live with. Two of them cannot be repaired afterwards at any price —':
        'Երեքից մեկը կարող եք նշել և ապրել դրա հետ։ Մյուս երկուսը հետագայում ոչ մի գնով ուղղելի չեն,',
    'and neither of those two announces itself anywhere in the file.':
        'և այդ երկուսից ոչ մեկը ֆայլում ինքն իրեն ի ցույց չի դնում։',
    'The same three numbers you were shown at the start. You now know where every one of them came from.':
        'Նույն երեք թիվը, որ ցույց տրվեց սկզբում։ Այժմ գիտեք, թե որտեղից է գալիս դրանցից յուրաքանչյուրը։',
    'The four claims a trustworthy sample makes':
        'Չորս պնդում, որ անում է հավաստի նմուշը',
    'What is it?':
        'Ի՞նչ է դա',
    'A value in SI units — with the sensitivity, the sign convention and the byte order you assumed, stated.':
        'ՄՄ միավորներով արժեք՝ նշելով ընդունված զգայունությունը, նշանի պայմանավորվածությունը և բայթերի կարգը։',
    'How much of it is information?':
        'Դրանից որքա՞նն է տեղեկույթ',
    'The effective resolution, from the noise density and YOUR bandwidth. 12.4 bits, not 16.':
        'Արդյունարար լուծաչափը՝ ելնելով աղմուկի խտությունից և ՁԵՐ թողունակությունից։ 12.4 բիթ, ոչ թե 16։',
    'Which band does it represent?':
        'Ո՞ր շերտն է այն ներկայացնում',
    'The measurement bandwidth, and evidence that a filter sat below it, before the sampler. Not the ODR.':
        'Չափման թողունակությունը և ապացույցն այն մասին, որ դրանից ցածր զտիչ է եղել՝ նմուշառիչից առաջ։ Ոչ թե ODR-ը։',
    'When did it happen?':
        'Ե՞րբ է դա տեղի ունեցել',
    'A timestamp whose error you can state, from a source you can name.':
        'Ժամանակային դրոշմ, որի սխալը կարող եք նշել, և որի աղբյուրը կարող եք անվանել։',
    'A log file that cannot answer these four is not data. It is a plausible file.':
        'Այն գրանցամատյանը, որը չի կարող պատասխանել այս չորսին, տվյալ չէ։ Այն ընդամենը ընդունելի տեսք ունեցող ֆայլ է։',
    'Week 4: Laboratory 2':
        '4-րդ շաբաթ․ Լաբորատոր աշխատանք 2',
    'Sampling, aliasing and the ADC — with the register bits in your hands':
        'Նմուշառում, ալիասինգ և ԱԹԿ — ռեգիստրի բիթերը ձեր ձեռքում',
    'PRE-LAB, before you arrive: compute the effective bits for TWO ODR settings, exactly as we did today.':
        'ՄԻՆՉ ԼԱԲՈՐԱՏՈՐԻԱ, մինչև գալը․ հաշվարկեք արդյունարար բիթերը ԵՐԿՈՒ ODR կարգավորման համար՝ ճիշտ այնպես, ինչպես այսօր արեցինք։',
    'The bench time is for measuring, not for deriving — and you will be asked for a timing plot.':
        'Լաբորատոր ժամանակը չափելու համար է, ոչ թե արտածելու — և ձեզնից կպահանջվի ժամանակային գծապատկեր։',
    'Bring one answer with you: which bit do you set so that 52 Hz actually means 52 Hz?':
        'Ձեզ հետ բերեք մեկ պատասխան․ ո՞ր բիթը պետք է սահմանել, որպեսզի 52 Հց-ը իրապես նշանակի 52 Հց',
    'AND THEN LECTURE 4':
        'ԵՎ ԱՊԱ՝ ԴԱՍԱԽՈՍՈՒԹՅՈՒՆ 4',
    'MEMS structures, transduction, fabrication and packaging — why the numbers in the datasheet are':
        'MEMS-ի կառուցվածքները, փոխակերպումը, արտադրությունը և պատյանավորումը — ինչու՞ են տվյալների թերթիկի թվերն այնպիսին, ինչպիսին են',
    'the numbers they are, and where drift comes from before anybody switches anything on.':
        'թվերն այնպիսին, ինչպիսին են, և թե որտեղից է գալիս դրեյֆը դեռ որևէ բան միացնելուց առաջ։',
    'Ninety seconds · on paper · handed in at the door':
        'Իննսուն վայրկյան · թղթի վրա · հանձնվում է դռան մոտ',
    '1  ·  JUDGEMENT':
        '1  ·  ԴԱՏՈՂՈՒԹՅՈՒՆ',
    'A colleague says:':
        'Գործընկերն ասում է․',
    '“we will sample at 1 kHz and filter it down in software afterwards.”':
        '«կնմուշառենք 1 կՀց հաճախությամբ և հետո ծրագրային ճանապարհով կզտենք»։',
    'In one sentence, what is wrong':
        'Մեկ նախադասությամբ՝ ինչն է սխալ',
    'with that plan?':
        'այդ ծրագրում',
    '2  ·  RETRIEVAL':
        '2  ·  ՎԵՐՀԻՇՈՒՄ',
    'Name one error in your Laboratory 1':
        'Նշեք 1-ին լաբորատոր աշխատանքի ձեր',
    'data that you now believe was':
        'տվյալներում մեկ սխալ, որը այժմ համարում եք',
    'IRREVERSIBLE.':
        'ԱՆԴԱՌՆԱԼԻ։',
    'One line. No explanation needed.':
        'Մեկ տող։ Բացատրություն պետք չէ։',
    "Question 2 is the one that matters. It is the input to Lecture 4's opening slide, so it will actually be read.":
        '2-րդ հարցն է կարևորը։ Այն 4-րդ դասախոսության բացման սլայդի հիմքն է, ուստի իրապես կկարդացվի։',
}
