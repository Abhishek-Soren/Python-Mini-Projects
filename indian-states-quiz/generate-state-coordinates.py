from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("INDIA STATES QUIZ")

image = "india-outline-map.gif"
screen.addshape(image)

turtle = Turtle()

turtle.shape(image)

test_dict = {
    "x": [],
    "y": [],
}


def get_mouse_click_coor(x, y):
    x_value = x
    y_value = y
    test_dict["x"].append(x_value)
    test_dict["y"].append(y_value)
    print(x, y)


screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()

df = pd.DataFrame(test_dict)
df.to_csv("x_y.csv")
