# -*- coding:UTF-8 -*-
import requests,json,os
from urllib import parse
from urllib.request import urlretrieve
from threading import Thread
class img(object):
    def __init__(self):
        self.target="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=replaceword1&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=©right=&word=replaceword2&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=replaceword3&rn=30&gsm=3c&1557964527823="
        self.keyword=''#关键字
        self.num=''#要爬取的数量
        self.names=[]#图片名字
        self.urls=[]#图片链接
    #获取图像url
    def geturl(self):
        for each in range(30,self.num+30,30):#因为我们设置百度时一次性获取30张的，所以我们直接加上30，多爬一点链接
            #这里是替换关键词，因为我们是自定义下载关键词的，所以在这里一次性替换掉
            target = self.target.replace('replaceword1',self.keyword).replace('replaceword2', self.keyword).replace('replaceword3',str(each))
            #这里就是获取json数据
            req = requests.get(url=target)
            html = json.loads(req.text)#把内容换成json
            html=html['data']#获取主体内容
            for i in range(len(html)-1):
                self.names.append(html[i]['di']+'.'+html[i]['type'])#这里就是不断的把名字和链接加到我们的列表里
                self.urls.append(html[i]['thumbURL'])
    #下载图像
    def download(self,url,name):#这里就是下载图像的函数，配合多线程使用，使下载速度加倍
        print ('正在下载：%s' %name)
        if not os.path.exists('img'):#这里是创建文件夹
            os.makedirs('img')
        name='img/'+name#这里就是换一个路径，下载到img下
        urlretrieve(url,name)#下载图像
    # 多线程下载图像
    def moredown(self):
        threads = []#这里我们使用多线程，要把这些线程放到列表里
        for i in range(self.num):#我们要下多少图片就开多少线程
            t =Thread(target=self.download(self.urls[i], self.names[i]))#把函数加到线程里面
            t.start()#开始线程
            threads.append(t)#把线程都加到列表里面，方便后面判断是否下载完毕
        for t in threads:
            t.join()#这里就是等待线程结束的代码
        print ("下载完成")

    #开始下载
    def start(self):
        s = input("请输入关键词：")
        if s=='':
            print ('你还没有输入关键词！')
            return
        im.keyword = parse.quote(s)
        n = input("请输入需要下载的数量：")
        if (not n.isdigit()) or n=='':
            print ('你输入的不是数字！')
            return
        im.num = int(n)
        self.geturl()
        self.moredown()
if __name__=="__main__":
    im = img()
    while True:
        im.start()

