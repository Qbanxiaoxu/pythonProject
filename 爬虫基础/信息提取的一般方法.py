import requests
r=requests.get('http://python123.io/ws/demo.html')
print(r.status_code)
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body.contents))
print(soup.body.contents[3])
print('==========')
for link in soup.find_all('a'):#.descendants
    print(link.get('href'))