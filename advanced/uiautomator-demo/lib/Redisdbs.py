#!/usr/bin/env python
#coding:utf-8
"""
  Author:  xulei --<>
  Purpose: redis服务
  Created: 09/03/18
"""
import logging
import redis
import traceback
import time


#----------------------------------------------------------------------
def getRedisConn(config_dict):
    """"""
    return setRedisConn(config_dict["host"], config_dict["port"], config_dict["db"], config_dict["retry"])
    

def setRedisConn(host="127.0.0.1", port=6379, db=1, retry=3, timeout=10):
    """
    :链接redis
    @host:主机
    @port:端口
    @timeout:超时秒数
    @db:database
    @retry:重试次数
    """
    logging.info("-->begin:getRedisConn,host[%s],port[%d],database[%d],timeout[%d]"%(host,port,db,timeout))
    r=None
    i=0

    while i<retry:
        try:
            pool = redis.ConnectionPool(host=host, port=port, db=db, decode_responses=True)
            r = redis.Redis(connection_pool=pool, decode_responses=True)
            if not r:
                logging.info("第[%d]连接失败，继续"%i)
            else:
                break
        except:
            logging.error(traceback.format_exc())
            time.sleep(1)
        i+=1
    return r


import redis

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


from config.mdb_config import redis_config
_redis=redis_config['suizhu']

class RedisClient(object):

    def __init__(self,HOST=_redis.get('host'),PORT=_redis.get('port'),DB=_redis.get('db')):
        self.pool = redis.ConnectionPool(host=HOST, port=PORT,db=DB, decode_responses=True)

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.getConnection()
        return self._conn

    def getConnection(self):
        self._conn = redis.Redis(connection_pool = self.pool)