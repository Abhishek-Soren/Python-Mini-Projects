import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

from turtle import Screen, Turtle
import pandas as pd
import string

data = pd.read_csv("./50_states.csv")
states = data["state"].to_list()
screen = Screen()
screen.title("US States Games")

image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer()

turtle = Turtle()
tim = Turtle()
tim.hideturtle()
tim.penup()

turtle.shape(image)

title_string = "Guess the State"
game_should_continue = True
score = 0

curr_state_list = []

while game_should_continue:
    answer = (screen.textinput(title=title_string, prompt="What's another state's name?"))
    another_state = string.capwords(answer)
    print(another_state)
    if another_state in states:
        if another_state in curr_state_list:
            continue

        curr_state_list.append(another_state)
        print("you are correct")
        score += 1
        title_string = f"{score}/50 States Correct"

        x_value = float(data[data.state == another_state].x)
        y_value = float(data[data.state == another_state].y)

        tim.goto(x_value, y_value)
        tim.write(another_state, align="center")

    if score == 3:
        game_should_continue = False

    screen.update()

screen.exitonclick()
