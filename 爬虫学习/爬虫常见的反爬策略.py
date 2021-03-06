#反爬策略1：通过ua限制或者其他头信息限制
#解决方案：构建用户代理池，或者其他头信息（第二节，糗事百科）

#反爬策略2：通过访问者ip限制
#解决方案：构建ip代理池（案例演示）

#反爬策略3：通过验证码限制
#解决方案：手工打码，验证码接口自动识别（api），或者通过机器学习自动识别（第8节知乎案例，手打打码）

#反爬策略4：通过数据的异步加载限制
#解决方案：抓包分析或者使用phantomsjs（第七节淘宝案例）

#反爬策略5：通过cookie限制
#解决方案：进行cookie处理（第八节）

#反爬策略6：通过js限制（请求的数据通过js随机生成）
#解决方案：分析js解密或者使用phantomjs



#构建ip代理池

#分布式爬虫编写
#自己编写分布式爬虫或者基于scrapy-redis实现分布式爬虫
