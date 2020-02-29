#scrapy模块的安装，常用指令实战，爬虫项目编写，使用scrapy编写当当网商品数据爬虫实战
#scrapy模块的安装
#0-升级pip：python -m pip install --upgrade pip（网络安装）
#1-安装wheel ：pip install wheel（网络安装）
#2-安装lxml（下载安装，下载后，进入改库的所在地，pip install 全文件名就可安装）
#3-安装twisted（下载安装）
#4-pip install scarpy（网络安装）
#5-下载安装pywin32并且配置（配置：将安装好的pywin32复制到c盘的window/system32中）

#scrapy的使用
#创建项目指令：scrapy startproject 项目名（用cmd框创建）
#spiders文件夹放爬虫，init初始化文件，items-py是定义爬的目标，
#middlewewares-py做中间处理，piplines-py做爬后处理，setting做全局配置

#指令
#scrapy genspider -1 查看当前爬虫下的模板（basic基础模板，crawl通用爬虫模板，csvfeed爬取csv数据的，xmlfeed爬取xml数据）
#scrapy genspider -t basic(模板） fst（文件名） baidu.com(域名） （在主目录下创建）
#scrapy crawl fst（文件名） 运行爬虫
#scrapy list 查看当前有哪些可用的爬虫文件
#scrapy 查看所有的scrapy指令

#编写一个scrapy爬虫项目的一般流程
#创建爬虫项目-编写items-创建爬虫文件-编写爬虫文件-编写pipelines-编写seeting全局配置
 


