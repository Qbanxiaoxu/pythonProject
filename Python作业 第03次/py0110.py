#用列表实现：有8个数，从大到小排序。
list=[12,1,3,5,2,4,24,22]
print("Before sorting:",list)
for i in range(len(list)):
    for j in range(len(list)-i-1):
        if list[j]<list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("After sorting:",list)
input("Press enter to end")