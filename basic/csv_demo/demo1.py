#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 18:35
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

import csv

with open('stock.csv', 'r') as fp:
    # reader是一个迭代器
    reader = csv.reader(fp)
    next(reader)
    for x in reader:
        name = x[1]
        time = x[2]
        volumn = x[-8]
        print({'name':name,'time':time,'volumn':volumn})


def read_csv_demo2():
    with open('stock.csv','r') as fp:
        # 使用DictReader创建的reader对象
        reader = csv.DictReader(fp)
        # 不会包含标题那行的数据
        for x in reader:
            # reader是一个迭代器，遍历这个迭代器，返回的是一个字典
            value = {"name": x['简称'], "time": x['日期'], "volumn": x['总市值(元)']}
            print(value)

if __name__ == '__main__':
    read_csv_demo2()