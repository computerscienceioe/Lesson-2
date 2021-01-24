import turtle

turtle.speed(10)

turtle.color("#FF6400")
turtle.begin_fill()
for i in range(30):
  turtle.forward(400/30)
  turtle.left(360.0/30)
turtle.end_fill()

turtle.penup()
turtle.setposition(150,0)
turtle.pendown()

turtle.color(0,255,255)
turtle.begin_fill()
for i in range(11):
  turtle.forward(400/11)
  turtle.left(360.0/11)
turtle.end_fill()

turtle.penup()
turtle.setposition(300,0)
turtle.pendown()

turtle.color(255,0,255)
turtle.begin_fill()
for i in range(7):
  turtle.forward(400/7)
  turtle.left(360.0/7)
turtle.end_fill()
