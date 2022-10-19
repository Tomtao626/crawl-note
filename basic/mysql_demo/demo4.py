#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 23:32
# @Author : Tom_tao
# @Site : 
# @File : demo4.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host="localhost",user="root",password="root",database="pymysql",port=3306)
cursor = conn.cursor()

# insert, delete, update操作都需要执行commit操作

# 删除操作
'''
    sql = """
        delete from user where id=1;
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()
'''

# 更新操作
sql = """
    update user set username="张三" where id=2;
"""
cursor.execute(sql)
conn.commit()
conn.close()
