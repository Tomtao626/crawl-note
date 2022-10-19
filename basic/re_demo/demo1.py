#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/8 18:56
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm

import re

# 1.从开头匹配某个字符串
'''
    text = "hello"
    ret = re.match('he', text)
    print(ret.group())  # >> he
'''

# 2. . 匹配任意的字符 不能匹配换行符 \n
'''
    text = "hello"
    ret = re.match('.', text)
    print(ret.group())   # >> h    
'''

# 3. \d 从头匹配任意的数字(0-9)
'''
    text = "666"
    ret = re.match('\d', text)
    print(ret.group())
'''

# 4. \D 匹配任意的非数字
'''
    text = "hd.."
    ret = re.match('\D', text)
    print(ret.group())
'''

# 5. \s 匹配空白字符(\n \t \r 空格)
'''
    text = "\t"
    ret = re.match("\s", text)
    print(ret.group())
'''
# 6. \w 匹配 a-z A-Z 下划线 数字
'''
    text = "_a"
    ret = re.match("\w", text)
    print(ret.group())
'''

# 7. \W 匹配非数字，非下划线 非字母a-z A-Z
'''
    text = "+="
    ret = re.match("\W", text)
    print(ret.group())
'''

# 8. []组合的方式，只要满足中括号的字符，就可以匹配
'''
    text = "0719-4640498aaaa"
    ret = re.match("[\d\-]+", text)
    print(ret.group())
'''

# 9.替代方案
# \d === [0-9]
# \D === [^0-9]
# \w === [0-9a-zA-Z_]
# \W === [^0-9a-zA-Z_]

# 9. * 匹配0或任意多个字符
'''
    text = "0999"
    ret = re.match("\d*", text)
    print(ret.group())
'''

# 10. + 匹配一个或多个字符
'''
    text = "abcd+"
    ret = re.match("\w+", text)
    print(ret.group())
'''

# 11. ? 匹配一个或者0个(有  只会匹配一个)
'''
    text = "abcd"
    ret = re.match("\w?", text)
    print(ret.group())
'''

# 12. {m} 匹配m个字符
'''
    text = "123"
    ret = re.match("\w{2}", text)
    print(ret.group())
'''

# 13. {m,n} 匹配m到n个字符
'''
    text = "abcd"
    ret = re.match("\w{1,3}", text)  # 匹配三个字符
    print(ret.group())
'''

# 14. ^ (脱字号)  以什么开头
'''
    text = "hello"
    # ret = re.match("^h", text)
    ret = re.search("^h", text)
    print(ret.group())
'''

# 15. $ 以什么结尾
'''
    text = "777jdhsj@vip.qq.com"
    ret = re.match("\w+@vip.qq.com$", text) # 以vip.qq.com结尾
    print(ret.group())
'''

# 16. | 匹配多个字符串或者表达式
'''
    text = "https"
    ret = re.match("(ftp|http|https)$", text)
    print(ret.group())
'''

# 17.贪婪模式和非贪婪模式
# 贪婪模式：正则尽可能多的匹配全部字符
# 非贪婪模式：正则尽可能少的匹配字符
'''
    text = "0909329"
    ret = re.match("\w+", text)  # 贪婪模式  匹配全部符合的  输出 0909329
    ret = re.match("\w+?", text) # 非贪婪模式  匹配符合的哪一个字符  输出 0
    print(ret.group())
'''
'''
    text = "<h1>TEST</h1>"
    ret = re.match("<.+>", text) # 贪婪模式  输出 <h1>
    # 之相匹配前一个标签<h1>  结果匹配了全部字符<h1>TEST</h1>  因为其也符合<.+>类型
    ret = re.match("<.+?>", text) # 非贪婪模式  输出 <h1>TEST</h1>
    # 满足条件 只会匹配符合的第一个字符
    print(ret.group())
'''
# 匹配 0 - 100之间的数字
# 可以出现的情况 1 2 3 10 100 99
# 不能出现的情况 09 101
# 有三种情况 1 99 100
'''
    text = "100"
    ret = re.match("[1-9]\d?$|100$", text)  # 非贪婪模式
    print(ret.group())
'''
# 而如果text=101，那么就会抛出一个异常。示例代码如下：
# text = '101'
# ret = re.match('[1-9]?\d$|100$',text)
# print(ret.group())
# >> AttributeError: 'NoneType' object has no attribute 'group'