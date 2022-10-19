#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/3 18:10
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm


from lxml import etree

text = """
    
"""


def parse_text():
    html = etree.HTML(text)
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

# def parse_tencent_file():
#     html = etree.parse("tencent.html")
#     print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse("lagou.html",parser=parser)
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

if __name__ == "__main__":
    parse_lagou_file()