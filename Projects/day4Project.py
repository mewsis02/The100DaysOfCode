# Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = input("Do you choose Rock, Paper, or Scissors: ")
player_choice = player_choice.lower()
if player_choice == "rock":
    player_choice = rock
if player_choice == "paper":
    player_choice = paper
if player_choice == "scissors":
    player_choice = scissors

bot_rand_choice = random.randint(1, 3)
bot_choice = "None."
if bot_rand_choice == 1:
    bot_choice = rock
if bot_rand_choice == 2:
    bot_choice = paper
if bot_rand_choice == 3:
    bot_choice = scissors

print(f"\nYou Chose: \n{player_choice}\nEnemy Chose: \n{bot_choice}\n")

if player_choice == bot_choice:
    print("You Tied!")
elif player_choice == rock and bot_choice == scissors:
    print("Rock smacks Scissors, so you win!")
elif player_choice == scissors and bot_choice == rock:
    print("Scissors gets smacked by Rock, so you lost.")
elif player_choice == scissors and bot_choice == paper:
    print("Scissors slices through Paper, so you win!")
elif player_choice == paper and bot_choice == scissors:
    print("Paper gets sliced by Scissors, so you lost!")
elif player_choice == paper and bot_choice == rock:
    print("Paper chucks the Rock, so you win!")
elif player_choice == rock and bot_choice == paper:
    print("Rock gets chucked by Paper, so you lost!")