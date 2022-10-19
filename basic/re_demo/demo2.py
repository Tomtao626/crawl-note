#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/8 21:14
# @Author : Tom_tao
# @Site : 
# @File : demo2.py
# @Software: PyCharm

import re

# 1.验证手机号码

'''
    text = "18372620761"
    ret = re.match("1[34578]\d{9}", text)
    print(ret.group())
'''


# 2.验证邮箱

'''
    text = "tom_tao626@qq.com"
    ret = re.match("\w+@[a-z0-9A-Z]+\.[a-z]+", text)
    print(ret.group())
'''

# 3.验证URL

'''
    text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    ret = re.match("(http|https|ftp)://[^\s]+", text)
    print(ret.group())
'''

# 4.验证身份证
'''
    text = "42032319961101341X"
    ret = re.match("\d{17}[\dxX]", text)
    print(ret.group())
'''