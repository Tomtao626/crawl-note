#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/19 11:54
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software: PyCharm

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

driver_path = r"d:\chromedriver\chromedriver.exe"

browser = webdriver.Chrome(executable_path=driver_path)
browser.get('https://www.baidu.com/')

# 根据标签id获取
# inputTag = browser.find_element_by_id('kw')
# inputTag = browser.find_elements(By.ID, 'kw')

# 根据标签name获取
# inputTag = browser.find_element_by_name('wd')
# inputTag = browser.find_elements(By.NAME, 'wd')

# 根据标签的类名class 获取
# inputTag = browser.find_element_by_class_name('s_ipt')
# inputTag = browser.find_elements(By.CLASS_NAME, 's_ipt')

# 根据xpath提取标签
# inputTag = browser.find_element_by_xpath("//input[@id='kw']")
# inputTag = browser.find_elements(By.XPATH, "\\input[@id='kw']")

# 根据css选择器获取
# 使用>直接获取子元素  即下面的input
# inputTag = browser.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag = browser.find_elements(By.CSS_SELECTOR, ".quickdelete-wrap > input")

# 获取多个符合条件的标签
inputTag = browser.find_elements_by_css_selector(".quickdelete-wrap > input")[0]  # 返回是一个列表  故取第一个 方可传入值
print(inputTag)
inputTag.send_keys('python')
 # 如果只是想要解析网页中的数据，则推荐将网页源代码扔给lxml来解析，因为lxml底层使用的是c，所以解析效率会更高
 # html = etree.HTML(browser.page_source)
 # 如果需要对元素进行一些操作，比如给一个文本框输入值，或者点击某个按钮，就必须使用selenium给我们提供的这些查找元素的方法