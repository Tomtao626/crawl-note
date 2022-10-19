# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi


class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparms = {
            'host': '',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparms)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (
        item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['origin_url'],
        item['article_id']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values(null,%s,%s,%s,%s,%s,%s,%s)"""
            return self._sql
        return self._sql


# 异步操作
class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparms = {
            'host': '',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dpool = adbapi.ConnectionPool('pymysql', **dbparms)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id,read_count,word_count,like_count,comment_count,subjects) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (
        item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['origin_url'],
        item['article_id'], item['read_count'], item['word_count'], item['like_count'], item['comment_count'],
        item['subjects']))

    def handle_error(self, error, item, spider):
        print(error)
