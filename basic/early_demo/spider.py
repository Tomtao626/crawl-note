#！ /usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
#初始化url
first_url = "http://www.xiaohuar.com/"
#发送一个请求
header = \
    {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    } #user-Agent就是一个铭牌
#包装一个请求
req = request.Request(url = first_url,headers = header)
response = request.urlopen(req)
#获取返回html
html  = response.read()
#提取img
soup = BeautifulSoup(html,'html.[arseer',from_encoding='GBK')
#获取所有的img
imgs = soup.find_all('imgs',src =re.compile(r'/d/file/\d+/\w+\.jpg'))
for img in imgs:
    #创建一个请求
    url = "http://www.xiaohuar.com" % img['src']  # %字符串格式化
    req = request.Request(url = url,headers=header)
    #获得了我们的图片信息
    data = request.urlopen(req).read()
    with open('%s.jpg'%img['alt'],'wb') as f:
        f.write(data)
