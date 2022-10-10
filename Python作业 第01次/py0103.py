grade=int(input("请输入成绩："))
if grade>=90 and grade<=100:
    print(grade,"分对应等级：A")
elif grade>=80:
    print(grade,"分对应等级：B")
elif grade>=70:
    print(grade, "分对应等级：C")
elif grade>=60:
    print(grade, "分对应等级：D")
elif grade>=0:
    print(grade, "分对应等级：E")
input("Press enter to end")