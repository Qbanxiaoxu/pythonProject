a=input("输入一个数字：")
a=float(a)
b=input("输入一个数字：")
b=float(b)
c=input("输入一个数字：")
c=float(c)
print("排列前：",a,b,c)
if a<b:
    temp=a
    a=b
    b=temp
if a<c:
    temp=a
    a=c
    c=temp
if b<c:
    temp=b
    b=c
    c=temp

print("排列后：",a,b,c)
input("Press enter to end")