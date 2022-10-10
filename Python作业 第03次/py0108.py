#1、水仙花数：是一个3位数，其各位数字立方和等于该数本身。例如：153=13+53+33。

import math

print("三位数的水仙花数：")
for i in range(100,1000):
    hundredsDigit=i//100
    tensDigit=(i%100)//10
    onesDigit=(i%100)%10
    if i==pow(hundredsDigit,3)+pow(tensDigit,3)+pow(onesDigit,3):
        print(i,end=" ")
input("\nPress enter to end")