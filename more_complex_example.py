import turtle

turtle.shape("turtle")
turtle.speed(40)


sides = 6

for x in range(100):
  turtle.forward(x * 3 / sides + x)
  turtle.left(360 / sides + 10)
  turtle.width(x * sides / 200)