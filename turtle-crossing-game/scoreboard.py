from turtle import Turtle, Screen

FONT = ("Courier", 24, "bold")
def draw_line():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(-300, 260)
    line.pendown()
    line.goto(300, 260)
    Screen().update()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def display(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.display()
