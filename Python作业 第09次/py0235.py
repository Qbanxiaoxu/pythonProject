# 随机生成10个0～10(含0和10)的整数，分别组成集合A和集合B，输出A和B的内容、长度、最大值、最小值以及它们的并集、交集和差集。A、B的长度随机，控制在3~7之间。
import random
A=set()
B=set()
lengthA=random.randint(3,7)
x=random.randint(0,10)
for i in range(0,lengthA):
    while x in A:
        x=random.randint(0,10)
    A.add(x)
lengthB=random.randint(3,7)
for i in range(lengthB):
    while x in B:
        x=random.randint(0,10)
    B.add(x)
print("A:",A,"B:",B)
print("LengthA:",lengthA,"LengthB:",lengthB)
print("minA:",min(list(A)),"minB:",min(list(B)))
print("maxA:",max(list(A)),"maxB:",max(list(B)))
print("并集:",A|B,"交集:",A&B,"差集:",A-B)