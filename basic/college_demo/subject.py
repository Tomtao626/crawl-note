#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/20 10:50
# @Author : Tom_tao
# @Site :
# @File : subject.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import pymysql
from threading import Thread


class Subject:
    def __init__(self, param):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.url = "http://xkkm.sdzk.cn/zy-manager-web/gxxx/searchInfor"
        self.param = param

    def get_page(self):
        try:
            response = requests.post(self.url, data=self.param, headers=self.headers).content
            page = BeautifulSoup(response, 'html.parser')
            return page
        except Exception as Err:
            print('Error1:', str(Err))

    def get_subject(self, page):
        college_id = self.param['dm']
        subject_infos = []
        subjects = page.find('div', {'id': 'ccc'}).find_all('tr')
        for subject in subjects:
            data = subject.find_all('td')
            gradation = data[1].text
            classification = data[2].text.strip()
            subject = data[3].text
            # 提取专业详情
            temp = str(data[4]).replace("\n", "").replace("\t", "")
            item = re.findall(r"\w+<br/>", temp)
            item.remove(item[0])
            major = "/".join(item).replace("<br/>", "")
            # 组合数据
            subject_infos.append((college_id, gradation, classification, subject, major))
        return subject_infos

    def insert_subject(self):
        page = self.get_page()
        data = self.get_subject(page)
        college_name = self.param['mc']
        db = DataBase()
        sql = "insert into major(college_id, gradation, classification, subject, major) values(%s,%s,%s,%s,%s)"
        rows = db.cur.executemany(sql, tuple(data))
        db.conn.commit()
        db.close()
        print(str(college_name), ":", str(rows), "条数据插入完成")


class DataBase:
    host = "localhost"
    user = "root"
    password = "root"
    database = "college_bak"

    def __init__(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()


def get_college():
    db = DataBase()
    sql = 'select college_id,college_name from college'
    db.cur.execute(sql)
    result = db.cur.fetchall()
    db.close()
    return result


if __name__ == "__main__":
    college_data = list(get_college())
    # 测试用
    college_data = college_data[:5]
    counts = len(college_data)
    print('正在获取', str(counts), '所高校的专业选课要求信息')
    # 开启多线程
    my_threads = []
    try:
        while True:
            # 开启线程数
            for i in range(5):
                data = college_data.pop()
                param = {'dm': data[0], 'mc': data[1]}
                subject = Subject(param)
                my_thread = Thread(target=subject.insert_subject())
                my_threads.append(my_thread)
                my_thread.start()
    except Exception as Err:
        print('Error2:', str(Err))
    finally:
        for thread in my_threads:
            thread.join()

        print('+'*50)
        print('Done')









