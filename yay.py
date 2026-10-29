import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(700,400)
polygon = turtle.Turtle()

num_sides = 12
side_length = 70
angle = 360.0 /num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.down()