str=input("字符串：")
Letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers="0123456789"
Spaces=" "
Lnum=0
Nnum=0
Snum=0
Onum=0
for s in str:
    if s in Letters:
        Lnum+=1
    elif s in Numbers:
        Nnum+=1
    elif s in Spaces:
        Snum+=1
    else:
        Onum+=1
print("字母的个数：",Lnum,"\n数字的个数：",Nnum,"\n空格的个数：",Snum,"\n其它字符的个数：",Onum)
