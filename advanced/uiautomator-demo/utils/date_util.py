#!/usr/bin/env python
# encoding: utf-8
'''
@author: qiuyan
@contact: winston@peipeiyun.com
@file: date_util.py
@time: 2019/7/6 2:36 PM
@desc:
'''

import datetime
import datetime
from pandas.tseries.offsets import Day
def rest_of_day():
    """
    :return: 截止到目前当日剩余时间
    """
    today = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
    tomorrow = today + datetime.timedelta(days=1)
    nowTime = datetime.datetime.now()
    # return (tomorrow - nowTime).microseconds  # 获取毫秒值
    return (tomorrow - nowTime).seconds  # 获取秒
    # return (tomorrow - nowTime).min  # 获取分钟

def dateformat(format="%Y-%m-%d"):
    """
    :return: 时间格式化
    """
    format_time = datetime.datetime.strftime(datetime.datetime.now(),format)
    return format_time

def get_yes_time(format="%Y-%m-%d"):
    """
    获取前一天时间
    :param format:
    :return:
    """
    now_time = datetime.datetime.now()  # 获取当前时间
    yes_time = (now_time - 1 * Day()).strftime(format)  # 格式化
    return yes_time


def get_before_time(before,format="%Y-%m-%d"):
    """
    获取前n天时间
    :param format:
    :return:
    """
    now_time = datetime.datetime.now()  # 获取当前时间
    yes_time = (now_time - before * Day()).strftime(format)  # 格式化
    return yes_time

