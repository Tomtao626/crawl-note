# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from celery.schedules import crontab

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = "Asia/Shanghai"  # 时区设置
worker_hijack_root_logger = True  # 关闭日志
result_expires = 600
worker_concurrency = 5
broker_url = 'redis://127.0.0.1:6379/1'
result_backend = 'redis://127.0.0.1:6379/2'
# worker_max_tasks_per_child = 100

# 导入任务所在文件
imports = [
    'ContabTasks.tasks.access_report',
    'ContabTasks.tasks.analysis'
]

include = (
    'ContabTasks.tasks'
)

# 需要执行任务的配置
beat_schedule = {

    #访问日志
    'test': {
        'task': 'ContabTasks.tasks.test.test',  #
        'schedule': crontab(minute=30, hour=1),  # 凌晨1:30分执行
        # 'schedule': crontab(minute="*/1"),  #
        'args': ()
    },

}
