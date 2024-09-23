from turtle import *

#draw petals
def petal(radius,number):
    for i in range(number): 
        begin_fill()
        circle(radius,60)
        lt(120)
        circle(radius,60)
        end_fill()
        rt(180)

#draw hexagon pattern
def hex(rad):
    for i in range(25):
        begin_fill()
        circle(rad,360,6)
        end_fill()
        rt(14.4)

#draw circle
def circles(rad,colors):
    up()
    goto(0,-rad)
    color(colors)
    down()
    begin_fill()
    circle(rad)
    end_fill()

speed(0)
bgcolor("black")
title("code a pookalam")
color("brown")
hex(105)
color("white")
hex(90)

home()
circles(165,"khaki")
circles(130,"gold")
circles(100,"orange")

color("firebrick")
up()
home()
fd(105)
down()
for i in range(50):
    rt(30)
    petal(20,1)
    rt(120)
    up()
    circle(-105,360/50)
    down()
    lt(90)

up()
home()
down()
color("blue")
petal(98,6)
rt(30)
color("red")
petal(98,6)
color("gold")
petal(45,6)

dot(15,"red")
dot(5,"yellow")
up()
home()
goto(-65,142)
down()
color("orange")

for j in range(200):
    fd(130)
    rt(49)
ht()
mainloop()