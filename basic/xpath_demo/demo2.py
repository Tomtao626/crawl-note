#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/3 23:50
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html", parser=parser)

# 获取所有的p标签
# //p
# xpath返回的是一个列表
'''
    ps = html.xpath("//p")
    for p in ps:
        print(etree.tostring(p, encoding="utf-8").decode("utf-8"))    
'''

# 获取第二个p标签
# //p[2]
'''
    p = html.xpath("//p[2]")[0]
    print(etree.tostring(p, encoding='utf-8').decode('utf-8'))
'''

# 获取所有class等于recruit-text的p标签
'''
    ps = html.xpath("//p[@class='recruit-text']")
    for p in ps:
        print(etree.tostring(p, encoding='utf-8').decode('utf-8'))
'''

# 获取所有a标签中的href属性
'''
    a_list = html.xpath("//a/h4")
    for a in a_list:
        print("https://careers.tencent.com/"+etree.tostring(a, encoding='utf-8').decode('utf-8'))
'''

# 抓取所有的职位信息 纯文本
positions = list()
ps = html.xpath("//p[position()<2]")
for p in ps:
    # 在某个标签下再执行xpath函数，获取这个标签下的子孙元素
    # 不能使用//xxx  而是使用.//xxx  代表当前标签下的元素
    href = p.xpath(".//span")[0]
    company = p.xpath("./span[1]/text()")[0]
    address = p.xpath("./span[2]/text()")[0]
    category = p.xpath("./span[3]/text()")[0]

    position = {
        'href': href,
        'company': company,
        'address': address,
        'category': category
    }
    positions.append(position)
    
print(positions)