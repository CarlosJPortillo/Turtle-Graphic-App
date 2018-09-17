import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
teddy = turtle.Turtle()
tess.color("blue")
teddy.color("red")
tess.shape("turtle")
teddy.shape("turtle")

print(list(range(5, 60, 2)))
tess.up()
teddy.up()
for size in range(5, 60, 2):
    teddy.stamp()
    tess.stamp()
    tess.forward(size)
    teddy.forward(size)
    tess.right(13)
    teddy.left(13)
tess.shape("square")
teddy.shape("circle")

wn.exitonclick()
