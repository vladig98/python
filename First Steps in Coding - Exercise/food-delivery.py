chickenMenu = 10.35
fishMenu = 12.4
vegetarianMenu = 8.15
deliveryFee = 2.5
desertPricePercentage = 0.2

numberOfChickenMenus = int(input())
numberOfFishMenus = int(input())
numberOfVegetarianMenus = int(input())

totalFoodPrice = numberOfChickenMenus * chickenMenu + numberOfFishMenus * fishMenu + numberOfVegetarianMenus * vegetarianMenu

amount = totalFoodPrice + totalFoodPrice * desertPricePercentage + deliveryFee

print(amount)