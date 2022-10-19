## scrapy运行流程

> + 1.首先爬虫主代码spiders开始运行 发送一个requests请求给爬虫引擎engine
> + 2.当引擎engine收到请求requests，会将其发送给调度器scheduler
> + 3.调度器scheduler处理之后，再将请求requests返回给引擎engine
> + 4.引擎engine收到返回的requests请求后，再将其发送给下载器downloader，
> + 5.下载器downloader从网络获取到数据后，返回一个response响应对象给引擎engine
> + 6.引擎engine收到response响应后，再将其返回给spider
> + 7.此时spider再返回一个处理过的模型items/requests对象给引擎engine
> + 8.引擎收到请求requests和items后，将items模型存入管道pipelines中，requests对象则返回给调度器scheduler

## 1.安装scrapy框架

```shell
pip install scrapy
```

## 2.win环境下 还需安装pypiwin32

> 如果不安装  运行scraapy项目时就会报错，安装方式 pip install pypiwin32

## 3.ubuntu环境下 还需安装一些第三方库

```shell
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev libffi-dev libssl-dev
```

## 4.创建爬虫

> 1.创建项目

在指定项目目录下，输入 `scrapy startproject [爬虫项目名]`

> 2.创建爬虫，进入项目所在的路径，输入 `scrapy genspider [爬虫名字] [爬虫的域名]`

注意 爬虫名字不能和项目名一致

## 5.项目目录结构

> + 1.items.py 用来存放爬虫爬取下来数据的模型
> + 2.middlewares.py 用来存放各种中间件的文件
> + 3.pipelines.py 用来将items的模型存储到本地磁盘中
> + 4.settings.py 本爬虫的一些配置信息  例如 请求头 多久发送一次请求 ip代理池等
> + 5.scrapy.cfg  项目的配置文件
> + 6.spiders包  以后所有的爬虫都是存放到这个里面

## 6.糗事百科笔记

> + 1.response是一个'scrapy.http.response.html.HtmlResponse'对象，可以执行xpath,css语法来提取数据
> + 2.提取出来的数据，是一个'Selector'或者是一个'SelectorList'对象，如果想要获取其中的字符串，那么应该执行'getall'或者'get'方法
> + 3.getall方法，获取'Selector'中的所有文本，返回的是一个列表 等价于extract方法
> + 4.get方法，获取的是'Selector'中的第一个文本，返回的是一个str类型
> + 5.如果数据解析回来，要传给pipelines处理，那么可以使用'yield'来返回；如果不使用yield，则要创建一个列表存储数据，最后返回这个列表
> + 6.item：建议在'items.py'中定义好模型，以后就不要使用字典
> + 7.pipelines：这个是专门用来存储数据的，其中有三个方法常用：
　　　　'open_spider(self, spider)'：当爬虫打开时执行
　　　　'process_item(self, item, spider)'：当爬虫有item传过来的时候会被调用
　　　　'close_spider(self, spider)'：当爬虫关闭的时候调用
　　　　要激活pipelines，在'settings.py'  68行 代码示例如下:
        ITEM_PIPELINES = {
                            'qiushibaike.pipelines.QiushibaikePipeline': 300,
                        }

JsonItemExporter和JsonLinesItwemExporter:
保存json数据时，可以使用这两个类，让操作更简单

1.'JsonItemExporter' 每次把数据添加到内存中，最后统一写入磁盘中，好处是存储的数据是一个满足json规则的数据；坏处是若数据量比较大，就比较耗内存
示例代码如下：
from scrapy.exporters import JsonItemExporter
class QiushibaikePipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json", 'wb')
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False,encoding='utf-8')
        self.exporter.start_exporting()

    def open_spider(self, spider):
        print("爬虫开始。。。")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("爬虫结束。。。")

2.'JsonLinesItemExporter'  每次调用export_item的时候就把这个个item存储到磁盘中；坏处是没一个字典时一行，整个文件不是一个满足json格式的文件。好处是每次处理数据时直接存储到了硬盘中，不会耗内存，数据比较安全。
示例代码如下：
from scrapy.exporters import JsonLinesItemExporter
class QiushibaikePipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False,encoding='utf-8')

    def open_spider(self, spider):
        print("爬虫开始。。。")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束。。。")

#CrawlSpider
需要使用'LinkExtractor'和'Rule'，这两个东西决定爬虫的走向
1.allow设置规则的方法：要能够限制再我们想要的url上面，不要跟其他的url产生相同的正则表达式即可
2.什么情况使用follow：如果在爬取页面的时候，需要将满足当前条件的url再进行跟选，那么就设置为True，否则设置为False
3.什么情况下指定callback：如果这个url对应的页面，只是为了获取更多的url，并不需要里面的数据，可以不指定callback；如果想要获取对应url里面的数据，那么就需要指定一个callback。


# Scrapy Shell
1.可以方便做一些数据提取的测试代码
2.若想要执行scrapy命令，需进入scrapy项目所在的环境中
3.如果想要读取某个项目的配置信息，需进入这个给项目目录中，再执行'scrapy shell命令'

# 模拟登录人人网
1.想要发送post请求，推荐使用scrapy.FormRequest犯法，可以方便的指定表单数据
2.若需要再爬虫一开始就发送post请求，就应重写start_requests方法，在这个方法中发送post请求