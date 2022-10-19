#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/25 12:34
# @Author : Tom_tao
# @Site : 
# @File : fanyi_qq_demo.py
# @Software: PyCharm

# 腾讯翻译

import requests
import json

text = input("输入翻译内容：")
a = 0  # 中文数
b = 0  # 非中文数
to = "0"
from_ = "1"

for i in text:
    if u'\u4e00' <= i <= u'\u9fff':
        a += 1
    else:
        b += 1

if a > b:  # 当中文数量大于非中文数量时，就中文转英文
    to = "1"
    from_ = "0"

'''
from =1 to = 0   ---》英-中
from =0 to = 1   ---》中-英
'''
data = {"from": from_,
        "to": to,
        "sourceText": text,
        "type": "1",
        "latitude": "1",
        "longitude": "1",
        "platform": "H5"}
url = "https://m.fanyi.qq.com/translate"
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
response = requests.post(url, headers=headers, data=data)
html = response.content.decode()
html_dict = json.loads(html)
print("翻译结果：", html_dict["targetText"])