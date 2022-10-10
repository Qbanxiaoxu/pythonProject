# 已知学生名单文件“名单 未排序.TXT”，把所有学生读入字典，按学号排序好后，重新写入文件“名单 已排序.TXT”。(文件名：py0226.py)
# 素材：
# 1) “名单 未排序.TXT”是原始数据。
# 2) “名单 已排序.TXT”是参考结果。
# 打开一个文件
f = open("名单 未排序.TXT", "r")
stu_list={}
while True:
    str = f.readline()
    if str:		#不为空
        #print(str.split(","))
        temp_list=str.split(",")
        stu_list[temp_list[0]]=temp_list[1]
        #print(str)
    else:
        break
stu_list=dict(sorted(stu_list.items()))
print(stu_list)
fd = open("名单 已排序.TXT",'a+')
for key,value in stu_list.items():
    #print(type(key),type(value))
    fd.write(key+","+value)

# 关闭打开的文件
f.close()
