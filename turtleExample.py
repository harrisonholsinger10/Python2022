import turtle

# Harrison Holsinger
# Turtle Olympic Logo and Sports Example

s = turtle.getscreen()
# Speed of drawing
turtle.speed(10)
# Hide Cursor
turtle.hideturtle()
# Background color
turtle.bgcolor("grey")

turtle.pensize(5)

# Purple circle
turtle.pencolor('purple')
turtle.penup()
turtle.setposition(-60, -60)
turtle.pendown()
turtle.circle(50)

# Blue circle
turtle.pencolor('blue')
turtle.penup()
turtle.setposition(60, -60)
turtle.pendown()
turtle.circle(50)

# Red circle
turtle.pencolor('red')
turtle.penup()
turtle.setposition(120, 0)
turtle.pendown()
turtle.circle(50)

# Yellow circle
turtle.pencolor('yellow')
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# Green circle
turtle.pencolor('green')
turtle.setposition(-120, 0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# Title
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(200)

# If pen color is not white, make it white
if turtle.pencolor() != "white":
    turtle.pencolor('white')
    turtle.write("Harrison's Masterpiece", font = 16)
    
# Background color
if turtle.bgcolor() == 'grey':
    turtle.bgcolor('black')

# Baseball
turtle.left(90)
turtle.forward(500)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25, 430)
turtle.end_fill()

# Baseball seam left
turtle.pencolor("red")
turtle.left(85)
turtle.forward(15)
turtle.left(65)
turtle.forward(25)
turtle.penup()

# Baseball seam right
turtle.left(190)
turtle.forward(50)
turtle.left(180)
turtle.pendown()
turtle.forward(15)
turtle.right(65)
turtle.forward(30)
turtle.penup()

# Background color
if turtle.bgcolor() == 'black':
    turtle.bgcolor('grey')

# Tennis Ball
turtle.right(165)
turtle.forward(40)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.color("green yellow", "green yellow")
turtle.begin_fill()
turtle.circle(25, 430)
turtle.end_fill()
turtle.penup()

# Background color
if turtle.bgcolor() == 'grey':
    turtle.bgcolor('black')

# Softball
turtle.right(140)
turtle.forward(40)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.color("yellow", "yellow")
turtle.begin_fill()
turtle.circle(25, 430)
turtle.end_fill()
turtle.penup()

# Background color
if turtle.bgcolor() == 'black':
    turtle.bgcolor('grey')

# Soccer ball
turtle.right(168)
turtle.forward(40)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(25, 430)
turtle.end_fill()
turtle.penup()

# Background color
if turtle.bgcolor() == 'grey':
    turtle.bgcolor('black')

# Golf ball
turtle.right(155)
turtle.forward(40)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.color("white", "white")
turtle.begin_fill()
turtle.circle(10, 430)
turtle.end_fill()
turtle.penup()

turtle.done()

