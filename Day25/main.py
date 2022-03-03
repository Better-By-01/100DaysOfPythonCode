# FILE_PATH = "/home/better-by-01/100DaysOfPythonCode/Day25/weather_data.csv"
# with open(FILE_PATH) as data:
#     contents = data.readlines()
#     for i in range(len(contents)):
#         contents[i] = contents[i].strip('\n')
#     print(contents)

# import csv

# with open(FILE_PATH) as data_file:
#     data = csv.reader(data_file)
#     # print(data)         # <_csv.reader object at 0x7efda099bdd0>
#     temperatures = []
#     for row in data:
#         if (row[1] != "temp"):
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("./Day25/weather_data.csv")
print(type(data))               # pandas DataFrame 2-D
print(data["temp"])             # pandas Series 1-D

data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()
# print(temp_list)      # a list

print(f"Mean temperature: {data['temp'].mean()}")
print(f"Max temperature: {data['temp'].max()}")


# Get data in columns

# print(data["condition"])
# is same as
print(data.condition)


# Get data in rows

print(f"{data[data.day == 'Monday']}\n")

# row data where max. temp. in a week
print(data[data.temp == data.temp.max()])


# monday's temp. to fahreheit
mon_temp = int(data[data.day == "Monday"].temp)
print((mon_temp*9/5)+32)



# Create a dataframe from scratch
data_dict = {
    "students": ["Ashu", "Aayush", "Varun"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./Day25/new_data.csv")


# Central Park Squirrel Data Analysis

data = pandas.read_csv("./Day25/2018_squirrel_data.csv")
fur_colors = data["Primary Fur Color"].dropna().unique()
squirrel_count = [] 
for color in fur_colors:  
    val = len(data[data["Primary Fur Color"] == color])
    squirrel_count.append(val)

data_dict = {}

data_dict["Fur_Color"] = fur_colors
data_dict["Count"] = squirrel_count

df = pandas.DataFrame(data_dict)
df.to_csv("./Day25/squirrel_count.csv")