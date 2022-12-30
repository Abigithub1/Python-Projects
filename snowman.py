from turtle import *

speed(0)
setup(800,700)

#background

penup()
goto(0,-320)
pendown()
color("cyan")
bgcolor('black')
begin_fill()
circle(320)
end_fill()

# Bottom of the body

penup()
goto(0,-280)
pendown()
color("white")
begin_fill()
circle(110)
end_fill()

# middle body

penup()
goto(0,-110)
pendown()
color("white")
begin_fill()
circle(90)
end_fill()

#Head of the body

penup()
goto(0,20)
pendown()
color("white")
begin_fill()
circle(70)
end_fill()


# Define function

def bcircle():
    color("black")
    begin_fill()
    circle(10)
    end_fill()

# Eyes
x=-20
for i in range(2):
    penup()
    goto(x,110)
    pendown()
    bcircle()
    x= x+40
# Buttons
y = 0
for i in range(5):
    penup()
    goto(0,y)
    pendown()
    bcircle()
    y-=55

# Mouth 
penup()
goto(0,70)
pendown()
color("black")
begin_fill()
circle(10)
end_fill()

penup()
goto(0,75)
pendown()
color("white")
begin_fill()
circle(10)
end_fill()
hideturtle()

# Right arm
penup()
goto(75,0)
pendown()
color("black")
begin_fill()
left(40)
for i in range (2):
    forward(75)
    left(90)
    forward(7)
    left(90)
end_fill()

# Right Finger 1
penup()
goto(115,38)
pendown()
begin_fill()
left(40)
for i in range(2):
    forward(25)
    left(90)
    forward(5)
    left(90)

end_fill()

# Right finger 2
begin_fill()
right(90)
for i in range(2):
    forward(25)
    left(90)
    forward(5)
    left(90)

end_fill()

# Left Arm
penup()
goto(-135,50)
pendown()
color("black")
begin_fill()
right(10)
for i in range (2):
    forward(75)
    right(90)
    forward(7)
    right(90)
end_fill()

#left finger1
penup()
goto(-112,58)
pendown()
color("black")
begin_fill()
right(40)
for i in range (2):
    forward(25)
    right(90)
    forward(5)
    right(90)
end_fill()

#left finger 2
begin_fill()
right(100)
penup()
goto(-108,31)
pendown()
for i in range(2):
    forward(25)
    right(90)
    forward(5)
    right(90)
end_fill()

# hat

penup()
goto(50,230)
pendown()
color("black")
begin_fill()
right(10)
forward(100)
right(90)
forward(10)
right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(45)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(45)
left(90)
forward(20)
right(90)
end_fill()

mainloop()
