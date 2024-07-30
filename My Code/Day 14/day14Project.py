# The Higher Lower Game

import random
import higher_lower_art
import higher_lower_GameData
print(higher_lower_art.logo)

numOfNames = 50
keepPlaying = True

score = 0
number1 = -1
number2 = -1
num1_dict = {}
num2_dict = {}
GameData = higher_lower_GameData.data


def start_game():
    global number1, number2, num1_dict, num2_dict, score
    score = 0
    number1 = random.randint(0, numOfNames)
    number2 = random.randint(0, numOfNames)
    while number1 == number2:
        number2 = random.randint(0, numOfNames)


def keep_asking():
    global number1, number2, num1_dict, num2_dict, score
    isNum1Higher = False
    isNum2Higher = False
    num1_dict = GameData[number1]
    print(f"Compare A: {num1_dict["name"]}, a {num1_dict["description"]}, from {num1_dict["country"]}.")
    print(higher_lower_art.vs)
    num2_dict = GameData[number2]
    print(f"Against B: {num2_dict["name"]}, a {num2_dict["description"]}, from {num2_dict["country"]}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if num1_dict["follower_count"] > num2_dict["follower_count"]:
        isNum1Higher = True
        isNum2Higher = False
    elif num2_dict["follower_count"] > num1_dict["follower_count"]:
        isNum1Higher = False
        isNum2Higher = True
    if choice == "a":
        if isNum1Higher:
            score += 1
            print(f"You are right! Your current score is {score}.\n")
            number1 = number2
            number2 = random.randint(0, numOfNames)
            while number1 == number2:
                number2 = random.randint(0, numOfNames)
            keep_asking()
        else:
            print(f"You are wrong! Your score is {score}.\n")
    elif choice == "b":
        if isNum2Higher:
            score += 1
            print(f"You are right! Your current score is {score}.\n")
            number1 = number2
            number2 = random.randint(0, numOfNames)
            while number1 == number2:
                number2 = random.randint(0, numOfNames)
            keep_asking()
        else:
            print(f"You are wrong! Your score is {score}.\n")
    else:
        print(f"I am sorry, but you entered {choice}, which is invalid, so you must restart!")
        start_game()


while keepPlaying:
    start_game()
    keep_asking()
    doYouWantToKeepPlaying = ""
    while doYouWantToKeepPlaying != "yes/no":
        doYouWantToKeepPlaying = input("Do you want to keep playing? yes or no: ").lower()
        if doYouWantToKeepPlaying == "yes":
            keepPlaying = True
            doYouWantToKeepPlaying = "yes/no"
        elif doYouWantToKeepPlaying == "no":
            keepPlaying = False
            doYouWantToKeepPlaying = "yes/no"
            print("Bye for now!")
        else:
            keepPlaying = False
            print("I am sorry, but that is an invalid answer.\n")
