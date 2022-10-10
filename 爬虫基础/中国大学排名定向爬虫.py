import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#过滤非标签
            tds=tr('td')
            ulist.append([tds[0].string.strip(),tds[1].a.string,tds[1].p.string,tds[2].get_text().strip(),tds[3].get_text().strip(),tds[4].string.strip(),tds[5].string.strip()])
def printUnivList(ulist,num):
    tplt= "{0:^10}\t{1:{7}^10}\t{2:^10}\t{3:{7}^10}\t{4:^10}\t{5:^10}\t{6:^10}"
    print(tplt.format('排名','学校','双一流','位置','类型','总分','办学层次',chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],u[5],u[6],chr(12288)))
def main():
    unifo=[]
    url='https://www.shanghairanking.cn/rankings/bcur/2022'
    html=getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,20)
main()