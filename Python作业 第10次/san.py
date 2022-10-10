import jieba
file1=open("三国演义.txt","r",encoding="utf-8")
txt=file1.read()
file1.close()
#精准拆分
words=jieba.lcut(txt)
#print(words)
#统计人名及出现次数
counts={}
for word in words:
    if len(word)>1:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]=counts[word]+1
#初步统计结果，前20位
print("==========初步统计结果，前20位===========")
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
#排除非人名单词
excludes={"将军","却说","二人","不可","不能","如此","商议","如何","天下","不敢","今日","于是","东吴","大喜","荆州","军士","左右","军马","引兵","次日"}
for word in excludes:
    if word in counts:
        del(counts[word])
#刘备
LiuBei={"玄德","玄德曰","刘皇叔","刘使君"}
for word in LiuBei:
    if word in counts:
        counts["刘备"]=counts["刘备"]+counts[word]
        del(counts[word])
#曹操
LiuBei={"丞相"}
for word in LiuBei:
    if word in counts:
        counts["曹操"]=counts["曹操"]+counts[word]
        del(counts[word])
#诸葛亮
LiuBei={"孔明曰","孔明"}
for word in LiuBei:
    if word in counts:
        counts["诸葛亮"]=counts["诸葛亮"]+counts[word]
        del(counts[word])
#关羽
LiuBei={"云长","关公"}
for word in LiuBei:
    if word in counts:
        counts["关羽"]=counts["关羽"]+counts[word]
        del(counts[word])

print("==========合并后统计结果===========")
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))