from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y_value = random.randint(-220, 200)
            new_x_value = random.randint(320, 1000)
            new_car.goto(new_x_value, new_y_value)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(self.car_speed)
            car.speed(1)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
