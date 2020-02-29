#request模块爬虫编写实战(实战使用request实现芸西社区博文爬虫）
#请求方式主要就是get
#text 响应数据 ； content 响应数据（b） ； encoding 网页编码 ； cookies 响应cookie
#url 当前请求的url  status——code  状态码
#用request提取的都是响应，，需要加上以上对应的状态
#例如：
#rst=request.get("http://www.aliwx.com.cn/")
#此时若想要提取该网页标题，很简单，但正则匹配的字符串应该是rst.text
#若想修改浏览器信息，只需要在request使用get方法时候改变其他参数，有个headers参数
#request.utils.dict_from_cookiejar(rst.cookies)这可以将cooies转为字典序
#关于post方法的使用，该方法是请求url后的资源，并且添加新的数据
#新的数据在请求的参数data中添加，例如：
postdata={"name":"测试",}
rst=request.post("http://xxx.com/",data=postdata)
