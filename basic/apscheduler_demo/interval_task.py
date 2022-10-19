#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/1 10:19 上午
# @Author : admin
# @Software: PyCharm
# @File: interval_task.py 间隔性任务

import os
from datetime import datetime
# 导入调度器模块 BlockingScheduler，这是最简单的调度器，调用 start 方阻塞当前进程，
# 如果你的程序只用于调度，除了调度进程外没有其他后台进程，那么请用 BlockingScheduler 非常有用，此时调度进程相当于守护进程。
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    '''
    定义一个函数 tick 代表我们要调度的作业程序。
    '''
    print("tick! the time is %s" % datetime.now())


if __name__ == "__main__":
    '''
    实例化一个 BlockingScheduler 类，不带参数表明使用默认的作业存储器-内存，
    默认的执行器是线程池执行器，最大并发线程数默认为 10 个（另一个是进程池执行器）。
    '''
    scheduler = BlockingScheduler()
    # 添加一个作业 tick，触发器为 interval，每隔 3 秒执行一次，
    # 另外的触发器为 date，cron。date 按特定时间点触发，cron 则按固定的时间间隔触发。
    scheduler.add_job(tick, 'interval', seconds=3)
    print("press ctrl+{0} to exit".format('Break' if os.name == 'nt' else 'C  '))
    print(os.name)
    # 加入捕捉用户中断执行和解释器退出异常，pass 关键字，表示什么也不做。
    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemError):
        pass
