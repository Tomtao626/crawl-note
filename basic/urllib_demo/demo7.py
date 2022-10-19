#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/2 20:17
# @Author : Tom_tao
# @Site : 
# @File : demo7.py
# @Software: PyCharm

from urllib import request
from http.cookiejar import MozillaCookieJar

# 保存cookie信息
cookiejar = MozillaCookieJar('cookie.txt')
# 加载
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open("http://httpbin.org/cookies/set?course=abc")
for cookie in cookiejar:
    print(cookie)

# cookiejar.save(ignore_discard=True)