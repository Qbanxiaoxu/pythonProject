import turtle
import math

turtle.setup(1024,800,0,0)       #绘画窗口的宽度、高度，左上角的X坐标、Y坐标。
turtle.speed(2)                      # 速度
turtle.pencolor("white")            #颜色。本例中，如果不要
go=-612#起点位置
def drawShape(n):
    global go#保持n边形相隔100
    if n<3:
        print("不能构成n边形")
        return
    elif n<=4:
        go+=200+100*math.sin(math.radians((n-2)*180/n)-90)
    else:
        go=go+200+100*math.sin(math.radians((n-2)*180/n)-90)+100*math.sin(math.radians((n-3)*180/(n-1)-90))
    turtle.goto(go,100)
    turtle.pencolor("black")
    turtle.pendown() # 落下画笔
    angle = 180*(n-2)/n # n边形内角和除以n得到n边形外角的值
    for i in range(n):
        turtle.forward(100)
        turtle.right(180-angle)# 求补角得到内角
    turtle.penup()

drawShape(3)
drawShape(4)
drawShape(5)
drawShape(6)
turtle.done()            #保持窗口 = turtle.done()