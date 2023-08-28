from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Score

ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
score = Score()

screen = Screen()

screen.title("Pong Game")
screen.setup(height=600, width=800)
screen.bgcolor("light coral")
screen.tracer(0)
screen.listen()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


should_continue = True

while should_continue:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        score.update_l_score()
        ball.refresh()

    if ball.xcor() < -380:
        score.update_r_score()
        ball.refresh()


    score.display()

screen.exitonclick()
