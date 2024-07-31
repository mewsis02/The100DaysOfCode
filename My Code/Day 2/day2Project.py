# Day 2: Tip Calculator

print("")
bill = float(input("What is the bill amount: "))
tip_amount = int(input("What percent are we paying: "))
numOfPeople = int(input("How many people are paying: "))
price_per_person = bill * (1 + (tip_amount/100)) / numOfPeople
price_per_person = "{:.2f}".format(round(price_per_person, 2))
print("")
print(f"Every person here will pay ${price_per_person}.")