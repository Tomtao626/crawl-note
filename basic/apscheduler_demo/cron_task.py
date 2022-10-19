#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/1 10:43 上午
# @Author : admin
# @Software: PyCharm
# @File: cron_task.py

import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print("tick,the time is %s"% datetime.now())

if __name__ == "__main__":
    '''
    定时 cron 任务也非常简单，直接给触发器 trigger 传入 'cron' 即可。
    hour =10 ,minute =53 这里表示每天的10：53 分执行任务。这里可以填写数字，也可以填写字符串
    '''
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour="10", minute="53")
    print("press ctrl+{0} to exit".format("break" if os.name == 'nt' else 'C  '))

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemError):
        pass