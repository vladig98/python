
# **Лаб: Условни конструкции**
Задачи за упражнение в клас и за домашно към курса ["Основи на програмирането" @ СофтУни](https://softuni.bg/courses/programming-basics).

Тествайте решенията си в **Judge** системата: <https://judge.softuni.org/Contests/2413/Conditional-Statements-Lab>
1. ## **Отлична оценка**
Първата задача от тази тема е да се напише **конзолна програма**, която **чете оценка** (реално число), въведена от потребителя и отпечатва "**Excellent!",** ако оценката е **5.50** или по-висока.
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1">6</td><td colspan="1">Excellent!</td><td colspan="1">5</td><td colspan="1"><i>(няма изход)</i></td><td colspan="1">5\.50</td><td colspan="1">Excellent!</td><td colspan="1">5\.49</td><td colspan="1"><i>(няма изход)</i></td></tr>
</table>
### **Насоки:**
1. Създайте Python файл с подходящо име, например **excellent\_grade**. Създайте една променлива, в която да запазите **реално** **число** – оценката, което ще прочетете от конзолата:

 

1. Направете проверка за стойността на оценката. Ако тя е по-голяма или равна на 5.50 отпечатайте изхода по условие:

1. Стартирайте програмата с **Ctrl + Shift + F10** и я **тествайте** с различни входни стойности:

|||
| :- | :- |
1. ## **По-голямото число**
Да се напише програма, която чете **две цели числа** въведени от потребителя и отпечатва **по-голямото от двете**. 
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top"><p>5</p><p>3</p></td><td colspan="1" valign="top">5</td><td colspan="1" valign="top"><p>3</p><p>5</p></td><td colspan="1" valign="top">5</td><td colspan="1" valign="top"><p>10</p><p>10</p></td><td colspan="1" valign="top">10</td><td colspan="1" valign="top"><p>-5</p><p>5</p></td><td colspan="1" valign="top">5</td></tr>
</table>
### **Насоки:**
1. Създайте Python файл с подходящо име в проекта
1. Прочетете две цели числа от конзолата:

1. Сравнете, дали първото число **first\_number** e по-голямо от второто **second\_number**. Отпечатайте по-голямото число.

1. ## **Четно или нечетно**
Да се напише програма, която чете **цяло число**, въведено от потребителя, и печата дали е **четно** или **нечетно**. 

Ако е **четно** отпечатайте "**even"**, ако е нечетно "**odd"**.
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1">2</td><td colspan="1">even</td><td colspan="1">3</td><td colspan="1">odd</td><td colspan="1">25</td><td colspan="1">odd</td><td colspan="1">1024</td><td colspan="1">even</td></tr>
</table>
### **Насоки:**
1. Създайте Python файл с подходящо име в съществуващия проект;
1. Прочетете едно цяло число от конзолата:

1. Проверете дали числото е четно, като го разделите модулно на 2 и проверите дали има остатък от делението. Ако няма остатък, отпечатайте изход "**even**". В противен случай отпечатайте "**odd**":

1. ## **Познай паролата**
Да се напише програма, която **чете парола** (текст), въведена от потребителя и проверява дали въведената парола **съвпада** с фразата "**s3cr3t!P@ssw0rd**".** При съвпадение да се изведе "**Welcome**". При несъвпадение да се изведе "**Wrong password!**". 
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top">qwerty</td><td colspan="1" valign="top">Wrong password!</td><td colspan="1" valign="top">s3cr3t!P@ssw0rd</td><td colspan="1" valign="top">Welcome</td><td colspan="1" valign="top">s3cr3t!p@ss</td><td colspan="1" valign="top">Wrong password!</td></tr>
</table>

1. ## **Число от 100 до 200**
Да се напише програма, която **чете цяло число**, въведено от потребителя и проверява дали е **под 100**, **между 100 и 200** или **над 200**. Ако числото е:

- под 100 отпечатайте: **"Less than 100"**
- между 100 и 200 отпечатайте: **"Between 100 and 200"**
- над 200 отпечатайте: **"Greater than 200"**

### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top">95</td><td colspan="1" valign="top">Less than 100</td><td colspan="1" valign="top">120</td><td colspan="1" valign="top">Between 100 and 200</td><td colspan="1" valign="top">210</td><td colspan="1" valign="top">Greater than 200</td></tr>
</table>
1. ## **Информация за скоростта**
Да се напише програма, която **чете скорост** **(реално число)**, въведена от потребителя** и отпечатва **информация за скоростта**. 

- При скорост **до 10** (включително) отпечатайте **"slow"**
- При скорост **над 10** и **до 50** (включително) отпечатайте **"average"** 
- При скорост **над 50** и **до 150** (включително) отпечатайте **"fast"**
- При скорост **над 150** и **до 1000** (включително) отпечатайте **"ultra fast"** 
- При по-висока скорост отпечатайте **"extremely fast"**
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top">8</td><td colspan="1" valign="top">slow</td><td colspan="1" valign="top">49\.5</td><td colspan="1" valign="top">average</td><td colspan="1" valign="top">126</td><td colspan="1" valign="top">fast</td><td colspan="1" valign="top">160</td><td colspan="1" valign="top">ultra fast</td><td colspan="1" valign="top">3500</td><td colspan="1" valign="top">extremely fast</td></tr>
</table>

1. ## **Лица на фигури**
Да се напише програма, в която потребителят **въвежда вида и размерите на геометрична** фигура и пресмята лицето й. Фигурите са четири вида: квадрат (**square**), правоъгълник (**rectangle**), кръг (**circle**) и триъгълник (**triangle**). На първия ред на входа се чете вида на фигурата (текст със следните възможности: **square**, **rectangle**, **circle** или **triangle**). 

- Ако фигурата е **квадрат (square)**: на следващия ред се чете едно дробно число - дължина на страната му
- Ако фигурата е **правоъгълник (rectangle)**: на следващите два реда четат две дробни числа - дължините на страните му
- Ако фигурата е **кръг (circle)**: на следващия ред чете едно дробно число - радиусът на кръга
- Ако фигурата е **триъгълник (triangle)**: на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея

Резултатът да се закръгли до **3 цифри след десетичната запетая**. 
### **Примерен вход и изход**

<table><tr><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th><th colspan="1" rowspan="2" valign="top"></th><th colspan="1"><b>вход</b></th><th colspan="1"><b>изход</b></th></tr>
<tr><td colspan="1" valign="top"><p>square</p><p>5</p></td><td colspan="1" valign="top">25\.000</td><td colspan="1" valign="top"><p>rectangle</p><p>7</p><p>2\.5</p></td><td colspan="1" valign="top">17\.500</td><td colspan="1" valign="top"><p>circle</p><p>6</p></td><td colspan="1" valign="top">113\.097</td><td colspan="1" valign="top"><p>triangle</p><p>4\.5</p><p>20</p></td><td colspan="1" valign="top">45\.000</td></tr>
</table>



