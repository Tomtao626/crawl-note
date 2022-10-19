#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/10 16:41
# @Author : Tom_tao
# @Site : 
# @File : main.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GrabVote(object):
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.my_url = "https://kyfw.12306.cn/otn/view/index.html"
        self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.commit_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        # win
        # self.driver = webdriver.Chrome(executable_path="d:\chromedriver\chromedriver.exe")
        # mac
        self.driver = webdriver.Chrome(executable_path="/Users/tao626/Documents/workspaces/selenium_driver_path/mac/chromedriver")

    def _login(self):
        self.driver.get(self.login_url)
        # 显式等待
        WebDriverWait(self.driver, 1000).until(
            EC.url_to_be(self.my_url)
        )
        print("登录成功")

    def wait_input(self):
        self.from_sattion = input("起始站:")
        self.to_station = input("目的地:")
        # 时间格式 yyyy-mm-dd的方式
        self.depart_time = input("出发时间:")
        self.passengers = input("乘客姓名(如有多个乘客，用英文逗号隔开):").split(",")
        self.trains = input("车次(如有多个车次，用英文逗号隔开):").split(",")

    def _order_ticket(self):
        # 跳转到查余票界面
        self.driver.get(self.search_url)
        # 等待出发地是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "fromStation"), self.from_sattion)
        )
        # 等待目的地是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )
        # 等待出发时间是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )
        # 等待查询按钮是否可以被点击
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )
        # 如果可以点击 那么就知道这个查询按钮，执行点击事件
        SearchBtn = self.driver.find_element_by_id("query_ticket")
        SearchBtn.click()

        # 在点击了查询按钮后，车次信息是否加载完毕
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
        )

        # 找到所有没有dattrain属性的tr标签 存储车次信息
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        # 遍历所有满足条件的tr标签
        for tr in tr_list:
            train_number = tr.find_element_by_class_name("number").text
            if train_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                if left_ticket == "有" or left_ticket.isdigit:
                    orderBtn = tr.find_element_by_class_name("btn72")
                    orderBtn.click()

                    # 等待是否进入了确认乘客的页面
                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.XPATH, ".//ul[@id='normal_passenger_id']/li"))
                    )
                    # 找到乘客信息
                    li_list = self.driver.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li")
                    for li in li_list:
                        if li.text in self.passengers:
                            print(li.text)
                            # 找到乘客对应的checkbox 并执行点击事件
                            check_box = li.find_element_by_class_name('check')
                            check_box.click()
                    # 找到提交按钮 执行点击事件
                    commitBtn = self.driver.find_element_by_id('submitOrder_id')
                    commitBtn.click()
                    # 等待确认弹窗出现
                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'dhtmlx_wins_body_outer'))
                    )
                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.ID, 'qr_submit_id'))
                    )
                    # 找到确认按钮 执行点击事件
                    confirmBtn = self.driver.find_element_by_id('qr_submit_id')
                    confirmBtn.click()
                    # 因为确认按钮可能会未被点击，所以用一个while循环点击，若正确点击了确认按钮，则调出while循环
                    while confirmBtn:
                        confirmBtn.click()
                        confirmBtn = self.driver.find_element_by_id('qr_submit_id')
                    # 打开一个新的窗口，并将driver转换成新的窗口
                    self.driver.execute_script('window.open("%s")' % self.order_url)
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    # 再次等待车次信息出现
                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
                    )

    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == '__main__':
    spider = GrabVote()
    spider.run()
