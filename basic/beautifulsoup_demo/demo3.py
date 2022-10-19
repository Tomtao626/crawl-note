#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/7 23:21
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software: PyCharm

from bs4 import BeautifulSoup

html = """
    <table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="1" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师(深圳)</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
    <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师(深圳)</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr><tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师(深圳)</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr><tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师(深圳)</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a id="test" class="test" target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html, 'lxml')

# 1.获取所有tr标签
'''trs = soup.select("tr")
for tr in trs:
    print(tr)'''

# 2.获取第2个tr标签
'''print(soup.select('tr')[1])'''

# 3.获取所有class等于even得tr标签
# 法一
# trs = soup.select("tr.even")
# 法二
'''trs = soup.select("tr[class='even']")
for tr in trs:
    print(tr)'''

# 4.获取所有a标签的href属性
'''alist = soup.select("a")
for a in alist:
    href = a['href']
    print(href)'''

# 5.获取所有的职位信息(纯文本)
'''trs = soup.select("tr")
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)'''