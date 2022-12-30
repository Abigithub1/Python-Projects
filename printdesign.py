import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)



def square(x):
    t.forward(x)
    for i in range(3):
        t.left(90)
        t.fd(x)
    t.left(90)

def pattern():
    for i in range(130):
        square(145)
        t.left(177)

s.bgcolor("black")
t.color('cyan')

pattern()

t.penup()
t.goto(-4,0)
t.pendown()
t.color("red")
t.write("Thank You",font = ("verdana",20,'bold'))
t.hideturtle()

turtle.done()
