#4、双素数是指一对差值为2的素数。例如：3和5就是一对双素数，5和7是一对双素数。编写函数找出所有小于等于1000的双素数，并以字典的形式存储。
s=[] #存所有素数
for i in range(2,1001):
    isSushu=True
    for j in range(2,i):
        if i%j==0:
            isSushu=False
    if isSushu==True:
        s.append(i)
#print(s)
dict={}
for i in range(1,len(s)):
    if s[i]-s[i-1]==2:
        dict[s[i-1]]=s[i]
print(dict)
input("Press enter to end")