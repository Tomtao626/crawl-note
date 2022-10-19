#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/19 23:11
# @Author : Tom_tao
# @Site : 
# @File : college.py
# @Software: PyCharm

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pymysql


class College:
    # 初始化
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.url = "http://xkkm.sdzk.cn/zy-manager-web/html/xx.html"
        self.conn = pymysql.connect('localhost', 'root', 'root')
        self.conn.select_db('college_bak')

    # 获取页面内容，返回Bs对象
    def get_page(self):
        try:
            response = requests.get(self.url, headers=self.headers).content
            page = BeautifulSoup(response, 'html.parser')
            return page
        except Exception as Err:
            print('Error1:', str(Err))

    # 解析页面内容，获取高校信息，添加到college_infos，并返回
    def get_college(self, page):
        college_infos = []
        # 先找到大表格，然后获取每一行的数据
        colleges = page.find('tbody', {'class': 'scrollTbody'}).find_all('tr')
        # 遍历每一行，获取高校信息
        for college in colleges:
            data = college.find_all('td')
            area = data[1].text
            college_id = data[2].text
            college_name = data[3].text
            college_site = data[5].find('a').get('href')
            # 组合信息，append
            college_infos.append((area, college_id, college_name, college_site))
        print('总计获取%s条数据' % str(len(college_infos)))
        return college_infos

    # 将数据插入数据库
    def insert_college(self, data):
        try:
            cur = self.conn.cursor()
            sql = "insert into college(area, college_id, college_name, college_site) values(%s, %s, %s, %s)"
            rows = cur.executemany(sql, tuple(data))
            self.conn.commit()
            self.conn.close()
            return rows
        except Exception as Err:
            print('数据插入失败！！！')
            print('Error2:', str(Err))


if __name__ == "__main__":
    college = College()
    data = college.get_college(college.get_page())
    rows = college.insert_college(data)
    print('总计插入%s条数据' % str(rows))
    print("-"*50)
    print("Done")