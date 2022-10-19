#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/2 2:24
# @Author : Tom_tao
# @Site : 
# @File : demo6.py
# @Software: PyCharm

# 人人网登录

from urllib import request,parse
from http.cookiejar import CookieJar

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

def get_opener():
    # 1.登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    # 1.4 使用opener发送登录的请求(邮箱/密码)
    data = {
        'email': "18372620761",
        'password': "Wangxi4228tp"
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)


def visit_profile(opener):
    # 2.访问个人主页
    dapeng_url = 'http://www.renren.com/880151247/profile'
    # 获取个人主页的页面时，不要新建一个opener，而应该用之前的opener，即登录所需的cookie信息
    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)