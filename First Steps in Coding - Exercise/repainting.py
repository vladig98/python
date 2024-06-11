nylonPerSquareMeter = 1.5
paintPerLiter = 14.5
paintThinnerPerLiter = 5

additionalPaintPercentage = 1.1
additionalNylonSquareMeters = 2
bagPrice = 0.4
costPerHourPercentage = 0.3

nylonSquareMeters = int(input())
paintLiters = int(input())
paintThinnerLiters = int(input())
hoursToCompleteTheJob = int(input())

nylonTotalPice = (nylonSquareMeters + additionalNylonSquareMeters) * nylonPerSquareMeter
paintTotalPrice = paintLiters * additionalPaintPercentage * paintPerLiter
paintThinnerTotalPrice = paintThinnerLiters * paintThinnerPerLiter

totalProductsPrice = nylonTotalPice + paintTotalPrice + paintThinnerTotalPrice + bagPrice

amount = totalProductsPrice + totalProductsPrice * costPerHourPercentage * hoursToCompleteTheJob

print(amount)