import importlib
current_day = 17

# Put All Lessons & Projects #'s w/o Any Code Here!
noLessons = [6, 7, 11, 14, 15]
noProjects = [6, 13]

print("Hello, Hanna! :3")
whichOne = int(input("Type 1 For Lessons, OR 2 For Projects: "))
whatDay = int(input("What Day are you working on: "))

if whatDay > current_day:
    print("That Day has not been worked on yet.")
else:
    print("")
    if whichOne == 1:
        index = 0
        noLessonsForDay = False
        while index < len(noLessons):
            if noLessons[index] == whatDay:
                print(f"There was no Lessons for Day {whatDay}!")
                noLessonsForDay = True
                break
            index += 1
        if not noLessonsForDay:
            runCodeForDay = f'My Code.Day {whatDay}.day{whatDay}Lessons'
            i = importlib.import_module(runCodeForDay)
    elif whichOne == 2:
        index = 0
        noProjectsForDay = False
        while index < len(noProjects):
            if noProjects[index] == whatDay:
                print(f"There was no Project for Day {whatDay}!")
                noProjectsForDay = True
                break
            index += 1
        if not noProjectsForDay:
            runCodeForDay = f'My Code.Day {whatDay}.day{whatDay}Project'
            i = importlib.import_module(runCodeForDay)
