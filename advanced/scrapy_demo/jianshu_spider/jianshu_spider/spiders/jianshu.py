# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleItem


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        author = response.xpath("//span[@class='FxYr8x']/a[@class='_1OhGeD']/text()").get()
        avatar = response.xpath("//div[@class='_2mYfmT']/a[@class='_1OhGeD']/img/@src").get()
        pub_time = response.xpath("//div[@class='s-dsoj']/time/text()").get()
        # https://www.jianshu.com/p/e86c6f35c556
        # https://www.jianshu.com/p/e86c6f35c556?utm_campaign=maleskine&utm_content=note
        url = response.url
        url1 = url.split("?")[0]
        article_id = url1.split("/")[-1]
        content = response.xpath("//article[@class='_2rhmJa']").get()
        read_count = response.xpath("//div[@class='s-dsoj']/span[last()]/text()").get()
        word_count = response.xpath("//div[@class='s-dsoj']/span[last()-1]/text()").get()
        like_count = response.xpath("//div[@class='-pXE92']/div[@class='_3nj4GN'][last()]/span/text()").getall()[-1]
        comment_count = response.xpath("//div[@class='-pXE92']/div[@class='_3nj4GN'][last()-1]/span/text()").getall()[-1]
        subjects = ",".join(response.xpath("//div[@class='_2Nttfz']/a/span/text()").getall())


        item = ArticleItem(
            title=title,
            author=author,
            avatar=avatar,
            pub_time=pub_time,
            article_id=article_id,
            content=content,
            origin_url=response.url,
            word_count=word_count,
            read_count=read_count,
            comment_count=comment_count,
            like_count=like_count,
            subjects=subjects
        )
        yield item