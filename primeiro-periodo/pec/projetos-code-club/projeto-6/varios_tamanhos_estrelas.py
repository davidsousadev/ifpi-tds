from turtle import *

def drawStar(starSize):
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawStar(50)
forward(100)
drawStar(30)
left(120)
forward(150)
drawStar(70)

hideturtle()
done()