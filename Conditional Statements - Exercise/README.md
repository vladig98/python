﻿
# <a name="_hlk532038311"></a>**Упражнение: Условни конструкции**
Задачи за упражнение към курса ["Основи на програмирането" @ СофтУни](https://softuni.bg/courses/programming-basics).

Тествайте решенията си в **judge системата**: <https://judge.softuni.bg/Contests/2414>
1. ## **Сумиране на секунди** 
Трима спортни състезатели финишират за някакъв **брой секунди** (между **1** и **50**). Да се напише програма, която чете времената на състезателите в секунди, въведени от потребителя и пресмята **сумарното им време** във формат "**минути:секунди**". Секундите да се изведат с **водеща нула** (2 à "02", 7 à "07", 35 à "35"). 

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top"><p>35</p><p>45</p><p>44</p></td><td colspan="1" valign="top">2:04</td><td colspan="1" valign="top"><p>22</p><p>7</p><p>34</p></td><td colspan="1" valign="top">1:03</td><td colspan="1" valign="top"><p>50</p><p>50</p><p>49</p></td><td colspan="1" valign="top">2:29</td><td colspan="1" valign="top"><p>14</p><p>12</p><p>10</p></td><td colspan="1" valign="top">0:36</td></tr>
</table>
### **Насоки:**
1. Прочетете входните данни (**секундите на състезателите**):

1. Създайте **нова променлива**, в която да съхраните **сбора от секундите на тримата състезатели**:

1. След като сте намерили **сбора от секундите** трябва да ги **превърнете в минути и секунди** (например, ако сборът е **85 секунди това са 1 минута и 25 секунди, защото 1 минута има 60 секунди**). Създайте **две нови променливи**. В първата изчислете **колко минути е сборът от секунди** като **разделите сбора на 60**. Във втората променлива **изчислете секундите с помощта на деление с остатък (%)**, за да вземете **остатъка при деление с 60**. Например имате общ сбор от 134 секунди (2 минути и 14 секунди) **след целочисленото деление (//) на 60 ще получим 2, а след  делението с остатък (%) ще получим оставащите секунди(14):**

   Закръглете получената стойност за минутите **надолу**, за да премахнете дробната част от стойността.

1. След като вече знаете **колко минути и секунди** е общия сбор, трябва да ги принтирате в правилния формат **(минути : секунди)**. Ако секундите са **по-малко от 10**, печатайте **0 преди числото**

1. ## **Бонус точки**
Дадено е **цяло число** – начален брой точки. Върху него се начисляват **бонус точки** по правилата, описани по-долу. Да се напише програма, която пресмята **бонус точките, които получава числото** и **общия брой точки** (числото + бонуса).

- Ако числото е **до 100** включително, бонус точките са **5**;
- Ако числото е **по-голямо от 100**, бонус точките са **20%** от числото;
- Ако числото е **по-голямо от 1000**, бонус точките са **10%** от числото.

- Допълнителни бонус точки (начисляват се отделно от предходните):
  - За **четно** число à + 1 т.
  - За число, което **завършва на 5** à + 2 т.
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top">20</td><td colspan="1" valign="top"><p>6</p><p>26</p></td><td colspan="1" valign="top">175</td><td colspan="1" valign="top"><p>37\.0</p><p>212\.0</p></td><td colspan="1" valign="top">2703</td><td colspan="1" valign="top"><p>270\.3</p><p>2973\.3</p></td><td colspan="1" valign="top">15875</td><td colspan="1" valign="top"><p>1589\.5</p><p>17464\.5</p></td></tr>
</table>
### **Насоки:**
1. Прочетете входните данни (**числото**):

1. Създайте **нова променлива**, в която ще си изчислите **натрупаните бонус точки**. Задайте й **начална стойност 0**:

1. Направете **if-elif конструкция**, за да проверите големината числото и да изчислите бонуса:

1. Направете **нова if-elif конструкция**, за да **изчислите допълнителния бонус**. Ако числото **е четно към до момента натрупания бонус добавете 1**, а ако **завършва на 5 към бонуса добавете 2**. За да проверите дали едно число **е четно трябва да го разделите на 2 и ако получавате остатък при делението 0**, то значи числото е **четно**, но ако **получите остатък 1**, това означава, че числото е **нечетно**. Например числото 34 е четно, защото 34 / 2 = 17 и остатъкът е 0, а числото 35 е нечетно, защото 35 / 2 = 17 с остатък 1. За да проверите дали едно число завършва на 5 трябва **да разделите числото на 10** и ако **получите остатък при делението 5**, то значи числото завършва на 5. Например числото 245 / 10 = 24 с остатък 5.

1. Принтирайте **на два реда** резултатите. На първия ред **натрупания бонус**, а на втория - **крайното число**, което ще намерите, като **съберете началния брой точки и бонуса**:

1. ## **Време + 15 минути**
<a name="ole_link4"></a>Да се напише програма, която **чете час и минути** от 24-часово денонощие, въведени от потребителя и изчислява колко ще е **часът след 15 минути**. Резултатът да се отпечата във формат **часове:минути**. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с **водеща нула,** когато е необходимо. 
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top"><p>1</p><p>46</p></td><td colspan="1" valign="top">2:01</td><td colspan="1" valign="top"><p>0</p><p>01</p></td><td colspan="1" valign="top">0:16</td><td colspan="1" valign="top"><p>23</p><p>59</p></td><td colspan="1" valign="top">0:14</td><td colspan="1" valign="top"><p>11</p><p>08</p></td><td colspan="1" valign="top">11:23</td><td colspan="1" valign="top"><p>12</p><p>49</p></td><td colspan="1" valign="top">13:04</td></tr>
</table>
# **Примерни изпитни задачи**
1. ## **Магазин за детски играчки**
Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели иска да отиде на екскурзия. 

**Цени на играчките:**

- **Пъзел - 2.60 лв.**
- **Говореща кукла - 3 лв.**
- **Плюшено мече - 4.10 лв.**
- **Миньон - 8.20 лв.**
- **Камионче - 2 лв.**

Ако поръчаните играчки са **50 или повече** магазинът прави **отстъпка 25%** **от общата цена**. От спечелените пари Петя трябва да даде **10% за наема** на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
### **Вход**
От конзолата се четат **6 реда**:

1. **Цена на екскурзията - реално число в интервала [1.00 … 10000.00]**
1. **Брой пъзели - цяло число в интервала [0… 1000]**
1. **Брой говорещи кукли - цяло число в интервала [0 … 1000]**
1. **Брой плюшени мечета - цяло число в интервала [0 … 1000]**
1. **Брой миньони - цяло число в интервала [0 … 1000]**
1. **Брой камиончета - цяло число в интервала [0 … 1000]**
### **Изход**
На конзолата се отпечатва:

- Ако **парите са достатъчни** се отпечатва:
  - **"Yes! {оставащите пари} lv left."**
- Ако **парите НЕ са достатъчни** се отпечатва:
  - **"Not enough money! {недостигащите пари} lv needed."**

**Резултатът трябва да се форматира до втория знак след десетичната запетая**.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|<p>40\.8</p><p>20</p><p>25</p><p>30</p><p>50</p><p>10</p>|Yes! 418.20 lv left.|<p>**Сума**: 20 \* 2.60 + 25 \* 3 + 30 \* 4.10 + 50 \* 8.20 + 10 \* 2 = **680** лв.</p><p>**Брой на играчките**: 20 + 25 + 30 + 50 + 10 = **135**</p><p>**135 > 50 => 25% отстъпка**; 25% от 680 = **170 лв. отстъпка**</p><p>**Крайна цена**: 680 – 170 = **510** лв.</p><p>**Наем**: 10% от 510 лв. = **51** лв.</p><p>**Печалба**: 510 – 51 = **459** лв. </p><p>**459 > 40.8** =>** 459 – 40.8** = **418.20** лв. **остават**</p>|
|**Вход**|**Изход**|**Обяснения**|
|<p>320</p><p>8</p><p>2</p><p>5</p><p>5</p><p>1</p>|Not enough money! 238.73 lv needed.|<p>**Сума**: 8 \* 2.60 + 2 \* 3 + 5 \* 4.10 + 5 \* 8.20 + 1 \* 2 = **90.3** лв.</p><p>**Брой на играчките**: 8 + 2 + 5 + 5 + 1 = **21**</p><p>**21 < 50 => няма отстъпка** </p><p>**Наем**: 10% от 90.3 = **9.03** лв.</p><p>**Печалба**: 90.3 – 9.03 = **81.27** лв.</p><p>**81.27 < 320** => 320 – 81.27** = **238.73** лв. **не достигат**</p>|

1. ## **Годзила срещу Конг**
Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да **напишете програма**, която да изчисли, **дали предвидените средства са достатъчни** за снимането на филма. За снимките  ще бъдат нужни **определен брой статисти, облекло** за всеки един статист и **декор.**

Известно е, че:

- Декорът за филма е **на стойност 10% от бюджета.** 
- При **повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.**
### **Вход**
От конзолата се четат **3 реда**:

1. **Бюджет за филма – реално число в интервала [1.00 … 1000000.00]**
1. **Брой на статистите – цяло число в интервала [1 … 500]**
1. **Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]**
### **Изход**
На конзолата трябва да се отпечатат **два реда**:

- <a name="ole_link5"></a><a name="ole_link6"></a>Ако  парите за декора и дрехите **са повече от бюджета**:
  - <a name="ole_link7"></a>"**Not enough money!"**
  - **"Wingard needs {парите недостигащи за филма} leva more."**
- Ако парите за декора и дрехите са **по малко или равни на бюджета**:
  - **"Action!"** 
  - "**Wingard starts filming with {останалите пари} leva left."**

Резултатът трябва да е **форматиран до втория знак** след десетичната запетая.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|<p>20000 </p><p>120</p><p>55\.5</p><p></p>|<p>Action!</p><p>Wingard starts filming with 11340.00 leva left.</p><p></p>|<p>Сума за декор: 10% от 20000 = 2000 лв.</p><p>Сума за облекло: 120 \* 55.5 = 6660 лв.</p><p>Обща сума за филма: 2000 + 6660 = 8660 лв.</p><p>20000 – 8660 = 11340 лева остават.</p>|
|<p>15437\.62</p><p>186</p><p>57\.99</p>|<p>Action!</p><p>Wingard starts filming with 4186.33 leva left.</p>|<p>Сума за декор: 10% от 15437.62 = 1543.762 лв.</p><p>Сума за облекло: 186 \* 57.99 = 10786.14 лв.</p><p>Статистите са повече от 150 следователно има 10% отстъпка на облеклото.</p><p>10% от 10786.14 е 1078.614</p><p>10786\.14 – 1078.614 = 9707.526 лв. за облекло</p><p>Обща сума за филма: 1543.762 + 9707.526 = 11251.288</p><p>15437\.62 – 11251.288 = 4186.331 лева остават</p>|
|<p>9587\.88</p><p>222</p><p>55\.68</p>|<p>Not enough money!</p><p>Wingard needs 2495.77 leva more.</p>|<p>Сума за декор: 10% от 9587.88 = 958.788 лв.</p><p>Сума за облекло: 11124.864 лв.</p><p>Обща сума за филма: 958.788 + 11124.864 = 12083.652</p><p>9587\.88 – 12083.652 = 2495.77 лева не достигат</p>|
1. ## **Световен рекорд по плуване**
Иван решава да подобри Световния рекорд по плуване на дълги разстояния. **На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,  разстоянието в метри, което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.** Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид, че: **съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.** Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата, **резултатът трябва да се закръгли надолу до най-близкото цяло число.**

**Да се изчисли времето в секунди, за което Иван** **ще преплува разстоянието и разликата спрямо Световния рекорд.** 
### **Вход**
От конзолата се четат **3 реда**:

1. **Рекордът в секунди – реално число;**
1. **Разстоянието в метри – реално число;**
1. **Времето в секунди, за което плува разстояние от 1 м.** **- реално число.**
### **Изход**
Отпечатването на конзолата зависи от резултата:

- Ако **Иван е подобрил Световния рекорд (времето му е по-малко от рекорда)** отпечатваме:
  - **"** **Yes, he succeeded! The new world record is {времето на Иван} seconds."**
- Ако **НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда)** отпечатваме:
  - **"No, he failed! He was {недостигащите секунди} seconds slower."**

**Резултатът трябва да се форматира до втория знак след десетичната запетая**.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|<p>10464</p><p>1500</p><p>20</p>|No, he failed! He was 20786.00 seconds slower.|<p>**Иван трябва да преплува 1500 м.:  1500 \* 20 = 30000 сек.**</p><p>**На всеки 15 м. към времето му се добавят 12.5 сек.:** </p><p>**1500 / 15 = 100 \* 12.5 = 1250 сек.**</p><p>**Общо време: 30000 + 1250 = 31250 сек.**</p><p>**10464 < 31250**</p><p>**Времето, което не му е стигнало за да подобри рекорда:** </p><p>**31250 – 10464 = 20786 сек.**</p>|
|**Вход**|**Изход**|**Обяснения** |
|<p>55555\.67</p><p>3017</p><p>5\.03</p>|Yes, he succeeded! The new world record is 17688.01 seconds.|<p>**Иван трябва да преплува 3017 м.: 3017 \* 5.03 = 15175.51 сек.**</p><p>**На всеки 15 м. към времето му се добавят 12.5 сек.:** </p><p>**3017/ 15 = 201 \* 12.5 = 2512.50 сек.**</p><p>**Общо време: 15175.51 + 2512.50 = 17688.01 сек.**</p><p>**Рекордът е подобрен: 55555.67 > 17688.01**</p>|
## **7. Пазаруване** 
Петър иска да купи **N** видеокарти, **M** процесора и **P** на брой рам памет. Ако броя на видеокартите е **по-голям** от този на процесорите получава **15% отстъпка** от крайната сметка. Важат следните цени:

- Видеокарта – **250 лв./бр**.
- Процесор – **35% от цената на закупените видеокарти/бр**.
- Рам памет – **10% от цената на закупените видеокарти/бр**.

Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
### **Вход**
Входът се състои от четири реда:

1. Бюджетът на Петър - **реално** число в интервала **[1.0…100000.0]**
1. Броят видеокарти - **цяло** число в интервала **[1…100]**
1. Броят процесори - **цяло** число в интервала **[1…100]**
1. Броят рам памет - **цяло** число в интервала **[1…100]**
### **Изход**
На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:

- Ако бюджета е достатъчен:

  "**You have {остатъчен бюджет} leva left!**"

- Ако сумата надхвърля бюджета:

  "**Not enough money! You need {нужна сума} leva more!**"

Резултатът да се форматира до втория знак след десетичната запетая.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :-: | :-: | :-: |
|<p>900</p><p>2</p><p>1</p><p>3</p>|You have 198.75 leva left!|<p>Бюджет: 900 лв</p><p>Сума за видеокарти: 2 \* 250 = 500 лв.</p><p></p><p>Цената за процесор: 35% от 500 = 175 лв. </p><p>Сума за процесори: 1 \* 175 = 175 лв.</p><p></p><p>Цената за рам памет: 10% от 500 = 50 лв.</p><p>Сума за рам памет: 3 \* 50 = 150 лв. </p><p></p><p>Обща сума: 500 + 175 + 150 = 825 лв.</p><p>Броя на видеокартите е по-голям от броя на процесорите, затова той получава 15% отстъпка от крайната цена: 825 – 15% = 701.25 лв.</p><p>701\.25 <= 900 </p><p>=> парите са му достатъчни </p><p>=> остават 900 – 701.25 = 198.75 лв.</p>|
|<p>920\.45</p><p>3</p><p>1</p><p>1</p>|Not enough money! You need 3.92 leva more!|<p>Бюджет: 920.45 лв</p><p>Сума за видеокарти: 3 \* 250 = 750 лв.</p><p></p><p>Цената за процесор: 35% от 750 = 262.50 лв. </p><p>Сума за процесори: 1 \* 262.50  = 262.50  лв.</p><p></p><p>Цената за рам памет: 10% от 750 = 75 лв.</p><p>Сума за рам памет: 1 \* 75 = 75 лв. </p><p></p><p>Обща сума: 750 + 262.50 + 75 = 1087.50 лв.</p><p>Броя на видеокартите е по-голям от броя на процесорите, затова той получава 15% отстъпка от крайната цена: 1087.50 – 15% = 924.37 лв.</p><p>924\.37 > 920.45</p><p>=> парите не са му достатъчни </p><p>=> нужни са 924.375  –  920.45 = 3.92 лв.</p>|
## **8. Обедна почивка**
По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма, с която ще разберете дали **имате достатъчно време** да изгледате епизода. По време на почивката отделяте **време за обяд** и **време за отдих**. **Времето за обяд** ще бъде **1/8 от времето за почивка**, а **времето за отдих** ще бъде **1/4 от времето за почивка**. 
### **Вход**
От конзолата се четат **3 реда**:

1. **Име на сериал** – **текст**
1. **Продължителност на епизод**  – **цяло число** в диапазона **[10… 90]**
1. **Продължителност на почивката**  – **цяло число** в диапазона **[10… 120]**
### **Изход**
На конзолата да се изпише един ред:

- Ако **времето е достатъчно** да изгледате епизода: 

  "**You have enough time to watch {име на сериал} and left with {останало време} minutes free time.**"

- Ако **времето** **не Ви е достатъчно**:

  "**You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes.**"

**Времето в двете изходни съобщения да се закръгли до най-близкото цяло число нагоре.**
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :-: | :-: | :-: |
|<p>Game of Thrones</p><p>60</p><p>96</p><p></p>|You have enough time to watch Game of Thrones and left with 0 minutes free time.|<p>Време за обяд : 96 \* 1/8 = 12.0</p><p>Време за отдих : 96 \* 1/4 = 24.0</p><p>Останало време : 96 - 12 - 24 = 60</p><p>Останалото време е по-голямо или равно на продължителността на епизода, следователно печатаме подходящия изход.</p>|
|<p>Teen Wolf</p><p>48</p><p>60</p>|You don't have enough time to watch Teen Wolf, you need 11 more minutes.|<p>Време за обяд : 60 \* 1/8 = 7.5</p><p>Време за отдих : 60 \* 1/4 = 15.0</p><p>Останало време : 60 – 7.5 - 15 = 37.5 </p><p>Останалото време е по-малко от продължителността на епизода, следователно печатаме подходящия изход.</p>|




