from turtle import *

shape ("turtle")
speed(11)
color("Red")
pensize(6)
lados = 36
angulo = 3600 / lados
for count in range(lados):
    forward(100)
    right(angulo)
    
done()