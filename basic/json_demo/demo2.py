#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 18:16
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

import json

json_str = '[{"username": "tom", "age": 20, "country": "china"}, {"username": "alice", "age": 21, "country": "russia"}, {"username": "张三", "age": 22, "country": "US"}]'
print(eval(json_str))
# persons = json.loads(json_str)
# print(type(persons))
# print(persons)

with open('person.json', 'r', encoding='utf-8') as fp:
    persons = json.load(fp)
print(type(persons))
print(persons)