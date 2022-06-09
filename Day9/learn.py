# Dictionaries
    # {key: value} pairs

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# In dictionaries elements are identified by their keys
print(programming_dictionary["Function"] + "\n")

# Adding new items to dictionaries
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(f"{programming_dictionary}\n")

# Creating an empty dictionary.
empty_dictionaries = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"] + '\n')

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    # print(key + ": " + (programming_dictionary[key]))
# OUTPUT:
# Bug
# Function
# Loop



# Nesting

# {
#     Key: [List],
#     Key: {Dict},
# }

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}


# Nesting List in a List
# ["A", "B", ["C", "D"]]

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {
               "cities_visited": ["Paris", "Lille", "Dijon"], 
               "total_visits": 12,
              },
    "Germany": ["Berlin", "Hamburg"]
}
print(travel_log)


# Nesting a dictionary inside a list
# [{
#     Key: [List],
#     Key: {Dict},
# },
# {
#     Key: Value,
#     Key2: Value,
# }]

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
    }
]



# Quiz Question

# Which line of code will change the starting_dictionary to the final_dictionary?

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

# Sol.
# starting_dictionary["c"] = 7
# final_dictionary = starting_dictionary
