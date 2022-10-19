#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/20 10:15
# @Author : Tom_tao
# @Site : 
# @File : demo7.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver_path = r"d:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.baidu.com/")

driver.execute_script("window.open('https://www.douban.com/')")
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
print(driver.current_url)
print(driver.page_source)

# 虽然在窗口中切换到了新的页面，但driver并未切换
# 如果想要在代码中切换到新的页面，并做一些爬虫
# 那么应该使用driver.switch_to_window来切换到指定的窗口
# 从driver.window_handlers中取出具体第几个窗口
# driver.window_handlers是一个列表，里面装的都是窗口句柄
# 它会按照打开页面的顺序来存储窗口的句柄


# 隐式等待
# driver.implicitly_wait(5)
# driver.find_element_by_id('efdfdfdfd')


# 显式等待
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, 'form_email'))
)
print(element)