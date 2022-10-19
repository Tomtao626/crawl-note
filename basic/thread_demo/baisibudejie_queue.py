#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/18 16:51
# @Author : Tom_tao
# @Site : 
# @File : baisibudejie_queue.py
# @Software: PyCharm

'''
    GIL全局解释器锁：
    Python自带的解释器是CPython。CPython解释器的多线程实际上是一个假的多线程（在多核CPU中，只能利用一核，不能利用多核）。同一时刻只有一个线程在执行，为了保证同一时刻只有一个线程在执行，在CPython解释器中有一个东西叫做GIL（Global Intepreter Lock），叫做全局解释器锁。这个解释器锁是有必要的。因为CPython解释器的内存管理不是线程安全的。当然除了CPython解释器，还有其他的解释器，有些解释器是没有GIL锁的，见下面：

    Jython：用Java实现的Python解释器。不存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/Jython
    IronPython：用.net实现的Python解释器。不存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/IronPython
    PyPy：用Python实现的Python解释器。存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/PyPy
    GIL虽然是一个假的多线程。但是在处理一些IO操作（比如文件读写和网络请求）还是可以在很大程度上提高效率的。在IO操作上建议使用多线程提高效率。在一些CPU计算操作上不建议使用多线程，而建议使用多进程。
    多线程下载百思不得姐段子作业：
'''

import csv
import threading
from queue import Queue

import requests
from lxml import etree


class BSSpider(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(BSSpider, self).__init__(*args, **kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            response = requests.get(url, headers=self.headers)
            text = response.text
            html = etree.HTML(text)
            descs = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in descs:
                jokes = desc.xpath(".//text()")
                joke = "\n".join(jokes).strip()
                link = self.base_domain + desc.xpath(".//a/@href")[0]
                self.joke_queue.put((joke, link))
            print('=' * 30 + "第%s页下载完成！" % url.split('/')[-1] + "=" * 30)


class BSWriter(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    def __init__(self, joke_queue, writer, gLock, *args, **kwargs):
        super(BSWriter, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        while True:
            try:
                joke_info = self.joke_queue.get(timeout=40)
                joke, link = joke_info
                self.lock.acquire()
                self.writer.writerow((joke, link))
                self.lock.release()
                print('保存一条')
            except:
                break


def main():
    page_queue = Queue(10)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp = open('bsbdj.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content', 'link'))

    for x in range(1, 11):
        url = 'http://www.budejie.com/text/%d' % x
        page_queue.put(url)

    for x in range(5):
        t = BSSpider(page_queue, joke_queue)
        t.start()

    for x in range(5):
        t = BSWriter(joke_queue, writer, gLock)
        t.start()


if __name__ == '__main__':
    main()
