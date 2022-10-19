#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/18 18:05
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

from selenium import webdriver
import time

driver_path = r"d://chromedriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)
browser.get('https://www.baidu.com/')

time.sleep(5)

# 关闭当前页面
# browser.close()

# 推出浏览器
browser.quit()