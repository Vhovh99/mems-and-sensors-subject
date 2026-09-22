# -*- coding: utf-8 -*-
"""Armenian slide text for Lecture 4 — MEMS structures, transduction, fabrication and packaging.

Terminology follows tools/i18n/GLOSSARY-hy.md, which is the course's single source
of truth; register follows the instructor's own hand corrections recovered in
hy_instructor.py. The companion reader chapter is reader/ch04-structures-and-fabrication.md.

Loaded by translate_deck.py before hy_instructor, so any string the instructor has
personally corrected still wins.
"""

HY = {
    'MEMS structures, transduction,':
        'MEMS-ի կառուցվածքները, փոխակերպումը,',
    'fabrication and packaging':
        'արտադրությունը և պատյանավորումը',
    'Lecture 4 of 16   ·   80 minutes   ·   Module A: Foundations':
        'Դասախոսություն 4 / 16   ·   80 րոպե   ·   Մոդուլ Ա․ Հիմունքներ',
    'Two weeks ago a question had no answer. Today you learn why — and what to do instead.':
        'Երկու շաբաթ առաջ մեկ հարց մնաց անպատասխան։ Այսօր կիմանաք՝ ինչու, և ինչ անել դրա փոխարեն։',
    'MEMS & Sensors  ·  Lecture 4  ·  Structures, transduction, fabrication and packaging':
        'MEMS և տվիչներ  ·  Դասախոսություն 4',
    "From Lecture 3's exit tickets — answered before we start":
        '3-րդ դասախոսության ելքի տոմսերից՝ պատասխանված մինչ սկսելը',
    'INSTRUCTOR: fill these three in from the Lecture 3 exit tickets before class.':
        'ԴԱՍԱԽՈՍԻՆ․ լրացրեք այս երեքը 3-րդ դասախոսության ելքի տոմսերից՝ մինչ դասը։',
    'Retrieval, unaided':
        'Վերհիշում՝ առանց օգնության',
    "Lecture 1's scaling laws — say them before I show them":
        '1-ին դասախոսության մասշտաբման օրենքները — ասեք դրանք, մինչ ցույց տամ',
    'stiffness falls,':
        'կոշտությունը նվազում է,',
    'but only linearly':
        'բայց միայն գծայնորեն',
    'mass collapses —':
        'զանգվածը կտրուկ ընկնում է —',
    'the cube is the killer':
        'խորանարդն է վճռորոշը',
    'resonance climbs:':
        'ռեզոնանսը բարձրանում է․',
    'this is why MEMS are fast':
        'ահա թե ինչու են MEMS-երն արագ',
    'the world becomes':
        'աշխարհը դառնում է',
    'all surface':
        'ամբողջովին մակերևույթ',
    'Shrink a device and it gets faster and cheaper. It also gets lighter — and lighter means noisier.':
        'Փոքրացրեք սարքը, և այն կդառնա ավելի արագ և ավելի էժան։ Այն կդառնա նաև ավելի թեթև, իսկ ավելի թեթևը նշանակում է ավելի աղմկոտ։',
    'Today those four relations stop being physics and become manufacturing. Every one of them is a consequence of how the device was made.':
        'Այսօր այս չորս հարաբերությունները դադարում են ֆիզիկա լինելուց և դառնում արտադրություն։ Դրանցից յուրաքանչյուրը սարքի պատրաստման եղանակի հետևանք է։',
    'THE DEBT FROM LECTURE 2':
        'ՊԱՐՏՔԸ 2-ՐԴ ԴԱՍԱԽՈՍՈՒԹՅՈՒՆԻՑ',
    'Lecture 2, slide 22. The answer was: it is not in the datasheet, and it cannot be. I left that unpaid on purpose. Today it gets paid.':
        '2-րդ դասախոսություն, սլայդ 22։ Պատասխանն էր․ այն տվյալների թերթիկում չկա և լինել չի կարող։ Այդ պարտքը միտումնավոր թողեցի չմուծված։ Այսօր այն մուծվում է։',
    'Why no manufacturer can answer it':
        'Ինչու՞ ոչ մի արտադրող չի կարող պատասխանել դրան',
    'Because the specification is not describing a component':
        'Որովհետև տեխնիկական բնութագիրը բաղադրիչ չի նկարագրում',
    'A silicon structure a few micrometres thick':
        'Մի քանի միկրոմետր հաստությամբ սիլիցիումային կառուցվածք',
    'Suspended over a sealed cavity, free to move':
        'Կախված է հերմետիկ խոռոչի վրայով և ազատ շարժվում է',
    'Glued into a plastic box with an adhesive that cures and shrinks':
        'Սոսնձված է պլաստիկ պատյանում սոսինձով, որը կարծրանալիս կծկվում է',
    'Soldered to a board that flexes when you tighten a screw':
        'Զոդված է տպասալին, որը ծռվում է պտուտակը ձգելիս',
    'The manufacturer owns line 1 and part of line 3. Lines 3 and 4 are yours — and they are where the error enters.':
        'Արտադրողին է պատկանում 1-ին տողը և 3-րդ տողի մի մասը։ 3-րդ և 4-րդ տողերը ձերն են, և հենց այնտեղ է մտնում սխալը։',
    'POLL 1':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1',
    "In Lecture 2 you were asked for a device's cross-axis sensitivity after it is soldered to your board, and the answer was that the number is not in the datasheet.":
        '2-րդ դասախոսությունում ձեզ հարցվեց սարքի միջառանցքային զգայունությունը ձեր տպասալին զոդելուց հետո, և պատասխանն էր, որ այդ արժեքը տվյալների թերթիկում չկա։',
    'Why is it not there?':
        'Ինչու՞ այն այնտեղ չկա',
    'It is proprietary — competitors would learn from it':
        'Դա գաղտնի տեղեկություն է — մրցակիցները դրանից բան կսովորեին',
    'It depends on your board and your assembly, so no manufacturer can specify it':
        'Այն կախված է ձեր տպասալից և ձեր հավաքումից, ուստի ոչ մի արտադրող չի կարող բնութագրել այն',
    'It is in the application note, not the datasheet':
        'Այն կիրառական նշումներում է, ոչ թե տվյալների թերթիկում',
    'It is the same as the package-level figure, so printing it twice would be redundant':
        'Այն նույնն է, ինչ պատյանի մակարդակի արժեքը, ուստի երկու անգամ տպելն ավելորդ կլիներ',
    'Commit now. I am not telling you the answer until the end of the lecture — by which point you will have drawn the reason yourselves.':
        'Ընտրեք հիմա։ Պատասխանը չեմ ասելու մինչև դասախոսության վերջը, և այդ պահին դուք ինքներդ արդեն կգծեք պատճառը։',
    'The packaging tax, in the datasheet you already own':
        'Պատյանավորման հարկը՝ ձեզ արդեն պատկանող տվյալների թերթիկում',
    'ISM330DHCX · DS13012 Rev 6 · read the conditions column first':
        'ISM330DHCX · DS13012 Rev 6 · նախ կարդացեք պայմանների սյունակը',
    '25 °C, package level, not board level':
        '25 °C, պատյանի մակարդակ, ոչ տպասալի',
    '“after soldering”  —  the manufacturer is telling you, in the specification itself, that your assembly is part of the error.':
        '«զոդումից հետո»  —  արտադրողը հենց տեխնիկական բնութագրում ձեզ ասում է, որ ձեր հավաքումը սխալի մաս է կազմում։',
    '▸  Row 1 is an OFFSET: the output when the input is zero. Row 2 is DRIFT: how that offset moves.':
        '▸  1-ին տողը ԶՐՈՅԱԿԱՆ ՇԵՂՈՒՄ է․ ելքը, երբ մուտքը զրո է։ 2-րդ տողը ԴՐԵՅՖ է․ թե ինչպես է շարժվում այդ շեղումը։',
    '▸  Row 3 is the number Lecture 2 asked for — and its condition line admits it is not yours.':
        '▸  3-րդ տողն այն արժեքն է, որը պահանջեց 2-րդ դասախոսությունը, և դրա պայմանների տողն ընդունում է, որ այն ձերը չէ։',
    "Against Lecture 2's 8.73 mg":
        '2-րդ դասախոսության 8.73 mg-ի դիմաց',
    'The number on the board since week two':
        'Թիվը, որը գրատախտակին է երկրորդ շաբաթից',
    'a 0.5° tilt  =  sin(0.5°) × 1 g  =  8.73 mg':
        '0.5° թեքություն  =  sin(0.5°) × 1 g  =  8.73 mg',
    '— the entire signal we are trying to measure':
        '— ամբողջ ազդանշանը, որը փորձում ենք չափել',
    'TYP  ZERO-G LEVEL':
        'ԲՆՈՐՈՇ  ԶՐՈՅԱԿԱՆ g-Ի ՄԱԿ.',
    '±10 mg   ÷   8.73 mg':
        '±10 mg   ÷   8.73 mg',
    'MAX  ZERO-G LEVEL':
        'ԱՌԱՎ.  ԶՐՈՅԱԿԱՆ g-Ի ՄԱԿԱՐԴԱԿ',
    '±65 mg   ÷   8.73 mg':
        '±65 mg   ÷   8.73 mg',
    'Even the TYPICAL offset exceeds the whole quantity we are trying to measure. The maximum is seven and a half times it.':
        'Անգամ ԲՆՈՐՈՇ շեղումը գերազանցում է այն ամբողջ մեծությունը, որը փորձում ենք չափել։ Առավելագույնը յոթ ու կես անգամ ավելին է։',
    'CHUNK 1':
        'ԲԱԺԻՆ 1',
    'Five structures':
        'Հինգ կառուցվածք',
    'do all the work':
        'կատարում է ամբողջ աշխատանքը',
    'Proof mass on a flexure. Cantilever beam. Diaphragm. Resonator. Comb.':
        'Իներտ զանգված ճկուն կախոցի վրա։ Կախովի հեծան։ Թաղանթ։ Ռեզոնատոր։ Սանրաձև կառուցվածք։',
    'Five shapes cover every device in Lectures 5 to 11. Learn the shapes, not the catalogue.':
        'Հինգ ձև ծածկում է 5-ից 11-րդ դասախոսությունների բոլոր սարքերը։ Սովորեք ձևերը, ոչ թե ցանկը։',
    'Structure 1, and you have seen it before':
        'Կառուցվածք 1, և դուք արդեն տեսել եք այն',
    "A capacitive MEMS accelerometer, in cross-section — Lecture 1's figure, unchanged":
        'Ունակային MEMS արագաչափ՝ լայնական հատույթում — 1-ին դասախոսության նկարը, անփոփոխ',
    'flexures,  k':
        'ճկուն կախոցներ,  k',
    'Acceleration moves the mass, one gap grows and the other shrinks, and the differential C = εA/d is the signal.':
        'Արագացումը շարժում է զանգվածը, մի բացակը մեծանում է, մյուսը՝ փոքրանում, և տարբերակային C = εA/d-ն ազդանշանն է։',
    'In week one this was a drawing. Today it is a thing somebody etched, released, glued into a box and soldered down — and every one of those verbs changes d.':
        'Առաջին շաբաթում սա գծապատկեր էր։ Այսօր դա առարկա է, որը ինչ-որ մեկը փորագրել է, ազատել, սոսնձել պատյանում և զոդել, և այդ գործողություններից յուրաքանչյուրը փոխում է d-ն։',
    'Proof mass on a flexure: the three relations':
        'Իներտ զանգված ճկուն կախոցի վրա․ երեք հարաբերությունը',
    'Everything an accelerometer datasheet says is a consequence of m, k and d':
        'Արագաչափի տվյալների թերթիկի ամեն ինչ m-ի, k-ի և d-ի հետևանք է',
    'the measurand becomes a force —':
        'չափվող մեծությունը դառնում է ուժ —',
    'this is the only physics':
        'սա միակ ֆիզիկան է',
    'the force becomes a displacement —':
        'ուժը դառնում է տեղաշարժ —',
    'the flexure sets the sensitivity':
        'ճկուն կախոցը սահմանում է զգայունությունը',
    'and the same m and k set':
        'և նույն m-ը և k-ը սահմանում են',
    'the usable bandwidth':
        'օգտագործելի թողունակությունը',
    'One structure, one measurand, two specifications you cannot choose independently: sensitivity and bandwidth share m and k.':
        'Մեկ կառուցվածք, մեկ չափվող մեծություն և երկու բնութագիր, որոնք հնարավոր չէ ընտրել անկախ․ զգայունությունը և թողունակությունը կիսում են նույն m-ը և k-ը։',
    'This is why the datasheet has selectable full-scale ranges but not selectable sensitivity at a fixed range: the mass and the springs were fixed by a mask set, once, for the whole production run. Range is switched in the electronics. The mechanics are not negotiable.':
        'Ահա թե ինչու տվյալների թերթիկն ունի ընտրելի չափման լրիվ տիրույթներ, բայց ոչ ընտրելի զգայունություն ֆիքսված տիրույթում․ զանգվածը և զսպանակները մեկ անգամ սահմանվել են դիմակների հավաքածուով՝ ողջ արտադրական խմբաքանակի համար։ Տիրույթը փոխարկվում է էլեկտրոնիկայում։ Մեխանիկան բանակցելի չէ։',
    'Structures 2 and 3':
        'Կառուցվածքներ 2 և 3',
    'Cantilever beam · diaphragm over a cavity':
        'Կախովի հեծան · թաղանթ խոռոչի վրայով',
    'CANTILEVER BEAM':
        'ԿԱԽՈՎԻ ՀԵԾԱՆ',
    'SENSES':
        'ԶԳՈՒՄ Է',
    'force, and it is the flexure above':
        'ուժ, և դա վերևի ճկուն կախոցն է',
    'IN THIS COURSE':
        'ԱՅՍ ԴԱՍԸՆԹԱՑՈՒՄ',
    'L8 — force and tactile sensors':
        'L8 — ուժի և հպման տվիչներ',
    'Note the cube on t: thickness is set by DEPOSITION, so a 5 % film error is a 16 % stiffness error.':
        'Ուշադրություն դարձրեք t-ի խորանարդին․ հաստությունը սահմանվում է ՆՍՏԵՑՄԱՄԲ, ուստի թաղանթի 5 % սխալը կոշտության 16 % սխալ է։',
    'DIAPHRAGM OVER A CAVITY':
        'ԹԱՂԱՆԹ ԽՈՌՈՉԻ ՎՐԱՅՈՎ',
    'deflection  ∝  ΔP·a⁴ / (E·t³)':
        'ճկվածք  ∝  ΔP·a⁴ / (E·t³)',
    'pressure, sound':
        'ճնշում, ձայն',
    'L8 pressure · L11 microphone':
        'L8 ճնշում · L11 խոսափող',
    'No proof mass anywhere in this device. Remember that at the next poll.':
        'Այս սարքում իներտ զանգված ընդհանրապես չկա։ Հիշեք դա հաջորդ քվեարկության ժամանակ։',
    'The beam and the flexure are the same object. Structure 2 is not a new idea — it is structure 1 with the mass taken off the end.':
        'Հեծանը և ճկուն կախոցը միևնույն առարկան են։ 2-րդ կառուցվածքը նոր գաղափար չէ․ դա 1-ին կառուցվածքն է՝ ծայրից հանված զանգվածով։',
    'The diaphragm is the first structure that needs a SEALED CAVITY underneath it — which is why pressure sensors are packaging problems before they are electronics problems.':
        'Թաղանթն առաջին կառուցվածքն է, որին անհրաժեշտ է ՀԵՐՄԵՏԻԿ ԽՈՌՈՉ իր տակ, և հենց դրա համար ճնշման տվիչները պատյանավորման խնդիրներ են՝ նախքան էլեկտրոնիկայի խնդիր դառնալը։',
    'Structures 4 and 5':
        'Կառուցվածքներ 4 և 5',
    'Resonator · comb — and the comb is the reason gyroscopes exist':
        'Ռեզոնատոր · սանրաձև կառուցվածք — և սանրաձևն է պատճառը, որ գիրոսկոպները գոյություն ունեն',
    'RESONATOR':
        'ՌԵԶՈՆԱՏՈՐ',
    'f₀ shifts with mass, stress, T':
        'f₀-ը շեղվում է զանգվածով և T-ով',
    'mass, gas, temperature, time':
        'զանգված, գազ, ջերմաստիճան, ժամանակ',
    'L9 gas sensing · timing references':
        'L9 գազի զգացում · ժամանակային հենակետեր',
    'You do not measure an amplitude here. You measure a FREQUENCY — which is the cheapest thing to measure well.':
        'Այստեղ ամպլիտուդ չեք չափում։ Չափում եք ՀԱՃԱԽԱԿԱՆՈՒԹՅՈՒՆ, ինչը լավ չափելու ամենաէժան մեծությունն է։',
    'COMB STRUCTURE':
        'ՍԱՆՐԱՁԵՎ ԿԱՌՈՒՑՎԱԾՔ',
    'displacement — and it applies force too':
        'տեղաշարժ — և կիրառում է նաև ուժ',
    'L5 · L6 · L10 MEMS mirror':
        'L5 · L6 · L10 MEMS հայելի',
    'The only structure that both SENSES and DRIVES.':
        'Միակ կառուցվածքը, որը միաժամանակ ԶԳՈՒՄ Է և ԳՈՐԾԱՐԿՈՒՄ։',
    'A drive comb sustains a vibration. A sense comb reads the Coriolis deflection of that vibration. That is a gyroscope — and it is why one exists at all.':
        'Գործարկող սանրը պահպանում է տատանումը։ Զգացող սանրը ընթերցում է այդ տատանման Կորիոլիսյան շեղումը։ Դա գիրոսկոպ է, և հենց դա է դրա գոյության պատճառը։',
    'n is the number of finger pairs. The gap d is set by lithography — so the smallest feature a fab can print sets the capacitance, and that sets the noise floor.':
        'n-ը մատների զույգերի թիվն է։ d բացակը սահմանվում է վիմագրությամբ, ուստի արտադրամասի տպագրելի ամենափոքր տարրը սահմանում է ունակությունը, իսկ դա՝ աղմուկային հատակը։',
    'The five structures, in one table':
        'Հինգ կառուցվածքը՝ մեկ աղյուսակում',
    'This is the whole of Chunk 1 — it is in the handout':
        'Սա ամբողջ 1-ին բաժինն է — առկա է բաշխվող նյութում',
    'Structure':
        'Կառուցվածք',
    'Governing relation':
        'Հիմնական հարաբերություն',
    'Senses':
        'Զգում է',
    'In this course':
        'Այս դասընթացում',
    'Proof mass on a flexure':
        'Իներտ զանգված ճկուն կախոցի վրա',
    'acceleration, angular rate':
        'արագացում, անկյունային արագություն',
    'L5 accelerometer, L6 gyroscope':
        'L5 արագաչափ, L6 գիրոսկոպ',
    'Cantilever beam':
        'Կախովի հեծան',
    'force (it is the flexure above)':
        'ուժ (դա վերևի ճկուն կախոցն է)',
    'L8 force / tactile':
        'L8 ուժ / հպում',
    'Diaphragm over a cavity':
        'Թաղանթ խոռոչի վրայով',
    'deflection ∝ ΔP·a⁴/(E·t³)':
        'ճկվածք ∝ ΔP·a⁴/(E·t³)',
    'L8 pressure, L11 microphone':
        'L8 ճնշում, L11 խոսափող',
    'Resonator':
        'Ռեզոնատոր',
    'L9 gas microheater, timing':
        'L9 գազի միկրոջեռուցիչ, ժամանակաչափում',
    'Comb structure':
        'Սանրաձև կառուցվածք',
    'displacement — sense AND drive':
        'տեղաշարժ — զգում ԵՎ գործարկում',
    'L5, L6, L10 MEMS mirror':
        'L5, L6, L10 MEMS հայելի',
    'Five, not a taxonomy. Five is what fits in working memory — and five is genuinely enough for seven lectures.':
        'Հինգ, ոչ թե դասակարգում։ Հինգն այն է, ինչ տեղավորվում է աշխատանքային հիշողությունում, և հինգն իրապես բավական է յոթ դասախոսության համար։',
    'POLL 2':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 2',
    'Four MEMS devices. Which one does NOT contain a proof mass?':
        'Չորս MEMS սարք։ Դրանցից ո՞րը ՉԻ պարունակում իներտ զանգված',
    'a 3-axis accelerometer':
        'եռառանցք արագաչափ',
    'a vibrating-structure gyroscope':
        'տատանվող կառուցվածքով գիրոսկոպ',
    'a barometric pressure sensor':
        'բարոմետրիկ ճնշման տվիչ',
    'a MEMS microphone':
        'MEMS խոսափող',
    'Vote alone, hands up on my count. Then I am going to tell you something honest about this question.':
        'Քվեարկեք ինքնուրույն, ձեռքերը վեր՝ իմ հաշվով։ Ապա ձեզ ազնիվ բան կասեմ այս հարցի մասին։',
    'POLL 2   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 2   ·   ՊԱՏԱՍԽԱՆ',
    'If you voted D you were right about the physics and I asked a bad question — a microphone is a diaphragm too. Both C and D respond to pressure across a membrane, not to the inertia of a suspended block.':
        'Եթե քվեարկել եք D, ֆիզիկայի առումով ճիշտ էիք, իսկ ես վատ հարց էի տվել․ խոսափողը նույնպես թաղանթ ունի։ Ե՛վ C-ն, և՛ D-ն արձագանքում են թաղանթի վրայի ճնշմանը, ոչ թե կախված զանգվածի իներցիային։',
    'Why five shapes cover seven lectures':
        'Ինչու՞ հինգ ձևը ծածկում է յոթ դասախոսություն',
    'Every device in Module B, and the structure underneath it':
        'Մոդուլ Բ-ի բոլոր սարքերը և դրանց հիմքում ընկած կառուցվածքը',
    'Lecture':
        'Դասախոսություն',
    'Transduction':
        'Փոխակերպում',
    'accelerometer':
        'արագաչափ',
    'proof mass on a flexure':
        'իներտ զանգված ճկուն կախոցի վրա',
    'capacitive':
        'ունակային',
    'gyroscope':
        'գիրոսկոպ',
    'comb drive + proof mass':
        'սանրաձև գործարկիչ + իներտ զանգված',
    'magnetometer':
        'մագնիսաչափ',
    'none — nothing moves':
        'չկա — ոչինչ չի շարժվում',
    'electromagnetic':
        'էլեկտրամագնիսական',
    'pressure sensor':
        'ճնշման տվիչ',
    'diaphragm over a cavity':
        'թաղանթ խոռոչի վրայով',
    'piezoresistive':
        'պիեզոդիմադրական',
    'force / tactile':
        'ուժ / հպում',
    'cantilever beam':
        'կախովի հեծան',
    'gas sensor':
        'գազի տվիչ',
    'resonator / microheater':
        'ռեզոնատոր / միկրոջեռուցիչ',
    'thermal':
        'ջերմային',
    'comb':
        'սանրաձև',
    'electrostatic drive':
        'էլեկտրաստատիկ գործարկում',
    'diaphragm':
        'թաղանթ',
    'Eight devices. Five shapes. One of them needs no moving structure at all — and knowing which is worth as much as knowing the rest.':
        'Ութ սարք։ Հինգ ձև։ Դրանցից մեկին ընդհանրապես շարժվող կառուցվածք պետք չէ, և իմանալը, թե որին, արժե այնքան, որքան մնացածն իմանալը։',
    'THE POINT OF CHUNK 1':
        '1-ԻՆ ԲԱԺՆԻ ԻՄԱՍՏԸ',
    'You are not about to learn':
        'Դուք չեք սովորելու',
    'eleven devices.':
        'տասնմեկ սարք։',
    'You are about to learn five structures and six transduction principles, and then watch them get recombined seven times. Module B is not a catalogue. It is one method, applied.':
        'Դուք սովորելու եք հինգ կառուցվածք և վեց փոխակերպման սկզբունք, ապա կհետևեք, թե ինչպես են դրանք յոթ անգամ վերահամակցվում։ Մոդուլ Բ-ն ցանկ չէ։ Դա մեկ մեթոդ է՝ կիրառված։',
    'One structure, four different sensors':
        'Մեկ կառուցվածք, չորս տարբեր տվիչ',
    'The resonator, to show that the shape is the reusable part':
        'Ռեզոնատորը՝ ցույց տալու համար, որ ձևն է վերաօգտագործելի մասը',
    'MASS':
        'ԶԱՆԳՎԱԾ',
    'a molecule lands on it;':
        'մոլեկուլը նստում է դրա վրա;',
    'f₀ drops':
        'f₀-ն նվազում է',
    'GAS':
        'ԳԱԶ',
    'a coating adsorbs a species;':
        'ծածկույթը կլանում է նյութը;',
    'the mass changes':
        'զանգվածը փոխվում է',
    'TEMPERATURE':
        'ՋԵՐՄԱՍՏԻՃԱՆ',
    "Young's modulus changes;":
        'Յունգի մոդուլը փոխվում է;',
    'f₀ tracks it':
        'f₀-ն հետևում է դրան',
    'TIME':
        'ԺԱՄԱՆԱԿ',
    'nothing changes;':
        'ոչինչ չի փոխվում;',
    'f₀ IS the output':
        'f₀-ն ԻՆՔՆ Է ելքը',
    'Same beam. Same equation. Four products — and one of them is a bug in the other three.':
        'Նույն հեծանը։ Նույն հավասարումը։ Չորս արտադրանք, և դրանցից մեկը մյուս երեքի համար խանգարում է։',
    'Temperature shifts f₀ whether you asked it to or not: in a gas sensor that is an error term to compensate, and in a thermometer it is the whole product.':
        'Ջերմաստիճանը շեղում է f₀-ը՝ անկախ ձեր ցանկությունից․ գազի տվիչում դա փոխհատուցման ենթակա սխալի բաղադրիչ է, իսկ ջերմաչափում՝ ամբողջ արտադրանքը։',
    'CHUNK 2':
        'ԲԱԺԻՆ 2',
    'Six principles,':
        'Վեց սկզբունք,',
    'one question that sorts them':
        'մեկ հարց, որը դասակարգում է դրանք',
    'Capacitive · piezoresistive · piezoelectric · thermal · electromagnetic · optical':
        'Ունակային · պիեզոդիմադրական · պիեզոէլեկտրական · ջերմային · էլեկտրամագնիսական · օպտիկական',
    'The question: can it measure something that is not moving?':
        'Հարցը․ կարո՞ղ է այն չափել այն, ինչ չի շարժվում',
    'The two that carry Module B':
        'Երկուսը, որոնք տանում են Մոդուլ Բ-ն',
    'Both answer yes to the static question':
        'Երկուսն էլ ստատիկ հարցին պատասխանում են այո',
    'CAPACITIVE':
        'ՈՒՆԱԿԱՅԻՆ',
    'STATIC (DC) RESPONSE:   YES':
        'ՍՏԱՏԻԿ (DC) ԱՐՁԱԳԱՆՔ․   ԱՅՈ',
    'SIGNAL':
        'ԱԶԴԱՆՇԱՆ',
    'small, high-impedance':
        'փոքր, բարձր դիմադրությամբ',
    'MAIN WEAKNESS':
        'ՀԻՄՆԱԿԱՆ ԹՈՒՅԼ ԿՈՂՄԸ',
    'needs on-chip electronics; stray capacitance everywhere':
        'պահանջում է էլեկտրոնիկա նույն բյուրեղում; ամենուր՝ մակաբույծ ունակություն',
    'EXPLAINS THE DATASHEET LINE':
        'ԲԱՑԱՏՐՈՒՄ Է ՏՎՅԱԼՆԵՐԻ ԹԵՐԹԻԿԻ ՏՈՂԸ',
    'why the ISM330DHCX can measure tilt at all':
        'ինչու՞ ISM330DHCX-ն ընդհանրապես կարող է չափել թեքություն',
    'PIEZORESISTIVE':
        'ՊԻԵԶՈԴԻՄԱԴՐԱԿԱՆ',
    'millivolts from a bridge':
        'միլիվոլտեր կամրջակից',
    'a strong temperature coefficient — the bridge drifts':
        'ուժեղ ջերմաստիճանային գործակից — կամրջակը դրեյֆ ունի',
    'why pressure sensors need temperature compensation':
        'ինչու՞ ճնշման տվիչներին անհրաժեշտ է ջերմաստիճանային փոխհատուցում',
    'Capacitive measures a GAP. Piezoresistive measures a STRAIN. Both hold their reading when the world stops moving — and that is not a given.':
        'Ունակայինը չափում է ԲԱՑԱԿ։ Պիեզոդիմադրականը չափում է ԴԵՖՈՐՄԱՑԻԱ։ Երկուսն էլ պահում են իրենց ցուցմունքը, երբ աշխարհը դադարում է շարժվել, և դա ինքնըստինքյան տրված չէ։',
    'The one that answers no':
        'Այն մեկը, որը պատասխանում է ոչ',
    'Piezoelectric — self-generating, and blind to anything still':
        'Պիեզոէլեկտրական — ինքնագեներացնող և կույր ամեն անշարժի նկատմամբ',
    'PIEZOELECTRIC':
        'ՊԻԵԶՈԷԼԵԿՏՐԱԿԱՆ',
    'STATIC (DC) RESPONSE:   NO':
        'ՍՏԱՏԻԿ (DC) ԱՐՁԱԳԱՆՔ․   ՈՉ',
    'charge, self-generating — no supply needed':
        'լիցք, ինքնագեներացնող — սնում պետք չէ',
    'no DC response at all; the charge leaks away':
        'ընդհանրապես DC արձագանք չկա; լիցքը հոսում է դուրս',
    'why vibration sensors quote a LOW-frequency limit':
        'ինչու՞ վիբրացիայի տվիչները նշում են ՑԱԾՐ հաճախականային սահման',
    'TILT  (the input) — stepped to 0.5° and held':
        'ԹԵՔՈՒԹՅՈՒՆ  (մուտքը) — բարձրացված 0.5°-ի և պահված',
    'held for years':
        'պահվում է տարիներ',
    "PIEZOELECTRIC OUTPUT — decays with the amplifier's τ":
        'ՊԻԵԶՈԷԼԵԿՏՐԱԿԱՆ ԵԼՔ — մարում է ուժեղարարի τ-ով',
    'A piezoelectric element responds to a CHANGE in strain. Hold it still and the output goes to zero — not badly, but exactly to zero.':
        'Պիեզոէլեկտրական տարրն արձագանքում է դեֆորմացիայի ՓՈՓՈԽՈՒԹՅԱՆԸ։ Պահեք այն անշարժ, և ելքը կդառնա զրո՝ ոչ թե վատ, այլ ճիշտ զրո։',
    'Thermal and electromagnetic':
        'Ջերմային և էլեկտրամագնիսական',
    'Honestly brief — you meet both again in Module B':
        'Ազնվորեն համառոտ — երկուսին էլ կհանդիպեք Մոդուլ Բ-ում',
    'THERMAL':
        'ՋԵՐՄԱՅԻՆ',
    'STATIC (DC) RESPONSE:   YES, SLOWLY':
        'ՍՏԱՏԻԿ (DC) ԱՐՁԱԳԱՆՔ․   ԱՅՈ, ԴԱՆԴԱՂ',
    'microvolts, or a resistance change':
        'միկրովոլտեր կամ դիմադրության փոփոխություն',
    'slow; and it heats itself, so it measures its own power':
        'դանդաղ; և ինքն իրեն տաքացնում է, ուստի չափում է իր իսկ հզորությունը',
    'the warm-up time on a gas sensor':
        'գազի տվիչի տաքացման ժամանակը',
    'ELECTROMAGNETIC':
        'ԷԼԵԿՏՐԱՄԱԳՆԻՍԱԿԱՆ',
    'large, low-impedance — the easy signal':
        'մեծ, ցածր դիմադրությամբ — հարմար ազդանշանը',
    'hard to shrink, and it responds to every magnet nearby':
        'դժվար է փոքրացնել, և արձագանքում է շրջակա ամեն մագնիսի',
    'the hard- and soft-iron terms in Lecture 7':
        'կոշտ և փափուկ երկաթի բաղադրիչները 7-րդ դասախոսությունում',
    'Thermal is the only principle whose own operation disturbs the measurand. Electromagnetic is the only one that fights the scaling laws instead of using them.':
        'Ջերմայինը միակ սկզբունքն է, որի աշխատանքն ինքը խանգարում է չափվող մեծությանը։ Էլեկտրամագնիսականը միակն է, որը պայքարում է մասշտաբման օրենքների դեմ՝ դրանք օգտագործելու փոխարեն։',
    'Optical':
        'Օպտիկական',
    'The last principle, and the one that costs the most package':
        'Վերջին սկզբունքը, և ամենաշատ պատյան պահանջողը',
    'OPTICAL':
        'ՕՊՏԻԿԱԿԱՆ',
    'can be very large — sometimes no amplifier at all':
        'կարող է շատ մեծ լինել — երբեմն ուժեղարար ընդհանրապես պետք չէ',
    'needs a window, and the window sees ambient light':
        'անհրաժեշտ է պատուհան, իսկ պատուհանը տեսնում է շրջակա լույսը',
    'the cover-window design in Lecture 10':
        'ծածկող պատուհանի նախագծումը 10-րդ դասախոսությունում',
    'THE THREE BRIEF ONES COME BACK HERE':
        'ԵՐԵՔ ՀԱՄԱՌՈՏՆԵՐԸ ՎԵՐԱԴԱՌՆՈՒՄ ԵՆ ԱՅՍՏԵՂ',
    'magnetometers, and why they need calibrating in situ':
        'մագնիսաչափեր, և ինչու՞ դրանք պետք է չափաբերվեն տեղում',
    'gas sensing, self-heating and warm-up':
        'գազի զգացում, ինքնատաքացում և տաքացման ժամանակ',
    'optical':
        'օպտիկական',
    'MEMS mirrors, and the window you must design':
        'MEMS հայելիներ, և պատուհանը, որը պետք է նախագծեք',
    'Three principles, one slide each. That is proportionate.':
        'Երեք սկզբունք, յուրաքանչյուրին՝ մեկ սլայդ։ Դա համաչափ է։',
    'Optical is the only principle where the PACKAGE is part of the transduction: no window, no measurement.':
        'Օպտիկականը միակ սկզբունքն է, որտեղ ՊԱՏՅԱՆԸ փոխակերպման մաս է կազմում․ չկա պատուհան, չկա չափում։',
    'POLL 3':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 3',
    'A piezoelectric accelerometer — representative industrial vibration type — is mounted on the solar-tracker frame from Lecture 2 to measure its tilt. The frame is tilted to 0.5° and held there.':
        'Պիեզոէլեկտրական արագաչափը՝ արդյունաբերական վիբրացիոն տիպի բնորոշ ներկայացուցիչ, ամրացված է 2-րդ դասախոսության արևին հետևող շրջանակին՝ դրա թեքությունը չափելու համար։ Շրջանակը թեքվում է 0.5°-ի և պահվում այդ դիրքում։',
    'Thirty seconds later, the reported tilt is:':
        'Երեսուն վայրկյան անց հաղորդվող թեքությունը՝',
    '0.5°, correctly':
        '0.5°, ճիշտ',
    '0.5° but very noisy':
        '0.5°, բայց շատ աղմկոտ',
    "it depends on the amplifier's gain":
        'կախված է ուժեղարարի ուժեղացման գործակցից',
    'Vote. Then in pairs: one of you argues it reads 0.5°, the other argues it reads zero — then decide. Two minutes.':
        'Քվեարկեք։ Ապա զույգերով․ մեկդ պնդում է, որ ցույց է տալիս 0.5°, մյուսը՝ որ զրո, ապա որոշեք։ Երկու րոպե։',
    'POLL 3   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 3   ·   ՊԱՏԱՍԽԱՆ',
    "Zero. Charge appears when the strain CHANGES; held still, it leaks away through the amplifier's input impedance in a few seconds. A piezoelectric accelerometer has no DC response. It cannot measure tilt — not badly, at all.":
        'Զրո։ Լիցքը հայտնվում է, երբ դեֆորմացիան ՓՈՓՈԽՎՈՒՄ Է; անշարժ պահելիս այն մի քանի վայրկյանում հոսում է դուրս ուժեղարարի մուտքային դիմադրության միջով։ Պիեզոէլեկտրական արագաչափը DC արձագանք չունի։ Այն չի կարող չափել թեքություն՝ ոչ թե վատ, այլ ընդհանրապես։',
    'Six principles, sorted by one question':
        'Վեց սկզբունք՝ դասակարգված մեկ հարցով',
    'Can it measure something that is standing still?':
        'Կարո՞ղ է այն չափել այն, ինչ անշարժ է',
    'Principle':
        'Սկզբունք',
    'Static (DC)?':
        'Ստատիկ (DC)',
    'Signal':
        'Ազդանշան',
    'Main weakness':
        'Հիմնական թույլ կողմը',
    'Capacitive':
        'Ունակային',
    'needs on-chip electronics; stray C':
        'էլեկտրոնիկան՝ նույն բյուրեղում; մակաբույծ C',
    'Piezoresistive':
        'Պիեզոդիմադրական',
    'mV from a bridge':
        'mV կամրջակից',
    'strong temperature coefficient':
        'ուժեղ ջերմաստիճանային գործակից',
    'Piezoelectric':
        'Պիեզոէլեկտրական',
    'charge, self-generating':
        'լիցք, ինքնագեներացնող',
    'no DC response; the charge leaks':
        'DC արձագանք չկա; լիցքը հոսում է դուրս',
    'Thermal':
        'Ջերմային',
    'yes, slowly':
        'այո, դանդաղ',
    'µV or resistance':
        'µV կամ դիմադրություն',
    'slow; self-heating':
        'դանդաղ; ինքնատաքացում',
    'Electromagnetic':
        'Էլեկտրամագն.',
    'large, low-impedance':
        'մեծ, ցածր դիմադրությամբ',
    'hard to shrink; magnetically susceptible':
        'դժվար փոքրացվող; մագնիսականորեն խոցելի',
    'can be very large':
        'կարող է շատ մեծ լինել',
    'needs a window; ambient light':
        'անհրաժեշտ է պատուհան; շրջակա լույս',
    'One “no” in the whole column — and it belongs to the principle that looks most impressive on a front page.':
        'Ամբողջ սյունակում մեկ «ոչ», և այն պատկանում է այն սկզբունքին, որն առաջին էջում ամենատպավորիչ տեսք ունի։',
    'And what each one explains in a datasheet':
        'Ի՞նչ է բացատրում յուրաքանչյուրը',
    "The reason this chunk exists: every principle is a specification's cause":
        'Այս բաժնի գոյության պատճառը․ յուրաքանչյուր սկզբունք տեխնիկական բնութագրի պատճառ է',
    'The datasheet line it explains':
        'Տվյալների թերթիկի տողը, որը բացատրում է',
    'why vibration sensors quote a low-frequency limit':
        'ինչու՞ վիբրացիայի տվիչները նշում են ցածր հաճախականային սահման',
    'A specification is never arbitrary. Somewhere behind every line is a structure, a principle, or a process step.':
        'Տեխնիկական բնութագիրը երբեք կամայական չէ։ Յուրաքանչյուր տողի հետևում կանգնած է կառուցվածք, սկզբունք կամ գործընթացի քայլ։',
    'CHUNK 3':
        'ԲԱԺԻՆ 3',
    'How it is made,':
        'Ինչպես է այն պատրաստվում,',
    'and what that costs you':
        'և ինչ արժե դա ձեզ',
    'Four process steps. One consequence each. That is the whole treatment.':
        'Չորս գործընթացային քայլ։ Յուրաքանչյուրին՝ մեկ հետևանք։ Ահա ամբողջ շարադրանքը։',
    'This is not a fabrication course — fabrication is here because it explains the datasheet.':
        'Սա արտադրության դասընթաց չէ — արտադրությունն այստեղ է, քանի որ բացատրում է տվյալների թերթիկը։',
    'Four steps, in order':
        'Չորս քայլ՝ ըստ հերթականության',
    'One consequence each — and that is the entire treatment':
        'Յուրաքանչյուրին՝ մեկ հետևանք, և ահա ամբողջ շարադրանքը',
    'LITHOGRAPHY':
        'ՎԻՄԱԳՐՈՒԹՅՈՒՆ',
    'minimum feature size':
        'նվազագույն տարրի չափը',
    '→ the comb gap d':
        '→ սանրի d բացակը',
    '→ the capacitance':
        '→ ունակությունը',
    '→ the noise floor':
        '→ աղմուկային հատակը',
    'DEPOSITION':
        'ՆՍՏԵՑՈՒՄ',
    'film thickness, and':
        'թաղանթի հաստությունը և',
    'RESIDUAL STRESS —':
        'ՄՆԱՑՈՐԴԱՅԻՆ ԼԱՐՎԱԾՈՒԹՅՈՒՆԸ —',
    'the structure is curved':
        'կառուցվածքը ծռված է',
    'before you use it':
        'դեռ օգտագործելուց առաջ',
    'ETCHING':
        'ՓՈՐԱԳՐՈՒՄ',
    'isotropic or anisotropic':
        'իզոտրոպ, թե՞ անիզոտրոպ',
    'decides which shapes':
        'որոշում է, թե որ ձևերն են',
    'are possible at all':
        'ընդհանրապես հնարավոր',
    'RELEASE':
        'ԱԶԱՏՈՒՄ',
    'the sacrificial layer goes,':
        'զոհաբերվող շերտը հեռանում է,',
    'the structure is free —':
        'կառուցվածքն ազատ է —',
    'and can STICK':
        'և կարող է ԿՊՉԵԼ',
    'PAIRS · 3 MINUTES · cards on your desk: put the four steps in order, then match each one to its consequence.':
        'ԶՈՒՅԳԵՐՈՎ · 3 ՐՈՊԵ · քարտերը ձեր սեղանին․ դասավորեք չորս քայլերը հերթականությամբ, ապա յուրաքանչյուրին համապատասխանեցրեք իր հետևանքը։',
    'Then one question: which of the four is the reason a MEMS accelerometer is noisier than a bench instrument?':
        'Ապա մեկ հարց․ չորսից ո՞րն է պատճառը, որ MEMS արագաչափն ավելի աղմկոտ է, քան լաբորատոր չափիչ սարքը',
    'Bulk or surface':
        'Ծավալային, թե՞ մակերևութային',
    'Two ways to build the same shape, and the trade-off is mass':
        'Նույն ձևը կառուցելու երկու եղանակ, և փոխզիջումը զանգվածն է',
    'BULK MICROMACHINING':
        'ԾԱՎԱԼԱՅԻՆ ՄԻԿՐՈՄՇԱԿՈՒՄ',
    'SURFACE MICROMACHINING':
        'ՄԱԿԵՐԵՎՈՒԹԱՅԻՆ ՄԻԿՐՈՄՇԱԿՈՒՄ',
    '▸  etches INTO the wafer':
        '▸  փորագրում է թիթեղի ՄԵՋ',
    '▸  builds UP from thin films':
        '▸  կառուցում է ՎԵՐԵՎ՝ բարակ թաղանթներից',
    '▸  thick structures, large proof masses':
        '▸  հաստ կառուցվածքներ, մեծ իներտ զանգվածներ',
    '▸  micrometres thick, small masses':
        '▸  միկրոմետրերի հաստություն, փոքր զանգվածներ',
    '▸  low noise floor':
        '▸  ցածր աղմուկային հատակ',
    '▸  higher noise floor':
        '▸  ավելի բարձր աղմուկային հատակ',
    '▸  big die, expensive, hard to integrate':
        '▸  մեծ բյուրեղ, թանկ, դժվար ինտեգրելի',
    '▸  cheap, small, on the same die as the electronics':
        '▸  էժան, փոքր, էլեկտրոնիկայի հետ նույն բյուրեղում',
    '▸  pressure sensors, high-grade inertial':
        '▸  ճնշման տվիչներ, բարձրակարգ իներցիոն սարքեր',
    '▸  consumer IMUs — the part in your kit':
        '▸  զանգվածային IMU-ներ — ձեր հավաքածուի սարքը',
    "The trade-off is MASS — and by Lecture 1's m ∝ L³ you could already predict which one is quieter.":
        'Փոխզիջումը ԶԱՆԳՎԱԾՆ է, և 1-ին դասախոսության m ∝ L³-ով դուք արդեն կարող էիք կանխատեսել, թե որն է ավելի քիչ աղմկոտ։',
    "Your kit's part is not the quietest accelerometer buildable — only the quietest that fits beside its own ADC.":
        'Ձեր հավաքածուի սարքը կառուցելի ամենաքիչ աղմկոտ արագաչափը չէ, այլ միայն ամենաքիչ աղմկոտն այնպիսիններից, որոնք տեղավորվում են իրենց սեփական ԱԹԿ-ի կողքին։',
    'Release: the step that makes it a machine':
        'Ազատում․ քայլը, որը դարձնում է այն մեքենա',
    'The sacrificial layer — and what happens when the beam comes down instead':
        'Զոհաբերվող շերտը, և ինչ է լինում, երբ հեծանն իջնում է դրա փոխարեն',
    '1 · AS DEPOSITED':
        '1 · ՆՍՏԵՑՎԱԾ ՎԻՃԱԿՈՒՄ',
    'SUBSTRATE':
        'ՀԵՆՔ',
    'SACRIFICIAL LAYER':
        'ԶՈՀԱԲԵՐՎՈՂ ՇԵՐՏ',
    'structural film on top of a':
        'կառուցվածքային թաղանթը դրված է',
    'sacrificial layer — nothing moves yet':
        'զոհաբերվող շերտի վրա — դեռ ոչինչ չի շարժվում',
    '2 · RELEASED':
        '2 · ԱԶԱՏՎԱԾ',
    'free to move':
        'ազատ շարժվում է',
    'the sacrificial layer is etched away.':
        'զոհաբերվող շերտը փորագրվում և հեռացվում է։',
    'The beam is free. This is the machine.':
        'Հեծանն ազատ է։ Ահա մեքենան։',
    '3 · STUCK':
        '3 · ԿՊՉԱԾ',
    'welded shut':
        'հերմետիկ կպած',
    'surface forces pull it down and it':
        'մակերևութային ուժերն այն ներքև են քաշում և',
    'stays down. The device is dead.':
        'մնում է ներքև։ Սարքն անգործունակ է։',
    "Stiction is Lecture 1's A/V ∝ 1/L arriving as a yield problem: at this scale surface forces beat the restoring force of the spring.":
        'Ստիկցիան 1-ին դասախոսության A/V ∝ 1/L-ն է, որը հայտնվում է որպես ելքային բերքի խնդիր․ այս մասշտաբում մակերևութային ուժերը գերազանցում են զսպանակի վերականգնող ուժը։',
    'Stiction is also a field failure: condensation, shock or electrostatics can bring a beam down later.':
        'Ստիկցիան նաև շահագործման ընթացքի ձախողում է․ խտացումը, հարվածը կամ էլեկտրաստատիկան կարող են հեծանն իջեցնել ավելի ուշ։',
    'The package is not protection. It is physics.':
        'Պատյանը պաշտպանություն չէ։ Դա ֆիզիկա է։',
    'Cavity · die attach · wire bond · seal · getter':
        'Խոռոչ · բյուրեղի ամրացում · լարային միացում · խափանում · գազակլանիչ',
    'LID  ·  HERMETIC SEAL':
        'ԿԱՓԱՐԻՉ  ·  ՀԵՐՄԵՏԻԿ ԽԱՓԱՆՈՒՄ',
    'CAVITY — sealed, often at reduced pressure':
        'ԽՈՌՈՉ — հերմետիկ, հաճախ իջեցված ճնշմամբ',
    'MEMS DIE':
        'MEMS ԲՅՈՒՐԵՂ',
    'DIE ATTACH':
        'ԲՅՈՒՐԵՂԻ ԱՄՐԱՑՈՒՄ',
    'GETTER':
        'ԳԱԶԱԿԼԱՆԻՉ',
    'wire bonds':
        'լարային միացումներ',
    'PCB — YOUR BOARD':
        'ՏՊԱՍԱԼ — ՁԵՐ ՏՊԱՍԱԼԸ',
    'WHAT EACH PART IS ACTUALLY FOR':
        'ԻՆՉԻ ՀԱՄԱՐ Է ԻՐԱԿԱՆՈՒՄ ՅՈՒՐԱՔԱՆՉՅՈՒՐ ՄԱՍԸ',
    'CAVITY':
        'ԽՈՌՈՉ',
    'a void at a controlled pressure —':
        'դատարկություն վերահսկվող ճնշմամբ,',
    'and that pressure sets the damping':
        'և այդ ճնշումը սահմանում է դեմպֆերումը',
    'an adhesive that cures, shrinks':
        'սոսինձ, որը կարծրանում է, կծկվում',
    'and stresses the die on day one':
        'և առաջին օրվանից լարում է բյուրեղը',
    'WIRE BOND':
        'ԼԱՐԱՅԻՆ ՄԻԱՑՈՒՄ',
    'a mechanical link to a moving':
        'մեխանիկական կապ շարժվող',
    'object: a spring, and a stress':
        'առարկայի հետ․ զսպանակ և լարվածություն',
    'SEAL':
        'ԽԱՓԱՆՈՒՄ',
    'keeps dust out of a 1–2 µm gap':
        'փոշին հեռու է պահում 1–2 մկմ բացակից,',
    'where one speck is fatal':
        'որտեղ մեկ մասնիկը ճակատագրական է',
    'absorbs gas that leaks in, so the':
        'կլանում է ներս թափանցող գազը, ուստի',
    'damping stays as designed':
        'դեմպֆերումը մնում է նախագծայինը',
    'Two of the five put the die under stress before you ever power it up. That stress is the “after soldering” in the conditions column.':
        'Հինգից երկուսը բյուրեղը լարման տակ են դնում դեռ սնումը միացնելուց առաջ։ Հենց այդ լարվածությունն է պայմանների սյունակի «զոդումից հետո»-ն։',
    'Nothing on this slide is optional, and nothing on it is specified for your board.':
        'Այս սլայդում ոչինչ ըստ ցանկության չէ, և ոչինչ բնութագրված չէ ձեր տպասալի համար։',
    'Two tens of a milli-g, and they are not the same ten':
        'Երկու տասնյակ միլի-g, և դրանք նույն տասը չեն',
    'Name this collision out loud — it is a guaranteed exam misconception otherwise':
        'Անվանեք այս զուգադիպությունը բարձրաձայն — այլապես այն երաշխավորված քննական շփոթ է',
    "Lecture 2's 10 mg":
        '2-րդ դասախոսության 10 mg-ը',
    "Lecture 4's 10 mg":
        '4-րդ դասախոսության 10 mg-ը',
    'What it is':
        'Ի՞նչ է դա',
    'offset DRIFT over temperature':
        'զրոյական շեղման ԴՐԵՅՖ ջերմաստիճանով',
    'zero-g OFFSET after soldering':
        'զրոյական g-ի ՇԵՂՈՒՄ զոդումից հետո',
    'Where it comes from':
        'Որտեղի՞ց է գալիս',
    'the temperature coefficient of the structure':
        'կառուցվածքի ջերմաստիճանային գործակիցը',
    'die attach, package and solder stress':
        'բյուրեղի ամրացման, պատյանի և զոդման լարվածությունը',
    'The arithmetic':
        'Հաշվարկը',
    '±10 mg typ, ±65 mg max':
        '±10 mg typ., ±65 mg max.',
    'Against the 8.73 mg signal':
        '8.73 mg ազդանշանի դիմաց',
    '1.15× typ,  7.45× max':
        '1.15× typ.,  7.45× max.',
    'Can you fix it?':
        'Կարո՞ղ եք ուղղել',
    'NO — it moves after you calibrate':
        'ՈՉ — շարժվում է չափաբերումից հետո',
    'YES — one-point calibration on your board':
        'ԱՅՈ — մեկ կետով չափաբերում ձեր տպասալի վրա',
    'Cost of the fix':
        'Ուղղման արժեքը',
    'one measurement, once, per unit':
        'մեկ չափում, մեկ անգամ, յուրաքանչյուր սարքի համար',
    'Fabrication and packaging hand you a LARGE but REMOVABLE error. The temperature coefficient hands you a SMALL-LOOKING but IRREMOVABLE one.':
        'Արտադրությունը և պատյանավորումը ձեզ տալիս են ՄԵԾ, բայց ՈՒՂՂԵԼԻ սխալ։ Ջերմաստիճանային գործակիցը տալիս է ՓՈՔՐ ԹՎԱՑՅԱԼ, բայց ԱՆՈՒՂՂԵԼԻ սխալ։',
    'That both land on ten is a coincidence. The DIFFERENCE between them is the thesis of Module A.':
        'Այն, որ երկուսն էլ ընկնում են տասի վրա, զուգադիպություն է։ Դրանց միջև ՏԱՐԲԵՐՈՒԹՅՈՒՆՆ է Մոդուլ Ա-ի հիմնական դրույթը։',
    'POLL 4':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 4',
    'You are specifying a pressure sensor for the capstone project. Four numbers matter. Which one must you measure on your own assembly, because no datasheet can give it to you?':
        'Ամփոփիչ նախագծի համար ընտրում եք ճնշման տվիչ։ Կարևոր են չորս թիվ։ Դրանցից ո՞րը պետք է չափեք ձեր սեփական հավաքման վրա, քանի որ ոչ մի տվյալների թերթիկ չի կարող տալ այն ձեզ',
    'the noise density at your chosen bandwidth':
        'աղմուկի սպեկտրային խտությունը ձեր ընտրած թողունակությունում',
    'the sensitivity at 25 °C':
        'զգայունությունը 25 °C-ում',
    'the zero-offset shift caused by your enclosure clamping the sensor':
        'զրոյական շեղման փոփոխությունը, որն առաջացնում է տվիչը սեղմող ձեր պատյանը',
    'the total error band over the operating temperature range':
        'սխալի ընդհանուր գոտին աշխատանքային ջերմաստիճանային տիրույթում',
    'Transfer question. Different measurand, same distinction you have been building for the last two chunks.':
        'Փոխանցման հարց։ Այլ չափվող մեծություն, նույն տարբերակումը, որը կառուցում էիք վերջին երկու բաժնում։',
    'POLL 4   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 4   ·   ՊԱՏԱՍԽԱՆ',
    'A, B and D are all in the datasheet — D is the very figure Lecture 2 taught you to prefer. C depends on your enclosure, your screw torque and your gasket, and it exists nowhere but on your own bench.':
        'A-ն, B-ն և D-ն բոլորն էլ առկա են տվյալների թերթիկում, իսկ D-ն հենց այն ցուցանիշն է, որին նախապատվություն տալ սովորեցրեց 2-րդ դասախոսությունը։ C-ն կախված է ձեր պատյանից, պտուտակի ձգման մոմենտից և միջադիրից, և գոյություն ունի միայն ձեր սեփական լաբորատոր սեղանին։',
    'The stress chain':
        'Լարվածության շղթան',
    'Seven links, and only the first is specified by anyone':
        'Յոթ օղակ, և միայն առաջինն է որևէ մեկի կողմից բնութագրված',
    'THE CHAIN':
        'ՇՂԹԱՆ',
    'WHAT IT CONTRIBUTES':
        'ԻՆՉ Է ՆԵՐՄՈՒԾՈՒՄ',
    'SPECIFIED BY ANYONE?':
        'ԲՆՈՒԹԱԳՐՎԱ՞Ծ Է',
    'DIE':
        'ԲՅՈՒՐԵՂ',
    'the transduction itself':
        'փոխակերպումն ինքը',
    'yes — the datasheet':
        'այո — տվյալների թերթիկը',
    'DIE ATTACH ADHESIVE':
        'ԲՅՈՒՐԵՂԻ ԱՄՐԱՑՄԱՆ ՍՈՍԻՆՁ',
    'offset shift, hysteresis':
        'զրոյական շեղման փոփոխություն, հիստերեզիս',
    'partly — “after soldering”':
        'մասամբ — «զոդումից հետո»',
    'PACKAGE BODY':
        'ՊԱՏՅԱՆԻ ԻՐԱՆ',
    'the temperature coefficient':
        'ջերմաստիճանային գործակիցը',
    'partly':
        'մասամբ',
    'SOLDER JOINTS':
        'ԶՈԴԱԿՆԵՐ',
    'asymmetric stress → cross-axis error':
        'անհամաչափ լարվածություն → միջառանցքային սխալ',
    'NO':
        'ՈՉ',
    'PCB FLEX':
        'ՏՊԱՍԱԼԻ ԾՌՈՒՄ',
    'offset and cross-axis, load-dependent':
        'զրոյական շեղում և միջառանցքային սխալ՝ բեռից կախված',
    'MOUNTING SCREW':
        'ԱՄՐԱՑՄԱՆ ՊՏՈՒՏԱԿ',
    'offset that changes when it is retightened':
        'զրոյական շեղում, որը փոխվում է կրկին ձգելիս',
    '5 mm RUBBER PAD':
        '5 մմ ՌԵՏԻՆԵ ՄԻՋԱԴԻՐ',
    "Lecture 1's war story, in one part":
        '1-ին դասախոսության պատմությունը՝ մեկ դետալում',
    "Lecture 1's story ended on the seventh link. Lecture 4 ends on the same picture.":
        '1-ին դասախոսության պատմությունն ավարտվեց յոթերորդ օղակի վրա։ 4-րդ դասախոսությունն ավարտվում է նույն պատկերով։',
    'POLL 1   ·   ANSWER':
        'ՔՎԵԱՐԿՈՒԹՅՈՒՆ 1   ·   ՊԱՏԱՍԽԱՆ',
    'Not secrecy, and not an application note. The chain you just drew has seven links and the manufacturer owns one of them. The number cannot exist — but the METHOD does: measure it on your own assembly.':
        'Ոչ գաղտնիություն, ոչ էլ կիրառական նշումներ։ Ձեր հենց նոր գծած շղթան ունի յոթ օղակ, և արտադրողին է պատկանում դրանցից մեկը։ Այդ արժեքը գոյություն ունենալ չի կարող, բայց ՄԵԹՈԴԸ՝ այո․ չափեք այն ձեր սեփական հավաքման վրա։',
    'The honest ledger of going small':
        'Փոքրացման ազնիվ հաշվեկշիռը',
    'Built with you — I ask for each row before I show it':
        'Կառուցվում է ձեզ հետ — յուրաքանչյուր տողը հարցնում եմ, մինչ ցույց տալը',
    'Shrinking the device':
        'Սարքի փոքրացումը',
    'buys you':
        'տալիս է',
    'costs you':
        'արժենում է',
    'less mass → a higher noise floor':
        'ավելի քիչ զանգված → ավելի բարձր աղմուկային հատակ',
    'higher bandwidth':
        'ավելի բարձր թողունակություն',
    'resonance moves into your signal band':
        'ռեզոնանսը մտնում է ձեր ազդանշանի շերտ',
    'area / volume ∝ 1/L':
        'մակերես / ծավալ ∝ 1/L',
    'fast thermal response':
        'արագ ջերմային արձագանք',
    'surface forces dominate → stiction':
        'մակերևութային ուժերը գերակշռում են → ստիկցիա',
    'batch fabrication':
        'խմբաքանակային արտադրություն',
    'unit cost, integration with electronics':
        'միավորի արժեք, ինտեգրում էլեկտրոնիկայի հետ',
    'tolerances you cannot control':
        'թույլտվություններ, որոնք չեք վերահսկում',
    'packaging':
        'պատյանավորում',
    'protection, handling':
        'պաշտպանություն, գործածություն',
    'stress you cannot specify':
        'լարվածություն, որը չեք կարող բնութագրել',
    'The datasheet quantifies the middle column. The last two rows of the right-hand column are yours to measure.':
        'Տվյալների թերթիկը քանակապես բնութագրում է միջին սյունակը։ Աջ սյունակի վերջին երկու տողերը ձերն են՝ չափելու։',
    'WHAT THIS LECTURE EXISTS TO EARN':
        'ԻՆՉԻ ՀԱՄԱՐ Է ԳՈՅՈՒԹՅՈՒՆ ՈՒՆԻ ԱՅՍ ԴԱՍԱԽՈՍՈՒԹՅՈՒՆԸ',
    'Micro-scale is a trade,':
        'Միկրոմասշտաբը փոխզիջում է,',
    'not an improvement.':
        'ոչ թե բարելավում։',
    'Everything you gained, you gained by giving something up. The datasheet quantifies the gains — and the last two rows of that ledger are yours to measure, on your own board, with your own screwdriver.':
        'Այն ամենը, ինչ ձեռք բերեցիք, ձեռք բերեցիք որևէ բան զիջելով։ Տվյալների թերթիկը քանակապես բնութագրում է ձեռքբերումները, իսկ այդ հաշվեկշռի վերջին երկու տողերը ձերն են՝ չափելու ձեր սեփական տպասալի վրա, ձեր սեփական պտուտակահանով։',
    'Module A ends here':
        'Մոդուլ Ա-ն ավարտվում է այստեղ',
    'Four lectures. One method. Now watch it get applied seven times.':
        'Չորս դասախոսություն։ Մեկ մեթոդ։ Այժմ հետևեք, թե ինչպես է այն կիրառվում յոթ անգամ։',
    'You can now draw the chain, turn a request into a specification, read a datasheet against a requirement, and explain why a device behaves differently on your own board.':
        'Այժմ կարող եք գծել շղթան, պահանջը վերածել տեխնիկական բնութագրի, տվյալների թերթիկը կարդալ պահանջի դիմաց և բացատրել, թե ինչու է սարքն այլ կերպ իրեն պահում ձեր սեփական տպասալի վրա։',
    'LECTURES 5–11 ARE SEVEN INSTANCES OF ONE PATTERN':
        '5–11 ԴԱՍԱԽՈՍՈՒԹՅՈՒՆՆԵՐԸ ՄԵԿ ՕՐԻՆԱՉԱՓՈՒԹՅԱՆ ՅՈԹ ԴՐՍԵՎՈՐՈՒՄ ԵՆ',
    'MEASURAND':
        'ՉԱՓՎՈՂ ՄԵԾՈՒԹՅՈՒՆ',
    'STRUCTURE':
        'ԿԱՌՈՒՑՎԱԾՔ',
    'SPECIFICATIONS':
        'ՏԵԽՆԻԿԱԿԱՆ ԲՆՈՒԹԱԳՐԵՐ',
    'INTERFACE':
        'ԻՆՏԵՐՖԵՅՍ',
    'CALIBRATION':
        'ՉԱՓԱԲԵՐՈՒՄ',
    'FAILURE MODES':
        'ՁԱԽՈՂՄԱՆ ԵՂԱՆԱԿՆԵՐ',
    'Seven devices, one method. If you can state that pattern, the next seven weeks are one idea applied seven times rather than a list to memorise.':
        'Յոթ սարք, մեկ մեթոդ։ Եթե կարողանում եք ձևակերպել այդ օրինաչափությունը, հաջորդ յոթ շաբաթը մեկ գաղափարի յոթ կիրառում է, ոչ թե անգիր անելու ցանկ։',
    'NEXT:  Lecture 5 — the accelerometer in full: structure 1 and principle 1, down to a register value.':
        'ՀԱՋՈՐԴԸ․  Դասախոսություն 5 — արագաչափն ամբողջությամբ․ 1-ին կառուցվածքը և 1-ին սկզբունքը՝ մինչև ռեգիստրի արժեք։',
    'Two questions · ninety seconds · handed in at the door':
        'Երկու հարց · իննսուն վայրկյան · հանձնվում է դռան մոտ',
    '1  ·  YOUR PROJECT':
        '1  ·  ՁԵՐ ՆԱԽԱԳԻԾԸ',
    'Name one specification of the':
        'Նշեք ձեր ամփոփիչ նախագծի տվիչի',
    'sensor in your capstone project':
        'մեկ տեխնիկական բնութագիր,',
    'that you will have to measure':
        'որը ստիպված կլինեք չափել',
    'yourself — and say which stress':
        'ինքներդ, և ասեք, թե լարվածության',
    'path makes it necessary.':
        'որ ուղին է դա անհրաժեշտ դարձնում։',
    '2  ·  THE PATTERN':
        '2  ·  ՕՐԻՆԱՉԱՓՈՒԹՅՈՒՆԸ',
    'Module A is over.':
        'Մոդուլ Ա-ն ավարտված է։',
    'In one sentence: what is the':
        'Մեկ նախադասությամբ․ ո՞րն է այն',
    'pattern that Lectures 5–11':
        'օրինաչափությունը, որը 5–11',
    'will repeat?':
        'դասախոսությունները կկրկնեն',
    'Question 2 is the one I am grading myself on. If fewer than half of you can state the pattern, Lecture 5 opens with it and I am not behind.':
        '2-րդ հարցի համար ես ինքս ինձ եմ գնահատում։ Եթե ձեզանից կիսից պակասը կարողանա ձևակերպել օրինաչափությունը, 5-րդ դասախոսությունը կսկսվի դրանից, և ես հետ չեմ մնացել։',
    'Reading: reader chapter 4 — structures and fabrication. Its failure section is the mounting-screw story.':
        'Ընթերցանություն․ ուսումնական ձեռնարկի 4-րդ գլուխ — կառուցվածքներ և արտադրություն։ Դրա ձախողման բաժինն ամրացման պտուտակի պատմությունն է։',
}
