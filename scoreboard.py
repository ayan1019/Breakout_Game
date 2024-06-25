from turtle import Turtle

try:
    score = int(open("score.txt", "r").read())

except FileNotFoundError:
    score = open("score.txt", "w").write(str(0))

except ValueError:
    score = 0

FONT = ('arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highscore = score
        self.goto(x=-380, y=260)
        self.lives = lives
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore} \ "
                   f" | Lives: {self.lives}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset_score(self):
        self.clear()
        self.score = 0
        self.update_score()
        open("score.txt", "w").write(str(self.highscore))
