# -*- coding: utf-8 -*-
import re

import scrapy

from fang.items import NewHouseItem,ESFHouseItem


class SoufangwangSpider(scrapy.Spider):
    name = 'soufangwang'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub("\s", "", province_text)
            # 判断某个省份第二行的城市是否再这个省份下
            if province_text:
                province = province_text
            # 排除海外的房源  不爬取
            if province == '其它':
                continue
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # 构建新房的url链接
                url_model = city_url.split("//")
                scheme = url_model[0]
                domain = url_model[1]
                if "bj." in domain:
                    newhouse_url = "http://newhouse.fang.com/house/s/"
                    esf_url = "http://esf.fang.com/"
                else:
                    newhouse_url = scheme + "//" + "newhouse." + domain + "house/s/"
                    # 构建二手房的url链接
                    esf_url = scheme + "//" + "esf." + domain
                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info": (province, city)})
                yield scrapy.Request(url=newhouse_url, callback=self.parse_esf, meta={"info": (province, city)})

    def parse_newhouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            house_type_list = list(map(lambda x: re.sub(r"\s", "", x), house_type_list))
            rooms = list(filter(lambda x: x.endswith("居"), house_type_list))
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r"\s|－|/", "", area)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district = re.search(r".*\[(.+)\].*", district_text).group(1)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)
            origin_url = response.urljoin(li.xpath(".//div[@class='nlcd_name']/a/@href").get())
            item = NewHouseItem(name=name, rooms=rooms, area=area, address=address, district=district, sale=sale,
                                origin_url=origin_url, province=province, city=city, price=price)
            yield item
        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={"info": (property, city)})

    def parse_esf(self, response):
        province, city = response.meta.get("info")
        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            item = ESFHouseItem(province=province,city=city)
            item['name'] = dl.xpath("//p[@class='add_shop']/a/text()").get()
            infos = dl.xpath("//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x:re.sub(r"\s","",x),infos))
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif '层' in info:
                    item['rooms'] = info
                elif '向' in info:
                    item['toward'] = info
                elif '㎡' in info:
                    item['area'] = info
                else:
                    item['year'] = info.replace("建筑年代：", "")

            item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item['price'] = dl.xpath(".//dd[@class='price_right']/span[@class='red']//text()").getall()
            # 等价于
            # item['price'] = dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall()
            item['unit'] = dl.xpath(".//dd[@class='price_right']/span[last()]/text()").getall()
            item['origin_url'] = response.urljoin(dl.xpath(".//dd/h4[@class='clearfix']/a/@href").get())
            yield item
        next_url = response.xpath("//div[@id='list_D10_15']/p[1]/a/@href").get()
        yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_esf,meta={"info":(property,city)})