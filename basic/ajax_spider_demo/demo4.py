#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/19 12:39
# @Author : Tom_tao
# @Site : 
# @File : demo4.py
# @Software: PyCharm

# input框嵌入值 再清除
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver_path = r"d:\chromedriver\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=driver_path)
# browser.get('https://www.baidu.com/')
# inputTag = browser.find_elements(By.ID, 'kw')[0]
# inputTag.send_keys('python')
# time.sleep(3)
# inputTag.clear()

# 操作checkbox
# from selenium import webdriver
# import time
#
# driver_path = r"d:\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.52pojie.cn/')
#
# rememberBtn = driver.find_element_by_name('cookietime')
# time.sleep(3)
# rememberBtn.click()
# time.sleep(3)
# rememberBtn.click()


# 操作select标签
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# driver_path = r"d:\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('http://kfq.yangzhou.gov.cn/kfq/selectlink/201304/c5ddcc30c14447fabaa23d471fab2433.shtml')
#
# selectBtn = Select(driver.find_element_by_name('allContry'))
# 通过index选中
# selectBtn.select_by_index(1)
# 通过value选中
# selectBtn.select_by_value('http://www.ndrc.gov.cn/')
# 根据可使的文本选中
# selectBtn.select_by_visible_text('国家发展和改革委员会')
# 取消选中所有选项
# selectBtn.deselect_all()

# 操作点击事件
from selenium import webdriver
import time

driver_path = r"d:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
time.sleep(3)
submitTag = driver.find_element_by_id('su')
submitTag.click()