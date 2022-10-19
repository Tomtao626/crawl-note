#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 16:58
# @Author : Tom_tao
# @Site : 
# @File : baisibudejie.py
# @Software: PyCharm

import re

import requests


def parse_page(url):
    headers = {
        'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    text = response.text
    usernames = re.findall(r'<div\sclass="u-txt">.*?<a .*?>(.*?)</a>', text, re.DOTALL)
    pub_times = re.findall(r'<div\sclass="u-txt">.*?<span .*?>(.*?)</span>', text, re.DOTALL)
    descs = re.findall(r'<div\sclass="j-r-list-c-desc">.*?<a .*?>(.*?)</a>', text, re.DOTALL)
    contents = list()
    for value in zip(usernames, pub_times, descs):
        username, pub_time, desc = value
        content = {
            'username': username,
            'pub_time': pub_time,
            'desc': desc
        }
        contents.append(content)
    for content in contents:
        print(content)
        print("="*40)

def main():
    for x in range(1,11):
        url = "http://www.budejie.com/{}".format(x)
        parse_page(url)


if __name__ == "__main__":
    main()
