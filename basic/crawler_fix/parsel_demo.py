"""
__project_ = 'python_crawler'
__file_name__ = 'parsel_demo'
__author__ = 'BroadLink'
__time__ = '2021/6/8 16:03'
__product_name = PyCharm
"""
import re

import parsel
import requests

"""
parsel支持三大功能
    .css()
    .xpath()
    .re()
"""

base_url = "https://news.baidu.com"
body = requests.get(base_url, verify=False).text
# with open('page.html', 'w', encoding='utf-8') as fp:
#     fp.write(body)
selector = parsel.Selector(text=body)
sheets = selector.xpath('//div[@class="hotnews"]').getall()
# 热点新闻
for i in sheets:
    print(re.findall('<a.+?href=\"(.+?)\".*>', i))

# title
# xpath
# titles = selector.xpath("//title/text()").extract()
title_first_xpath = selector.xpath("//title/text()").extract_first()
print(title_first_xpath)
# re
title_first_re = selector.re("<title>(\S+)</title>")[0]
print(title_first_re)
# css
title_first_css = selector.css("title::text").extract_first()
print(title_first_css)
# re/xpath结合
str_one = selector.xpath("//title/text()").re("\S\S")
print(str_one)
# css/re结合
str_one = selector.css("title::text").re("\S\S")
print(str_one)
