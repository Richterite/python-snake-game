from turtle import Turtle


with open("highscore_counter.txt") as data:
    highscore_data = int(data.read())

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = highscore_data
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.get_score()

    def game_over(self):
        self.goto(0,0)
        if self.score > self.highscore:
            with open("highscore_counter.txt", mode="w") as new:
                new.write(f"{self.score - 1}")
        self.write("GAME OVER", align=ALIGNMENT, move=False, font=FONT)

    def get_score(self):
        self.clear()
        self.write(f"score = {self.score} HighScore = {self.highscore}", align=ALIGNMENT, move=False, font=FONT)
        self.score += 1



