# -*- coding:utf8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
import pypinyin

# 链接地址解析-------------------------------------------------------------------------
url = "https://www.cnur.com/rankings/188.html"

HttpResponseObject = urllib.request.urlopen(url)
# print(HttpResponseObject)
strHtml=HttpResponseObject.read()
soup = BeautifulSoup(strHtml.decode('utf-8'), "lxml")

# 找第一层标签---------<table width="580px" align="center">------------------------------
data = soup.find_all("table", {"cellpadding":"0" ,"cellspacing":"0", "width":"545" ,"data-sort":"sortDisabled" ,"align":"center"} )
                                    # find_all返回满足条件的【所有】结果
                                    # find返回满足条件的【第1个】结果

list_all=[]             #此列表通过【list_all.append(一维列表)】得到二维列表
for data1 in data:      #【"table", {"width":"580px", "align":"center"}】的结果可能有多个，遍历所有【此类table】

    # 找第二层标签：tr标签，表格的行----------------------------------------------------
    div_tr_all=data1.find_all("tr")
    for i in range(2,len(div_tr_all)):          #遍历tr。range(2,XXX)：0,1行是标题行，跳过
        div_tr=div_tr_all[i]
        list0=[]                                #存储一行中所有字符串
        #print(div_tr)
        # 找第三层标签：td标签，所有单元格--------------------------------------------------
        div_td_all = div_tr.find_all( "td" )
        for div_td in div_td_all:               #遍历td
            str1=div_td.text
            #print("#{",str1,"}#")
            # str1=str1.replace("\n","")      #去掉\n、\t。不用这两行，结果如何？此行不能用split，为什么？
            # str1=str1.replace("\t","")
            str1=re.sub( r'\t|\n', "", str1 )   #re库的替换
            list0.append( str1 )
        list_all.append(list0)
#排序--------------------------------------------------------------------
list_all.sort(key=lambda x : pypinyin.pinyin(x[1], style=pypinyin.Style.TONE3), reverse=True)
print(list_all)
print("==========按“学校名称”、“升序”排序显示所有数据==========")
for i in range(len(list_all)):
    print(list_all[i])