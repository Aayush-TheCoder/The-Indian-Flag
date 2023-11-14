import turtle #importing turtle module
from turtle import * #importing all mess available in turtle module

# some initial settings
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
speed(0)
turtlesize(10)
pensize(2)
bgpic("bg.png")
penup()
goto(-150, 330)
speed(5)
pendown()

# saffron color filling
begin_fill()
fillcolor("#F4C430") # this is the hex color code of saffron

def line(forward_value, right_angle):
    forward(forward_value)
    right(right_angle)

for i in range(2):
    line(300, 90)
    line(200, 90)

end_fill()

right(90)
forward((200/3)*2)
left(90)

# white color filling
begin_fill()
fillcolor("white")
forward(300)
left(90)
forward(200/3)
left(90)
forward(300)
left(90)
forward((200/3)*2)
left(90)
end_fill()

# green color fillings
begin_fill()
fillcolor("green")
forward(300)
left(90)
forward(200/3)
left(90)
forward(300)
right(90)
end_fill()

# support for our flag
begin_fill()
fillcolor("grey")
forward((200/3)*2)
pendown()
left(90)
penup()
forward(20)
pendown()
left(90)
forward(500)
left(90)
forward(20)
left(90)
forward(500)
end_fill()

begin_fill()
fillcolor("yellow")
right(45)
circle(15)
right(45)
end_fill()

# ashoka chakra
r = (200/6)
penup()
goto(0, (330-(200/3)))
pendown()
pensize(4)
pencolor("blue")
circle(-r)

for i in range(24):
    circle(-1.5)
    circle(-r, 15)

penup()
goto(0, (330-(200/2)+5))
pendown()
pensize(1)
begin_fill()
fillcolor("blue")

for i in range(24):
    circle(-5, 15)
    left(90)
    forward(r-5)
    right(180)
    forward(r-5)
    left(90)

end_fill()

hideturtle()

done()
