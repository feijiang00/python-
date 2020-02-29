#目标站点：taobao.com/需求数据：商品名，商品价格，评论数/要求：自动翻页并输出
#技术选择 urllib
#首先判断分析网址：发现商品名称和商品的价格可以正则获取，但是评论数需要抓包
#评论数在抓包中很可能出现的是，网页源代码，json数据，js数据
#最后发现淘宝商品的评论数就是藏在一个js网页中，可以通过商品id获取
#cookiejar






#案例：
#使用的技术urllib，掌握的要领，没有什么新学的还是老套路，这里总结一波吧：
#首先分析淘宝要爬取的任何一个关键词的商品的url页面，直接找到商品id，通过构造商品id进入商品的详情页，根据自己需要想拿什么就拿什么
#有些数据比如评论数是需要通过抓包获取的，大概就这些了。我觉得难点是对全局的把握，如何直接写出来，最好的办法就是多练练吧
import urllib.request
import random
import re
#用户代理池
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",#谷歌浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",#ie浏览器
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",#360浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",#火狐浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
#每次调用ua函数，都会更换用户代理浏览器
def UA():
    opener=urllib.request.build_opener()
    thisua=random.choice(uapools)#从浏览器池中随机选择一个
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]#将随机选出的ua放在header中
    urllib.request.install_opener(opener)#构造为全局
    print("当前使用的UA："+str(thisua))
keyname="女装"
key=urllib.request.quote(keyname)#将中文名字编码放进url中
for i in range(1,10) :
    print("--------------第"+str(i)+"页商品------------------")
    if i % 3 == 0:
        UA()
    url="https://s.taobao.com/search?q="+key+"&s="+str((i-1)*44)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='"nid":"(.*?)"'
    idlist=re.compile(pat).findall(data)
    for j in range(0,len(idlist)):
        thisid=idlist[j]
        thisurl="https://item.taobao.com/item.html?id="+str(thisid)
        itemdata=urllib.request.urlopen(thisurl).read().decode("gbk","ignore")
        titlepat='<h3 class="tb-main-title" data-title="(.*?)"'
        detailpat='<p class="tb-subtitle"(.*?)</p>'
        pricepat='<em class="tb-rmb-num">(.*?)</em>'
        title=re.compile(titlepat,re.S).findall(itemdata)
        if(len(title)>0):
            title=title[0]
        else:
            continue
        detail=re.compile(detailpat,re.S).findall(itemdata)
        if(len(detail)>0):
            detail=detail[0]
        else:
            detail=0
        price=re.compile(pricepat,re.S).findall(itemdata)
        if(len(price)>0):
            price=price[0]
        else:
            price=0
        print("--------------------------------")
        print("商品名:"+str(title))
        print("描述信息:"+str(detail))
        print("价格:"+str(price))
