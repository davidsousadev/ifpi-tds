from turtle import *

shape ("turtle")
speed(11)
color("Blue")
pensize(7)
lados = 360
angulo = 360 / lados
for count in range(lados):
    forward(1)
    right(angulo)
    
done()