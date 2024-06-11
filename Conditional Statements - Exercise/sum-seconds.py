import math

seconds_one = int(input())
seconds_two = int(input())
seconds_three = int(input())

total = seconds_one + seconds_two + seconds_three

minutes = math.floor(total / 60)
seconds = total % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')