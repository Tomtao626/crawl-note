#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/13 23:47
# @Author : Tom_tao
# @Site : 
# @File : redis_事务.py
# @Software: PyCharm

# 事务的特点
# 事务是一个单独隔离的操作 事务中的所有命令都会序列化、按顺序地执行 在执行过程中 不会被其他客户端发送过来的命令请求打断
# 事务是一个原子操作 命令要么全部执行 要么全部不执行
# 事务有四个性质  ACID  原子性 一致性  隔离性 持久性
# 事务从开始到执行会经历三个阶段：
# 开始事务 命令入队  执行事务

# 代码示例：
import redis
import sys

def run():
    try:
        conn = redis.StrictRedis('127.0.0.1')
        # python中redis事务是通过pipeline的封装实现的
        pipe = conn.pipeline()
        pipe.sadd('s001','a')
        sys.exit()
        # 在事务还未提交前推出 所以事务不会被执行
        pipe.sadd('s001','b')
        pipe.execute()
        pass
    except Exception as err:
        print(err)
        pass

if __name__ == '__main__':
    run()