# Conditional Statements, Logical Operators

print("Welcome to the Hanna's Rollers!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("\nYou can ride the rollercoaster!")
    age = int(input("\nWhat is your age? "))
    if (age < 12):
        bill = 5
        print("Child Tickets are $5.")
    elif (age <= 18):
        bill = 7
        print("Youth Tickets are $7.")
    elif (age >= 45 and age <= 55):
        print("Midlife Crisis Tickets going for Free!")
    else:
        bill = 12
        print("Adult Tickets are $12.")

    wants_photo = input("\nDo you want your photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"\nPlease pay the ${bill} fee first!")

else:
    print("Sorry, you are not tall enough to ride yet.")

print("")
# My Auditorium Lesson
print("The Love Calculator is calculating your score...")
name1 = input("What is your full name: ")
name2 = input("What is their full name: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = list(name1.lower())
name2 = list(name2.lower())
love_letters = 0
true_letters = 0

temp = 0
while len(name1) > temp:
    if name1[temp] == "t" or name1[temp] == "r" or name1[temp] == "u" or name1[temp] == "e":
        true_letters += 1
    if name1[temp] == "l" or name1[temp] == "o" or name1[temp] == "v" or name1[temp] == "e":
        love_letters += 1
    temp += 1

temp = 0
while len(name2) > temp:
    if name2[temp] == "t" or name2[temp] == "r" or name2[temp] == "u" or name2[temp] == "e":
        true_letters += 1
    if name2[temp] == "l" or name2[temp] == "o" or name2[temp] == "v" or name2[temp] == "e":
        love_letters += 1
    temp += 1

love_score = f"{true_letters}{love_letters}"
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 or love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")