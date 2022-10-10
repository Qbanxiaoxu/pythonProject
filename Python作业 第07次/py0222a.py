#创建一个列表来表示学生的信息：学号、姓名、性别、出生日期、日龄。
# 1、只用datetime包中提供的函数实现计算日龄。(datetime包的使用参见教材132页)
# 2、提示：日期是可以相减的。
import datetime
student=['20040112','李华','男']
year=int(input("出生年份："))
month=int(input("出生月份："))
day=int(input("出生号数："))
birthday=datetime.date(year,month,day)
#print(type(birthday))
student.append(str(birthday))
age_in_days=(datetime.date.today()-birthday).days
student.append(age_in_days)
print(student)
