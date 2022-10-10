#完数：它的因子之和恰好等于该数本身，如：6=1+2+3。求1000以内的所有完数。

#import math

print("1000以内的完数：")
for i in range(1,1000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j;
    if i==sum:
        print(i,end="\t")
        for j in range(1,i):
            if i%j==0:
                print(j,end=" ")
        print()
input("Press enter to end")