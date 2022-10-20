#!/usr/bin/env python
# encoding: utf-8
'''
@author: qiuyan
@contact: winston@peipeiyun.com
@file: __init__.py.py
@time: 2018/12/17 11:56 AM
@desc:
'''
from loguru import logger
logger.add("log/task/task_logs.log",format="{time} {level} {message}",rotation="10 MB")

import datetime
from dateutil.relativedelta import relativedelta

def dayport_time(delay_day=1):
    if delay_day:
        start = datetime.date.today()-datetime.timedelta(days=delay_day)
    else:
        start = datetime.date.today()
    star_time = start.strftime('%Y-%m-%d')+' 00:00:01'
    end_time = start.strftime('%Y-%m-%d')+' 23:59:59'
    return star_time,end_time,start.strftime('%Y-%m-%d')

def month_datetime():
    mydate = datetime.datetime.now()
    start_date = datetime.datetime(mydate.year,mydate.month-1,1)
    end_date = start_date+relativedelta(months=1,days=-1)
    return start_date.strftime('%Y-%m-%d'),end_date.strftime('%Y-%m-%d')+' 23:59:59',end_date.strftime('%Y-%m')

# print(month_datetime())