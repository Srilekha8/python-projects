from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    sb = Scoreboard()
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_snake(pos)

    def add_snake(self, position):
        trt = Turtle("circle")
        trt.color("white")
        trt.penup()
        # since the width and height of the square is 20px
        trt.goto(position)
        self.segments.append(trt)

    def move_snake(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        if self.head.xcor()>280  or self.head.xcor()<-290 or self.head.ycor()<-280 or self.head.ycor()>280:
            return False
        else:
            self.head.forward(MOVE_DISTANCE)
            return True

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow_the_snake(self):
        self.add_snake(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]