#!/usr/bin/env python
# encoding: utf-8
'''
@author: qiuyan
@contact: winston@peipeiyun.com
@file: config.py
@time: 2019/2/18 3:31 PM
@desc:
'''

broker_url = 'redis://127.0.0.1:6379/1'
result_backend = 'redis://127.0.0.1:6379/2'


# db_conf ={
#     "host": "rm-uf65900c10532c07790130.mysql.rds.aliyuncs.com",  # 数值类型：字符串
#     "port": 3306,  # 数值类型：整型
#     "user": "mayun",  # 数值类型：字符串
#     "password": "Qiuyan@123520",  # 数值类型：字符串
#     "database": "mayun",  # 选择使用的database, 数值类型：字符串
# }

REDIS = {
    'host':'127.0.0.1',
    'port':6379,
    'db':1,
    'username':'username',
    'password':'passwrod'
}