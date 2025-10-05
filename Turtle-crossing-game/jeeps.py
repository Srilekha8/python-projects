from turtle import Turtle
import random as rd


JEEP_POS =[(300,-200),(300,-100),(300,0),(300,100),(300,150),(300,200)]
COLORS = ['green',"yellow","red","blue","purple"]
MOVE_DISTANCE = 5
INCREMENT_SPEED = 10


class Jeep():

    def __init__(self):
        self.cars = []
        self.speed = 0

    def creat_jeeps(self):
        choice = rd.randint(1,6)
        if choice==1:
            jeep = Turtle()
            jeep.shape("square")
            jeep.shapesize(stretch_wid=1, stretch_len=3)
            jeep.color(rd.choice(COLORS))
            jeep.penup()
            jeep.setheading(180)
            jeep.goto(300, rd.randint(-250,250))
            self.cars.append(jeep)

    def move_jeeps(self):
        for car in self.cars:
            car.forward(MOVE_DISTANCE+self.speed)

