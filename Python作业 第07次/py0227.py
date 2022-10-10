# （1）求出m和n两个数之间所有“明7暗7”数，即数字中有7或能整除7，如37，63.
# （2）分别求出m! 和 n!
# （3）求m和n的最大公约数和最小公倍数。
# （4）求出m和n两个数之间的所有回文数。

def is_seven(m,n):
    print(m, "和", n, "两个数之间所有“明7暗7”数：",end="")
    for i in range(min(m,n),max(m,n)+1):
        if i%7==0:
            print(i,end=" ")
        else:
            numstr=str(i)
            if "7" in numstr:
                print(i,end=" ")
    print()
def factorial(m,n):
    def factorial_mn(x):
        if x==0:
            return 1
        else:
            return x*factorial_mn(x-1)
    print(m,"的阶乘：",factorial_mn(m),"\t",n,"的阶乘：",factorial_mn(n))
def gygb(m,n):
    minx = min(m, n)
    for i in range(1, minx + 1):
        if (m % i == 0 and n % i == 0):
            maxgy = i
    mingb = m * n / maxgy
    print(m, "和", n, "的最大公约数为：{0}   最小公倍数为：{1}".format(maxgy,int(mingb)))

def huiwen(m,n):
    print(m, "和", n,"两个数之间的所有回文数：",end="")
    for i in range(min(m,n),max(m,n)+1):
        stri=str(i)
        istr=stri[::-1]
        if stri==istr:
            print(i,end=" ")
    print()

m=int(input("m="))
n=int(input("n="))
is_seven(m,n)
factorial(m,n)
gygb(m,n)
huiwen(m,n)