#flower.py
import turtle as t
t.pensize(6)
t.pencolor("blue")
for i in range (6):
             t.circle(60,180)
             t.right(120)
t.left(60)
t.circle(120,360)
t.left(30)
for i in range(6):
             t.fd(120)
             t.left(60)
t.left(30)
for i in range(3):
             t.fd(120*pow(3,0.5))
             t.left(120)
t.right(30)
t.fd(120)
t.left(90)
for i in range(3):
             t.fd(120*pow(3,0.5))
             t.left(120)
t.down()
