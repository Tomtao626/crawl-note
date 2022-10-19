#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: abstract_factory.py 
@time: 2020/12/04
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

import requests

url = "http://www.pythontip.com/python-patterns/detail/abstract_factory"

content = requests.get(url)
print(content.text)
