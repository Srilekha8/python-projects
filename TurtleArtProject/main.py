# Draw square with turtle
import turtle
from turtle import Turtle,Screen
import random as rd

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
positon = [0,90,180,270]
# turtle drawing square
hatchy = Turtle()
screen = Screen()



# for i in range(10):
#     hatchy.forward(10)
#     hatchy.penup()
#     hatchy.forward(10)
#     hatchy.pendown()


# drawing all polygons

'''def draw (sides, color):
    hatchy.pencolor(color)
    angle = int(360/sides)
    for i in range(sides):
        hatchy.forward(100)
        hatchy.left(angle)

ls = {3 :'#FF0000',4:'#9933FF',5:'#27F5EB',6: '#BE27F5',7:'#F527A3',8:'#5EF527',9:'#E7F527',10:'#35F527'}
for side in ls:
    draw(side, ls[side])'''


# random walk


turtle.colormode(255)
def gen_rand_color():
    r = rd.randint(0,255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    col = (r,g,b)
    return  col
'''
hatchy.pensize(7)
hatchy.speed("fast")
turtle.colormode(255)

for i in range(300):

    hatchy.color(gen_rand_color())
    hatchy.forward(20)
    hatchy.setheading(rd.choice(positon))'''


def circle_pattern():
    ''' draw circle in a pattern '''
    hatchy.speed("fastest")
    hatchy.color(gen_rand_color())
    deg = int(input("How much the position should be tilted : "))
    for i in range(int(360/deg)):
        hatchy.color(gen_rand_color())
        hatchy.circle(100)
        hatchy.left(deg)
        hatchy.circle(100)

circle_pattern()
screen.exitonclick()


