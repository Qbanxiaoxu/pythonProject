#删除一个列表[1,7,8,8,2,1,55,6]里面的重复元素，得[1,7,8,2,55,6]。用多种方法实现：
#b. 必须保持原来的存储顺序。(文件名：py0217b.py)
elist=[1,7,8,8,2,1,55,6]
elist1=[]
for i in elist:
    if i not in elist1:
        elist1.append(i)
elist=elist1
print(elist)