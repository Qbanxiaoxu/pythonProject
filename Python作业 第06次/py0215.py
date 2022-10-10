#1、有一字符串，把其中的所有单词的首字母变成大写，其它字母变小写。

str0="The Mate X supports next-generation 5G networks and will cost 2,299 euros ($2,606) when released in the summer"
str1=str0.lower()
print(str0)
list0=str1.split()
list1=[]
#print(list0)
for s in list0:
    list1.append(s.capitalize())
#print(list1)
str2=' '.join(list1)
print(str2)