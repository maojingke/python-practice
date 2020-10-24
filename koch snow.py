import turtle as t
def koch(size,n):
             if n==0:
                          t.fd(size)
             else:
                          for angle in [0,60,-120,60]:
                                       t.left(angle)
                                       koch(size/3,n-1)
def main():
             t.pensize(2)
             koch(200,3)
             t.hideturtle()
t.setup(800,400)
t.penup()
t.fd(-150)
t.left(90)
t.fd(100)
t.right(90)
t.pendown()
for i in range(3):
             main()
             t.right(120)

             
