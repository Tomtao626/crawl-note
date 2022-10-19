#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 16:05
# @Author : Tom_tao
# @Site : 
# @File : gushiwen.py
# @Software: PyCharm

import requests
import re


def parse_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(r'<div\sclass="contson" .*?>(.*?)</div>', text, re.DOTALL)
    contents = list()
    for content in content_tags:
        x= re.sub(r'<.*?>',"",content)
        contents.append(x.strip())
    poems = list()
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print("="*40)

def main():
    for x in range(1,11):
        url = "https://www.gushiwen.org/default_{}.aspx".format(x)
        parse_page(url)




if __name__ == "__main__":
    main()