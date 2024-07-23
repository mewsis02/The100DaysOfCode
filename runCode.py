import importlib


def my_lessons(day):
    runCodeForDay = f'Lessons.day{day}Lessons'
    i = importlib.import_module(runCodeForDay)


def my_projects(day):
    runCodeForDay = f"Projects.day{day}Project"
    i = importlib.import_module(runCodeForDay)
