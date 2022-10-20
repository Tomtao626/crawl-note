#!/usr/bin/env python
# coding:utf-8

# mysql连接配置:数据库
mysql_config = {
    "matchdb": {
        "host": "localhost",  # 数值类型：字符串
        "port": 3306,  # 数值类型：整型
        "user": "root",  # 数值类型：字符串
        "password": "1qazxsw2",  # 数值类型：字符串
        "database": "matchdb",  # 选择使用的database, 数值类型：字符串
    },
}

# redis连接配置
"""
redis_config = {
    "suizhu": {
        "host": "127.0.0.1",  # 数值类型：字符串
        "port": 6379,  # 数值类型：整型
        "db": 2,  # 选择使用的database, 数值类型：整型
        "retry": 3,  # 重试次数,数值类型：整型
    },
}
"""


# mongo连接配置
"""
mongo_config = {
    "user": {
        "host": "192.168.10.11",
        "port": 27017,
        "dbname": "xxxx",
        "user": "",
        "pwd": "",
        "timeout": 5,
        "retry": 3
    },
    "price": {
        "host": "192.168.10.10",
        "port": 27017,
        "dbname": "xxxx",
        "user": "",
        "pwd": "",
        "timeout": 5,
        "retry": 3
    },
}
"""
