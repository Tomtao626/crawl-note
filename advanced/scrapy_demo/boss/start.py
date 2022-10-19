#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/12 15:19
# @Author : Tom_tao
# @Site : 
# @File : start.py
# @Software: PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl zhipin".split())