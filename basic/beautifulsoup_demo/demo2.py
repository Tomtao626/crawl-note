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
            <td class="1 square"><a id="test" class="test" target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2019-11-25</td>
        </tr>
    </tbody>
</table>
"""
# 1.获取所有tr标签
# 2.获取第2个tr标签
# 3.获取所有class等于even得tr标签
# 4.将所有id等于test，class也等于test的a标签提取出来
# 5.获取所有a标签的href属性
# 6.获取所有的职位信息(纯文本)

soup = BeautifulSoup(html, 'lxml')

# 1.获取所有tr标签
'''
    trs = soup.find_all('tr')
    for tr in trs:
        print(tr)
    '''
    
# 2.获取第2个tr标签
'''
    tr = soup.find_all('tr', limit=2)[1]
    print(tr)
'''

# 3.获取所有class等于even得tr标签
# trs = soup.find_all('tr', class_='even')
# for tr in trs:
#     print(tr)

'''
    trs = soup.find_all('tr', attrs={'class': 'even'})
    for tr in trs:
        print(tr)
'''

# 4.将所有id等于test，class也等于test的a标签提取出来
# a_list = soup.find_all('a',attrs={'id': "test",'class': "test"})
'''
    a_list = soup.find_all('a', id="test", class_="test")
    for a in a_list:
        print(a)
'''

# 5.获取所有a标签的href属性
'''
    a_list = soup.find_all('a')
    for a in a_list:
        # 1.通过下标操作方式
        # href = a['href']
        # print(href)
        # 2.通过attrs属性的方式
        href = a.attrs['href']
        print(href)
'''

# 6.获取所有的职位信息(纯文本)
'''    
    trs = soup.find_all('tr')[1:]
    movies = list()
    for tr in trs:
        movie = dict()
        # 方法一
        # tds = tr.find_all("td")
        # title = tds[0].string
        # category = tds[1].string
        # nums = tds[2].string
        # city = tds[3].string
        # pubtime = tds[4].string
        # movie['title'] = title
        # movie['category'] = category
        # movie['nums'] = nums
        # movie['city'] = city
        # movie['pubtime'] = pubtime
        # movies.append(movie)
    
        # 方法二
        # infos = list(tr.strings)
        infos = list(tr.stripped_strings)
        movie['title'] = infos[0]
        movie['category'] = infos[1]
        movie['nums'] = infos[2]
        movie['city'] = infos[3]
        movie['pubtime'] = infos[4]
        movies.append(movie)
    print(movies)
'''

tr = soup.find_all('tr')[1]
#text = tr.get_text() # 返回一个字符串
text = list(tr.strings)  # 返回一个生成器 即列表  包含空白字符
print(type(text)) # str类型
print(text)