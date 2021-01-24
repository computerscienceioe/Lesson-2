import turtle

turtle.speed(5)

# Correct version
for i in range(13):
  turtle.forward(30)
  turtle.left(360.0/13)

turtle.penup()
turtle.forward(200)
turtle.pendown()

# Incorrect version
for i in range(13):
  turtle.forward(30)
  turtle.left(360/13)
