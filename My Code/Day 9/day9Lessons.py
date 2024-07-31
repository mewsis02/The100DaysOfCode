# Day 9: Dictionaries & Nesting

# Python Dictionaries
programming_dictionary = {
    "Bug":       "An error in a program that prevents the program from running as expected.",
    "Function":  "A piece of code that you can easily call over and over again.",
}

# Retrieving Items from a Dictionary
# print(programming_dictionary["Bug"])

# Adding Items to a Dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Edit an Item in a Dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a Dictionary
for Key in programming_dictionary:
    print(Key)
    print(programming_dictionary[Key])

# Nesting a List in a Dictionary
programming_dictionary["Stats"] = ["Health", "Level", "Experience", "Currency"]

# Nesting a Dictionary inside a Dictionary
programming_dictionary["The Game"] = {
    "Player Stats": programming_dictionary["Stats"],
    "Enemy Stats":  programming_dictionary["Stats"]
}

# Nesting Dictionaries into a List
travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(travel_log)
print(programming_dictionary)
# Create an Empty Dictionary OR Wipe an Existing Dictionary
programming_dictionary = {}
print(programming_dictionary)
