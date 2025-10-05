from turtle import Screen
import time
from tortoiseMowa import Tortoise
from jeeps import Jeep
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Toy-Toy-Tortoi")
screen.tracer(0)

tort = Tortoise()
jeep = Jeep()
scorebrd = Scoreboard()
screen.listen()
screen.onkey(tort.up,"Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    if tort.ycor()>290:
        jeep.speed+=2
        tort.goto(0,-280)
        scorebrd.show_level()
        print("speed Increased")

    jeep.creat_jeeps()
    jeep.move_jeeps()
    for car in jeep.cars:
        if (abs(car.xcor() - tort.xcor()) < 25) and (abs(car.ycor() - tort.ycor()) < 20):
            scorebrd.game_over()
            game_on=False

screen.exitonclick()