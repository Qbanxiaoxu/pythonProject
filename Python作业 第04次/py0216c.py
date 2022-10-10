s=[9,7,8,3,2,1,55,6]
elements=0
maximum=0
minimum=1.7976931348623157e+308
sum=0
average=0
for ls in s:
    elements+=1
    sum=sum+ls
    if ls>=maximum:
        maximum=ls
    if ls<=minimum:
        minimum=ls
average=float(sum/elements)

print("列表元素个数：",elements,"\n列表最大值：",maximum,"\n列表最小值",minimum,"\n列表和：",sum,"\n列表平均值：",average)