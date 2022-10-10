# CrowTaobaoPrice.py
import requests
import re


def getHTMLText(url):
    try:
        kv = {'authority': 's.taobao.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 't=05735a81c0d039ff6f0d63208fc99a33; cna=nCIfGwx02TQCAbbweQZg1+9s; xlly_s=1; _samesite_flag_=true; cookie2=1368c0111d3a87c6b89f0a7e958ce954; _tb_token_=f98b36bd55b73; sgcookie=E100%2FUSWv4m2At8wNZ9zMUqGPVx7KpqITx6wEA7VYV60D0mRuP3IsC5qdqAICBPQn9L%2BBONBW8FeE8Y2dtRMAesUBx6PhoVbj4VC9qD3yFJB4TxsuhkE49KKWKPkL0GeNfI%2B; unb=2209066292300; uc1=pas=0&cookie21=V32FPkk%2FgPzW&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie14=UoeyDbhpV6KGpw%3D%3D&existShop=false&cookie15=URm48syIIVrSKA%3D%3D; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UUphw2VT4Z2cXDamtA%3D%3D&vt3=F8dCv4ZvFikvdvHeLus%3D&nk2=F5RGNee1Qn2Zf4k%3D; csg=67f845e9; lgc=tb339134831; cancelledSubSites=empty; cookie17=UUphw2VT4Z2cXDamtA%3D%3D; dnk=tb339134831; skt=717fb75f141b6ded; existShop=MTY2MzA3NjQ2MA%3D%3D; uc4=id4=0%40U2grGNp6fPzuP%2BAx3UM1T6OH0YBjhzGy&nk4=0%40FY4NAASMy%2FiVeQehyzmj1W5%2BGvyjiw%3D%3D; tracknick=tb339134831; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=10d; _nk_=tb339134831; cookie1=VAMVKZ5ORLFhcxT5q4WcYX%2BquEdAke4Uy0iHTnFM4P0%3D; enc=Bn7u%2Bc06Xm89fZmCWHrvfYlBu89lXnkLacjWdtCUPS%2FxjKkjbqF5IQ5azChfgvHxzTNKEQUziRrTTsvPlGfW43rY2I4%2BhCSV2vYP2IBNClg%3D; JSESSIONID=CD0CE14A2C8A5C23C6C6950738AE8DBC; isg=BDg4VxuAr7smksM_qs7H7JQpCebKoZwrBlMZpXKphHMmjdh3GrFsu06vQYU9xlQD; l=eB_oBrOHTEQrPXyyBOfanurza77OSIRYYuPzaNbMiOCPOm1B5jzOW6oAXh86C3GVh6LMR35Wn1oBBeYBqQAonxv92j-la_kmn; tfstk=coyPBAXdQTBz9SPagxMU3U0Ek5ZRwvPQsgmKZNex4Xp4p0fDGenDW9yudn8nZ',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        r = requests.get(url, timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()