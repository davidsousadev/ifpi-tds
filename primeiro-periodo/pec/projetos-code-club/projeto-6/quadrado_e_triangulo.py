from turtle import *

def triangle():
    pendown()
    begin_fill()
    for side in range(3):
        left(120)
        forward(150)
    end_fill()
    penup()

def square():
    pendown()
    begin_fill()
    for side in range(4):
        right(90)
        forward(100)
    end_fill()
    penup()

def drawStar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

square()
forward(200)
triangle()
forward(100)
drawStar()
hideturtle()
done()