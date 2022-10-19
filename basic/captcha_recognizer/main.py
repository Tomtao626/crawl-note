#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/11 16:28
# @Author : Tom_tao
# @Site : 
# @File : main.py
# @Software: PyCharm

from urllib import request
from base64 import b64encode
import requests

captcha_url = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=350817400,1876187630&fm=26&gp=0.jpg'
request.urlretrieve(captcha_url, 'captcha.png')

recognize_url = "https://tongyongwe.market.alicloudapi.com/generalrecognition/recognize?type=en"

formdata = {}
with open('captcha.png','rb') as fp:
    data = fp.read()
    pic = b64encode(data)
    formdata['pic'] = pic
# 从阿里云获取appcode
appcode = 'xxxxxxxxxxxxxxxxxxx'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Authorization': 'APPCODE ' + appcode
}

response = requests.post(url=recognize_url,data=formdata,headers=headers)
result = response.json()
code = result['result']
print(code)