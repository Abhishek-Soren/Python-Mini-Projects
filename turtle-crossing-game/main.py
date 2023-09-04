import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, draw_line
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")

car_manager = CarManager()

scoreboard = Scoreboard()

draw_line()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.at_finish_line():
        player.refresh()
        car_manager.increase_car_speed()
        scoreboard.increase_score()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
