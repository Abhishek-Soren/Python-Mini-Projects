from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_clockwise():
    tim.right(10)


def turn_anti_clockwise():
    tim.left(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(move_forward, "d")
screen.onkey(move_backward, "a")
screen.onkey(turn_clockwise, "w")
screen.onkey(turn_anti_clockwise, "s")
screen.onkey(clear_screen, "c")

screen.exitonclick()
