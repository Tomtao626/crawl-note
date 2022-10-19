#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 18:54
# @Author : Tom_tao
# @Site : 
# @File : demo9.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver_path = r"d:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))
print(submitBtn.get_attribute("value"))
# 保存截屏
driver.save_screenshot('baidu.png')
