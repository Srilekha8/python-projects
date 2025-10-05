import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("blue")
screen.title("Pong")
screen.tracer(0)

left_pad = Paddle((-380,0),"yellow")
right_pad = Paddle((380,0),"red")
ball = Ball()
sboard = Scoreboard()


screen.listen()
screen.onkey(left_pad.up,"u")
screen.onkey(left_pad.down,"d")
screen.onkey(right_pad.up,"Up")
screen.onkey(right_pad.down,"Down")

game_on = True
while(game_on):
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect Collision
    if ball.ycor() >390 or ball.ycor()<-390:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(left_pad)<50 and ball.xcor()<-380 or ball.distance(right_pad)<50 and ball.xcor()>380:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset()
        sboard.l_point()

    if ball.xcor()<-380:
        ball.reset()
        sboard.r_point()
screen.exitonclick()