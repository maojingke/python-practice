#mangshev1.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.bk(250)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("pink")
turtle.right(40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,40)
turtle.fd(40)
turtle.circle(15,180)
turtle.fd(25)
turtle.done()
