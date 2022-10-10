list1=[5,10,20,24,80]
print("插入前：",list1)
n=int(input("n="))
list2=[0]*(len(list1)+1)
for i in range(len(list1)):
    if n>list1[i]:
        list2[i]=list1[i]
    else:
        list2[i]=n
        break
for i in range(i,len(list1)):
    list2[i+1]=list1[i]
list1=list2
print("插入后：",list1)
input("Press enter to end")