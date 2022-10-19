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

# 多线程类的实现
class test1Thread(threading.Thread):
    def run(self):
        for x in range(3):
            print("test1----%s" % threading.current_thread())
            time.sleep(1)

class test2Thread(threading.Thread):
    def run(self):
        for x in range(3):
            print("test2----%s" % threading.current_thread())
            time.sleep(1)

def main():
    t1 = test1Thread()
    t2 = test2Thread()

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
