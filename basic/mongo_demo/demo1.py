#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/10 23:36
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm


import pymongo

#获取链接mongodb的对象
client = pymongo.MongoClient("127.0.0.1", port=27017)

db = client.zhihu

collection = db.qa

# 插入写入数据
# collection.insert({"username": "tom"})
# collection.insert_many([
#     {"username": "tao",
#      "work":"teacher",
#      },
#     {
#         "username": "alice",
#         "work": "doctor",
#     }
# ])

# 查找数据
# 获取集合中所有数据
# cursor = collection.find()
# for x in cursor:
#     print(x)
# 获取集合中的一条数据
# result = collection.find_one({"work":"doctor"})
# print(result)

# 更新数据
# collection.update_one({"username":"alice"},{"$set":{"username":"ahahah"}})
# collection.update_many({"username":"alice"},{"$set":{"username":"ahahah"}})

# 删除数据
# collection.delete_one({"username":"alice"})
# collection.delete_many({"username":"alice"})