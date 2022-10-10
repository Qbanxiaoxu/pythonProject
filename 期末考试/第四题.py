import random
def password_grade():
    p0='abcdefghijklmnopqrstuvwxyz'
    p1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p2='0123456789'
    p3=' !@#%^&*'
    passwordSource = p0+p1+p2+p3
    length=random.randint(2,10)
    password_temp=random.sample(passwordSource, length)
    password="".join(password_temp)
    print('生成的密码：'+password)
    grade_list=[0,0,0,0,0]
    for g in password_temp:
        if len(password_temp) >= 8:
            grade_list[4]=1
        if g in p0:
            grade_list[0]=1
        if g in p1:
            grade_list[1]=1
        if g in p2:
            grade_list[2] = 1
        if g in p3:
            grade_list[3] = 1
    #print(grade_list)
    return sum(grade_list)

print("强度级别:",password_grade())