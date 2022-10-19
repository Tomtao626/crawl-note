#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 22:20
# @Author : Tom_tao
# @Site : 
# @File : demo3.py
# @Software: PyCharm

import threading

VALUE = 0
glock = threading.Lock()

def add_value():
    global VALUE
    glock.acquire()
    for x in range(1000000):
        VALUE += 1
    glock.release()
    print('value:%d' % VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()