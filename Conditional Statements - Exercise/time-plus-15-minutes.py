import math

hour = int(input())
minutes = int(input())

totalMinutes = hour * 60 + minutes + 15

newHours = math.floor(totalMinutes / 60)
newMinutes = totalMinutes % 60

if newHours >= 24:
    newHours -= 24

if newMinutes < 10:
    print(f'{newHours}:0{newMinutes}')
else:
    print(f'{newHours}:{newMinutes}')