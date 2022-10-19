#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 19:42
# @Author : Tom_tao
# @Site : 
# @File : lagou1.py
# @Software: PyCharm
import time
import re
import requests
from lxml import etree

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'user_trace_token=20200303155109-6f397865-0d1b-45ed-8a45-1918646fc0d1; LGUID=20200303155109-91ccaab8-56e7-4c14-a364-4a17cf93697b; _ga=GA1.2.606398285.1583221870; LG_LOGIN_USER_ID=aa3365371e8f9aa1ac0f83e14c5449a48e33ab8d27be3f4e; LG_HAS_LOGIN=1; index_location_city=%E6%9D%AD%E5%B7%9E; _gid=GA1.2.523507336.1586089206; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221714a48b5a4525-0d198b056a8c46-f313f6d-2073600-1714a48b5a587e%22%2C%22%24device_id%22%3A%221714a48b5a4525-0d198b056a8c46-f313f6d-2073600-1714a48b5a587e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAAECABBJAAGI68829522001ABAF9B140C7EF806E919C; WEBTJ-ID=20200406153318-1714e686aa82f8-0f47073d792c72-f313f6d-2073600-1714e686aa9812; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20200406153318-7d981c29-5966-4fc9-a081-bc2989936570; PRE_SITE=https%3A%2F%2Fwww.lagou.com; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586089206,1586150831,1586158399; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=fefbf744bdcc064b49d3aecde4f6ee96; X_HTTP_TOKEN=055ab803b58207091689516851e19e533583247363; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586159861; LGRID=20200406155741-5bc98aed-4fd4-4c35-8293-998170455a6c; SEARCH_ID=41ce591ef5e24c7fba4dcd9bc3ba05a3',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }

def request_page_url():
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false"
    data = {
        'first': 'false',
        'pn': 1,
        'kd': 'python',
    }
    for x in range(1, 14):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data)
        # json方法，如果返回来的是json数据，那么这个方法会自动load成字典
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId
            parse_position_detail(position_url)
            break
        break

def parse_position_detail(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath('.//text()')[0].strip()
    city = re.sub(r"[\s/]", "", city)
    work_years = job_request_spans[2].xpath('.//text()')[0].strip()
    work_years = re.sub(r"[\s/]", "", work_years)
    education = job_request_spans[3].xpath('.//text()')[0].strip()
    education = re.sub(r"[\s/]", "", education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    print(desc)

def main():
    request_page_url()

if __name__ == '__main__':
    main()