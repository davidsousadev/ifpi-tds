from turtle import *

def drawPlanet(planetSize, planetColor):
    color(planetColor)
    pendown()
    begin_fill()
    for side in range(360):
        left(1)
        forward(planetSize)
        
    end_fill()
    penup()

bgcolor("Black")

drawPlanet(5, "Blue")
forward(100)

hideturtle()
done()