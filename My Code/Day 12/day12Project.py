# Day 12: Your Guess - A Number Guessing Game

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import your_guess_art
print(your_guess_art.logo)

default_num_of_guesses = 12
keepPlayingYourGuess = True

game_mode = input("Would you like to play on Normal mode, or Hard mode? Type Normal or Hard: ").lower()
if game_mode == "normal":
    default_num_of_guesses = 9
elif game_mode == "hard":
    default_num_of_guesses = 6
else:
    print("That was an invalid response, so I gave you Easy Mode.\n")

while keepPlayingYourGuess:

    isAnswerWrong = True
    num_of_guesses = default_num_of_guesses
    answer = random.randint(1, 100)
    keepGuessing = True

    while keepGuessing:
        print(f"\nYou have {num_of_guesses} guesses remaining.")
        player_guess = int(input("Give me a guess between 1 and 100: "))
        num_of_guesses -= 1
        if player_guess == answer:
            isAnswerWrong = not isAnswerWrong
        elif player_guess > answer:
            print(f"I am sorry, but you guessed too high with {player_guess}.")
        elif player_guess < answer:
            print(f"I am sorry, but you guessed too low with {player_guess}.")

        if num_of_guesses == 0 or not isAnswerWrong:
            keepGuessing = False
            if num_of_guesses == 0:
                print(f"\nYou lost! The correct answer was {answer}!")
            elif not isAnswerWrong:
                print(f"\nYay, You guessed the correct answer of {answer} with {num_of_guesses} guesses remaining! :3")

            makeAnotherGuess = input("Would you like to guess another number? Type yes or no: ").lower()
            if makeAnotherGuess == "yes":
                keepPlayingYourGuess = True
            elif makeAnotherGuess == "no":
                keepPlayingYourGuess = False
                print("Come again soon!")
            else:
                keepPlayingYourGuess = False
                print("That was an invalid response. Goodbye.\n")
