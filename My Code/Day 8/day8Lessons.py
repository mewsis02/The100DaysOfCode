# Functions with Inputs

# Simple Function
def greet():
    print("")
    print("Hello Hanna! :3")
    print("Please subscribe to my channel called #hanna4life!")
    print("I love you, Hanna, and I wish you a wonderful day!")


# Function That Allows For Input
def greet_with_name(name):
    print("")
    print(f"Hello {name}! :3")
    print(f"Please subscribe to my channel called #{name}4life!")
    print(f"I love you, {name}, and I wish you a wonderful day!")


# Function That Allows For Multiple Input
def greet_with(name, location):
    print("")
    print(f"Hello {name} from {location}! :3")
    print(f"Please subscribe to my channel called #{name}4{location}!")
    print(f"I love you, {name} from {location}. Have a wonderful day!")


# greet()
# greet_with_name(input("What is your name? "))
# greet_with(input("What is your name? "), input("What is your birth city? "))

# Functions with Keyword Arguments
greet_with(location=input("What is your birth city? "), name=input("What is your name? "))
