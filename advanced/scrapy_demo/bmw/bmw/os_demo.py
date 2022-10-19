#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/11 17:17
# @Author : Tom_tao
# @Site : 
# @File : os_demo.py
# @Software: PyCharm

import os

# 获取当前文件所在目录路径
file_path1 = os.path.dirname(__file__)
print(file_path1)  #D:/code/python_crawler/scrapy_demo/bmw/bmw

# 获取当前文件所在目录的上一级目录
file_path2 = os.path.dirname(os.path.dirname(__file__))
print(file_path2)  #D:/code/python_crawler/scrapy_demo/bmw

# 目录拼接
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
print(file_path)   # D:/code/python_crawler/scrapy_demo/bmw\images

# 判断文件夹是否存在
if not os.path.exists(file_path):
    # 创建文件夹
    os.mkdir(file_path)
else:
    print("images文件夹存在")