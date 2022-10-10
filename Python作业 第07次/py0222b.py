#1、编写函数实现计算日龄的功能，把列表作为参数。不能用Python内部函数。
#2、编写lambda函数实现闰年功能，返回值为【True：闰年，False：非闰年】。可使用条件运算符。
import datetime

is_leap_year=lambda year:True if year%400==0 else (True if year%4==0 else False)

def age_in_days(stulist):
    agedays=0
    days_on_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nowdatenum=str(datetime.date.today()).split("-")
    birthnum=stulist[3].split("-")
    #print(birthnum)
    #print(nowdatenum)
    for y in range(int(birthnum[0])+1,int(nowdatenum[0])):
        if is_leap_year(y):
            agedays+=366
        else:
            agedays+=365
    for m1 in range(int(birthnum[1])+1,13):
        agedays+=days_on_month[m1]
    for m2 in range(1,int(nowdatenum[1])):
        agedays+=days_on_month[m2]
    agedays+=days_on_month[int(birthnum[1])]-int(birthnum[2])
    agedays+=int(nowdatenum[2])
    return agedays

student=['20040112','李华','男','2002-11-05']
print("日龄：",age_in_days(student))
student.append(age_in_days(student))
print(student)