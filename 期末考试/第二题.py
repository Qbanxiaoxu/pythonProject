list1=[2,4,6,8,10,12,12]
list2=[3,3,5,6,7,8,9,11,11,12]
print("原列表:")
print(list1)
print(list2)
def deletere(l1,l2):
    global list1
    global list2
    list_temp1=[]
    list_temp2 = []
    for m in l1:
        if m not in l2 :
            list_temp1.append(m)
    for n in l2:
        if n not in l1:
            list_temp2.append(n)
    list1=list_temp1
    list2=list_temp2

print("删除重复元素后:")
deletere(list1,list2)
print(list1)
print(list2)