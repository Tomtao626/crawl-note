#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/20 4:54
# @Author : Tom_tao
# @Site : 
# @File : demo6.py
# @Software: PyCharm

from selenium import webdriver

driver_path = r"d:\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

for cookie in driver.get_cookies():
    print(cookie)

print("*"*40)

print(driver.get_cookie("PSTM"))
driver.delete_cookie("PSTM")
print("*"*40)

print(driver.get_cookie("PSTM"))

driver.delete_all_cookies()
