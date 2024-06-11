import math

slownessEvery15Meters = 12.5

recordToBeat = float(input())
distanceToSwim = float(input())
timeToSwim1Meter = float(input())

totalSecondsToSwim = distanceToSwim * timeToSwim1Meter

slowingDownCounter = math.floor(distanceToSwim / 15)

totalSecondsToSwim += slowingDownCounter * slownessEvery15Meters

if totalSecondsToSwim < recordToBeat:
    print(f'Yes, he succeeded! The new world record is {(totalSecondsToSwim):.2f} seconds.')
else:
    print(f'No, he failed! He was {(totalSecondsToSwim - recordToBeat):.2f} seconds slower.')