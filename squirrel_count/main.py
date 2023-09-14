import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]
color_list = color.to_list()

gray_count = color_list.count("Gray")

#other way to get the number of gray squirrels
gray_count_new = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_count_new)


cinnamon_count = color_list.count("Cinnamon")

cinnamon_count_new = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_count_new)

black_count = color_list.count("Black")

black_count_new = len(data[data["Primary Fur Color"] == "Black"])
print(black_count_new)

print(gray_count, cinnamon_count, black_count)

new_color_list = {
    "fur color" : ["Gray", "Cinnamon", "Black"],
    "count" : [gray_count, cinnamon_count, black_count],
}
print(new_color_list)
df = pd.DataFrame(new_color_list)

df.to_csv("squirrel_count.csv")