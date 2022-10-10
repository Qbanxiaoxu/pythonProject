#用lambda函数判断一个数是否素数，显示格式如：7是素数、8不是素数。
n=int(input("n="))


is_prime= lambda x,y:False if x%y==0 else True
ss=True
for i in range(2,n):
    ss=is_prime(n,i)
    if ss==False:
        break
if ss==False:
    print(n, "不是素数")
else:
    print(n, "是素数")
sum0=lambda x:str(x)+"是" if not [y for y in range(2,x) if x%y==0] else str(x)+"不是"
print(sum0(9)+"素数")