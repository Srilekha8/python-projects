from turtle import Turtle as turt, Screen as srn

trt = turt()
sc = srn()

def move_for():
    trt.forward(10)

def move_back():
    #trt.left(180)
    trt.backward(15)

def move_cwise():
    trt.right(10)

def move_anti_cwise():
    trt.left(20)

def clear_screen():
    trt.clear()
    trt.penup()
    trt.home()
    trt.seth(0)
    trt.pendown()

sc.onkey(key="f",fun=move_for)
sc.onkey(key="b",fun=move_back)
sc.onkey(key="c",fun=move_cwise)
sc.onkey(key="a",fun=move_anti_cwise)
sc.onkey(clear_screen, "w")
sc.listen()
sc.exitonclick()
