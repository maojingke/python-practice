import turtle as t
import time
def drawgap():
             t.penup()
             t.fd(5)
def drawline(draw):
             drawgap()
             t.pendown() if draw else t.penup()
             t.fd(40)
             drawgap()
             t.right(90)
def drawnum(digit):
             drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
             drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
             drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
             drawline(True) if digit in [0,2,6,8] else drawline(False)
             t.left(90)
             drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
             drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
             drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
             t.left(180)
             t.penup()
             t.fd(20)
def drawdate(time):
             for c in time:
                          t.pencolor('red')
                          if c=='-':
                                       t.write('年',font=('Arial',28,"normal"))
                          elif c=='=':
                                       t.write('月',font=('Arial',28,"normal"))
                                       t.penup()
                                       t.fd(40)
                          elif c=='+':
                                       t.write('日',font=('Arial',28,"normal"))
                          else:
                                       drawnum(eval(c))
             #将获取时间中的"-","=","+"符号分别换成年月日
def main():
             t.penup()
             t.fd(-300)
             t.pensize(5)
             drawdate(time.strftime("%Y-%m=%d+",time.gmtime()))
             #获取系统当前时间戳
             t.hideturtle()
             #隐藏海龟画笔
             t.down()
main()

