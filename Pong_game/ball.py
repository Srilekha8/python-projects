from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.goto(0,80)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        xcr = self.xcor()+self.x_move
        ycr = self.ycor()+self.y_move
        self.goto(xcr,ycr)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,80)
        self.bounce_x()
