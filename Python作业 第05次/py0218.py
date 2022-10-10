#3、有一字符串，有字母、数字、空格、其它字符。
# 1) 统计单词个数。可以使用split()函数。可以用WORD的统计作为参考，
# 2) 统计每个字母出现次数，未出现的字母次数为0。大小写为同一字母。使用字典来统计。
# 3) 统计出现的字母。大小写为同一字母。使用集合来统计。
# The Mate X supports next-generation 5G networks and will cost 2,299 euros ($2,606) when released in the summer. 共16个单词。

# 1) 统计单词个数。可以使用split()函数。可以用WORD的统计作为参考，
wnum=0 #统计单词数
str="The Mate X supports next-generation 5G networks and will cost 2,299 euros ($2,606) when released in the summer"
str1=str.split()
#print(str1)
for s in str1:
    if s.isalnum():
        #print(s,"*")
        wnum+=1
    if '-' in s:
        wnum+=1
print("单词个数：",wnum)

# 2) 统计每个字母出现次数，未出现的字母次数为0。大小写为同一字母。使用字典来统计。
dict_letter={}
str2=str.lower()#转化为小写字母
#print(str2)
Letters1="abcdefghijklmnopqrstuvwxyz"
for key in Letters1:
    dict_letter[key]=str2.count(key)
print("每个字母出现次数：")
print(dict_letter)

# 3) 统计出现的字母。大小写为同一字母。使用集合来统计。
str3=""#字符串转化为字母
for s in str:
    if s.isalpha():
        str3+=s
str31=str3.lower()#转化为小写
set_str=set(str31)
print("出现的字母：")
print(set_str)

input("Press enter to end")