import runCode
current_day = 15

print("Hello, Hanna! :3")
whichOne = int(input("Type 1 For Lessons, OR 2 For Projects: "))
whatDay = int(input("What Day are you working on: "))

if whatDay > current_day:
    print("That Day has not been worked on yet.")
else:
    if whichOne == 1:
        print(f"Pulling up Day {whatDay} Lessons now...\n")
        runCode.my_lessons(whatDay)
    elif whichOne == 2:
        print(f"Pulling up Day {whatDay} Projects now...\n")
        runCode.my_projects(whatDay)
