graphicsCardPrice = 250
processorPricePercentage = 0.35
RAMPricePercentage = 0.10

discountIfGraphicsCardCountIsBiggerThanProcessorsCount = 0.85

budget = float(input())
numberOfGraphicCards = int(input())
numberOfProcessors = int(input())
numberOfRAMSticks = int(input())

graphicCardsTotalPrice = numberOfGraphicCards * graphicsCardPrice

processorPrice = graphicCardsTotalPrice * processorPricePercentage
RAMStickPrice = graphicCardsTotalPrice * RAMPricePercentage

totalPrice = graphicCardsTotalPrice + numberOfProcessors * processorPrice + numberOfRAMSticks * RAMStickPrice

if numberOfGraphicCards > numberOfProcessors:
    totalPrice *= discountIfGraphicsCardCountIsBiggerThanProcessorsCount

if totalPrice <= budget:
    print(f'You have {budget - totalPrice:.2f} leva left!')
else:
    print(f'Not enough money! You need {totalPrice - budget:.2f} leva more!')