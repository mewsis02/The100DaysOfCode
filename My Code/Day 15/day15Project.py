# Day 15: Hanna's Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_gained = 0.00
runCoffeeMachine = True

while runCoffeeMachine:
    # If haveEnoughIngredients = 3, then run the Coffee Machine, because you have enough ingredients!
    haveEnoughIngredients = 0
    missingWhichIngredients = ""
    which_coffee = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if which_coffee == "off":
        break
    elif which_coffee == "report":
        print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g")
        print(f"Money: ${round(money_gained, 3)}")
    elif which_coffee == "espresso" or which_coffee == "latte" or which_coffee == "cappuccino":
        if resources["water"] >= MENU[which_coffee]["ingredients"]["water"]:
            haveEnoughIngredients += 1
        if resources["milk"] >= MENU[which_coffee]["ingredients"]["milk"]:
            haveEnoughIngredients += 1
        if resources["coffee"] >= MENU[which_coffee]["ingredients"]["coffee"]:
            haveEnoughIngredients += 1
        if haveEnoughIngredients < 3:
            print(f"I am sorry, but you are missing {3 - haveEnoughIngredients} ingredients.")
        elif haveEnoughIngredients == 3:
            # coins = Quarters, Dimes, Nickels, Pennies
            coins = [0, 0, 0, 0]
            coins[0] = int(input("How many Quarters: "))
            coins[1] = int(input("How many Dimes: "))
            coins[2] = int(input("How many Nickels: "))
            coins[3] = int(input("How many Pennies: "))
            total_value = 0.00 + (coins[0] * 0.25) + (coins[1] * 0.10) + (coins[2] * 0.05) + (coins[3] * 0.01)
            if total_value < MENU[which_coffee]["cost"]:
                missing_money = MENU[which_coffee]["cost"] - total_value
                print(f"I am sorry, but you are missing ${missing_money}. All money will be refunded.")
            else:
                leftover_change = total_value - MENU[which_coffee]["cost"]
                total_value -= leftover_change
                money_gained += total_value
                if leftover_change > 0.00:
                    print(f"Your change is ${round(leftover_change, 3)}!")
                resources["water"] -= MENU[which_coffee]["ingredients"]["water"]
                resources["milk"] -= MENU[which_coffee]["ingredients"]["milk"]
                resources["coffee"] -= MENU[which_coffee]["ingredients"]["coffee"]
                print(f"Here is your {which_coffee}. Enjoy!")
    else:
        print("That coffee does not exist! Please Try Again!")
