from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150

### Write your code below:
def makeTriangle():
    for i in range(3):
        pendown()
        forward(50)
        left(120)
        penup()

def makeSquare():
    for i in range(4):
        pendown()
        forward(100)
        left(90)
        penup()

#makeTriangle()
#makeSquare()

def makeShape():
    sides = int(input('Enter number of sides:'))
    length = int(input('Enter length:'))
    for i in range(sides):
        pendown()
        forward(length)
        angles=360/sides
        left(angles)
        penup()

#makeShape()
while True:
    makeShape()

# Close window on click.
exitonclick()
