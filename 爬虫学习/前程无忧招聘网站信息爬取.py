#招聘信息爬取案例（目的：1-学习request，2-解决解码问题，3-掌握进入页面爬取）
#目标站点zhipin.com(boss直聘网站）
#data=bytes(response.text,response.encodeing).decode("utf-8","ignore")
#该代码是先将网页解码为二进制，在将二进制解码为utf-8
#最后的网页分析结果
#https://www.zhipin.com/c101010100/?query=Java&page=2
#https://www.zhipin.com/c101010100/?query=Java&page=3
#https://www.zhipin.com/c101010100/?query=Java&page=4

import requests
import re
key="java"
data={"query":key,"page"="2",}#作为url参数加入其中
hd={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
response=requests.get("https://zhipin.com/c101010100/?",params=data,headers=hd)#有了response后就可以直接使用它的属性了


import requests
import re
key="java"
page="2"
url="https://www.zhipin.com/c101010100/?query="+str(key)+"&page="+str(page)
# data={"query":key,"page":"2",}#作为url参数加入其中
hd={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
#response=requests.get(url,headers=hd)#有了response后就可以直接使用它的属性了
#解码问题
#data=bytes(response.text,response.encoding).decode("utf-8","ignore")#先将response解码为二进制，在解码为utf-8存入data中
#print(data)/这里遇到一个问题，我print了一下。原因是boss爬取的时候需要带上cooikes，这让我会想起requests库的get方法的一个cookie参数，话不多说继续开始
#获取文档中的cookies
f=open(r'test.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
response=request.get(url,headers=hd,cookies=cookies)
data=bytes(response.text,response.encoding).decode("utf-8","ignore")
for i in range(0,10):
    # company={}
    # startdata={}
    # salary={}
    # good={}
    url="https://www.zhipin.com/c101010100/?query="+str(key)+"&page="+str(i+1)
    response = requests.get(url, headers=hd, cookies=cookies)  # 有了response后就可以直接使用它的属性了
    # 解码问题
    data = bytes(response.text, response.encoding).decode("utf-8", "ignore")  # 先将response解码为二进制，在解码为utf-8存入data中
    pat1='ka="search_list_company_.*?_custompage" target="_blank">(.*?)</a></h3>'#当遇到不一样的就.*?直接忽略掉（关键)
    pat2='<span class="job-pub-time">(.*?)</span>'#日期的正则表达
    pat3='<span class="red">(.*?)</span>'
    pat4='<div class="info-desc">(.*?)</div>'
    company= re.compile(pat1, re.S).findall(data)
    startdata=re.compile(pat2, re.S).findall(data)
    salary=re.compile(pat3, re.S).findall(data)
    good=re.compile(pat4, re.S).findall(data)
    #这个网站的cookies几乎过三分钟就失效了
    print(company)
    for j in range(0, 30):
        print("------------------------------------------")
        print("公司:"+company[j])
        print("日期:"+startdata[j])
        print("薪水:"+salary[j])
        print("福利:"+good[j])
#我发现并不是几分钟这个网站的cookies就失效了，而是我大量爬取的时候就失效了，我写好后，没爬完cookies就失效了，等我学到自动获取cookies我再回来




