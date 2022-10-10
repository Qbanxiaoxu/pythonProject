import requests
r=requests.get('http://python123.io/ws/demo.html')
print(r.status_code)
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
# print(soup.title)
# print(type(soup.title))
# print(soup.a)
# print(soup.a.string)
# print(soup.a.parent.name)
# print(soup.a.attrs)#标签属性
print(soup.find_all('a'))