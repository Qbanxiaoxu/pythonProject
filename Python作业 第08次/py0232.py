#从键盘输入圈数，连续画4条可视为一圈。

import turtle
def drawGraphic(n):
    turtle.setup(1000, 800, 500, 400)  # 绘画窗口的宽度、高度，左上角的X坐标、Y坐标。
    turtle.speed(3)  # 速度
    turtle.pencolor("white")  # 颜色。本例中，如果不要
    turtle.goto(0, 0)  # 从点【-200,100】开始。默认从【0,0】开始，就中心点。

    side_len=10
    turtle.pencolor("black")  # 颜色
    for i in range(n):
        turtle.seth(0)
        turtle.pendown()
        turtle.forward(side_len)
        side_len+=10
        turtle.seth(90)
        turtle.forward(side_len)
        side_len+=10
        turtle.seth(180)
        turtle.forward(side_len)
        side_len+=10
        turtle.seth(270)
        turtle.forward(side_len)
        side_len+=10

n=int(input("请输入圈数："))
drawGraphic(n)
turtle.done()            #保持窗口 = turtle.done()

