from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        Screen().tracer(0)
        self.penup()
        self.shape("square")
        self.setposition(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        Screen().update()

    def move_up(self):
        new_y = self.ycor() + 20
        if self.ycor() <= 240:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if self.ycor() >= -240:
            self.goto(self.xcor(), new_y)
