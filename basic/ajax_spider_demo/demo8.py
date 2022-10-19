#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 17:35
# @Author : Tom_tao
# @Site : 
# @File : demo8.py
# @Software: PyCharm

# 设置代理

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://117.88.4.29:3000")

driver_path = r"d:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get("http://httpbin.org/ip")