import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
r=requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
print(r.status_code)
print(r.encoding)
r.encoding=r.apparent_encoding
print(r.text)
print(r.request.headers)
kv={'user-agent':'Mozilla/5.0'}
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
r1=requests.get(url,headers=kv)#修改headers模拟浏览器访问
print(r1.status_code)