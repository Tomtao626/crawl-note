#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/7 12:58
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
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
            <td class="1 square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
    </tbody>
</table>
"""
bs = BeautifulSoup(html, "lxml")
print(bs.prettify())