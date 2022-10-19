#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 17:59
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

import json

persons = [
    {
        'username':'tom',
        'age': 20,
        'country': 'china'
    },
    {
        'username': 'alice',
        'age': 21,
        'country': 'russia'
    },
    {
        'username': '张三',
        'age': 22,
        'country': 'US'
    }
]
json_str = json.dumps(persons)

# 使用文件模块操作json数据存入文件
# with open('persons.json', 'w') as fp:
#     fp.write(json_str)

# 使用json的dump函数存入文件
with open('person.json', 'w', encoding='utf-8') as fp:
    json.dump(persons, fp, ensure_ascii=False) # fp是指针

# 如果json数据中有中文，则需要转码utf-8  并在进行dump文件时，关闭编码属性 ensure_ascii=False
