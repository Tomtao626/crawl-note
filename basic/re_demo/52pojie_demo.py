#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/25 13:42
# @Author : Tom_tao
# @Site : 
# @File : 52pojie_demo.py
# @Software: PyCharm

# 52破解  编程语言区

import urllib.request
import re

page_number = 1  # 页数
title_naumber = 1  # 每个帖子的编号
mData = {}
url = "https://www.52pojie.cn/forum-24-1.html"  # 爬第一页的地址
page = urllib.request.urlopen(url).read()  # 获取到该地址的所有内容
page = page.decode('gbk')  # 转码

zz_pageNumber = r'<span title="共.+?页">(.+?)</span>'
# 匹配出总页数
str_pagenumber = re.findall(zz_pageNumber, page, re.S)  # str_pagenumber = [' / 177 页', ' / 177 页']
# 将非数字用空字符串替换然后转化成int类型
page_Maxnumber = int(re.sub('\D', '', str_pagenumber[0]))  # \D表示非数字
# print(page_Maxnumber)
for index in range(page_Maxnumber):
    url = "https://www.52pojie.cn/forum-24-%d.html" % page_number  # 爬的地址
    if page_number > 2:
        page = urllib.request.urlopen(url).read()  # 获取到该地址的所有内容
        page = page.decode('gbk', 'ignore')  # 转码
    # 正则表达式
    # 匹配整个页面
    zz = r'<tbody id="normalthread_.+?">(.+?)</tbody>'
    # 匹配链接和标题
    zz_mData = r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'

    # 匹配所有符合规则的内容存到html集合里面
    html = re.findall(zz, page, re.S)  # re.S表示.可以代表\n
    # print(html)
    for line in html:
        html_link = re.findall(zz_mData, line, re.S)  # 举例 ('thread-739688-1-1.html', '【Python】萌新跟我来入门Python爬虫')]
        # 标题
        title = html_link[0][1]  # '【Python】萌新跟我来入门Python爬虫'
        # 链接
        link = html_link[0][0]  # link = 'thread-739688-1-1.html'
        print('%d、%s https://www.52pojie.cn/%s' % (title_naumber, title, link))
        title_naumber = title_naumber + 1
    print("第%d页\n" % page_number)
    page_number = page_number + 1