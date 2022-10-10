m=int(input("m="))
n=int(input("n="))
minx=min(m,n)
#print(minx)
for i in range(1,minx+1):
    if(m%i==0 and n%i==0):
        maxgy=i
print(m,"和",n,"的最大公约数为：",maxgy)
mingb=m*n/maxgy
print(m,"和",n,"的最小公倍数为：",int(mingb))
input("Press enter to end")