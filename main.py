# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from numpy.ma.core import maximum
from numpy.ma.extras import average
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list =data["temp"].to_list()
# # print(maximum(temp_list)) print the average
#
# print(data["temp"].mean())
# print(data ["temp"].max())
#
# #get data in column
# print(data["condition"])
# #samme result
# print(data.condition)

#Get data in the row
# print(data[data.day == "Monday"])

#Which row has the maximum temperature
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# #convert mondays temp to Fahrenheit
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"{monday_temp_F} Fahrenheit")

#create a dataframe from scratch
# data_dict = {
#     "students": ["Anders", "Annika", "Agnes", "Anton"],
#     "scores": [62, 68, 66, 64]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



