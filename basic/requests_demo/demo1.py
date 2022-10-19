#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/2 20:42
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm


import requests


# response = requests.get("http://www.baidu.com")
# print(type(response.text))
# print(response.text)

# print(type(response.content))
# print(response.content.decode('utf-8'))

# print(response.url)
# print(response.encoding)
# print(response.status_code)
params = {
    'wd': '中国'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
response = requests.get("https://www.baidu.com/s", params=params, headers=headers)

with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)