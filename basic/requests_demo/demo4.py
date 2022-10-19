#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/3 0:51
# @Author : Tom_tao
# @Site : 
# @File : gushiwen.py
# @Software:

import requests

# response = requests.get("https://www.baidu.com/")
# print(response.cookies)
data = {
        'email': "xxxxxxxxxxx",
        'password': "xxxxxx"
    }
login_url = "http://www.renren.com/PLogin.do"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
session = requests.Session()

session.post(login_url, data=data, headers=headers)

response = session.get('http://www.renren.com/880151247/profile')

with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)