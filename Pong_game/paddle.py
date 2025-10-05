from time import sleep
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos, clr):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color(clr)
        self.penup()
        self.goto(pos)

    def up(self):
        ycr = self.ycor()+20
        self.goto(self.xcor(),ycr)

    def down(self):
        ycr = self.ycor() - 20
        self.goto(self.xcor(), ycr)