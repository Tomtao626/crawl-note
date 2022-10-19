#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/13 16:44
# @Author : Tom_tao
# @Site : 
# @File : interval_task.py
# @Software: PyCharm


import threading
import time


# 传统方式
'''
def test1():
    for x in range(3):
        print("test1----%s"% x)
        time.sleep(1)
        
def test2():
    for x in range(3):
        print("test2----%s"% x)
        time.sleep(1)

def main():
    test1()
    test2()

if __name__ == '__main__':
    main()
'''

# 多线程
'''
def test1():
    for x in range(3):
        print("test1----%s" % x)
        time.sleep(1)


def test2():
    for x in range(3):
        print("test2----%s" % x)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()
    # 获取所有的线程
    print(threading.enumerate())
if __name__ == "__main__":
    main()
'''