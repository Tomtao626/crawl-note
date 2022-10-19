#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/17 0:01
# @Author : Tom_tao
# @Site : 
# @File : demo6.py
# @Software: PyCharm
# 队列

from queue import Queue
import time
import threading

q = Queue(4)

# for x in range(4):
#     q.put(x)
#
# for x in range(4):
#     print(q.get())
def set_value(q):
 index = 0
 while True:
     q.put(index)
     index += 1
     time.sleep(2)

def grt_value(q):
    while True:
        print(q.get())

def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=grt_value, args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
