import re

import requests

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "访问异常"
from bs4 import BeautifulSoup
demo=getHTMLText("http://search.people.cn/s?keyword=感动")
soup=BeautifulSoup(demo,"html.parser")
ulst=[]
all_url = soup.find_all('a')
for ul in all_url:
    try:
        href=ul.attrs['href']
        ulst.append(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href)[0])
    except:
        continue

shi=getHTMLText("https://search.sohu.com/?keyword=感动")
print(shi)
# print(all_url)
# print(div_0)
# print(url_l)