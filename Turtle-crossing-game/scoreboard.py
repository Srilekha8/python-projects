from turtle import Turtle

FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.show_level()

    def show_level(self):
        self.level+=1
        self.clear()
        self.write(f'Level : {self.level}',align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align='center', font=FONT )