import requests
import re
key="java"
page="2"
# data={"query":key,"page":"2",}#作为url参数加入其中
hd={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
#获取文档中的cookies
f=open(r'test.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
#然后我发现每一页都是正好30个招聘信息，一共刚好10页，而且不一样的关键词也是如此（ps：有点巧合，一般不会这么简单，需要读取n个/每页的m个+1得到页数）
#要爬取的内容，薪水，岗位名称，公司名称，发布日期，公司福利一共五个信息（ps：我原以为还需要进入每个招聘网页的小网页中查看详细信息，这个网址都不需要）
for i in range(0,10):
    # company={}
    # startdata={}
    # salary={}
    # good={}
    url="http://www.zhipin.com/c101010100/?query="+str(key)+"&page="+str(i+1)
    print(cookies)
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
