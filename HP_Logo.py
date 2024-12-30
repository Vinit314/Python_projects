# This code we will make logo of Deadly Hollows...
# from Harry Potter Franchise using Turtle module.
# The logo consist of a straight line, a circle and a triangle

# all the number shown are taken by trail and error method
import turtle

t = turtle.Turtle()

# Next four line is to get the position of cursor
# at the point where all three geometrical figures meet
t.penup()
t.right(90)
t.backward(200)
t.pendown()

# this will make straight line
t.forward(400)

# this will make the circle
t.left(90)
t.circle(133.2)

# this will make the triangle
t.forward(231)

for i in range(2):
    t.left(120)
    t.forward(462)

t.left(120)
t.forward(231)

turtle.done()
