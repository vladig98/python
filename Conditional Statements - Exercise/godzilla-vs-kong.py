decor = 0.1
discount150OrMoreStatists = 0.9

movieBudget = float(input())
numberOfStatists = int(input())
pricePerWardrobe = float(input())

decorPrice = movieBudget * decor
wardrobePrice = numberOfStatists * pricePerWardrobe

if numberOfStatists > 150:
    wardrobePrice *= discount150OrMoreStatists

totalMoviePrice = decorPrice + wardrobePrice

if totalMoviePrice > movieBudget:
    print('Not enough money!')
    print(f'Wingard needs {round(totalMoviePrice - movieBudget, 2):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {round(movieBudget - totalMoviePrice, 2):.2f} leva left.')