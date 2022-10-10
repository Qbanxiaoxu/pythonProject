name=''
list_stu=[]
while name!='-':
    list_temp=[]
    name=input("请输入学生姓名:")
    if name!='-':
        list_temp.append(name)
        try:
            math_grade=int(input("请输入学生数学成绩:"))
        except:
            math_grade=int(input("输入有误请重新输入学生数学成绩:"))
            list_temp.append(math_grade)
        else:
            list_temp.append(math_grade)
        try:
            chinese_grade=int(input("请输入学生语文成绩:"))
        except:
            chinese_grade=int(input("输入有误！请重新输入学生语文成绩:"))
            list_temp.append(chinese_grade)
        else:
            list_temp.append(chinese_grade)
        list_temp.append(math_grade+chinese_grade)
        list_stu.append(list_temp)
#①	按总分从大到小的顺序，显示所有学生的所有信息及平均分。
dict_stu={}
info_stu=[]
list_stu.sort( key=lambda x :x[3], reverse=True )
for stu in list_stu:
    dict_stu_grade={}
    dict_stu_grade['姓名']=stu[0]
    dict_stu_grade['数学成绩']=stu[1]
    dict_stu_grade['语文成绩'] = stu[2]
    dict_stu_grade['总分']=stu[3]
    info_stu.append(dict_stu_grade)
#print(info_stu)
shuxue=0
yuwen=0
for s in list_stu:
    shuxue=shuxue+s[1]
    yuwen=yuwen+s[2]
dict_fen={}
dict_fen['数学总平均分']=shuxue/(len(list_stu))
dict_fen['语文总平均分'] =yuwen/(len(list_stu))
info_stu.append(dict_fen)
print(info_stu)
print("=================按照总分降序=============================")
for i in info_stu:
    print(i)