# -*- coding: utf-8 -*-
"""Armenian translations, part 5 — Lecture 2: the arithmetic, the real part, close."""
HY = {
"CHUNK 3  ·  MINUTES 46–70": "ՄԱՍ 3  ·  ՐՈՊԵ 46–70",
"Now compute it": "Այժմ հաշվե՛ք",
"Four terms. One requirement. Twenty minutes.":
    "Չորս բաղադրիչ։ Մեկ պահանջ։ Քսան րոպե։",
"At the end of this you will know which part you should have chosen.":
    "Վերջում կիմանաք, թե որ սարքը պետք էր ընտրեիք։",
"Noise density becomes noise": "Աղմուկի խտությունը դառնում է աղմուկ",
"…once you choose a bandwidth": "…երբ ընտրում եք թողունակությունը",
"noiseRMS  =  noise density  ×  √bandwidth":
    "աղմուկRMS  =  աղմուկի խտություն  ×  √թողունակություն",
"▸  The units tell you the answer.": "▸  Միավորները ցույց են տալիս պատասխանը։",
"µg/√Hz × √Hz = µg. If your units do not cancel, you have used the wrong number.":
    "µg/√Hz × √Hz = µg։ Եթե միավորները չեն կրճատվում, սխալ թիվ եք օգտագործել։",
"▸  Bandwidth, not ODR.": "▸  Թողունակություն, ոչ ODR։",
"The ODR was 200 Hz. Using √200 gives 1.41 mg — a wrong answer that looks right.":
    "ODR-ը 200 Hz էր։ √200-ի օգտագործումը տալիս է 1.41 mg — սխալ պատասխան, որը ճիշտ է "
    "երևում։",
"▸  Halve the bandwidth, gain √2.": "▸  Կիսե՛ք թողունակությունը, շահե՛ք √2։",
"Noise is not a property of the sensor alone. It is a property of the sensor and the "
"bandwidth you chose.":
    "Աղմուկը միայն տվիչի հատկություն չէ։ Այն տվիչի և ձեր ընտրած թողունակության "
    "հատկությունն է։",
"POLL 3   ·   MINUTE 56": "ՀԱՐՑՈՒՄ 3   ·   ՐՈՊԵ 56",
"Noise density 100 µg/√Hz. You configure ODR = 200 Hz and measurement bandwidth = "
"50 Hz. What RMS noise appears in your readings?":
    "Աղմուկի խտությունը 100 µg/√Hz։ Կարգավորում եք ODR = 200 Hz և չափման "
    "թողունակություն = 50 Hz։ Ի՞նչ RMS աղմուկ կհայտնվի ձեր ցուցմունքներում",
"Every wrong answer here is a specific arithmetic mistake — so this is the most useful "
"vote of the day. Take it seriously.":
    "Այստեղ ամեն սխալ պատասխան կոնկրետ թվաբանական սխալ է — ուստի սա օրվա ամենաօգտակար "
    "քվեարկությունն է։ Լուրջ վերաբերվե՛ք։",
"POLL 3   ·   MINUTE 56   ·   ANSWER": "ՀԱՐՑՈՒՄ 3   ·   ՐՈՊԵ 56   ·   ՊԱՏԱՍԽԱՆ",
"100 µg/√Hz × √50 Hz = 707 µg = 0.71 mg.  Now compare that with the 8.73 mg we are "
"trying to measure — and ask whether noise was ever the problem.":
    "100 µg/√Hz × √50 Hz = 707 µg = 0.71 mg։  Այժմ համեմատե՛ք այն 8.73 mg-ի հետ, որը "
    "փորձում ենք չափել — և հարցե՛ք՝ արդյոք աղմուկը երբևէ խնդի՞ր էր։",
"Three more terms, and one of them is not small":
    "ԵՒս երեք բաղադրիչ, և դրանցից մեկը փոքր չէ",
"LSB / √12": "LSB / √12",
"Both utterly negligible against 8.73 mg.":
    "Երկուսն էլ բոլորովին անտեսելի են 8.73 mg-ի դիմաց։",
"OFFSET": "ԶՐՈՅԱԿԱՆ ՇԵՂՈՒՄ",
"calibrated out": "ստուգաչափմամբ հեռացվում է",
"A single bench calibration removes this — at one temperature.":
    "Մեկ լաբորատոր ստուգաչափումը հեռացնում է սա — մեկ ջերմաստիճանում։",
"OFFSET DRIFT": "ԶՐՈՅԱԿԱՆ ՇԵՂՄԱՆ ԴՐԵՅՖ",
"TC × ΔT": "ՋԳ × ΔT",
"Calibrated at 20 °C, used 0–40 °C, so ΔT = ±20 °C.":
    "Ստուգաչափված 20 °C-ում, օգտագործվում է 0–40 °C, ուստի ΔT = ±20 °C։",
"Part A drifts by 10 mg. The entire quantity we are trying to measure is 8.73 mg.":
    "Սարք Ա-ի շեղումը 10 mg է։ Ամբողջ մեծությունը, որը փորձում ենք չափել, 8.73 mg է։",
"The error budget": "Սխալանքի հաշվեկազմը",
"Root-sum-square, because the terms are independent":
    "Քառակուսիների գումարի արմատ, քանի որ բաղադրիչները անկախ են",
"Term": "Բաղադրիչ",
"Part A": "Սարք Ա",
"Where it came from": "Որտեղից է եկել",
"Noise  (100 µg/√Hz × √50 Hz)": "Աղմուկ  (100 µg/√Hz × √50 Hz)",
"datasheet × your bandwidth": "datasheet × ձեր թողունակությունը",
"Quantisation  (LSB/√12)": "Քվանտացում  (LSB/√12)",
"resolution and full scale": "լուծունակություն և լրիվ տիրույթ",
"Offset drift  (TC × ΔT)": "Զրոյական շեղման դրեյֆ  (ՋԳ × ΔT)",
"temp. coefficient × 20 °C": "ջերմ. գործակից × 20 °C",
"TOTAL  (RSS)": "ԸՆԴԱՄԵՆԸ  (RSS)",
"√(sum of squares)": "√(քառակուսիների գումար)",
"AS A TILT ANGLE": "ՈՐՊԵՍ ԹԵՔՈՒԹՅԱՆ ԱՆԿՅՈՒՆ",
"asin(mg / 1000)": "asin(mg / 1000)",
"AGAINST ±0.5°": "±0.5°-Ի ԴԻՄԱՑ",
"FAILS": "ՉԻ ԲԱՎԱՐԱՐՈՒՄ",
"passes, 4× margin": "բավարարում է, 4× պաշար",
"the requirement": "պահանջը",
"All values in mg unless stated. Bandwidth 50 Hz, calibrated at 20 °C, used over "
"0–40 °C.":
    "Բոլոր արժեքները mg-ով, եթե այլ բան նշված չէ։ Թողունակություն 50 Hz, ստուգաչափված "
    "20 °C-ում, օգտագործվում է 0–40 °C։",
"One term dominates. It was on page nine, and it was not on either front page.":
    "Մեկ բաղադրիչ գերիշխում է։ Այն իններորդ էջում էր, և ոչ մի առաջին էջում չկար։",

# ── the real part ────────────────────────────────────────────────────────────
"Now the part on your bench": "Այժմ՝ ձեր լաբորատորիայի սարքը",
"ISM330DHCX · the same budget, run twice from its own datasheet":
    "ISM330DHCX · նույն հաշվեկազմը, երկու անգամ՝ իր datasheet-ից",
"using TYP": "ըստ TYP",
"using MAX": "ըստ MAX",
"from DS13012 Rev 6": "DS13012 Rev 6-ից",
"both printed, same row": "երկուսն էլ տպված, նույն տողում",
"Noise, × √50 Hz": "Աղմուկ, × √50 Hz",
"your bandwidth": "ձեր թողունակությունը",
"Quantisation, LSB/√12": "Քվանտացում, LSB/√12",
"16-bit, ±2 g": "16-բիթ, ±2 g",
"Offset drift TC": "Զրոյական շեղման ՋԳ",
"Drift, × 20 °C": "Շեղում, × 20 °C",
"0–40 °C, cal at 20 °C": "0–40 °C, ստուգաչափ. 20 °C-ում",
"TOTAL (RSS)": "ԸՆԴԱՄԵՆԸ (RSS)",
"asin(mg/1000)": "asin(mg/1000)",
"One part number. One datasheet. Two columns — and the requirement sits between them.":
    "Մեկ սարքի կոդ։ Մեկ datasheet։ Երկու սյունակ — և պահանջը գտնվում է նրանց միջև։",
"POLL 1   ·   MINUTE 70   ·   ANSWER": "ՀԱՐՑՈՒՄ 1   ·   ՐՈՊԵ 70   ·   ՊԱՏԱՍԽԱՆ",
"The right FIRST answer was C — you did not have enough information. The right SECOND "
"answer, after twelve minutes of arithmetic, is B.":
    "ՃԻՇՏ ԱՌԱՋԻՆ պատասխանը Գ-ն էր — բավարար տեղեկույթ չունեիք։ Ճիշտ ԵՐԿՐՈՐԴ պատասխանը, "
    "տասներկու րոպե թվաբանությունից հետո, Բ-ն է։",
"Part A resolves eight times finer": "Սարք Ա-ն ութ անգամ ավելի բարձր",
"than Part B — and cannot do the job.": "լուծունակություն ունի — և չի կատարում խնդիրը։",
"Part B resolves 0.028° of tilt: eighteen times finer than the ±0.5° we need. "
"Resolution was never the deciding variable. It only looked like it was, because it was "
"the number on the front page.":
    "Սարք Բ-ն տարբերակում է 0.028° թեքություն. տասնութ անգամ ավելի մանր, քան պահանջվող "
    "±0.5°-ը։ Լուծունակությունը երբեք որոշիչ մեծություն չէր։ Այն միայն այդպես երևաց, "
    "որովհետև առաջին էջի թիվն էր։",

# ── decision table ───────────────────────────────────────────────────────────
"Your turn: three candidates": "Ձեր հերթն է. երեք թեկնածու",
"Teams of three · 8 minutes · commit to one":
    "Երեքական խմբեր · 8 րոպե · ընտրե՛ք մեկը",
"Criterion": "Չափանիշ",
"Weight": "Կշիռ",
"Meets ±0.5° over 0–40 °C": "Բավարարում է ±0.5° 0–40 °C-ում",
"pass/fail": "այո/ոչ",
"fail": "ոչ",
"pass": "այո",
"Total error as an angle": "Ընդհանուր սխալանքը որպես անկյուն",
"high": "բարձր",
"Unit price at 500 off": "Միավորի գինը 500 հատի դեպքում",
"medium": "միջին",
"Current draw": "Հոսանքի սպառում",
"Library already exists": "Գրադարանն արդեն գոյություն ունի",
"LOW": "ՑԱԾՐ",
"yes": "այո",
"no": "ոչ",
"PART C": "ՍԱՐՔ Գ",
"offset ±5 mg": "զր. շեղում ±5 mg",
"TC ±0.05 mg/°C": "ՋԳ ±0.05 mg/°C",
"€11.50, 0.9 mA": "€11.50, 0.9 mA",
"Write one sentence:   “We specify Part ___ because ___”   — naming the DOMINANT ERROR "
"TERM, not the headline.":
    "Գրե՛ք մեկ նախադասություն.   «Մենք ընտրում ենք Սարք ___, որովհետև ___»   — նշելով "
    "ԳԵՐԻՇԽՈՂ ՍԽԱԼԱՆՔԻ ԲԱՂԱԴՐԻՉԸ, ոչ վերնագիրը։",
"Part C is the trap in the other direction: technically the best part, six times the "
"price, and it buys no capability the requirement asks for. Over-specifying is also an "
"engineering failure.":
    "Սարք Գ-ն թակարդ է հակառակ ուղղությամբ. տեխնիկապես լավագույն սարքը, վեց անգամ ավելի "
    "թանկ, և ոչ մի հատկություն չի ավելացնում, որ պահանջն ուզում է։ Ավելորդ բնութագրումը "
    "նույնպես ինժեներական ձախողում է։",

# ── poll 4 transfer ──────────────────────────────────────────────────────────
"POLL 4   ·   MINUTE 72": "ՀԱՐՑՈՒՄ 4   ·   ՐՈՊԵ 72",
"New problem. Water level in an outdoor tank, 2 m deep (≈20 kPa full scale), to ±20 mm, "
"water 5–35 °C.  P: total error band ±0.25 % FS over 0–50 °C.  Q: ±0.05 % FS at 25 °C, "
"temperature coefficient not specified.":
    "Նոր խնդիր։ Ջրի մակարդակը բացօթյա բաքում, 2 մ խորություն (≈20 kPa լրիվ տիրույթ), "
    "±20 մմ ճշտությամբ, ջուրը 5–35 °C։  P. ընդհանուր սխալանքի շերտ ±0.25 % FS 0–50 °C-ում։  "
    "Q. ±0.05 % FS 25 °C-ում, ջերմաստիճանային գործակիցը նշված չէ։",
"Sensor Q — five times better accuracy": "Տվիչ Q — հինգ անգամ ավելի լավ ճշտություն",
"Sensor P — its error is bounded over the whole temperature range; Q's is specified at "
"one point only":
    "Տվիչ P — նրա սխալանքը սահմանափակված է ամբողջ ջերմաստիճանային տիրույթում. Q-ինը "
    "նշված է միայն մեկ կետում",
"Either — the temperature coefficient can be measured later":
    "Ցանկացածը — ջերմաստիճանային գործակիցը կարելի է չափել հետո",
"Sensor Q, calibrated at 25 °C before installation":
    "Տվիչ Q, ստուգաչափված 25 °C-ում մինչ տեղադրումը",
"Different measurand, different error term. Same question underneath.":
    "Այլ չափվող մեծություն, այլ սխալանքի բաղադրիչ։ Ներքևում՝ նույն հարցը։",
"POLL 4   ·   MINUTE 72   ·   ANSWER": "ՀԱՐՑՈՒՄ 4   ·   ՐՈՊԵ 72   ·   ՊԱՏԱՍԽԱՆ",
"A total error band over the operating range beats a headline accuracy at one "
"temperature. An unspecified coefficient is not a small error — it is an unbounded one.":
    "Աշխատանքային տիրույթում ընդհանուր սխալանքի շերտը գերազանցում է մեկ ջերմաստիճանում "
    "նշված վերնագրային ճշտությունը։ Չնշված գործակիցը փոքր սխալանք չէ — այն "
    "անսահմանափա՛կ է։",

# ── selection rule and summary ───────────────────────────────────────────────
"The course's selection rule": "Դասընթացի ընտրության կանոնը",
"Quoted from your own semester plan": "Մեջբերում ձեր սեփական կիսամյակային պլանից",
"“Avoid selecting a part only because an Arduino library exists;":
    "«Խուսափե՛ք սարք ընտրելուց միայն այն պատճառով, որ Arduino գրադարան կա.",
"students must still see the underlying configuration and data path.”":
    "ուսանողները պետք է տեսնեն հիմքում ընկած կարգավորումն ու տվյալների ուղին»։",
"Part A had a library. Part A cannot do the job.":
    "Սարք Ա-ն գրադարան ուներ։ Սարք Ա-ն չի կատարում խնդիրը։",
"What to choose on instead — parts that expose the engineering:":
    "Ինչի հիման վրա ընտրել՝ սարքեր, որոնք բացահայտում են ինժեներությունը.",
"selectable range and ODR": "ընտրելի տիրույթ և ODR",
"documented bandwidth and noise": "փաստաթղթավորված թողունակություն և աղմուկ",
"self-test": "ինքնաստուգում",
"data-ready interrupt": "տվյալի պատրաստության ընդհատում",
"FIFO where relevant": "FIFO, որտեղ տեղին է",
"an accessible register map": "հասանելի ռեգիստրների քարտեզ",
"a complete datasheet": "ամբողջական datasheet",
"Turn the requirement into a number before you read any datasheet.":
    "Պահանջը վերածե՛ք թվի, մինչ որևէ datasheet կարդալը։",
"0.5° became 8.73 mg, and 8.73 mg decided everything that followed.":
    "0.5°-ը դարձավ 8.73 mg, և 8.73 mg-ը որոշեց հետագա ամեն ինչ։",
"Find the dominant term. Everything else is decoration.":
    "Գտե՛ք գերիշխող բաղադրիչը։ Մնացած ամեն ինչ զարդարանք է։",
"10 mg and 0.7 mg combine to 10.02 mg. The small term never mattered.":
    "10 mg-ը և 0.7 mg-ը միասին տալիս են 10.02 mg։ Փոքր բաղադրիչը երբեք նշանակություն "
    "չուներ։",
"Resolution is not accuracy, and neither is precision.":
    "Լուծունակությունը ճշտություն չէ, ոչ էլ ճշգրտությունը։",
"Systematic → calibration. Random → bandwidth. Drift → component choice.":
    "Համակարգային → ստուգաչափում։ Պատահական → թողունակություն։ Շեղում → բաղադրիչի ընտրություն։",
"A number without its conditions is not a number.":
    "Թիվը առանց իր պայմանների թիվ չէ։",
"typ at 25 °C is not a guarantee, and an unspecified coefficient is unbounded.":
    "typ 25 °C-ում երաշխիք չէ, իսկ չնշված գործակիցը անսահմանափակ է։",

# ── exit ticket and close ────────────────────────────────────────────────────
"Anonymous · hand it in at the door": "Անանուն · հանձնե՛ք դռան մոտ",
"1  ·  COMPUTE": "1  ·  ՀԱՇՎԵ՛Ք",
"A sensor gives 200 µg/√Hz.": "Տվիչը տալիս է 200 µg/√Hz։",
"You set a 100 Hz bandwidth.": "Դուք սահմանում եք 100 Hz թողունակություն։",
"State the RMS noise.": "Նշե՛ք RMS աղմուկը։",
"2  ·  JUDGEMENT": "2  ·  ԴԱՏՈՂՈՒԹՅՈՒՆ",
"Name the one specification you": "Նշե՛ք այն մեկ բնութագիրը, որը",
"will look for first, for the rest": "առաջինը կփնտրեք ձեր ողջ",
"of your career, before the": "կարիերայի ընթացքում, մինչ",
"headline number.": "վերնագրային թիվը։",
"3  ·  MUDDIEST POINT": "3  ·  ԱՄԵՆԱԱՆՀԱՍԿԱՆԱԼԻ ԿԵՏԸ",
"What is the one thing today": "Ո՞րն է այսօրվա այն մեկ բանը,",
"you are least sure about?": "որում ամենաքիչ վստահ եք",
"One sentence.": "Մեկ նախադասություն։",
"Question 1 is the one I will actually grade myself on. If the room cannot do it, I "
"taught it badly.":
    "1-ին հարցով ես գնահատում եմ ինքս ինձ։ Եթե լսարանը չի կարողանում, նշանակում է վատ եմ "
    "դասավանդել։",
"Tuesday: Laboratory 1": "Երեքշաբթի. Լաբորատորիա 1",
"Datasheet to data — bring the pre-lab sheet, signed":
    "Datasheet-ից տվյալ — բերե՛ք նախալաբորատոր թերթը, ստորագրված",
"You already found number 5 on the hunt: the device-identification register.":
    "Որսի ժամանակ արդեն գտել եք 5-րդը՝ սարքի նույնականացման ռեգիստրը։",
"On Tuesday you read it off real silicon — and prove your sensor is the sensor":
    "Երեքշաբթի կկարդաք այն իրական բյուրեղից — և կապացուցեք, որ ձեր տվիչը",
"you think it is.": "հենց այն տվիչն է։",
"AND THEN LECTURE 3": "ԵՎ ԱՊԱ՝ ԴԱՍԱԽՈՍՈՒԹՅՈՒՆ 3",
"From physical quantity to trustworthy samples — sampling, aliasing,":
    "Ֆիզիկական մեծությունից մինչև վստահելի նմուշներ — նմուշառում, ալիասինգ,",
"quantisation, and the ADC configuration that killed the motor.":
    "քվանտացում, և ԱԹԿ-ի կարգավորումը, որը սպանեց շարժիչը։",
}

# ── stragglers: strings that mix prose with numbers ──────────────────────────
HY.update({
"Bandwidth:  ≥ 4 kHz, anti-aliased.    Sample rate:  ≥ 8 kHz.":
    "Թողունակություն.  ≥ 4 kHz, հակաալիասինգային.    Նմուշառում.  ≥ 8 kHz։",
"tilt of 0.5°  →  sin(0.5°) × 1 g  =  8.73 mg":
    "0.5° թեքում  →  sin(0.5°) × 1 g  =  8.73 mg",
"code 8412": "կոդ 8412",
"A:  ±40 mg  →  0": "Ա.  ±40 mg  →  0",
"B:  ±10 mg  →  0": "Բ.  ±10 mg  →  0",
"A:  0.061/3.46 = 0.018": "Ա.  0.061/3.46 = 0.018",
"B:  0.488/3.46 = 0.141": "Բ.  0.488/3.46 = 0.141",
"A:  0.5 × 20 = 10.0": "Ա.  0.5 × 20 = 10.0",
"B:  0.1 × 20 =  2.0": "Բ.  0.1 × 20 =  2.0",
})
