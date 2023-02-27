#This program calculates and displays travel expenses
# 2/26/23
# CTI-110 P2HW1 - Travel
# Harmony Lewis

budget = float(input("Please enter your budget for this trip."))
print("User Budget:", "$",budget)
destination = input("Please enter your travel destination.")
print("Your destination is:", destination)
gas = float(input("How much do you think you will spend on gas?"))
print("You believe around", "$",gas, "will be spent on gas.")
hotel = float(input("How much do you think a hotel would cost you?"))
print("You beleive around", "$", hotel, "will be spent on a hotel.")
food = float(input("Lastly, how much do you need for food?"))
print("You believe around", "$", food, "will be needed for food.")

# Math #
totalExpenses = gas + hotel + food
print("Your total expenses are:",totalExpenses)
moneyAfterTrip = budget - totalExpenses
print("Remaining Balance after Trip:", moneyAfterTrip)

# Details #
print("-" * 30, "Travel Expenses", "-" * 30)
print("Location:",destination)
print("Initial Budget:", "$", budget)
print(" ")
print("Fuel:", "$", gas)
print("Hotel:", "$", hotel)
print("Food:", "$", food)
print(" ")
print("Remaining Balance", "$", moneyAfterTrip)