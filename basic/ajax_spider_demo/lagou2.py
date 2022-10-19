#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/6 16:11
# @Author : Tom_tao
# @Site : 
# @File : lagou2.py
# @Software: PyCharm

import re
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LagouSpider(object):
    driver_path = r"d:\chromedriver\chromedriver.exe"

    def __init__(self):
        self.positions = list()
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']/span[last()]")))
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            if "pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(1)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        # 切换
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//sapn[@class='name']")))
        source = self.driver.page_source
        self.parse_detail_page(source)
        # 关闭详情页
        self.driver.close()
        # 切换至列表页
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spans = html.xpath("//dd[class='job_request']//span")
        salary = job_request_spans[0].xpath(".//text()")[0].strip()
        city = job_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub("[\s/]", "", city)
        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub("[\s/]", "", work_years)
        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub("[\s/]", "", education)
        desc = "".join(html.xpth("//dd[@class='job_bt']//text()")).strip()
        company_name = html.xpath("//h2[@class=fl]/text()")[0].strip()
        position = {
            'name': position_name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.positions.append(position)
        print(position)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
