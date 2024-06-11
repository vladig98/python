shoes = 0.6
jersey = 0.8
ball = 0.25
accessories = 0.2

yearlySubscriptionPrice = int(input())

shoesPrice = yearlySubscriptionPrice * shoes
jerseyPrice = shoesPrice * jersey
ballPrice = jerseyPrice * ball
accessoriesPrice = accessories * ballPrice

amount = yearlySubscriptionPrice + shoesPrice + jerseyPrice + ballPrice + accessoriesPrice

print(amount)