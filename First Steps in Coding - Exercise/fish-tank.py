length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

literPerCubicMeter = 0.001

amount = length * width * height * literPerCubicMeter * (1 - (percentage / 100))

print(amount)