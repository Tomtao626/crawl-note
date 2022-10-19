#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 23:18
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software:

import pymysql

conn = pymysql.connect(host="localhost",user="root",password="root",database="pymysql",port=3306)
cursor = conn.cursor()

# sql = """
#     select username,age,password from user where id=1;
# """

# fetchall()
# sql= """
#     select * from user;
# """
# cursor.execute(sql)
# # 查询全部数据
# results = cursor.fetchall()
# for result in results:
#     print(result)


# fetchone()
# sql= """
#     select * from user;
# """
# cursor.execute(sql)
# while True:
#     查询单条数据
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break
# conn.close()


# fetchmany() 查询任意多少条记录
sql = """
    select * from user;
"""
cursor.execute(sql)
results = cursor.fetchmany(2) # 查询两条
for result in results:
    print(result)