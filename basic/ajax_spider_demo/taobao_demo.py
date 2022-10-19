#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/25 12:22
# @Author : Tom_tao
# @Site : 
# @File : taobao_demo.py
# @Software: PyCharm

'''
    淘宝网实操，自动输入想要的商品关键字（如：手机），点击确定按钮搜索，跳转到登录界面使用二维码人工登录，再跳转到商品界面进行爬取商品信息。
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# driver_path = r"d:\chromedriver\chromedriver.exe"
driver_path = r"/Users/tao626/Documents/workspaces/selenium_driver_path/mac/chromedriver"
browser = webdriver.Chrome(driver_path)
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 8)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
input.send_keys('手机')
button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-search.tb-bg')))
button.click()
time.sleep(15)
img = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'J_ItemPic.img')))
price = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'price.g_price.g_price-highlight')))
name = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'J_ClickStat')))
num = 0
for i in img:
    print('第', num + 1, '个商品介绍：')
    print('img:', i.get_attribute('src'))
    print('price:', price[num].text)
    print('name:', name[num].text)
    num = num + 1
