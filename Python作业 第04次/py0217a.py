#删除一个列表[1,7,8,8,2,1,55,6]里面的重复元素，得[1,7,8,2,55,6]。用多种方法实现：
#a. 使用集合来去掉重复元素，不要求保持原来的存储顺序。(文件名：py0217a.py)
elist=[1,7,8,8,2,1,55,6]
thisset=set(elist)
elist=list(thisset)
print(elist)