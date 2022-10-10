#2、编写非递归函数求前n项“斐波那契数列”。(文件名：py0221a.py)
def fab(n):
    l0 = [0]*n
    if n==1:
        l0[0] = 1
    elif n==2:
        l0[0] = 1
        l0[1] = 1
    elif n>=3:
        l0[0]=1
        l0[1]=1
        for i in range(3,n+1):
            l0[i-1]=l0[i-2]+l0[i-3]
    return l0

n=int(input("n="))
print(fab(n))
