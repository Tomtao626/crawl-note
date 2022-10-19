#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/3 0:28
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

import requests

data = {
    'first': "true",
    'pn': '1',
    'kd': 'python'
}

headers = {
    'Referer':'https://www.lagou.com/jobs/list_python/p-city_3?px=default',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false', data=data, headers=headers)
print(response.text)
print(response.json)  # dict