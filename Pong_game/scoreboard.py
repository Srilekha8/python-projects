from time import sleep
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()


    def l_point(self):
        self.lscore+=1
        self.update_score()

    def r_point(self):
        self.rscore+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(250, 300)
        self.write(f"{self.lscore}", align='center', font=("Arial", 20, "normal"))
        self.goto(-250, 300)
        self.write(f"{self.rscore}", align='center', font=("Arial", 20, "normal"))
