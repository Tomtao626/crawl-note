#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/25 12:02
# @Author : Tom_tao
# @Site : 
# @File : mzcww_pic.py
# @Software: PyCharm


# [url]http://mzsock.com[/url] 美足船袜网
# -*- coding: UTF-8 -*-

import os
import re
import time

import requests
from fake_useragent import UserAgent


class Mzsock():
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}

    def get_categroy_url(self):
        url = "http://mzsock.com"
        response = requests.get(url, headers=self.headers).text
        ul = re.findall(r'<ul id="chenxing_menu" class="cx_menu l">(.+?)</ul>', response, re.S)[0]
        categroy_urls = re.findall(r'<li id=".+?"><a href="(.+?)">.+?</a></li>', ul, re.S)[1:-1]
        return categroy_urls

    def get_urllist(self, categroy_urls):
        urllist = []
        for url in categroy_urls:
            response = requests.get(url, verify=False, headers=self.headers).text
            num = re.findall(r'</i>共找到.+?>(.+?)</em>篇帖子</span>', response, re.S)[0]
            pagenum = round(int(num) / 20)  # 取整，四舍五入
            print(pagenum)
            for i in range(1, pagenum + 1):
                pageurl = f'{url}page/{i}/'
                urllist.append(pageurl)
        return urllist

    def get_contentlist(self, urllist):
        contentlist = []
        for url in urllist:
            response = requests.get(url, headers=self.headers).text
            div = re.findall(r'<ul class="post-list cl" id="post-list">(.+?)</ul>', response, re.S)[0]
            hrefs = re.findall(r'<a class="img" href="(.+?)" title=".+?" target="_blank">', div, re.S)
            contentlist.extend(hrefs)
            print(hrefs)
        return contentlist

    def get_content(self, contentlist):
        for url in contentlist:
            response = requests.get(url, headers=self.headers).text
            h1 = re.findall(r'<h1>(.+?)[(](.+?)[)]</h1>', response, re.S)[0]
            title = h1[0]
            title = re.sub(r'[\|\/\<\>\:\*\?\\\"]', "_", title)  # 剔除不合法字符
            print(title)
            os.makedirs(f'mzsock/{title}/', exist_ok=True)  # 创建目录
            page_num = h1[1][6:-7]
            page_num = page_num.split('/')[1]
            print(page_num)
            for i in range(1, int(page_num) + 1):
                content_url = f'{url[:-5]}_{i}.html'
                content_response = requests.get(content_url, headers=self.headers).text
                div = \
                    re.findall(r'<div class="picsbox picsboxcenter chenxing_pic_images">(.+?)</div>', content_response,
                               re.S)[0]
                img_urls = re.findall(r'<img src="(.+?)"  alt=".+?" width', div, re.S)
                x = 1
                for img_url in img_urls:
                    img_name = f'{i}_{x}{img_url[-4:]}'
                    self.bctp(f'mzsock/{title}/', img_url, img_name)
                    x = x + 1

    def bctp(self, lj, img_url, img_name):
        print("开始下载图片！")
        try:
            r = requests.get(img_url, timeout=5, headers=self.headers)
            with open(f'{lj}/{img_name}', 'wb') as f:
                f.write(r.content)
                print(f'下载{img_name}图片成功！')
                time.sleep(1)
        except Exception as e:
            if "port=443): Read timed out" in str(e):
                time.sleep(2)
                try:
                    r = requests.get(img_url, timeout=5, headers=self.headers)
                    with open(f'{lj}/{img_name}', 'wb') as f:
                        f.write(r.content)
                        print(f'下载{img_name}图片成功！')
                except Exception as e:
                    print(f'下载{img_name}图片失败！')
                    print(f'错误代码：{e}')
                    with open(f'{lj}/spider.txt', 'a+', encoding='utf-8') as f:
                        f.write(f'错误代码：{e}---下载 {img_url} 图片失败\n')
            else:
                print(f'下载{img_name}图片失败！')
                print(f'错误代码：{e}')
                with open(f'{lj}/spider.txt', 'a+', encoding='utf-8') as f:
                    f.write(f'错误代码：{e}---下载 {img_url} 图片失败\n')


if __name__ == '__main__':
    spider = Mzsock()
    categroy_urls = spider.get_categroy_url()
    urllist = spider.get_urllist(categroy_urls)
    contentlist = spider.get_contentlist(urllist)
    spider.get_content(contentlist)
