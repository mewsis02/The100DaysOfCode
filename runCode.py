import importlib

# Put All Lessons & Projects #'s w/o Any Code Here!
noLessons = [6, 7, 11, 14, 15]
noProjects = [6, 13]


# Pulls up the Lessons
def my_lessons(day):
    index = 0
    noLessonsForDay = False
    while index < len(noLessons):
        if noLessons[index] == day:
            print(f"There was no Lessons for Day {day}!")
            noLessonsForDay = True
            break
        index += 1
    if not noLessonsForDay:
        runCodeForDay = f'Lessons.day{day}Lessons'
        i = importlib.import_module(runCodeForDay)


# Pulls up the Projects
def my_projects(day):
    index = 0
    noProjectsForDay = False
    while index < len(noProjects):
        if noProjects[index] == day:
            print(f"There was no Project for Day {day}!")
            noProjectsForDay = True
            break
        index += 1
    if not noProjectsForDay:
        runCodeForDay = f'Lessons.day{day}Lessons'
        i = importlib.import_module(runCodeForDay)
