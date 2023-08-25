from turtle import Turtle, Screen
import random

continue_race = None
win_turtle_color = ""
screen = Screen()
tommy = Turtle()

def finish_line():
    # draw finish line
    tommy.hideturtle()
    tommy.penup()
    tommy.goto(x=225, y=200)
    tommy.pendown()
    tommy.right(90)
    tommy.forward(400)


screen.setup(width=500, height=500)

user_input = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Guess the color : ").lower()


colors = ["purple", "indigo", "blue", "green", "yellow", "orange", "red"]

t_list = []
y_axis = -120

finish_line()

for i in range(7):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_axis)
    y_axis += 40
    t_list.append(tim)

if user_input:
    continue_race = True

while continue_race:

    for i in range(7):
        distance = random.randint(0, 10)

        t_list[i].forward(distance)

        position = t_list[i].xcor()

        if position >= 230:
            continue_race = False
            win_turtle_color = colors[i]
            break

if user_input == win_turtle_color:
    print("Congratulations. Your bet has won the race.")
    print(f" Turtle-{win_turtle_color} won the race.")
else:
    print(f"Oh NO! You Lose. Your bet Turtle-{user_input}")
    print(f" Turtle-{win_turtle_color} won the race.")

screen.exitonclick()
