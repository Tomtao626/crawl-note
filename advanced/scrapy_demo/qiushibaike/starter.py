#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/10 23:22
# @Author : Tom_tao
# @Site : 
# @File : starter.py
# @Software: PyCharm

from scrapy import cmdline


# cmdline.execute("scrapy crawl qsbk".split())
cmdline.execute(["scrapy", "crawl", "qsbk"])