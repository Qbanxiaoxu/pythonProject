#3、列表s=[9,7,8,3,2,1,55,6]，求元素个数、最大值、最小值、和、平均值。elements, maximum, minimum, sum, average
s=[9,7,8,3,2,1,55,6]
elements=len(s)
maximum=max(s)
minimum=min(s)
sum=sum(s)
average=float(sum/elements)
print("列表元素个数：",elements,"\n列表最大值：",maximum,"\n列表最小值",minimum,"\n列表和：",sum,"\n列表平均值：",average)