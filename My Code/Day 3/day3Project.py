# Day 3: Love Island - Choose Your Fate!

print('''
        _.-%/______________________/////
        `.-%\~~~~~~~~~~~~~~~~~~~~~~\\\\\\\\\\ ''')
print("")
print("Welcome to Love Island~!")
print("Your mission is to find your way back to your lover!")

# Write your code below this line 👇

print("")
print("You start in a white room, with two doors. You must pick a direction, and soon!")
choice = input("Enter L for door on Left, R for door on Right: ")

print("")
if choice == "L":
    print("You open the door, and run down a long hallway to The Pool Of Lava.")
    print("Will you wait for a path to open up, or try crossing the pool?")
    choice = input("Please Type W to wait, or C to Cross The Pool Of Lava: ")
    print("")
    if choice == "W":
        print("You wait, and a portal opens up to cross The Pool Of Lava.")
        print("You enter the portal, and come to a room with Three Doors.")
        choice = int(input("Please Type 1, 2, or 3: "))
        print("")
        if choice == 2:
            print("You open the door, and see your lover waiting for you,")
            print("and you run and give your lover a hug! Happy Ending!")
        if choice == 1:
            print("You open the door, and see the bully from High School in front of you.")
            print("You try to fight them, but get bashed in the head. The End!")
        if choice == 3:
            print("You open the door, and see the sunlight, and decide to go into it,")
            print("only to realize that there were 5 snipers lying in wait. The End!")
    elif choice == "C":
        print("You saw some rocks, and decided to try jumping on top of them, but")
        print("you missed one rock, and drowned. The End!")

elif choice == "R":
    print("You open the door, and see a long bridge made of rope.")
    print("You decide to try crossing it, and you fall to your death. The End!")