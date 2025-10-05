import colorgram
import turtle as tt
import random as rd

colors = colorgram.extract('painting.jpg', 15)
rgb_lst = []
x = -250
y = -250

for col in colors:
    r = col.rgb.r
    g = col.rgb.g
    b = col.rgb.b
    grp = (r,g,b)
    rgb_lst.append(grp)

tur = tt.Turtle()
screen = tt.Screen()
tt.colormode(255)
print(f"x cord and y cor is {tur.xcor()} , {tur.ycor()}")
tur.penup()
tur.speed("fastest")
tur.hideturtle()

for i in range(10):
    tur.setx(x)
    tur.sety(y)
    print(f"x cord and y cor is {tur.xcor()} , {tur.ycor()}")
    for j in range(10):
        tur.pendown()
        tur.dot(20, rd.choice(rgb_lst))
        tur.penup()
        tur.forward(50)
    y=y+50
screen.exitonclick()

