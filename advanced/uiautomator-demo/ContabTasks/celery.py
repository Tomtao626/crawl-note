# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import logging
from celery import Celery
app = Celery('ContabTasks')
app.config_from_object('ContabTasks.celeryconfig')

if __name__ == '__main__':
    app.start()


#python3 dir/bin/celery -B -lsA asyn_crontab_tasks worker -l info