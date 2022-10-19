#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/2 1:55
# @Author : Tom_tao
# @Site : 
# @File : demo5.py
# @Software: PyCharm


from urllib import request
# 不使用cookie去请求
dapeng_url = 'http://www.renren.com/880151247/profile'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Cookie':'anonymid=k79c3ypyhqgpfv; depovince=GW; _r01_=1; JSESSIONID=abc5mXGtdZmdo5jjjpxcx; ick_login=9be638d5-5695-40ef-89e4-94c07e48f302; taihe_bi_sdk_uid=a7b7b858edaba3fc5ea0eb6a1a198743; taihe_bi_sdk_session=20ebc274221063f2414d0be7ef6450ab; _de=D953C142EA5A80F9340E4CEC836F3769696BF75400CE19CC; t=f76609e58a27224c75a9620cef2de5a54; societyguester=f76609e58a27224c75a9620cef2de5a54; id=973549754; xnsid=68c00db7; jebecookies=d1ef185c-be7e-4e23-99af-25f13f341fbd|||||; ver=7.0; loginfrom=null; jebe_key=1558e138-7c3f-41e2-96c2-da60e0180ab8%7C30ce80726b487004ed987cea484b54e8%7C1583085518517%7C1%7C1583085519026; jebe_key=1558e138-7c3f-41e2-96c2-da60e0180ab8%7C30ce80726b487004ed987cea484b54e8%7C1583085518517%7C1%7C1583085519030; wp_fold=0; XNESSESSIONID=ee7a4773553e'
}
req = request.Request(url=dapeng_url, headers=header)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('eeee.html', 'w',encoding='utf-8') as fp:
    # write()函数必须写入一个str类型的数据
    # resp.read()读出来的是一个bytes类型的数据
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))