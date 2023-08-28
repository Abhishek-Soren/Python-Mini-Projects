from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.display()

    def update_l_score(self):
        self.l_score += 1

    def update_r_score(self):
        self.r_score += 1

    def display(self):
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))
        self.clear()
