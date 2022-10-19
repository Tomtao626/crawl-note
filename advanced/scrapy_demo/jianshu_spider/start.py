#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/12 17:24
# @Author : Tom_tao
# @Site : 
# @File : start.py
# @Software: PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl jianshu".split())