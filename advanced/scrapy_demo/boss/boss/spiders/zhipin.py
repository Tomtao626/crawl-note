# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1&ka=page-1']

    rules = (
        # 匹配职位列表页
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d'), follow=True),
        # 匹配职位详情页
        Rule(LinkExtractor(allow=r'.+job_detail/\w+.html'), callback="parse_job", follow=False),
    )

    def parse_job(self, response):
        title = response.xpath("//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='name']/span/text()").get().strip()
        job_info = response.xpath("//div[@class='job-primary detail-box']/div[@class='info-pro=imary']/p//text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company_name = response.xpath("//div[class='company-info']//a/text()").get().strip()
        item = BossItem(
            title=title,
            salary=salary,
            city=city,
            work_years=work_years,
            education=education,
            company_name=company_name
        )
        yield item