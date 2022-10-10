# -*- coding:utf8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re

# 链接地址解析-------------------------------------------------------------------------
url = "http://www.gaosan.com/gaokao/43980.html"

HttpResponseObject = urllib.request.urlopen(url)
strHtml=HttpResponseObject.read()
soup = BeautifulSoup(strHtml.decode('utf-8'), "lxml")

# 找到第一层标签------------------------<table width="580px" align="center">------------------------------------------------
data = soup.find_all("table", {"width":"580px", "align":"center"} )
                                    # find_all返回满足条件的【所有】结果
                                    # find返回满足条件的【第1个】结果
list_all=[]
for data1 in data:      #【"table", {"width":"580px", "align":"center"}】的结果可能有多个，遍历所有【此类table】
    for tr in data1:        #tr标签
        i = 0
        list0=[]
        for td in tr:       #td标签
            i = i + 1
            if (i > 1):
                str1=td.text
                list1=re.split("\n|\t",str1)
                for str2 in list1:
                    if str2!="":
                        list0.append(str2)
list1=[]
for i in range(0, len(list0)):
    list1.append( list0[ i ] )
    if i%9==7:
        list1[7]=float(list1[7])        #第7列是社会影响
    if i%9==8:
        list_all.append(list1)          #得到二维列表
        list1=[]

list_all.sort( key=lambda x :x[ 7 ], reverse=False )#升序
print(list_all)
print("==========按“社会影响”、“升序”排序显示所有数据===========")
for i in range(len(list_all)):
    print(list_all[i])

