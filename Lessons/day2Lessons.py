# Data Types, Numbers, Operations, Type Conversion, F-Strings

print("")
# Data Types

# Strings
print("Hello"[4])  # prints o from word Hello

# Integers
print(123 + 345)
print(123_456_789)

# Floats
print(3.1459)

# Booleans
True
False


print("")
# Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))


print("")
# Mathematical Operations
3 + 5
7 - 4
3 * 2
6/3
2 ** 3

# PEMDAS
# () then ** then * or /, from left to right, then + or -, from left to right
print(3 * (3 + 3) / 3 - 3)


print("")
# Number Manipulation and F-Strings
result = 4/2
result /= 2
print(result)

score = 0
height = 1.8
isWinning = True

score += 1
print(score)

# F-Strings
print(f"The player that is a height of " + height + " has a score of " + score + " and is " + isWinning + " to themselves.")