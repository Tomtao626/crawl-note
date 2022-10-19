#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 19:13
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

import csv

def writer_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        ('张三',22,180),
        ('赵六',22,190),
        ('李四',22,187)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

def writer_csv_demo2():
    headers = ['username', 'age', 'height']
    values = [
        {'username': '张三', 'age': 22, 'height': 180},
        {'username': '赵六', 'age': 21, 'height': 190},
        {'username': '李四', 'age': 20, 'height': 187}
    ]
    with open('classroom1.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        # 写入表头数据时，需要调用writerheader方法
        writer.writeheader()
        writer.writerows(values)


if __name__ == '__main__':
    writer_csv_demo1()
    writer_csv_demo2()

