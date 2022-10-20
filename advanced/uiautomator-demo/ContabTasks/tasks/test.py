#!/usr/bin/env python
# encoding: utf-8
'''
@author: zhaowenpeng
@contact: winston@peipeiyun.com
@software: garner
@file: test.py
@time: 2020/6/3 10:56 上午
@desc:
'''

from ContabTasks.celery import app
from loguru import logger

@app.task
@logger.catch
def test():
    print('test----------------')
