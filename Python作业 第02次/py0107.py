n=int(input("n="))
factorial=1
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        factorial=factorial*j
    sum=sum+factorial
    factorial=1
for i in range(1,n):
    print(i,"!",end="+",sep='')
print(n,"!","=",sum,sep='')
input("\nPress enter to end")