# Day 11: The Blackjack Capstone Project

import random

# Order  : Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, King, Queen, Jack
the_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playNewGame = "yes"

def Blackjack():

    player_cards = [ the_deck[random.randint(0, 12)], the_deck[random.randint(0, 12)] ]
    player_cards_total = player_cards[0] + player_cards[1]
    display_player_cards = f"{str(player_cards[0])} + {str(player_cards[1])}"

    computer_cards = [ the_deck[random.randint(0, 12)], the_deck[random.randint(0, 12)] ]
    computer_cards_total = computer_cards[0] + computer_cards[1]
    play_another_card = True
    playNewGame = "yes/no"

    while play_another_card == True:

        print(f"Computer Score : {computer_cards[0]}")
        print(f"Your Score     : {display_player_cards}")

        # You Lost/Won Based on if you or computer had Blackjack
        if computer_cards[0] == 11 and computer_cards[1] == 10 or computer_cards[0] == 10 and computer_cards[1] == 11:
            print("You have lost the game because of a Blackjack!")
            play_another_card = False

        elif player_cards[0] == 11 and player_cards[1] == 10 or player_cards[0] == 10 and player_cards[1] == 11:
            print("You have won the game with a Blackjack!")
            play_another_card = False

        if play_another_card == True:
            # Pulls a new card to be played if you say yes
            play_new_card = input("Would you like to play a new card? yes or no: ").lower()
            if play_new_card == "yes":
                new_player_card_value = the_deck[random.randint(0, 12)]
                # Checks if the new card is an Ace and if the player's value is over 21
                if player_cards_total + new_player_card_value > 21 and new_player_card_value == 11:
                    player_cards.append(1)
                    print("You have pulled an Ace with a value of 1!\n")
                else:
                    # Adds the new card to player cards
                    player_cards.append(new_player_card_value)
                    print(f"You have pulled a card with a value of {new_player_card_value}!\n")
                player_cards_total += new_player_card_value
                display_player_cards += f" + {new_player_card_value}"

                if computer_cards_total <= 16:
                    new_computer_card_value = the_deck[random.randint(0, 12)]
                    # Checks if the new card is an Ace and if the computer's value is over 21
                    if computer_cards_total + new_computer_card_value > 21 and new_computer_card_value == 11:
                        computer_cards.append(1)
                        computer_cards_total += new_computer_card_value
                    else:
                        # Adds the new card to computer cards
                        computer_cards.append(new_computer_card_value)
                        computer_cards_total += new_computer_card_value

                # You Lose if your score goes over 21
                if player_cards_total > 21:
                    print("You have lost the game! Your total went over 21!")
                    play_another_card = False

            elif play_new_card == "no":
                play_another_card = False
                if player_cards_total > computer_cards_total:
                    print("You have won the game! You had a higher score!")
                    play_another_card = False

                elif computer_cards_total > player_cards_total:
                    print("You have lost the game! The computer had a higher score!")
                    play_another_card = False

                elif player_cards_total == computer_cards_total:
                    print("The game ended in a draw!")
                    play_another_card = False

            else:
                print("Please give me a valid response.\n")

    print(f"Your score was {player_cards_total}, and the computer's score was {computer_cards_total}.")
    playNewGame = input("\nDo you want to play another game of Blackjack? yes or no: ").lower()
    print("\n")
    if playNewGame != "yes":
        if playNewGame != "no":
            print("You gave me an invalid response, so")
    return playNewGame

while playNewGame == "yes":
    playNewGame = Blackjack()
print("Come again soon!")