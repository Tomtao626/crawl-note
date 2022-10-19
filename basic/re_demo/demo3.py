#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 12:25
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software: PyCharm


import re

# 在正则表达式中,"$" 本就具有特殊含义 用于匹配字符以什么结束
# 故此时采用"/"转义字符 进行转义
'''
    text = "Apple iphone 11pro max price is $999"
    ret = re.search("\$\d+", text)
    print(ret.group())
'''

# text = "\n"
# print(text)
# python中 如果不经过转义 会直接打印 换行
# 想打印出"\n"  则需要 对"\n" 使用"\"进行转义  即"\\n"
'''
    text = "\\n"
    print(text)  # 输出 \n
'''


'''
text = "\\n" # == "\n"
    # 在python中"\\n" == "\n"  因为使用"\"进行了转义
    # 故 "\\\\n" == "\\n"  第一个\对第二个\进行转义 第三个\对\n进行转义
    # 在正则表达式中 "\\n" == \n
    ret = re.match("\\\\n", text)
    print(ret.group()) # 输出 \n
'''

# 使用原生字符串 
# text = r"\n"
# print(text) # 输出 \n
# r == raw  原生字符串  不会对\n进行转义  该是什么就是什么
'''
    text = "\c"
    ret = re.match(r"\\c", text)
    print(ret.group())
'''

# 分组 group
'''
text = "Apple's price is $299.Orange's price is $999"
ret = re.match(".*(\$\d+).*(\$\d+)", text)
print(ret.group())  # 打印全部符合条件的字符 == print(ret.group(0))
print(ret.group(1))  # 打印第一个符合条件的字符
print(ret.group(2))  # 打印第二个符合条件的字符
# 所有的子分组都拿出来
print(ret.groups())  # 打印全部符合的子分组的字符
'''

# findall() 函数
'''
    text = "Apple's price is $299.Orange's price is $999"
    ret = re.findall("\$\d+",text)
    print(ret)
'''

# sbu() 函数
# text = "Apple's price is $299.Orange's price is $999"
# ret = re.sub("\$\d+","$111",text)
# print(ret)
'''
    html = """
    <dd class="job_bt">
            <h3 class="description">职位描述：</h3>
            <div class="job-detail">
            <p>岗位职责：<br><br>1、负责WEB后端架构的设计，规划技术发展方向，制定技术实施方案；<br><br>2、提升后端团队整体技术能力，指导开发及运维；<br><br>3、负责WEB后端新技术研究及实现；<br><br>岗位要求：<br><br>1、4年以上WEB后端开发经验，精通Python语言，熟悉后端开发和运维的整体流程；<br><br>2、精通至少一种后台开发框架的使用和运维，比如Django；并且了解各个框架的基本设计原理；<br><br>3、精通至少一种数据库系统的使用和运维，比如MySQL，MongoDB；并且了解各个系统的设计原理；<br><br>4、熟悉系统运维及自动化业务部署，包括但不限于Docker，k8s；<br><br>5、了解前端Javascript开发<br><br>加分项：<br><br>熟悉音视频编解码，熟悉ffmpeg的优先。<br><br>熟悉其他主流编程语言如C，Java的优先。<br><br>有大规模大并发系统架构，设计，开发，测试以及运维经验的优先。<br><br>了解大数据处理和分析（Numpy，Pandas等）的优先。</p>
            </div>
        </dd>
    """
    ret = re.sub("<.+?>", "", html)
    print(ret)
'''

# split() 函数  字符分割
'''
    text = "hello&world new world"
    ret = re.split(" |&", text) # 或者  ret = re.split("[^a-zA-Z]",text)
    print(ret)
'''

# compile() 函数
'''
    text = "the number is 20.50"
    # r = re.compile("\d+\.?\d*")  # 多次使用
    r = re.compile(r"""
        \d+ # 小数点前面的数字
        \.? # 小数点本身
        \d* # 小数点后面的数字
    """, re.VERBOSE)  # 注释
    ret = re.search(r, text)
    print(ret.group())
'''