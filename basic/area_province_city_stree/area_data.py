#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 11:44 上午
# @Author : admin
# @Software: PyCharm
# @File: area_data.py

import requests
from urllib import request
from lxml import etree

headers = {
    'Referer': 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html"

response = requests.get(url=url,headers=headers)
print(response.text.encode('utf-8'))