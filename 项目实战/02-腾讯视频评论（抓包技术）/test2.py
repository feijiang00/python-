#案例项目：爬取腾讯视频的评论
import urllib 
import urllib.request
import re
#抓包是为了在很多一个网页的很多请求中找到藏着评论的这个网页，现在观察这两个网页可以发现，第一个网页的6605075079590517283处
#和第二个网页不同，（ps一般来说网页最后的数字不管，即使输入去掉它后的网址依旧可以访问）
#思考：现在和糗事百科不一样的情况是这是无规律的数字，难道还是需要一页页输入吗？肯定不是，不妨在第一个网页中看看能否找到第二个网页
#的那个关键性的数字
#https://video.coral.qq.com/varticle/4455757136/comment/v2?callback=_varticle4455757136commentv2&orinum=10&oriorder=o&page
# flag=1&cursor=6605249436949493250&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1581017626120
#https://video.coral.qq.com/varticle/4455757136/comment/v2?callback=_varticle4455757136commentv2&orinum=10&oriorder=o&page
# flag=1&cursor=6605075079590517283&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1581017626119
#"last":"6605249436949493250"果然，在第一个网页中找到了第二个网页的那个关键性数字，这样一来就好办了
#总体思路：先通过抓包分析，将评论网页的html爬取下来（str类型）。接着，根据该网页中的last值找到下一个网页的关键性数字，一直迭代下去
#该评论网页时json格式，可以直接用正则表达式提取。
cid='6605075079590517283'
for i in range(0,3):
    print("第"+str(i+1)+"页的评论数据")
    url = "https://video.coral.qq.com/varticle/4455757136/comment/v2?callback=_varticle4455757136commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + str(cid) + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1581017626119"
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    #接下来两件事情要做，提取评论和改变url
    pat='"content":"(.*?)"'
    comment=re.compile(pat,re.S).findall(data)
    for j in comment:
        print(str(j))
        print("-------------")
    pat2='"last":"(.*?)"'
    key=re.compile(pat2,re.S).findall(data)[0]

#第一次报错：urllib.error.HTTPError: HTTP Error 400: Bad Request
#我以为是浏览器识别我的爬虫，特意伪装了一下，，，，仔细一看报错是400
#这个报错的原因是语义有错误，当前的请求服务器无法理解。

#之后找了半天，400报错的原因都说是一些参数错了，服务器无法理解。果然最后是因为我的ignore这个参数拼错了
#然后发现并不是，是url写错了，尤其的拼接的时候特别需要注意。
