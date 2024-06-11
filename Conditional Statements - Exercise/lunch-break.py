import math

lunchTime = 8
relaxTime = 4

showName = input()
episodeLength = int(input())
breakLength = int(input())

lunchTimeDuration = breakLength / lunchTime
relaxTimeDuration = breakLength / relaxTime

remainingTime = breakLength - lunchTimeDuration - relaxTimeDuration

if remainingTime >= episodeLength:
    print(f'You have enough time to watch {showName} and left with {math.ceil(remainingTime - episodeLength)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {showName}, you need {math.ceil(episodeLength - remainingTime)} more minutes.')