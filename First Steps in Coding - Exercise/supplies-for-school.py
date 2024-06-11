packOfPens = 5.8
packOfMarkers = 7.2
cleaner = 1.2

numberOfPacksOfPens = int(input())
numberOfPacksOfMarkers = int(input())
numberOfLitersOfCleaner = int(input())
discountPercentage = int(input())
reversedDiscount = 100 - discountPercentage

amount = (numberOfPacksOfPens * packOfPens + numberOfPacksOfMarkers * packOfMarkers + numberOfLitersOfCleaner * cleaner) * reversedDiscount / 100

print(amount)