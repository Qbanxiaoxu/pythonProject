#http://www.baidu.com/s?wd=keyword
#http://www.so.com/s?q=keyword
import requests
keyword='计算机'
try:
    kv={'wd':keyword}
    r=requests.get('http://www.baidu.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(r.text)
except:
    print("产生异常")