from turtle import *
from math import sqrt

wn = Screen()
t = Turtle()

t.pensize(3)
t.penup()
t.goto(-600, 0) 
t.pendown()
t.color("green")
t.fillcolor("red")
t.begin_fill()

# Rajzolunk egy téglalapot és kitöltjük
width = 100
height = 200

t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.right(90)
t.forward(height)


t.end_fill()

HszA = 200
HszB = 200
HszC = sqrt(HszA**2 + HszB**2)

t.penup() 


# Homokóra alakzat

t.fillcolor("aqua")


t.right(90)  
t.forward(600)  

t.pendown ()   
t.begin_fill()
t.forward(HszA)  
t.right(135)
t.forward(HszC)
t.right(135+90)
t.forward(HszA)
t.left(135)
t.forward(HszC)

t.end_fill()

t.penup () 
t.right(135)  
t.forward(700)  

# Derékszög

t.pendown ()
t.fillcolor("blue")
t.begin_fill()
t.forward(HszA)
t.right(135)
t.forward(HszC)
t.right(135)
t.forward(HszB)

t.end_fill()

wn.mainloop()
