squareMetersForGreening = float(input())
pricePerSquareMeter = 7.61
discount = 0.18
reversedDiscount = 1 - discount
totalPrice = squareMetersForGreening * pricePerSquareMeter

print(f'The final price is: {totalPrice * reversedDiscount} lv.')
print(f'The discount is: {totalPrice * discount} lv.')