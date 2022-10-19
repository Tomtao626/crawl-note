#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/5 11:17
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

from lxml import etree
import requests

BASE_DOMAIN = 'https://dytt8.net'
req_url = 'https://dytt8.net/html/gndy/dyzz/list_23_1.html'
HEADERS = {
    'Referer': 'https://dytt8.net/html/gndy/dyzz/list_23_2.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}


# response.text
# response.content
# requests库默认会使用自己猜测的编码方式将抓取下来的网页进行解码，然后存储到text属性中
# 在电影天堂网页中，requests库将其编码猜错，故出现乱码

def get_detail_urls(url):
    response = requests.get(req_url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda req_url: BASE_DOMAIN + req_url, detail_urls)
    return detail_urls


def parse_detail_page(req_url):
    movie = dict()
    response = requests.get(req_url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title
    zoom = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoom.xpath(".//img/@src")
    cover = imgs[0]
    movie['cover'] = cover

    # movie['screenshot'] = screenshot

    def parse_info(info, rule):
        return info.replace(rule, "").strip()

    infos = zoom.xpath(".//text()")
    for index, info in enumerate(infos):
        # print(index)
        # print(info)
        # print("*"*30)
        if info.startswith("◎年　　代"):
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎语　　言"):
            info = parse_info(info, "◎语　　言")
            movie['language'] = info
        elif info.startswith("◎上映日期"):
            info = parse_info(info, "◎上映日期")
            movie['up_time'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎文件大小"):
            info = parse_info(info, "◎文件大小")
            movie['file_total'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['Running time'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎编　　剧"):
            info = parse_info(info, "◎编　　剧")
            movie['writers'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎标　　签"):
            info = parse_info(info, "◎标　　签")
            movie['tags'] = info
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("◎"):
                    break
            movie['profile'] = info
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie


def spider():
    base_url = 'https://dytt8.net/html/gndy/dyzz/list_23_{}.html'
    # 控制总共有7页
    movies = list()
    for x in range(1, 8):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        # 遍历一页当中所有电影详情url
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
        print(movies)


if __name__ == "__main__":
    spider()
