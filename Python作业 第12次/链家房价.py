# -*- coding:utf8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re

List_HouseAll  = []         #总表，所有房屋信息。二维列表。

# 链接地址解析-------------------------<链家房价>------------------------------------------------
url = "https://bj.lianjia.com/ershoufang/rs%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html.read().decode('utf-8'), "lxml")

# 找到【第1层标签】-------------------------------------------------------------------------
tag1_all = soup.find_all( "div", {"class":"info clear"} )
                                    # 单个或多个属性都可用字典形式,{"class":"item" ,"data-houseid":"101111735457"}
                                    # find_all返回满足条件的【所有】结果
                                    # find返回满足条件的【第1个】结果
#print(data)

# 遍历find_all找到的所有结果-------------------------------------------------------------------------
for tag1_InfoClear in tag1_all:
    # 【第3层标签】：获取房屋总价信息-------------------------------------------------------------------------
    tag3_totalPrice = tag1_InfoClear.find("div", class_="totalPrice totalPrice2")
    # print("总价：", tag3_totalPrice.text)

    #【第2层标签】：获取房屋名称信息-------------------------------------------------------------------------
    tag2_title=tag1_InfoClear.find("div", class_="title")
    # print("房屋名称：", tag2_title.text)            #如果是tag2_title.text，则结果不同

    #【第2层标签】：获取房屋位置信息-------------------------------------------------------------------------
    tag2_flood=tag1_InfoClear.find("div", class_="flood")             #找标签flood、positionInfo都可以
    # tag2_flood=tag1_InfoClear.find("div", class_="positionInfo")    #找标签flood、positionInfo都可以

    #【第3层标签】-------------------------------------------------------------------------
    tag3_a=tag2_flood.find_all("a")
    # print("位置：",end="")
    str_pos=""                  #存入字符串，在后面要添加至列表
    for tag3_a1 in tag3_a:      #遍历所有有a标签
        str_pos=str_pos+tag3_a1.text
    # print(str_pos)

    #【第2层标签】：获取房屋详细信息-------------------------------------------------------------------------
    # tag2_houseInfo=tag1_InfoClear.find("div", class_="address")     #找标签address、houseInfo都可以
    tag2_houseInfo=tag1_InfoClear.find("div", class_="houseInfo")     #找标签address、houseInfo都可以

    list_houseInfo=re.split('\|',tag2_houseInfo.text)
    # print("信息(原始信息)：",tag2_houseInfo.text)
    # print("信息(列表模式)：",list_houseInfo)

    # 【第3层标签】：获取房屋单价信息-------------------------------------------------------------------------
    tag3_unitPrice = tag1_InfoClear.find("div", class_="unitPrice")
    #print("单价：", tag3_unitPrice.text)

    #存入列表-------------------------------------------------------------------------
    List_HouseTemp=[]                           #临时变量，存每一个房屋信息，再追加至List_HouseAll中
    List_HouseTemp.append(eval(tag3_totalPrice.text.strip(" ").replace('万','')))  #存总价
    List_HouseTemp.append(tag2_title.a.text)     #存房屋名称
    List_HouseTemp.append(str_pos)              #存房屋位置
    List_HouseTemp.append(list_houseInfo[0].strip(" ")) #存屋型
    List_HouseTemp.append(eval(list_houseInfo[1].replace('平米',''))) #存面积
    List_HouseTemp.append(eval(re.findall("\d+\.?\d*", tag3_unitPrice.text.strip(" ").replace(",",''))[0])) # 存单价

    # for info_house in list_houseInfo:
    #     List_HouseTemp.append( info_house.strip(" "))                           #用strip()函数去掉字符串首尾空格
    # List_HouseTemp[3]=eval( List_HouseTemp[3].replace('平米','') )            #用replace()函数去掉【平米】，用eval()把字符串智能转换成数

    # 把当前房屋信息追加至总表中
    List_HouseAll.append(List_HouseTemp)

#显示二维列表-------------------------------------------------------------------------
for house0 in List_HouseAll:
    print(house0)
List_HouseAll.sort( key=lambda x :x[ 0 ], reverse=True )#升序
print("==========按“总价”降序显示所有数据===========")
for house1 in List_HouseAll:
    print(house1)