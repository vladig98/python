numberOfPagesInBook = int(input())
numberOfPagesPerHour = int(input())
numberOfDays = int(input())

from math import floor

totalHours = floor(numberOfPagesInBook / numberOfPagesPerHour)
hourPerDay = floor(totalHours / numberOfDays)

print(hourPerDay)