m=int(input("m="))
n=int(input("n="))
sum=0
for i in range(m,n+1):#包括n
    if i%2==0:
        sum=i+sum
print(m,"～",n,"之间所有偶数之和为：",sum)
input("Press enter to end")