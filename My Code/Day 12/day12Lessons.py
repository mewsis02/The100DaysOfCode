# Day 12: Local and Global Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) will give error because potion_strength is a local variable inside of drink_potion
# and is not defined as a variable on a global scope

# Global Scope
player_health = 10
computer_health = 15


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()


# Modifying Variables with Global Scope (using both return and global)
def drink_potion():
    global player_health
    player_health += 5
    return computer_health + 5


computer_health = drink_potion()
print(f"Your health has been recovered to: {player_health}")
print(f"The computer's health has been recovered to: {computer_health}")

# Global Constants
# are variables that never need to be changed while accessing them.
PI = 3.14159
URL = "https://www.google.com"
