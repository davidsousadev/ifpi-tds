from turtle import *

shape ("turtle")
speed(11)
color("Blue")
pensize(7)
lados = 5
angulo = 360 / lados
for count in range(lados):
    forward(100)
    left(angulo)
done()