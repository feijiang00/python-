#urllib爬虫项目编写实战
import urllib 
import urllib.request
data=urllib.request.urlopen("http://jd.com").read().decode("utf-8","ignore")
#1.使用urllib将网站保存到一个变量中的通用方式
#现在想获取该网站的标题（通过正则表达式）：
import re
pat="<title>(.*?)</title>"
re.compile(pat,re.S).findall(data)
#2.将网页爬取到硬盘文件中
urllib.request.urlretrieve("http://www.jd.com",filename="C:\\users\\江野\\desktop\\jd.html")
#3.浏览器伪装(爬取糗事百科）
data=urllib.request.urlopen("https://www.qiushibaike.com/").read().decode("utf-8","ignore")
#这时发现，报错了没有权限，是因为我们爬虫没有伪装成浏览器
opener=urllib.request.build_opener()#建立opener对象
#查看浏览器的标识，f12里面的network选项中的网站名中的headers里找到浏览器的标识
ua=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")#构造一个元组
opener.addheaders=[ua]#添加到headers中
urllib.request.install_opener(opener)#构建全局作用域
data=urllib.request.urlopen("https://www.qiushibaike.com/").read().decode("utf-8","ignore")
print(len(data))
#4.构建用户池代理
#需要引入新的库random
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"#谷歌浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"#ie浏览器
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"#360浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"#火狐浏览器
    ]
def UA():
    opener=urllib.request.buil
    print("当前使用的UA："+str(thisua))d_opener()
    thisua=random.choice(uapools)#从浏览器池中随机选择一个
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]#将随机选出的ua放在header中
    urllib.request.install_opener(opener)
url="https://qiushibaike.com/"
for i in range(0,10):
    if i%3==0:
        UA()
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    print(len(data))
#5.项目：批量爬取糗事百科的信息，注意：实现翻页功能
import random
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",#谷歌浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",#ie浏览器
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",#360浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"#火狐浏览器
    ]
def UA():
    opener=urllib.request.build_opener()
    thisua=random.choice(uapools)#从浏览器池中随机选择一个
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]#将随机选出的ua放在header中
    urllib.request.install_opener(opener)
    # print("当前使用的UA："+str(thisua))
url="https://qiushibaike.com/"
# for i in range(0,10):
#     if i%3==0:
#         UA()
#     data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
#     print(len(data))
#https://www.qiushibaike.com/hot/page/2/   糗事百科第二页
#我这里想把他们写进去一个文件中
f=open("糗事百科.txt",'a+',encoding='utf-8')
for i in range(0,3):
    UA()
    thisurl="https://www.qiushibaike.com/hot/page/"+str(i+1)
    data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    rst=re.compile(pat,re.S).findall(data)
    for j in range(0,len(rst)):
        print(rst[j])
        print("------------------------------------------")
        f.write(' '.join(rst))

