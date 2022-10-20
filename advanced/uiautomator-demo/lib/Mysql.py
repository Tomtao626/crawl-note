# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    File Name:   mysql
    Description: 
    Author:      wzj
    Date:        2019/7/23
-------------------------------------------------
    Change Activity:
-------------------------------------------------
"""

import time
from peewee import MySQLDatabase

class ReConnectMysqlDatabase(MySQLDatabase):
    """
    定时重连
    peewee推荐handler初始化时新建连接的方法有点浪费，参照torndb的方法重写了_ensure_connected
    """
    max_idle_time = 3600 * 2

    def __init__(self, database, thread_safe=True, autorollback=False,
                 field_types=None, operations=None, autocommit=True, **kwargs):
        super().__init__(database, thread_safe, autorollback, field_types, operations, autocommit, **kwargs)

    def _ensure_connected(self):
        # Mysql by default closes client connections that are idle for
        # 8 hours, but the client library does not report this fact until
        # you try to perform a query and it fails.  Protect against this
        # case by preemptively closing and reopening the connection
        # if it has been idle for too long (7 hours by default).
        if (self.is_closed() or
                (time.time() - self._last_use_time > self.max_idle_time)):
            self.reconnect()
        self._last_use_time = time.time()

    def reconnect(self):
        self.close()
        self.connect()

    def cursor(self, commit=None):
        self._ensure_connected()
        return self._state.conn.cursor()

