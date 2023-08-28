from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"SCORE : {self.score}", move=False, align=ALIGNMENT, font=FONT)
