from turtle import *
from random import *
def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()
def birds(birdSize, birdColor):
    color(birdColor)
    pendown()
    for side in range(2):
        left(144)
        forward(birdSize)
    penup()
def drawPlanet(planetSize, planetColor):
    color(planetColor)
    pendown()
    begin_fill()
    for side in range(360):
        left(1)
        forward(planetSize)
    right(90)
    for side in range(360):
        left(1)
        forward(planetSize)
    left(180)    
    for side in range(360):
        left(1)
        forward(planetSize)            
    end_fill()
    penup()
speed(11)        
bgcolor("#ADD8E6")
for bird in range(30):
    moveToRandomLocation()
    birds(5, "Black")

for clouds in range(10):
    moveToRandomLocation()
    drawPlanet(1, "White")
hideturtle()
done()