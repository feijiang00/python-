#这里我使用火狐浏览器爬取
import urllib
import urllib.request
import random
import re
#用户代理池
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",#谷歌浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",#ie浏览器
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",#360浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"#火狐浏览器
    ]
#每次调用ua函数，都会更换用户代理浏览器
def UA():
    opener=urllib.request.build_opener()
    thisua=random.choice(uapools)#从浏览器池中随机选择一个
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]#将随机选出的ua放在header中
    urllib.request.install_opener(opener)
    # print("当前使用的UA："+str(thisua))
cid="6360714875505375425"
#在第一个url中发现第二个url 的关键字藏在last中，那么ok
for i in range(0,5):
    url = "https://video.coral.qq.com/varticle/2369303658/comment/v2?callback=_varticle2369303658commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + str(cid) + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132"
    # 每爬取三次更换一个浏览器，模拟人类操作
    if i%3 == 0:
        UA()
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat1='"content":"(.*?)"' #正则表达式的外引号写单符号
    pat2='"last":"(.*?)"'#这是获取下一个url的cid的正则
    comment=re.compile(pat1,re.S).findall(data) #通过正则提取出来的评论是列表类型，放在comment变量中
    for item in comment:
        print(str(item))
        print("-------------------")
    #将其显示出来后第一个url的评论便爬取完毕，别忘了更改url的cid值，实现爬取第二页评论
    cid=re.compile(pat2,re.S).findall(data)[0]#我们需要的是列表的第一值，加上[0]，如果不加的话，cid就是一个列表对象
    print("该页爬取完毕")