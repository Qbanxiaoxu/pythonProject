#2、有多个正数，个数不确定，从键盘输入所有数，存入列表，并按从小到大排序，求出平均值。排序可自写算法，也可用内置函数。
clist=[]
while True:
    enter=input("请输入正数：")
    if enter=='#' :
        break
    else:
        clist.append(int(enter))
#print(clist)
print("原列表：",clist)
clist.sort(reverse = False)
print("从小到大排序：",clist)
s=sum(clist)
average=s/len(clist)
print("平均值：",average)








