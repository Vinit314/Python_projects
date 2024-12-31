# This code draws a logo of Deadly Hollows
# from Harry Potter Franchise
import turtle
import math

# Below given x is the side of the equilateral triangle.
# All other dimensions are calculated by this parameter.
x = 400  # This parameter is changeable

dr = turtle.Turtle()
y = x/2
# z is denoted for Apex height
# z = x * math.sin(math.degrees(60))
z = (math.sqrt(3) * x) / 2

# This is to get to the starting position
dr.right(90)
dr.penup()
dr.backward(100)
dr.pendown()

# This is to draw a straight line
dr.forward(z)
dr.right(90)

# This is draw the equilateral triangle
dr.forward(y)
dr.right(120)
dr.forward(x)  # you can use loop here
dr.right(120)
dr.forward(x)
dr.right(120)
dr.forward(y)

# The turtle drawing circle turning left
# to get the position we turned it to 180 degrees
dr.right(180)

# this is get the dimensions for the circle
# r is denoted for radius
# r = y/math.tan(math.degrees(60))
r = (x * math.sqrt(3)) / 6

# This is draw the circle
dr.circle(r)

turtle.done()
# Thank you
