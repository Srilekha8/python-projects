from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import  Scoreboard

from snake import Snake



screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("orange")
screen.tracer(0)


snake = Snake()
food = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    if  not snake.move_snake():
        sb.reset()
        snake.reset_snake()

    if snake.head.distance(food)<15:
        snake.grow_the_snake()
        food.refresh()
        sb.update_score()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) <10:
            sb.reset()
            snake.reset_snake()




























screen.exitonclick()