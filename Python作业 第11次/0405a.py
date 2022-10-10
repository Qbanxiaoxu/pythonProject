#mysql 创建表 插入数据
import pymysql
#数据库连接
db=pymysql.connect(host="localhost",
                   user="root",
                   password="xxp666666",
                   db="exercises",
                   port=3306)
#获取游标
cur=db.cursor()
#创建表
try:
    cur.execute("create table stu(id int PRIMARY KEY ,name varchar(20),class varchar(30),age varchar(10))")
except:
    print("错误，该表可能已存在，不能创建！")
#插入记录
sql="insert into stu(id,name,class,age) values(%s,%s,%s,%s)"
values=(20040112,"徐兴盼","20计算机科学与技术",18)
try:
    cur.execute(sql,values)
except:
    print("错误，该表可能已存在，不能创建！")
else:
    db.commit()
#读取记录
cur.execute("select *from stu")
results=cur.fetchall()
for item in results:
    print(item)
cur.close()#关闭游标
db.close()#关闭连接