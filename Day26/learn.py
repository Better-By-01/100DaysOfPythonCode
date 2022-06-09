import random
import pandas as pd
################ List and Dictionary Comprehension ####################

# List comprehension
# creating list from another list
# new_list = [new_item for item in list]

from numpy import short


numbers = [1,2,3]                   # also applicable for strings
numbers_list = [i+1 for i in numbers]
print(f"Numbers List: {numbers_list}")

name = "Ashutosh"
letters_list = [letter for letter in name]
print(f"Letters List: {letters_list}")

# NOTE:
# python sequences (an ordered set)
# means the order in which we input the items will be the same when we access them.
# -> list, range, string, tuple 

range_list = [i*2 for i in range(1,5)]
print(f"Range List: {range_list}")


# Conditional List comprehension
# new_list = [new_item for item in list if test]

# short names with length < 7 and in upper case
names = ["Ashutosh", "Aditya", "Aayush", "Varun", "Trupti"]
short_names = [name.upper() for name in names if len(name) < 7]
print(short_names)



# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}

# from an existing dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}


names = ["Ashutosh", "Aditya", "Aayush", "Varun", "Trupti"] 
students_score = {student:random.randint(1,101) for student in names}
print(students_score)

passed_score = {student:score for (student, score) in students_score.items() if score >= 60}
print(passed_score)


# Converting dictionary of temp. in C to F.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def ctof(temp_c):
    return ((temp_c*9/5)+32)

weather_f = {day:ctof(temp_c) for (day, temp_c) in weather_c.items()} 

print(weather_f)


# Iterate over pandas DataFrame

student_dict = {
    "student": ["Ashutosh", "Aditya", "Lily"],
    "score": [95, 82, 56]
}

# NOTE:
# loopint through dictionary:
# for (key, value) in student_dict.items(): 
#     print(value)

df = pd.DataFrame(student_dict)
# print(df)
for(key,value) in df.items():
    # print(key)                    # give titles of each column
    print(value)
    # 0    Ashutosh
    # 1      Aditya
    # 2        Lily
    # Name: student, dtype: object
    # 0    95
    # 1    82
    # 2    56
    # Name: score, dtype: int64

# Loop through rows of a data frame
for (index, row) in df.iterrows():
    # print(index)                    # gives the indices
    print(row)                        # each of this row is a pandas series object
                                      # so we can use things like row.score, row, student
    # student    Ashutosh
    # score            95
    # Name: 0, dtype: object
    # student    Aditya
    # score          82
    # Name: 1, dtype: object
    # student    Lily
    # score        56
    # Name: 2, dtype: object