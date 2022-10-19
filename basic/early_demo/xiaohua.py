# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # 域名范围
    allowed_domains = ['xiaohuar.com']
    # 起始url
    start_urls = [
        "http://www.xiaohuar.com/list-1-0.html",
        "http://www.xiaohuar.com/list-1-1.html",
        "http://www.xiaohuar.com/list-1-2.html",
        "http://www.xiaohuar.com/list-1-3.html",
        "http://www.xiaohuar.com/list-1-4.html",
        "http://www.xiaohuar.com/list-1-5.html",
        "http://www.xiaohuar.com/list-1-6.html",
        "http://www.xiaohuar.com/list-1-7.html",
        "http://www.xiaohuar.com/list-1-8.html",
        "http://www.xiaohuar.com/list-1-9.html",
        "http://www.xiaohuar.com/list-1-10.html",
        "http://www.xiaohuar.com/list-1-11.html",
        "http://www.xiaohuar.com/list-1-12.html",
        "http://www.xiaohuar.com/list-1-13.html",
        "http://www.xiaohuar.com/list-1-14.html",
        "http://www.xiaohuar.com/list-1-15.html",
        "http://www.xiaohuar.com/list-1-16.html",
        "http://www.xiaohuar.com/list-1-17.html",
        "http://www.xiaohuar.com/list-1-18.html",
        "http://www.xiaohuar.com/list-1-19.html",
        "http://www.xiaohuar.com/list-1-20.html",

    ]
    # 分析
    def parse(self, response):
        if 'www.xiaohuar.com/list-1' in response.url:
            #说明我们在获取img_url
            # 下载的html文档
            html = response.text
            # 获取img_url
            # /d/file/20170516/6e295fe48c33245be858c40d37fb5ee6.jpg
            img_urls = re.findall(r'/d/file/\d+/\w+\.jpg', html)
            # 循环的去下载
            for img_url in img_urls:
                # 完整域名
                if 'http://' not in img_url:
                    img_url = "http://www.xiaohuar.com%s" % img_url
                # 回调，返回response
                yield Request(img_url)
        else:
            # 下载图片
            url = response.url
            # 图片文件名
            title = re.findall(r'(\w*.jpg)', url)[0]
            # 保存图片
            with open('F:\scrapydownload\%s' % title, 'wb') as f:
                f.write(response.body)