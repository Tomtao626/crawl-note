#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/11 15:14
# @Author : Tom_tao
# @Site : 
# @File : start.py
# @Software: PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl douban".split())