#随机产生n个浮点数，范围在0~1000之间，求平均值。小数点显示2位。(n也是随机生成的，范围在5~20之间)。(文件名：模拟考试.py)
import random
n=random.randint(5,20)
list0=[]
for i in range(0,n):
    list0.append(float(random.uniform(0,1000)))
#a 存平均数
a=sum(list0)/len(list0)
print("平均值：{:.2f}".format(a))