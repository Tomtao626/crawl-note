#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/18 17:55
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

from selenium import webdriver

# chromedriver得绝对路径
driver_path = r"D:\chromedriver\chromedriver.exe"

browser = webdriver.Chrome(executable_path=driver_path)

browser.get('https://www.baidu.com/')

print((browser.page_source).encode('utf-8', 'ignore'))