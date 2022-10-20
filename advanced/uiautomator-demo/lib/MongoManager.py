#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/7 下午3:35
# @Author   : cancan
# @File     : MongoManager.py
# @Function : MongoDB 数据库管理类


import logging
import pymongo
import traceback
from config.mdb_config import mongo_config

class MongoManager(object):
    """MongoDB 数据库管理类"""

    # # 连接对象
    # _CONNECT_DICT = {}

    # 配置文件解析对象
    _PARSER = None

    # 客户端
    _CLIENT = {}
    @classmethod
    def init(cls, server_config):
        """初始化连接对象"""
        cls._PARSER = server_config

    @classmethod
    def _connect_db(cls,db_name):
        """连接 MongoDB"""
        if not cls._PARSER:
            cls.init(mongo_config)
        params = {
            'host': cls._PARSER[db_name].get('host'),
            'port': cls._PARSER[db_name].get('port'),
            'user': cls._PARSER[db_name].get('user'),
            'pwd': cls._PARSER[db_name].get('pwd'),
            'dbname': cls._PARSER[db_name].get('dbname')
        }
        conn = pymongo.MongoClient(host=params['host'],port=params['port'])
        try:
            if params['user'] and params['pwd']:
                cls._CLIENT[db_name]=conn.get_database(name=params["dbname"])
                cls._CLIENT[db_name].authenticate(name=params['user'], password=params['pwd'])
            logging.debug(
                'Connect MongoDB at {user}@{host}:{port},{dbname},{pwd} successful'.format(
                    **params)
            )
        except:
            logging.error(traceback.format_exc())
            logging.error('Connect MongoDB at {user}@{host}:{port},{dbname},{pwd} fails'.format(**params))


    @classmethod
    def get_db(cls, db_name):
        """获取数据库连接"""
        if db_name not in cls._CLIENT:
            cls._connect_db(db_name)
        return cls._CLIENT[db_name]

    @classmethod
    def get_coll_names(cls):
        return cls._CLIENT.getCollectionNames()
    
    @classmethod
    def insert(cls, db_name, coll_name, data, **kwargs):
        """插入数据"""

        db = cls.get_db(db_name)
        db[coll_name].insert(data, **kwargs)

    @classmethod
    def insert_many(cls, db_name, coll_name, data_list):
        """批量"""
        db = cls.get_db(db_name)
        db[coll_name].insert_many(data_list)

    @classmethod
    def find(cls, db_name, coll_name, *args, **kwargs):
        """查询数据"""

        db = cls.get_db(db_name)
        return db[coll_name].find(*args, **kwargs)

    @classmethod
    def find_one(cls, db_name, coll_name, query, *args):
        """查询单条数据"""

        db = cls.get_db(db_name)
        return db[coll_name].find_one(query, *args)

    @classmethod
    def find_one_by_id(cls, db_name, coll_name, doc_id, *args):
        """查询单条数据"""

        query = {'_id': doc_id}

        db = cls.get_db(db_name)
        return db[coll_name].find_one(query, *args)

    @classmethod
    def find_record_not_by_id(cls, db_name, coll_name, query, *args):
        """不通过 _id 查询"""

        db = cls.get_db(db_name)
        return db[coll_name].find_one(query, *args)

    @classmethod
    def push(cls, db_name, coll_name, query, data, **kwargs):
        """设置文档数据"""

        cls.update(db_name, coll_name, query, {'$push': data}, **kwargs)


    @classmethod
    def upsert(cls, db_name, coll_name, query, data):
        cls.update(db_name, coll_name, query, data,upsert=True)


    @classmethod
    def find_and_modify(cls, db_name, coll_name, query, update, **kwargs):
        """修改并查找"""

        db = cls.get_db(db_name)
        return db[coll_name].find_and_modify(query, update, **kwargs)

    @classmethod
    def set(cls, db_name, coll_name, query, data, **kwargs):
        """设置文档数据"""

        res = cls.update(db_name, coll_name, query, {'$set': data}, **kwargs)
        return res
    
    @classmethod
    def set_many(cls, db_name, coll_name, query, data, **kwargs):
        """设置文档数据"""

        res = cls.update_many(db_name, coll_name, query, {'$set': data}, **kwargs)
        return res
    
    @classmethod
    def unset(cls, db_name, coll_name, query, data, **kwargs):
        """删除文档字段"""

        res = cls.update(db_name, coll_name, query, {'$unset': data}, **kwargs)
        return res

    @classmethod
    def set_one(cls, db_name, coll_name, doc_id, data, **kwargs):
        """设置文档数据"""

        query = {'_id': doc_id}
        cls.update(db_name, coll_name, query, {'$set': data}, **kwargs)

    @classmethod
    def inc(cls, db_name, coll_name, query, data, **kwargs):
        """文档对应字段数据数值增加"""

        cls.update(db_name, coll_name, query, {'$inc': data}, **kwargs)

    @classmethod
    def inc_one(cls, db_name, coll_name, doc_id, data, **kwargs):
        """文档对应字段数据数值增加"""

        query = {'_id': doc_id}
        cls.update(db_name, coll_name, query, {'$inc': data}, **kwargs)

    @classmethod
    def add_to_set(cls, db_name, coll_name, query, data, **kwargs):
        """数组添加元素"""

        return cls.update(db_name, coll_name, query, {'$addToSet': data},
                          **kwargs)

    @classmethod
    def pull(cls, db_name, coll_name, query, data, **kwargs):
        """删除数组元素"""

        return cls.update(db_name, coll_name, query, {'$pull': data}, **kwargs)

    @classmethod
    def update_or_insert(cls, db_name, coll_name, query, data):
        """更新或者插入"""

        db = cls.get_db(db_name)
        # return cls.update(db_name, coll_name, query, data, upsert=True)
        return db[coll_name].update_one(query, {"$set": data}, upsert=True)

    @classmethod
    def update(cls, db_name, coll_name, query, update, **kwargs):
        """更新数据"""

        db = cls.get_db(db_name)
        return db[coll_name].update(query, update, **kwargs)
    
    @classmethod
    def update_many(cls, db_name, coll_name, query, update, **kwargs):
        """更新数据"""

        db = cls.get_db(db_name)
        return db[coll_name].update_many(query, update, **kwargs)

    @classmethod
    def remove(cls, db_name, coll_name, doc_id, multi=True, **kwargs):
        """删除数据"""

        query = {'_id': doc_id}
        db = cls.get_db(db_name)
        db[coll_name].remove(query, multi, **kwargs)
        
    @classmethod
    def getDb(cls, db_name, coll_name):
        """获取集合实例"""
        db = cls.get_db(db_name)
        return db[coll_name]