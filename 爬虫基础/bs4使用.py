import requests
import re
r=requests.get('http://www.so.com/s?q=计算机')
# print(r.status_code)
demo=r.text
# print(demo)
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
a = soup.find_all('a',href=True)
lists=[]
for i in a:
    try:
        href = i.attrs['href']
        lists.append(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href)[0])
        # print(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href)[0])
    except:
        continue
print(lists)