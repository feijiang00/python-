#知乎网（使用技术urllib）
#需求数据：登陆并爬取某个页面
#要求：实现自动登陆并保持登陆状态

#1 通过抓包技术，实现登陆


#找出判断验证码是否存在的网页，true  或者 false
#接着输入错误的验证码，通过抓包技术，找到验证码的网页（验证码可能会分为中文和英文），这里遇到一个问题：
##得到了验证码网址后，会发现验证码得到的网址和验证码提交的网址是一样的，其实是通过post 和put两个方法来区别的
#（知乎中的验证码图片是放在json中）----但是相应的文字并不是完完整整base64编码，会有变异，处理办法：
##保存真实的验证码图片，通过py得到真实的编码

#过于麻烦，先不学了！