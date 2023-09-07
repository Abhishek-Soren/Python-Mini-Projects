from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


def draw_line():
    tommy = Turtle()
    tommy.hideturtle()
    tommy.penup()
    tommy.goto(-300, 270)
    tommy.pendown()
    tommy.forward(600)


food = Food()
score = Score()

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor("turquoise")
screen.title("My Snake Game")

draw_line()

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

move_forward = True

while move_forward:
    time.sleep(0.1)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 260:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
