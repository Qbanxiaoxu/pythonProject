# -*- coding:utf8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re

List_HouseAll  = []         #总表，所有房屋信息。二维列表。

# 链接地址解析-------------------------<链家房价>------------------------------------------------
url = "https://bj.lianjia.com/zufang/rs%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html.read().decode('utf-8'), "lxml")

# 找到【第1层标签】<div class="content__list">div class="content__list--item" data-el="listItem"-----------------------
tag1_all = soup.find_all( "div", {"class":"content__list--item","data-el":"listItem"} )
                                    # 单个或多个属性都可用字典形式,{"class":"item" ,"data-houseid":"101111735457"}
                                    # find_all返回满足条件的【所有】结果
                                    # find返回满足条件的【第1个】结果

# 遍历find_all找到的所有结果-------------------------------------------------------------------------
for tag1_InfoClear in tag1_all:
    # 【第3层标签】：获取房屋价格信息-------------------------------------------------------------------------
    tag3_price = tag1_InfoClear.find("span", class_="content__list--item-price")
    #print("价格："+tag3_price.text)

    #【第2层标签】：获取房屋名称信息<p class="content__list--item--title">-----------------------
    tag2_title=tag1_InfoClear.find("p", class_="content__list--item--title")
    #print("房屋名称："+re.sub( r'\n', "", tag2_title.text ).strip(" "))

    #【第2层标签】：获取房屋位置信息<p class="content__list--item--des">-------------------------------------------
    tag2_flood=tag1_InfoClear.find("p", class_="content__list--item--des")             #找标签flood、positionInfo都可以
    # tag2_flood=tag1_InfoClear.find("div", class_="positionInfo")    #找标签flood、positionInfo都可以
    list_houseInfo = re.split('/', re.sub( r'\n| ', "", tag2_flood.text))
    for houseInfo in list_houseInfo:
        houseInfo.strip(" ")
    #print(list_houseInfo)
    #continue
    #存入列表-------------------------------------------------------------------------
    List_HouseTemp=[]                           #临时变量，存每一个房屋信息，再追加至List_HouseAll中
    List_HouseTemp.append(eval(re.findall("\d+\.?\d*", tag3_price.text.strip(" ").replace(",", ''))[0]))  # 存价格
    List_HouseTemp.append(re.sub( r'\n', "", tag2_title.text ).strip(" "))     #存房屋名称
    List_HouseTemp.append(list_houseInfo[0])              #存房屋位置
    List_HouseTemp.append(list_houseInfo[3]) #存屋型
    List_HouseTemp.append(eval(list_houseInfo[1].replace('㎡',''))) #存面积

    # 把当前房屋信息追加至总表中
    List_HouseAll.append(List_HouseTemp)

#显示二维列表-------------------------------------------------------------------------
for house0 in List_HouseAll:
    print(house0)