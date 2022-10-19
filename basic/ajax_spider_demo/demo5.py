#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/19 15:12
# @Author : Tom_tao
# @Site : 
# @File : demo5.py
# @Software: PyCharm

# 行为链
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"d:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')

action = ActionChains(driver)
action.move_to_element(inputTag)
action.send_keys_to_element(inputTag, 'python')
action.move_to_element(submitTag)
action.click(submitTag)
action.perform()