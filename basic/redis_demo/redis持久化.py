#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/14 0:16
# @Author : Tom_tao
# @Site : 
# @File : redis持久化.py
# @Software: PyCharm

# redis持久化就是把内存中的数据写入到磁盘中去，防止服务宕机了内存数据丢失
# 两种持久化方式
# RDB  redis datbase
# 核心函数 rdbSave() 生成rdb文件  rdbLoad() 从磁盘文件加载到内存中

# AOF append-only
# 每当执行服务(定时)任务或者函数时flushAppendOnlyFile函数都会调用
# 这个函数主要执行以下两个工作
# aof写入保存:
# write 根据条件 将aof_buf中的缓存xierudaoAOF文件
# save 根据条件 调用fsync或fdatasync函数 将AOF文件保存到磁盘中
# 存储结构：
# 内容是redis通讯协议(RESP)格式的命令文本存储
# 比较
# aof比rdb更新频率高 优先使用aof还原数据
# aof比rdb更安全也更大
# rdb性能优于aof
# 如果两个都配置了  优先加载aof

# RESP redis客户端和服务端之间通信的一种协议
# 即 客户端以规定格式的形式发送命令给服务器；服务器在执行最后一条命令后，返回结果。

"""
客户端发送命令的格式(类型)：5种类型
间隔符号，在Linux下是\r\n，在Windows下是\n
"""

"""
1. 简单字符串 Simple Strings, 以 "+"加号 开头
      格式：+ 字符串 \r\n
    字符串不能包含 CR或者 LF(不允许换行)
    eg: "+OK\r\n"
    注意：为了发送二进制安全的字符串，一般推荐使用后面的 Bulk Strings类型

2. 错误 Errors, 以"-"减号 开头
　　格式：- 错误前缀 错误信息 \r\n
    错误信息不能包含 CR或者 LF(不允许换行)，Errors与Simple Strings很相似，不同的是Erros会被当作异常来看待

3. 整数型 Integer， 以 ":" 冒号开头
　　格式：: 数字 \r\n

4. 大字符串类型 Bulk Strings, 以 "$"美元符号开头，长度限制512M
　　格式：$ 字符串的长度 \r\n 字符串 \r\n
    字符串不能包含 CR或者 LF(不允许换行);

5. 数组类型 Arrays，以 "*"星号开头
　　格式：* 数组元素个数 \r\n 其他所有类型 (结尾不需要\r\n)
    注意：只有元素个数后面的\r\n是属于该数组的，结尾的\r\n一般是元素的
"""