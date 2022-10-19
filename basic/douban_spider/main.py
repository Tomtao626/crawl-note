#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/4 23:32
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

# 豆瓣电影爬虫
import requests
from lxml import etree
# 将目标网站上的页面数据抓取下来

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}

url = 'https://movie.douban.com/cinema/nowplaying/shiyan/'
response = requests.get(url,headers=headers)
text = response.text
# print(response.text)
# response.text 返回一个经过解码后的字符串 是str(Unicode)类型
# response.content 返回的是一个原生的字符串 未经过处理的bytes类型数据

# 将抓取的数据按照一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[1]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
movies = list()
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    year = li.xpath("@data-release")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    category = li.xpath("@data-category")[0]
    poster = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'year': year,
        'region': region,
        'director': director,
        'actors': actors,
        'category': category,
        'poster': poster
    }
    movies.append(movie)
print(movies)
