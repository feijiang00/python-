#一些网站用爬虫去爬取的时候是爬取不了的，是需要cookies的。
#而requests中的get方法中就有cookies这个参数，这样我们只需要将网址中的cookies
#获取到了利用该参数就欧克了，但是浏览器中获取到的cookies格式不对
#浏览器中获取某网址的cookies的方法简单说下：
#打开网址network-》ctrl+r-》name右键勾选domain（这样能显示文档了）-》刷新，就可以看到name下的网址点开就可以找到cookies了
#如何转换呢？
#将其保存在一个text文档中，用python列表函数就可以转换了：
f=open(r'test.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
#这里还有自动获取cookies的方法，以后遇到在学习：
a=input("请输入用户名：")
b=input("请输入密码：")
data={'username':a,'password':b}#这里是把数据保存起来以便后面发送post请求使用
req=requests.post(url=target,data=data,headers=headers)#发送post请求，将账号密码发送
a=req.request.headers#这里是获取cookie数据
cookies={}#初始化cookies字典变量
for line in a['Cookie'].split('; '):
	 name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
#这样即可实现自动获取cookies