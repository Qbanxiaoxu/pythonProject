import requests
url="http://cs.ucla.edu/~rosen/161/notes/alphabeta.html"
def getHTMLText(url):

    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        print(r.status_code)
        print(r.request.headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text)
    except:
        return "产生异常"
getHTMLText(url)