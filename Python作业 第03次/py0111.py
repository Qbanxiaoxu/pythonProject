#用元组实现：需要逆序存储。逆序不是升降序，不是排序，也不是逆序显示。
# 原来的元组元素不要求排序，如：5、60、7、8、100，逆序后，元组中的元素依次是：100、8、7、60、5。


tup=(0,1,2,3,4,5,6,7,8,9)
lis=list(tup)
print("Before reverse order:",tup)
for i in range(int(len(tup)/2)):
    temp=lis[i]
    lis[i]=lis[len(tup)-i-1]
    lis[len(tup)-i-1]=temp
tup=tuple(lis)
print("After reverse order:",tup)
input("Press enter to end")
