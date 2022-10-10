# （1）求1+2+3+4+..+m。
# （2）判断m是否是素数。
# （3）判断m是否是完数，若是完数则输出其所有的因子

def sum(m):
    if m==0:
        return 0
    else:
        return m+sum(m-1)
# print(sum(4))
def isPrime(m):
    for i in range(2,m):
        if m%i==0:
            return False
    return True
# print(isPrime(3))
def compNum(m):
    sum = 0
    for i in range(1, m):
        if m % i == 0:
            sum = sum + i;
    if m == sum:
        # print(m, end="\t")
        # for j in range(1, m):
        #     if m % j == 0:
                # print(j, end=" ")
        # print()
        return True
    return False

# 从键盘输入n，调用上述三个函数完成功能。
# 1)1+2+..+n的结果。
# 2)n以内所有素数，以字典形式显示，如：{2:"是"，3："是"，4："否"，5："是"，6："否"}。
# n以内所有完数。以字典形式显示，如：{6：{1，2，3},…… }。
n=int(input("n="))
print("1+2+...+",n,"=",sum(n))
dictPrime={}
for i in range(2,n+1):
    if isPrime(i):
        dictPrime[i]="是"
    else:
        dictPrime[i]="否"
print(dictPrime)
dictComp={}
setComp=set()
for i in range(1,n+1):
    if compNum(i):
        for j in range(1, i):
            if i % j == 0:
                setComp.add(j)
        dictComp[i]=setComp
print(dictComp)