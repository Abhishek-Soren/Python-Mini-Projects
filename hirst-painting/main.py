# import colorgram
import random
import turtle as t


# To get colors from an image
# colors = colorgram.extract("img.jpg",25)
# color_list = []
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     color_tuple = (r, g, b)
#
#     color_list.append(color_tuple)
#
# print(color_list)

color_list_final = [(42, 77, 175), (83, 232, 204), (67, 202, 224), (209, 66, 21), (234, 170, 165), (218, 24, 102), (243, 234, 45), (27, 42, 163), (174, 178, 229), (58, 16, 10), (84, 81, 205), (206, 14, 31), (222, 139, 199), (237, 159, 211), (231, 44, 127), (23, 148, 26), (237, 226, 6), (220, 153, 78), (70, 210, 145), (69, 231, 240), (217, 80, 52)]

tim = t.Turtle()
tim.speed("fast")

tim.hideturtle()

t.colormode(255)

for x in range(-200,300,50):
    for y in range(-200,300,50):
        tim.penup()
        tim.setposition(y, x)
        tim.pendown()
        tim.dot(20, random.choice(color_list_final))


screen = t.Screen()
t.exitonclick()