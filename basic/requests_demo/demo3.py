#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/3 0:42
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software: PyCharm

import requests

proxy = {
    'http':'171.35.160.85:9999'
}

response = requests.get("http://httpbin.org/ip", proxies=proxy)
print(response.text)