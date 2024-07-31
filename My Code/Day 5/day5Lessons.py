# Day 5: For Loops With & Without Range

# For Loops
fruits = ["Apple", "Peach", "Pear"]
index = -1
for fruit in fruits:
  index += 1
  fruits[index] = fruit + " Pie"
  print(fruit)
print(fruits)

# For Loops With Range
total = 0
for number in range(1, 101):
  total += number
print(total)