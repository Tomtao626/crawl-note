#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: lianjia01.py
@time: 2020/09/27
@contact: tom@007vin.com
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

import asyncio
import aiohttp
from lxml import etree
import logging
import datetime
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['房源', '房子信息', '所在区域', '单价', '关注人数和发布时间', '标签'])
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
start = datetime.datetime.now()


class Spider(object):
    def __init__(self):
        self.semaphore = asyncio.Semaphore(6)  # 信号量，控制协程数，防止爬的过快被反爬
        self.header = {
            "Host": "hz.lianjia.com",
            "Referer": "https://hz.lianjia.com/ershoufang/",
            "Cookie": "lianjia_uuid=db0b1b8b-01df-4ed1-b623-b03a9eb26794; _smt_uid=5f2eabe8.5e338ce0; UM_distinctid=173ce4f874a51-0191f33cd88e85-b7a1334-144000-173ce4f874bd6; _jzqy=1.1596894185.1596894185.1.jzqsr=baidu.-; _ga=GA1.2.7916096.1596894188; gr_user_id=6aa4d13e-c334-4a71-a611-d227d96e064a; Hm_lvt_678d9c31c57be1c528ad7f62e5123d56=1596894464; _jzqx=1.1596897192.1596897192.1.jzqsr=cd%2Elianjia%2Ecom|jzqct=/ershoufang/pg2/.-; select_city=510100; lianjia_ssid=c9a3d829-9d20-424d-ac4f-edf23ae82029; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1596894222,1597055584; gr_session_id_a1a50f141657a94e=33e39c24-2a1c-4931-bea2-90c3cc70389f; CNZZDATA1253492306=874845162-1596890927-https%253A%252F%252Fwww.baidu.com%252F%7C1597054876; CNZZDATA1254525948=1417014870-1596893762-https%253A%252F%252Fwww.baidu.com%252F%7C1597050413; CNZZDATA1255633284=1403675093-1596890300-https%253A%252F%252Fwww.baidu.com%252F%7C1597052407; CNZZDATA1255604082=1057147188-1596890168-https%253A%252F%252Fwww.baidu.com%252F%7C1597052309; _qzjc=1; gr_session_id_a1a50f141657a94e_33e39c24-2a1c-4931-bea2-90c3cc70389f=true; _jzqa=1.3828792903266388500.1596894185.1596897192.1597055585.3; _jzqc=1; _jzqckmp=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22173ce4f8b4f317-079892aca8aaa8-b7a1334-1327104-173ce4f8b50247%22%2C%22%24device_id%22%3A%22173ce4f8b4f317-079892aca8aaa8-b7a1334-1327104-173ce4f8b50247%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.865060575.1597055587; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1597055649; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiOWQ4ODYyNmZhMmExM2Q0ZmUxMjk1NWE2YTRjY2JmODZiZmFjYTc2N2U1ZTc2YzM2ZDVkNmM2OGJlOWY5ZDZhOWNkN2U3YjlhZWZmZTllNGE3ZTUwYjA3NGYwNDEzMThkODg4NTBlMWZhZmRjNTIwNDBlMDQ2Mjk2NTYxOWQ1Y2VlZjE5N2FhZjUyMTZkOTcyZjg4YzNiM2U1MThmNjc5NmQ4MGUxMmU2YTM4MmI3ZmU0NmFhNTJmYmMyYWU1ZWI3MjU5YWExYTQ1YWFkZDUyZWVjMzM2NTFjYTA2M2NlM2ExMzZhNjEwYjFjYzQ0OTY5MTQwOTA4ZjQ0MjQ3N2ExMDkxNTVjODFhN2MzMzg5YWM3MzBmMTQxMjU4NzAwYzk5ODE3MTk1ZTNiMjc4NWEzN2M3MTIwMjdkYWUyODczZWJcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiYmExZDJhNWZcIn0iLCJyIjoiaHR0cHM6Ly9jZC5saWFuamlhLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _qzja=1.726562344.1596894309336.1596897192124.1597055583833.1597055601626.1597055649949.0.0.0.12.3; _qzjb=1.1597055583833.3.0.0.0; _qzjto=3.1.0; _jzqb=1.3.10.1597055585.1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
        }

    async def scrape(self, url):
        async with self.semaphore:
            session = aiohttp.ClientSession(headers=self.header)
            response = await session.get(url)
            result = await response.text()
            await session.close()
            return result

    async def scrape_index(self, page):
        url = f'https://hz.lianjia.com/ershoufang/pg{page}/'
        text = await self.scrape(url)
        await self.parse(text)

    async def parse(self, text):
        html = etree.HTML(text)
        lis = html.xpath('//*[@id="content"]/div[1]/ul/li')
        for li in lis:
            house_data = li.xpath('.//div[@class="title"]/a/text()')[0]             # 房源
            house_info = li.xpath('.//div[@class="houseInfo"]/text()')[0]           # 房子信息
            address = ' '.join(li.xpath('.//div[@class="positionInfo"]/a/text()'))  # 位置信息
            price = li.xpath('.//div[@class="priceInfo"]/div[2]/span/text()')[0]    # 单价 元/平米
            attention_num = li.xpath('.//div[@class="followInfo"]/text()')[0]       # 关注人数和发布时间
            tag = ' '.join(li.xpath('.//div[@class="tag"]/span/text()'))            # 标签
            sheet.append([house_data, house_info, address, price, attention_num, tag])
            logging.info([house_data, house_info, address, price, attention_num, tag])

    def main(self):
        # 100页的数据
        scrape_index_tasks = [asyncio.ensure_future(self.scrape_index(page)) for page in range(1, 101)]
        loop = asyncio.get_event_loop()
        tasks = asyncio.gather(*scrape_index_tasks)
        loop.run_until_complete(tasks)


if __name__ == '__main__':
    spider = Spider()
    spider.main()
    wb.save('house.xlsx')
    delta = (datetime.datetime.now() - start).total_seconds()
    print("用时：{:.3f}s".format(delta))
