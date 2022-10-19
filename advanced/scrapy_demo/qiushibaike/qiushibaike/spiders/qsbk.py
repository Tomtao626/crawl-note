# -*- coding: utf-8 -*-
import scrapy
from qiushibaike.items import QiushibaikeItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'  # 名字必须唯一
    allowed_domains = ['qiushibaike.com']
    base_domain = 'https://www.qiushibaike.com'
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        # selectorList
        divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in divs:
            # selector
            author = div.xpath('.//h2/text()').get().strip()
            content = div.xpath('.//div[@class="content"]//text()').getall()
            content = ",".join(content).strip()
            # duanzi = {
            #     'author': author,
            #     'content': content
            # }
            # yield duanzi
            item = QiushibaikeItem(author=author,content=content)
            yield item
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url, callback=self.parse)
        # items = list()
        # divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        # for div in divs:
        #     # selector
        #     author = div.xpath('.//h2/text()').get().strip()
        #     content = div.xpath('.//div[@class="content"]//text()').getall()
        #     content = ",".join(content).strip()
        #     item = QiushibaikeItem(author=author, content=content)
        #     items.append(item)
        # return items
