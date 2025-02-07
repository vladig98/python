﻿
**Първи стъпки в програмирането**

Задачи за упражнение в клас и за домашно към курса ["Основи на програмирането" @ СофтУни](https://softuni.bg/courses/programming-basics).

Тествайте задачите си в Judge системата:

` `<https://judge.softuni.org/Contests/2424/First-Steps-in-Coding-Exercise>
1. ## **Конвертор: от USD към BGN**
Напишете програма за **конвертиране на щатски долари** (USD) **в български лева** (BGN). Използвайте фиксиран **курс** между долар и лев: **1 USD** = **1.79549 BGN**.
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top">22</td><td colspan="1" valign="top">39\.50078 </td><td colspan="1" valign="top">100</td><td colspan="1" valign="top">179\.549</td><td colspan="1" valign="top">12\.5</td><td colspan="1" valign="top">22\.443625</td></tr>
</table>
### **Насоки**
1. Прочетете входните данни от конзолата (**щатските долари**):
1. Създайте **нова променлива**, в която ще направите конвертирането от щатски долари към български лева, като знаете **валутния курс**:
1. <a name="_hlk18574684"></a>Принтирайте получените български лева.

1. ## **Конвертор: от радиани в градуси**
Напишете програма, която чете **ъгъл в [радиани**](https://bg.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B4%D0%B8%D0%B0%D0%BD)** (десетично число) и го преобразува в [**градуси**](https://bg.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_\(%D1%8A%D0%B3%D1%8A%D0%BB\)). Използвайте формулата: **градус = радиан \* 180 / π**. Числото **π** в **Python** може да достъпите чрез модула math. За да ползвате функционалността му, първо трябва да включите констатата pi.

### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"><p></p><p></p></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top">3\.1416</td><td colspan="1" valign="top">180\.0004209182994</td><td colspan="1" valign="top">6\.2832</td><td colspan="1" valign="top">360\.0008418365988</td><td colspan="1" valign="top">0\.7854</td><td colspan="1" valign="top">45\.00010522957485</td></tr>
</table>
### **Насоки**
1. Прочетете входните данни от конзолата (**радианите**).
1. Създайте **нова променлива**, в която ще направите конвертирането от радиани към градуси, като знаете **формулата за изчисление**.
1. Принтирайте получените градуси.

1. ## **Калкулатор депозити**
Напишете програма, която изчислява каква **сума** ще получите в края на **депозитния период** при определен **лихвен процент**. Използвайте следната формула: 

**сума = депозирана сума  + срок на депозита \* ((депозирана сума \* годишен лихвен процент ) / 12)**
### **Вход**
От конзолата се четат **3 реда**:

1. **Депозирана сума – реално число в интервала [100.00 … 10000.00]**
1. **Срок на депозита (в месеци) – цяло число в интервала [1…12]**
1. **Годишен лихвен процент – реално число в интервала [0.00 …100.00]**
### **Изход**
Да се отпечата на конзолата сумата в края на срока.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|<p>**200**</p><p>**3**</p><p>**5.7**</p>|202\.85|<p>1\. Изчисляваме натрупаната лихва: **200** \* 0.057 (**5.7**%) = **11.40** лв.</p><p>2\. Изчисляваме лихвата за 1 месец: **11.40** лв. / **12** месеца = **0.95** лв.</p><p>3\. Общата сума е: **200** лв. + **3** \* **0.95** лв. = 202.85 лв.</p>|
|**Вход**|**Изход**||
|<p>**2350**</p><p>**6**</p><p>**7**</p><p></p>|2432\.25|<p>1\. Изчисляваме натрупаната лихва: **2350** \* 0.07 (**7**%) = **164.50** лв.</p><p>2\. Изчисляваме лихвата за 1 месец: **164.50** лв. / **12** месеца = **13.7083...** лв.</p><p>3\. Общата сума е: **2350** лв. + **6** \* **13.7083...** лв. = 2432.25 лв.</p>|
1. ## **Задължителна литература**
За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. Понеже Жоро предпочита да играе с приятели навън, вашата задача е да му помогнете да изчисли колко **часа на ден** трябва да отделя, за да прочете необходимата литература.
### **Вход**
От конзолата се четат **3 реда**:

1. **Брой страници** в текущата книга **– цяло число в интервала [1…1000]**
1. **Страници,** които прочита за 1 час **– цяло число в интервала [1…1000]**
1. **Броят на дните,** за които трябва да прочете книгата – **цяло число в интервала [1…1000]**
### **Изход**
Да се отпечата на конзолата **броят часове**, които Жоро трябва да отделя за четене всеки ден.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|<p>**212**</p><p>**20**</p><p>**2**</p>|5|<p>Общо време за четене на книгата: **212** страници / **20** страници за час = **10** часа общо</p><p>Необходимите часове на ден: **10** часа / **2** дни = 5 часа на ден</p><p></p>|
|**Вход**|**Изход**||
|<p>**432**</p><p>**15**</p><p>**4**</p>|7|<p>Общо време за четене на книгата: **432** страници / **15** страници за час = **28** часа общо</p><p>Необходимите часове на ден: **28** часа / **4** дни = 7 часа на ден</p><p></p>|

# **Примерни изпитни задачи**
1. ## **Учебни материали**
Учебната година вече е започнала и отговорничката на 10Б клас - Ани трябва да купи определен брой **пакетчета с химикали**, **пакетчета с маркери**, както и **препарат за почистване на дъска**. Тя е редовна клиентка на една книжарница, затова има **намаление** за нея, което представлява **някакъв процент от общата сума**. **Напишете програма, която изчислява колко пари ще трябва да събере Ани, за да плати сметката, като имате предвид следния ценоразпис:** 

- **Пакет химикали - 5.80 лв.** 
- **Пакет маркери - 7.20 лв.** 
- **Препарат - 1.20 лв (за литър)**
### **Вход**
От конзолата се четат **4 числа**:

- **Брой пакети химикали** - **цяло число в интервала [0...100]**
- **Брой пакети маркери** - **цяло число в интервала [0...100]**
- **Литри** **препарат за почистване на дъска** - **цяло число в интервала** **[0…50]**
- **Процент намаление** - **цяло число в интервала [0...100]**
### **Изход**
Да се отпечата на конзолата **колко пари ще са нужни на Ани**, за да си плати сметката.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Коментар**||
| :- | :- | :- | :- |
|<p>**2**</p><p>**3**</p><p>**4**</p><p>**25**</p>|28\.5|<p>**Цена на пакетите химикали** => **2** \* **5.80** = 11.60 лв.</p><p>**Цена на пакетите маркери** => **3** \* **7.20** = 21.60 лв.</p><p>**Цена на препарата** => **4** \* **1.20** = 4.80 лв.</p><p>**Цена за всички материали** => 11.60 + 21.60 + 4.80 = **38.00 лв.**</p><p>**25% = 0.25**</p><p>**Цена с намаление** = **38.00** – (**38.00** \* **0.25**) = 28.50 лв.</p>||
|**Вход**|**Изход**|**Коментар**||
|<p>**4**</p><p>**5**</p><p>**5**</p><p>**10**</p>|58\.68|<p>**Цена на пакетите химикали** => **4** \* **5.80** = 23.20 лв.</p><p>**Цена на пакетите маркери** => **5** \* **7.20** = 36 лв.</p><p>**Цена на препарата** => **5** \* **1.20** = 6.00 лв.</p><p>**Цена за всички материали** => 23.20 + 36 + 6.00 = **65.20 лв.**</p><p>**10% = 0.10**</p><p>**Цена с намаление** = **65.20** – (**65.20** \* **0.10**) = 58.68 лв.</p>||
1. ## **Пребоядисване**
Румен иска да пребоядиса хола и за целта е наел майстори. Напишете **програма,** която **изчислява разходите за ремонта**, предвид следните **цени**:

- **Предпазен найлон - 1.50 лв. за кв. метър**
- **Боя - 14.50 лв. за литър**
- **Разредител за боя - 5.00 лв. за литър**

За всеки случай, към **необходимите** материали, Румен иска да **добави** още **10%** от количеството **боя** и **2 кв.м. найлон**, разбира се и **0.40 лв. за торбички**. Сумата, която се **заплаща на майсторите** за **1 час** работа, е равна на **30%** от сбора на **всички разходи за материали**.
### **Вход**
Входът се чете от **конзолата** и съдържа **точно 4 реда**:

1. **Необходимо количество найлон (в кв.м.)** - **цяло число в интервала [1... 100]**
1. **Необходимо количество боя (в литри)** - **цяло число в интервала [1…100]**
1. **Количество** **разредител (в литри)** - **цяло число в интервала [1…30]**
1. **Часовете**, за които майсторите ще свършат работата - **цяло число в интервала [1…9]**
### **Изход**
Да се **отпечата** на конзолата **един ред**:

- **"{сумата на всички разходи}"**
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|<p>**10**</p><p>**11**</p><p>**4**</p><p>**8**</p>|727\.09|<p>Сума за найлон: (**10** + **2**) \* **1.50** = 18 лв.</p><p>Сума за боя: (**11** + **10%**) \* **14.50** = 175.45 лв.</p><p>Сума за разредител: **4** \* **5.00** = 20.00 лв.</p><p>Сума за торбички: **0.40 лв.**</p><p>Обща сума за материали: 18 + 175.45 + 20.00 + **0.40** = 213.85 лв.</p><p>Сума за майстори: (213.85 \* 30%) \* **8** = 513.24 лв.</p><p>Крайна сума: 213.85 + 513.24 = 727.09 лв.</p>|
|<p>**5**</p><p>**10**</p><p>**10**</p><p>**1**</p>|286\.52|<p>Сума за найлон: (**5** + **2**) \* **1.50** = 10.50 лв.</p><p>Сума за боя: (**10** + **10%**) \* **14.50** = 159.50 лв.</p><p>Сума за разредител: **10** \* **5.00** = 50.00 лв.</p><p>Сума за торбички: **0.40 лв.**</p><p>Обща сума за материали: 10.50 + 159.50 + 50.00 + **0.40** = 220.40 лв.</p><p>Сума за майстори: (220.40 \* 30%) \* **1** = 66.12 лв.</p><p>Крайна сума: 220.40 + 66.12 = 286.52 лв.</p>|

1. ## **Доставка на храна**
Ресторант отваря врати и предлага няколко менюта на преференциални цени: 

- **Пилешко меню –  10.35 лв.** 
- **Меню с риба – 12.40 лв.** 
- **Вегетарианско меню  – 8.15** лв. 

**Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.**

Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката). 

Цената на доставка е **2.50** лв и се начислява най-накрая**.**  
### **Вход**
От конзолата се четат **3 реда**:

- **Брой пилешки менюта – цяло число в интервала [0 … 99]**
- **Брой менюта с риба** **–** **цяло число в интервала [0 … 99]**
- **Брой вегетариански менюта – цяло число в интервала [0 … 99]**
### **Изход**
**Да се отпечата на конзолата един ред:  "{цена на поръчката}"**
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :-: | :-: | :- |
|<p>**2**</p><p>**4**</p><p>**3**</p>|116\.2|<p>**Цена за пилешките менюта: 2 броя \* 10.35  = 20.70**</p><p>**Цена за менютата с риба: 4 броя \* 12.40 = 49.60**</p><p>**Цена за вегетарианските менюта: 3 броя \* 8.15 = 24.45**</p><p>**Обща цена на менютата: 20.70 + 49.60 + 24.45 = 94.75**</p><p>**Цена на десерта: 20% от 94.75 = 18.95**</p><p>**Цена на доставка: 2.50 (по условие)**</p><p>**Обща цена на поръчката: 94.75 + 18.95 + 2.50 = 116.20**</p>|
|**Вход**|**Изход**||
|<p>**9**</p><p>**2**</p><p>**3**</p>|173\.38|<p>**Цена за пилешките менюта: 9 броя \* 10.35  = 93.15**</p><p>**Цена за менютата с риба: 2 броя \* 12.40 = 24.80**</p><p>**Цена за вегетарианските менюта: 3 броя \* 8.15 = 24.45**</p><p>**Обща цена на менютата: 93.15 + 24.80 + 24.45 = 142.40**</p><p>**Цена на десерта: 20% от 142.40 = 28.48**</p><p>**Цена на доставка: 2.50 (по условие)**</p><p>**Обща цена на поръчката: 142.40 + 28.48 + 2.50 = 173.38**</p>|
1. ## **Баскетболно оборудване**
Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка. **Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира, като знаете колко е таксата за тренировки по баскетбол за период от 1 година. Нужна екипировка:** 

- **Баскетболни кецове – цената им е 40% по-малка от таксата за една година**
- **Баскетболен екип – цената му е 20% по-евтина от тази на кецовете**
- **Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип**
- **Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка**
### **Вход**
От конзолата се четe **1 ред**:

- **Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]**
### **Изход**
Да се отпечата на конзолата **колко ще са разходите на Джеси, ако започне да спортува баскетбол.**
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :- | :- | :- |
|**365**|811\.76|<p>**Цена на тренировките за година: 365**</p><p>**Цена на баскетболните кецове: 365 – 40% = 219**</p><p>**Цена на баскетболен екип: 219 – 20% = 175.20**</p><p>**Цена на баскетболна топка: 1 / 4 от 175.20 = 43.80**</p><p>**Цена на баскетболни аксесоари: 1 /  5 от 43.80 = 8.76**</p><p>**Обща цена за екипировката: 365 + 219 + 175.20 + 43.80 + 8.76 = 811.76**</p>|
|**Вход**|**Изход**|**Обяснения**|
|**550**|1223\.2|<p>**Цена на тренировките за година: 550**</p><p>**Цена на баскетболните кецове: 550 – 40% = 330**</p><p>**Цена на баскетболен екип: 330 – 20% = 264**</p><p>**Цена на баскетболна топка: 1 / 4 от 264 = 66**</p><p>**Цена на баскетболни аксесоари: 1 /  5 от 66 = 13.20**</p><p>**Обща цена за екипировката: 550 + 330 + 264 + 66 + 13.20= 1223.2**</p>|

1. ## **Аквариум**
За рождения си ден Любомир получил аквариум с формата на паралелепипед. **Първоначално прочитаме от конзолата на отделни редове размерите му – дължина, широчина и височина в сантиметри.** Трябва да се пресметне колко литра вода ще събира аквариума, ако се знае, че определен процент от вместимостта му е заета от пясък, растения, нагревател и помпа. 

Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм<sup>3</sup>/. 

**Да се напише програма, която изчислява литрите вода, която са необходими за напълването на аквариума.**
### **Вход**
От конзолата се четат **4 реда**:

1. **Дължина в см – цяло число в интервала [10 … 500]**
1. **Широчина в см – цяло число в интервала [10 … 300]**
1. **Височина в см – цяло число в интервала [10… 200]**
1. **Процент**  **– реално число в интервала [0.000 … 100.000]**
### **Изход**
Да се отпечата на конзолата **едно число**:

- **литрите вода, които ще  събира аквариума**.
### **Примерен вход и изход**

|**Вход**|**Изход**|**Обяснения**|
| :-: | :-: | :- |
|<p>**85**</p><p>**75**</p><p>**47**</p><p>**17**</p>|248\.68875|<p>обем на аквариумa: **85** \* **75** \* **47** = **299625** см<sup>3</sup></p><p>обем в литри: **299625** \* 0.001 или  **299625** / 1000 => **299.625** литра</p><p>заето пространство: **17%** = **0.17**</p><p>нужни литри: **299.625** \* (1 - **0.17**) = 248.68875 литра</p>|
|**Вход**|**Изход**|**Обяснения**|
|<p>**105**</p><p>**77**</p><p>**89**</p><p>**18.5**</p>|586\.445475|<p>обем на аквариумa: **105** \* **77** \* **89** = **719565** см<sup>3</sup></p><p>обем в литри: **719565** \* 0.001  или **719565** / 1000 => **719.565** литра</p><p>заето пространство: **18.5%** = **0.185**</p><p>нужни литри: **719.565** \* (1 - **0.185**) = 586.445475 литра</p>|
##

