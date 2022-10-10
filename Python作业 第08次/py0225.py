#已知成绩文件“分数.txt”，读取所有分数，求最大值、最小值、平均值。
f = open("分数.txt", "r")
scores=f.read().splitlines()
f.close()
print(scores)
maxscore=0
for i in scores:
    if int(i)>maxscore:
        maxscore=int(i)
print("最大值：",maxscore)
minscore=int(scores[0])
for i in scores:
    if int(i)<minscore:
        minscore=int(i)
print("最大值：",minscore)
sum=0
for i in scores:
    sum+=int(i)
print("平均值：",float(sum/len(scores)))