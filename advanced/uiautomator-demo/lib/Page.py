#!/usr/bin/env python
# encoding: utf-8
'''
@author: qiuyan
@contact: winston@peipeiyun.com
@file: Page.py
@time: 2019/1/4 4:28 PM
@desc:
'''
class Paginator():
    """
        系统查询分页工具
    """
    def __init__(self, url_func, page=1, total=0, page_size=10):

        self.url_func = url_func
        self.page = 1 if int(page) < 1 else int(page)   #当前页
        self.total = int(total)   #总条数
        self.page_size = int(page_size)
        #总页数
        if self.total==0:
            self.page_num=1
        else:
            self.page_num = (self.total%self.page_size==0) and int(self.total/self.page_size) or int(self.total/self.page_size)+1
        if self.page>self.page_num:
            self.page = self.page_num
        self.page_bars = {}
        #开始数
        self.page_start=(self.page-1)*page_size+1
        #尾数
        self.page_end=self.page*page_size
        self.page_data={'page':self.page,
                        'page_size':self.page_size,
                        'page_num':self.page_num,
                        'total':self.total
                        }
        for _page in range(1, self.page_num + 1):
            _index = int(_page / 10)
            if not _index in self.page_bars:
                self.page_bars[_index] = {_page}
            else:
                self.page_bars[_index].add(_page)

    def to_dict(self):
        return {key:getattr(self,key) for key in ['page','total','page_size','page_num','page_start','page_end']}

from .Page import Paginator
import urllib
import ujson
PAGE_SIZE = 24
def get_page_url(request, page=1):
    """参数解析
    :page 页号
    :form_
    """
    path = request.path
    if request.method=='GET':
        args = request.args
    else:
        args = {key:request.form.get(key) for key in request.form.keys()}
    args.pop('page', '')
    def _page_url(p=page):
        return path + '?page={0}&'.format(p)+ urllib.parse.urlencode(args)
    return _page_url

def get_page_data(request,query,input_size=None,page=1,query_count=None):
    '''
    分页函数
    :param query:
    :param page_size:
    :return:
    '''
    page_size=30
    if input_size:
        page_size = input_size
    if request.method=='GET':
        if not input_size:
            _page_size = request.args.get("page_size",'')
            if not _page_size:
                if 'Mobile' in request.headers.get('user-agent'):
                    page_size = 8
                else:
                    page_size = PAGE_SIZE
            else:
                page_size = int(_page_size)
        else:
            page_size = PAGE_SIZE
        page = int(request.args.get("page", 1))
    elif request.method=='POST':
        if request.body:
            data = ujson.loads(request.body)
        else:
            data = {}
        page_size = data.get('page_size', 20)
        page = data.get('page', 1)
    offset = (page-1) * page_size
    result = query.limit(page_size).offset(offset)
    if not query_count:
        query_count = query.count()
    page_data = Paginator(get_page_url(request), page,query_count, page_size)
    page_data.result = result
    return page_data

def get_page_mongo_data(request,query,total_count=None):
    '''
    mongo分页函数
    :param query:
    :param page_size:
    :return:
    '''
    page_size=30

    if request.method=='GET':
        _page_size = request.args.get("page_size",'')
        if not _page_size:
            if 'Mobile' in request.headers.get('user-agent'):
                page_size = 8
            else:
                page_size = PAGE_SIZE
        else:
            page_size = int(_page_size)
        page = int(request.args.get("page", 1))
    elif request.method=='POST':
        if request.body:
            data = ujson.loads(request.body)
        else:
            data={}
        page_size = data.get('page_size', 20)
        page = data.get('page', 1)
    offset = (page-1) * page_size
    if total_count:
        total = total_count
    else:
        total = query.count(True)
    result = query.skip(offset).limit(page_size)
    page_data = Paginator(get_page_url(request), page, total, page_size)
    page_data.result = list(result)
    return page_data




def get_list_page_data(request,query,query_count=None):
    '''
    分页函数
    :param query:
    :param page_size:
    :return:
    '''
    if request.method=='GET':
        _page_size = request.args.get("page_size",PAGE_SIZE)
        page = request.args.get('page', 1)
    elif request.method=='POST':
        if request.body:
            data = ujson.loads(request.body)
        else:
            data = {}
        page_size = data.get('page_size', 20)
        page = data.get('page', 1)
    offset = (page-1) * page_size
    result = query[offset:offset+page_size]
    if not query_count:
        query_count = len(query)
    page_data = Paginator(get_page_url(request), page,query_count, page_size)
    page_data.result = result
    return page_data