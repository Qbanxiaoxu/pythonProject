import requests
import os
url='https://webstatic.mihoyo.com/upload/contentweb/2022/07/04/1ae0d0aaad9ee9b55652ea7ec67f0465_624394286022075834.png'
root="E://Python/自然语言处理//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb')as f:
            # print(r.content)
            f.write(r.content)
            f.close()
            print('图片保存成功')
    else:
        print('图片已经存在')
except:
    print('爬取失败')