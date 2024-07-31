# Day 5: Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password: "))
nr_symbols = int(input(f"How many symbols would you like: "))
nr_numbers = int(input(f"How many numbers would you like: "))

print("")
nr_chars = int(nr_letters) + int(nr_symbols) + int(nr_numbers)
which_one = 0
password = ""

for char in range(0, nr_chars):
  which_one = random.randint(1, 3) # 1 = Letter, 2 = Number, 3 = Symbol
  if which_one == 1:
    which_letter = random.randint(0, len(letters)-1)
    password += letters[which_letter]
  if which_one == 2:
    which_number = random.randint(0, len(numbers)-1)
    password += numbers[which_number]
  if which_one == 3:
    which_symbol = random.randint(0, len(symbols)-1)
    password += symbols[which_symbol]

print(f"\nYour {nr_chars} char password has been created below.")
print(f"\nYour new password is: {password}")