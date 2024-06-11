puzzle = 2.6
talkingDoll = 3
teddyBear = 4.1
minion = 8.2
truck = 2

discount50OrMore = 0.75
rentPercentage = 0.9

tripPrice = float(input())
numberOfPuzzles = int(input())
numberOfTalkingDolls = int(input())
numberOfTeddyBears = int(input())
numberOfMinions = int(input())
numberOfTrucks = int(input())

totalToys = numberOfPuzzles + numberOfTalkingDolls + numberOfTeddyBears + numberOfMinions + numberOfTrucks

totalToysPrice = numberOfPuzzles * puzzle + numberOfTalkingDolls * talkingDoll + numberOfTeddyBears * teddyBear + numberOfMinions * minion + numberOfTrucks * truck

if totalToys >= 50:
    totalToysPrice *= discount50OrMore

earnings = totalToysPrice * rentPercentage

if earnings >= tripPrice:
    print(f'Yes! {round(earnings - tripPrice, 2):.2f} lv left.')
else:
    print(f'Not enough money! {round(tripPrice - earnings, 2):.2f} lv needed.')