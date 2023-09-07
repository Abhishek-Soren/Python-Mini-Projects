from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0

        with open("high_score.txt", mode="r") as file:
            curr_high_score = file.read()

        self.high_score = int(curr_high_score)
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
