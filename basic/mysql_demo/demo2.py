#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 23:00
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='pymysql',port=3306)

cursor = conn.cursor()

cursor.execute("select 1")

# sql = """
#     insert into user(id,username,age,password) values(2,"alice",20,"222222")
# """
# cursor.execute(sql)
# conn.commit()

username = "spider"
age = 21
password = "333333"

sql = """
    insert into user(id,username,age,password) values(null,%s,%s,%s);
"""
cursor.execute(sql,(username, age, password))
conn.commit()
conn.close()