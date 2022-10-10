#1、	有文件“分数.txt”，求平均分。文件中的部分分数的格式有误，不允许修改文件，用“异常处理”计算。

import re

f = open("分数.txt", "r")
str=re.split('\n|,',f.read())
sum=0
for i in str:
    try:
        int(i)
    except:
        pass
    else:
        sum+=int(i)
        #print(int(i))
print("平均值：",float(sum/len(str)))

f.close()