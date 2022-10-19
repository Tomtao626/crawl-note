
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/13 22:04
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

import pymongo

db_config = {
    'type':'mongo',
    'host':'127.0.0.1',
    'port':'27017',
    'user':'spider_data',
    'passwd':'root',
    'db_name':'spider_data',
}

class Mongo():

    def __init__(self,db=db_config['db_name'],username=db_config['username'],password=db_config['passwd']):
        self.client = pymongo.MongoClient(f'mongodb://{db_config["host"]}:{db_config["port"]}')
        self.username = username
        self.password = password
        if self.username and self.password:
            self.dbl = self.client[db].authenticate(self.username,self.password)
        self.dbl = self.client[db]

    def find_data(self):
        data = self.dbl.test.find({"status":0})
        gen = (item for item in data)
        return gen


if __name__ == '__main__':
    m = Mongo()
    print(m.find_data())