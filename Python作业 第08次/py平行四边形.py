import turtle

turtle.setup(1024,400,100,100)       #绘画窗口的宽度、高度，左上角的X坐标、Y坐标。
turtle.speed(2)                      # 速度
turtle.pencolor("white")            #颜色。本例中，如果不要
turtle.goto(-200,100)                #从点【-200,100】开始。默认从【0,0】开始，就中心点。

def drawShape(color1):
    turtle.seth(0)                   # 0度
    turtle.pencolor(color1)          # 颜色

    #虚线
    for i in range(0, 10):
        turtle.pendown()             # 画笔抬起
        turtle.forward(10)           # 画线10点
        turtle.penup()               # 画笔抬起
        turtle.forward(10)           # 画线10点

    turtle.seth(-45)                 # -45度
    #实线
    for i in range(0, 10):
        turtle.pendown()
        turtle.forward(20)

    turtle.seth(180)                 # 180度
    #虚线
    for i in range(0, 10):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)

    turtle.seth(90 + 45)  # 180度
    #实线
    for i in range(0, 10):
        turtle.pendown()
        turtle.forward(20)

drawShape("red")
turtle.done()            #保持窗口 = turtle.done()

