# Object-Oriented Programming (OOP)

import turtle
rebecca = turtle.Turtle()
print(rebecca)
rebecca.shape("turtle")
rebecca.color("cyan2")

turn_left = 3
while turn_left > 0:
    rebecca.forward(100)
    rebecca.left(120)
    turn_left -= 1

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
