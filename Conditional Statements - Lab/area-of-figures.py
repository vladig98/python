figure = input()

if figure == 'square':
    side = float(input())
    print(side * side)
elif figure == 'rectangle':
    sideA = float(input())
    sideB = float(input())
    print(sideA * sideB)
elif figure == 'circle':
    radius = float(input())
    from math import pi

    print(pi * radius * radius)
else:
    base = float(input())
    height = float(input())

    print(base * height / 2)