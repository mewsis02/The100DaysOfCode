# Day 16: Hanna's OOP Coffee Machine

from .menu import Menu, MenuItem
from .coffee_maker import CoffeeMaker
from .money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
runCoffeeMachine = True

while runCoffeeMachine:
    money_machine.report()
    print("")
    coffee_maker.report()
    whichCoffee = menu.find_drink(input(f"What would you like? ({menu.get_items()}): ").lower())
    if whichCoffee == "off":
        runCoffeeMachine = False
    if whichCoffee != None:
        if coffee_maker.is_resource_sufficient(whichCoffee):
            if money_machine.make_payment(whichCoffee.cost):
                coffee_maker.make_coffee(whichCoffee)
