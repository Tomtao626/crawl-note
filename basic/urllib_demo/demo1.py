#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/28 0:39
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

from urllib import request
from urllib import parse
# 默认get 也可以更改为post
# resp = request.urlopen('http://www.baidu.com')
# 获取返回http状态码
# print(resp.getcode())
# 下载网页文件

#urlretrieve的用法
# request.urlretrieve('https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4181233763,782732842&fm=26&gp=0.jpg', 'nba_meina.jpg')

# urlencode的用法
# params = {"name":'李四',"age":18,"info":'hello world'}
# result = parse.urlencode(params)
# print(result)

# 错误用法 必须转码
'''
    url = 'http://www.baidu.com/s/wd=刘德华'
    resp = request.urlopen(url)
    print(resp.read())
'''

# 正确用法 使用urlencode()
'''
    url = 'http://www.baidu.com/s'
    params = {'wd':'刘德华'}
    qs = parse.urlencode(params)
    print(qs)
    url = url + "?" + qs
    resp = request.urlopen(url)
    print(resp.read())    
'''

# parse_qs函数的用法
params = {"name": '李四', "age": 18, "info": 'hello world'}
qs = parse.urlencode(params)
print('编码后:', qs)
qs_test = parse.parse_qs(qs)
print('解码后 还原:', qs_test)