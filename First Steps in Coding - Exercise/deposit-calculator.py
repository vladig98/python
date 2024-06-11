depositAmount = float(input())
depositPeriodInMonths = int(input())
depositInterestRate = float(input())

amount = depositAmount + depositPeriodInMonths * ((depositAmount * depositInterestRate / 100) / 12)

print(amount)