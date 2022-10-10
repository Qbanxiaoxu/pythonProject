str=input("字符串：")
Lnum=0
Nnum=0
Snum=0
Onum=0
#isspace()isdigit()isalpha()
for s in str:
    if s.isalpha():
        Lnum+=1
    elif s.isdigit():
        Nnum+=1
    elif s.isspace():
        Snum+=1
    else:
        Onum+=1
print("字母的个数：",Lnum,"\n数字的个数：",Nnum,"\n空格的个数：",Snum,"\n其它字符的个数：",Onum)