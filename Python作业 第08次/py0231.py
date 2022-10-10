import turtle

turtle.setup(1000,800,500,400)       #绘画窗口的宽度、高度，左上角的X坐标、Y坐标。
turtle.speed(3)                      # 速度
turtle.pencolor("white")            #颜色。本例中，如果不要
turtle.goto(-200,100)                #从点【-200,100】开始。默认从【0,0】开始，就中心点。

def drawCuboid(color0):
    turtle.seth(0)  # 0度
    turtle.pencolor(color0)  # 颜色

    turtle.pendown()
    turtle.forward(400)
    turtle.seth(-90)
    turtle.forward(200)
    turtle.seth(-180)
    turtle.forward(400)
    turtle.seth(-270)
    turtle.forward(200)

    turtle.seth(45)
    turtle.forward(160)
    turtle.seth(0)
    turtle.forward(400)
    turtle.seth(-90)
    turtle.forward(200)

    turtle.seth(-180)
    for i in range(0, 20):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
    turtle.seth(-270)
    for i in range(0, 10):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)

    turtle.goto(-200,-100)
    turtle.seth(45)
    for i in range(0, 8):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
    turtle.goto(200, -100)
    turtle.pendown()
    turtle.forward(160)
    turtle.penup()
    turtle.goto(200, 100)
    turtle.pendown()
    turtle.forward(160)

def eraseCuboid(color1):
    turtle.penup()
    turtle.goto(-200,100)
    drawCuboid(color1)

drawCuboid("red")
eraseCuboid("white")
turtle.done()            #保持窗口 = turtle.done()

