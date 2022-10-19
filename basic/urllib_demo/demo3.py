#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/1 14:00
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software: PyCharm

from urllib import request,parse

# url = 'https://www.lagou.com/zhaopin/Python/?labelWords=label'
# resp = request.urlopen(url)
# print(resp.read())

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false&isSchoolJob=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' ,
    'Referer': 'https://www.lagou.com/jobs/list_python?isSchoolJob=1'
}

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'Python'
}
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
