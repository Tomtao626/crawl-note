#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/15 14:13
# @Author : Tom_tao
# @Site : 
# @File : demo4.py
# @Software: PyCharm

# lock版生产者与消费者模式

import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += money
            print("%s生产了%d元钱,剩余%d元钱" % (threading.current_thread(), money, gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)


class Constumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("%s消费了%d元钱,剩余%d元钱" % (threading.Thread,money,gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print("%s消费者准备消费%d元钱,剩余%d元钱,不足" % (threading.Thread, money, gMoney))
            gLock.release()
            time.sleep(0.5)


def main():
    for x in range(3):
        t = Constumer(name="消费者 %s " % x)
        t.start()

    for x in range(5):
        t = Producer(name="生产者 %s " % x)
        t.start()



if __name__ == '__main__':
    main()