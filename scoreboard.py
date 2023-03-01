from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 320)
        self.score = 0
        self.color("white")
        self.updatescoreboard()
        self.hideturtle()

    def updatescoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.updatescoreboard()

    def you_lose(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER MAN!! WE'RE ALL FUCKED!!\n "
                   f"YOU FUCKING LOST!! TRY AGAIN!!", align="center", font=FONT)

