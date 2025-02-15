import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,500)
polygon=turtle.Turtle()
side=6
length=50
angle=360.0/side
for i in range (side):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()
