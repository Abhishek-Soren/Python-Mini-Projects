from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.refresh()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


