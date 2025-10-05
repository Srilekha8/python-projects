from turtle import Turtle

STARTING_POS = (0,-280)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 20

class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.left(90)


    def up(self):

        self.forward(MOVE_DISTANCE)

