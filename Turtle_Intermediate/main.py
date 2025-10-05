from turtle import Turtle, Screen
import  random as rd

colors =["red","yellow","blue","purple","orange","green","indigo","violet"]
screen = Screen()
is_race_on =False
screen.setup(width=700, height=600)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race? Enter a color")
x=-300
y=-150
all_turtles = []

for i in colors:
    new_trt = Turtle(shape="turtle")
    new_trt.color(i)
    new_trt.penup()
    new_trt.goto(x=x, y=y)
    y+=50
    all_turtles.append(new_trt)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:
        if turt.xcor() >330:
            is_race_on = False
            winner_color = turt.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner")
        else:
            turt.forward(rd.randint(0,10))

screen.exitonclick()