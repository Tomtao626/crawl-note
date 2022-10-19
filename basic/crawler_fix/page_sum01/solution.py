#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: solution.py
@time: 2021/01/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""
import re

"""
    爬虫的目标很简单，就是拿到想要的数据。
    这里有一个网站，里面有一些数字。把这些数字的总和，输入到答案框里面，即可通过本关。
    网站url: http://www.glidedsky.com/level/web/crawler-basic-1
    由于网站策略发生变化，cookie无法直接从浏览器拿到，需要登录进行身份鉴权
"""
import parsel
import requests
from lxml import etree

base_url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}
# 登录url
login_url = "http://www.glidedsky.com/login"
# 会话保持 在跨请求时保存某些参数
# 实例化session
session = requests.session()
# 根据session发送get请求 获取token
token_request = session.get(login_url, headers=headers)
# print(token_request.text)
_token = re.search('"_token" value="(.*?)"', token_request.text).group(1)
print(_token)
data = {
    "_token": _token,
    "email": "tp320670258@gmail.com",
    "password": "tp751825253"
}
# 发送post请求 登录
res = session.post(url=login_url, data=data)
# get请求获取目标页面数据
response = session.get(base_url)
data = etree.HTML(response.text)
# print(response.text)
last_list = "".join(data.xpath('//div[@class="row"]/div/text()')).split()
# 推导式
print(sum(int(i) for i in last_list))

# map
print(sum(map(int, last_list)))

# parsel
selector = parsel.Selector(response.text)
lis = selector.css("div.col-md-1").getall()
# print(lis)
sum = 0
for i in lis:
    num = int(re.findall('\s*([0-9]+)\s', i)[0])
    sum += num
print(sum)


# 如何在session中手动设置cookie
import requests
import time
mycookie = dict(PYSESSID='shdf7f734gfg673f319e133t3')
# 实例化session
session = requests.session()
# 通过requests.utils.add_dict_to_cookiejar方法对session对象设置cookie 之后所有的请求都会加上刚才定义的cookie
requests.utils.add_dict_to_cookiejar(session.cookies, dict(PYSESSID='shdf733fgeg34gfrfeeg353'))
# session.get("http://127.0.0.1:80", cookie=mycookie)
# 也可以通过requests.utils.cookiejar_from_dict 先生成一个cookiejar对象，时候在赋值给session.cookies。貌似还可以使用session.cookies.set()或者update()。
time.sleep(5)
# session.get("http://127.0.0.1:80")

# 手动格式化cookie

cookie = "SINAGLOBAL=821034395211.0111.1522571861723; wb_cmtLike_1850586643=1; un=tp320670258@gmail.com; wb_timefeed_1850586643=1; UOR=,,login.sina.com.cn; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWsNeq71O_sXkkXNnXFHgOW5JpX5KMhUgL.Fo2RSK5f1hqcShe2dJLoI0qLxK-L12qLB-zLxKqL1hnL1K2LxK-LBo5L12qLxKqL1hML1KzLxKnL1K.LB-zLxK-L1K-LBKqt; YF-V5-G0=c99031715427fe982b79bf287ae448f6; ALF=1556795806; SSOLoginState=1525259808; SCF=AqTMLFzIuDI5ZEtJyAEXb31pv1hhUdGUCp2GoKYvOW0LQTInAItM-ENbxHRAnnRUIq_MR9afV8hMc7c-yVn2jI0.; SUB=_2A2537e5wDeRhGedG7lIU-CjKzz-IHXVUm1i4rDV8PUNbmtBeLVrskW9NUT1fPIUQGDKLrepaNzTEZxZHOstjoLOu; SUHB=0IIUWsCH8go6vb; _s_tentry=-; Apache=921830614666.5322.1525261512883; ULV=1525261512916:139:10:27:921830614666.5322.1525261512883:1525239937212; YF-Page-G0=b5853766541bcc934acef7f6116c26d1"
print({i.split('=')[0].replace(' ', ''): i.split('=')[1] for i in cookie.split(";")})
