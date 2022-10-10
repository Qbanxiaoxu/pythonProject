#不能用任何python内部函数(除了len外)，自己写算法求解。在循环中只能用负数下标实现。
s=[9,7,8,3,2,1,55,6]
elements=len(s)
maximum=0
minimum=1.7976931348623157e+308
sum=0
average=0
for i in range(-len(s),0):
    sum=sum+s[i]
    if s[i]>=maximum:
        maximum=s[i]
    if s[i]<=minimum:
        minimum=s[i]
average=float(sum/elements)

print("列表元素个数：",elements,"\n列表最大值：",maximum,"\n列表最小值",minimum,"\n列表和：",sum,"\n列表平均值：",average)