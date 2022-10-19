#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/1 16:38
# @Author : Tom_tao
# @Site : 
# @File : gushiwen.py
# @Software: PyCharm

from urllib import request

# 未使用代理
# url = 'https://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())    b'{\n  "origin": "183.92.76.223"\n}\n'

# 使用代理
url = 'http://httpbin.org/ip'
# 1.使用request.ProxyHandler, 传入代理构建一个handler
handler = request.ProxyHandler({"http": "106.122.205.36:8118"})
# 2.使用其handler构建一个opener
opener = request.build_opener(handler)
# 3.使用opener发送一个请求
resp = opener.open(url)
print(resp.read())   # b'{\n  "origin": "183.92.76.223"\n}\n'