#统计所有字母的出现频度,依据频度从高到低，显示前5个字母及其频度，同时把结果写入文件“hamlet_字母频度.txt”。

import re
def Read01():
    f = open("hamlet.txt", "r", encoding='utf-8')
    str = f.read()
    # str = re.split('\n|,', f.read())
    # print(str)
    dict_letter = {}
    str2 = str.lower()  # 转化为小写字母
    # print(str2)
    Letters1 = "abcdefghijklmnopqrstuvwxyz"
    for key in Letters1:
        dict_letter[key] = str2.count(key)
    #print(dict_letter)
    dict_letter1=dict(sorted(dict_letter.items(), key=lambda x: x[1], reverse=True))
    #print(dict_letter1)
    dict_letter2={}
    for i, (k, v) in enumerate(dict_letter1.items()):
        dict_letter2[k]=v
        if i == 4:
         break
    print(dict_letter2)
    f1=open("hamlet_字母频度.txt","a+")
    for k,v in dict_letter2.items():
        # f1.write(k)
        # f1.write(' %d \n' % v)
        f1.write("{0:<5}{1:<}\n".format(k,v))

#统计所有单词的出现频度,依据频度从高到低，显示前10个单词及其频度，同时把结果写入文件“hamlet_单词频度.txt”。
def Read02():
    fp = open("hamlet.txt", "r",encoding='utf-8')
    txt = fp.read()
    new_article = re.sub(r'[^A-Za-z]', ' ', txt)
    #print(new_article)
    words = new_article.split()
    #print(words)
    word_counts = {}
    for word in words:
        if word.lower() in word_counts:
            word_counts[word.lower()] = word_counts[word.lower()] + 1
        else:
            word_counts[word.lower()] = 1
    word_counts1 = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    #print(word_counts1)
    dict_letter2 = {}
    for i, (k, v) in enumerate(word_counts1.items()):
        dict_letter2[k] = v
        if i == 9:
            break
    print(dict_letter2)
    f2 = open("hamlet_单词频度.txt", "a+")
    for k, v in dict_letter2.items():
        # f2.write(k)
        # f2.write(' %d \n' % v)
        f2.write("{0:<10}{1}\n".format(k,v))

Read01()
Read02()