#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/13 23:36
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

from redis import ConnectionPool,StrictRedis

redis_url = "redis://127.0.0.1:6379"
pool = ConnectionPool.from_url(redis_url,decode_responses = True)

r = StrictRedis(connection_pool=pool)

print(r)