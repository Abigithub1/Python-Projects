import turtle
# setting up screen,color and pen for drawing the soccer field

turtle.setup(1224,750)
turtle.bgcolor('dark green')
turtle.color('white')
turtle.pensize(12)


# Draw the outer square

turtle.penup()
turtle.goto(450,-250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.setheading(180)
turtle.forward(900)
turtle.setheading(270)
turtle.forward(500)
turtle.setheading(0)
turtle.forward(900)

# Drawing the right side goal area
turtle.goto(450,-100)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(200)
turtle.setheading(0)
turtle.forward(100)


# Drawing the left side goal area

turtle.penup()

turtle.goto(-450,-100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(100)
turtle.setheading(90)
turtle.forward(200)
turtle.setheading(180)
turtle.forward(100)

# Drawing the half line

turtle.penup()
turtle.goto(0,-250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)

# Drawing the circle middle
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.circle(100)
turtle.hideturtle()

turtle.done()
