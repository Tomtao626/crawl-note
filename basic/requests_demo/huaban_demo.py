#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/25 14:21
# @Author : Tom_tao
# @Site : 
# @File : huaban_demo.py
# @Software: PyCharm

# 花瓣网

import json
import re
import time
from hashlib import md5

import requests

headers = {
    'X-Requested-With': 'XMLHttpRequest'
}


def get_one_page(url):
    html = requests.get(url).text
    images_pattern = re.compile('app.page\["pins"\].*?"(.*?)extra.*?}}]', re.S)
    result1 = re.search(images_pattern, html).group(0)
    result = re.findall('"file_length":0, "pin_id":(\d+?),', result1)
    return result


def save_image(url):
    print(url)
    try:
        response = requests.get(url)
        img_url = 'http://hbimg.huabanimg.com/' + re.findall('"key":"(.*?)"', response.text)[2]
        time.sleep(1)  # 停顿1秒
        image = requests.get(img_url).content
        title = md5(image).hexdigest() + '.jpg'
        print(title)
        print('+' * 20 + '保存完成')
        with open('d:/code/python_crawler/requests_demo/girl_pic/' + title, 'wb') as file:  # 图片保存在D盘新建文件夹内，需先新建此文件夹
            file.write(image)
    except IndexError:
        print('保存失败')


def get_new_url(i, pin):
    for i in range(i):
        new_url = 'https://huaban.com/favorite/beauty/?k7162g1h&max=' + str(pin) + '&limit=20&wfl=1'
        response = requests.get(new_url, headers=headers)
        text = json.loads(response.text)
        data = text['pins']
        pin = data[-1]['pin_id']
        for item in data:
            yield make_url(str(item['pin_id']))


def make_url(id):
    url = 'https://huaban.com/pins/' + id
    return url


def main():
    url = 'https://huaban.com/explore/guzhuangmeinv/?'  # 网址可更改
    result = get_one_page(url)  # 是第一页的pin列表
    for item in result:
        save_image(make_url(item))
    pin = result[-1]
    for item in get_new_url(10, pin):
        save_image(item)


if __name__ == '__main__':
    main()
