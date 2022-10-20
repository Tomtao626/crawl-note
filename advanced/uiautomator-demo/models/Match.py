#!/usr/bin/env python
# encoding: utf-8
"""
@file: Match.py
@time: 2020/6/3 10:15 上午
@desc: Test
"""

from .basemodel import BaseModel
from peewee import IntegerField, CharField, TextField, BigIntegerField


class AttachModels(BaseModel):
    """
    红码/品牌/类型关联
    """
    devtypeid = IntegerField(default=0, verbose_name='类型ID', help_text='类型ID')
    ircodeid = IntegerField(primary_key=True, default=0, verbose_name='红码ID', help_text='红码ID')
    elecmodel = CharField(max_length=64, default='', verbose_name='设备型号', help_text='设备型号')
    remotemodel = CharField(max_length=64, default='', verbose_name='遥控器型号', help_text='遥控器型号')
    staticfile = CharField(max_length=256, default='', verbose_name='文件路径', help_text='文件路径')
    brandid = IntegerField(default=0, verbose_name='品牌ID', help_text='品牌ID')

    class Meta:
        table_name = 'attachmodels'
        verbose_name = '型号红码品牌关联'


class IrcodeInfo(BaseModel):
    """
    红码/品牌/类型关联
    """
    devtypeid = IntegerField(default=0, verbose_name='类型ID', help_text='类型ID')
    ircodeid = IntegerField(primary_key=True, default=0, verbose_name='红码ID', help_text='红码ID')
    brandid = IntegerField(default=0, verbose_name='品牌ID', help_text='品牌ID')
    versionid = IntegerField(default=0, verbose_name='版本ID', help_text='版本ID')
    createtime = CharField(max_length=255, default='', verbose_name='创建时间', help_text='创建时间')
    authorid = CharField(max_length=255, default='', verbose_name='作者ID', help_text='作者ID')
    status = CharField(max_length=255, default='', verbose_name='状态', help_text='状态')
    providerid = IntegerField(default=0, verbose_name='提供者ID', help_text='提供者ID')
    locateid1st = IntegerField(default=0, verbose_name='地区第一', help_text='地区第一')
    locateid2nd = IntegerField(default=0, verbose_name='地区第二', help_text='地区第二')
    locateid3rd = IntegerField(default=0, verbose_name='地区第三', help_text='地区第三')
    locateid4th = IntegerField(default=0, verbose_name='地区第四', help_text='地区第四')
    usenum = IntegerField(default=0, verbose_name='使用次数', help_text='使用次数')
    icodefile = CharField(max_length=255, default=0, verbose_name='红码文件', help_text='红码文件')
    fileid = BigIntegerField(default=0, verbose_name='文件ID', help_text='文件ID')
    rank = IntegerField(default=0, verbose_name='排序', help_text='排序')
    cversion = CharField(max_length=255, default=0, verbose_name='版本', help_text='版本')
    origin = CharField(max_length=255, default=0, verbose_name='来源', help_text='来源')
    order = CharField(max_length=255, default=0, verbose_name='订单', help_text='订单')
    interval = CharField(default=0, verbose_name='间隔', help_text='间隔')

    class Meta:
        table_name = 'ircodeinfo'
        verbose_name = '红码信息'

    def _to_dict(self):
        keys = ['devtypeid', 'ircodeid', 'brandid', 'fileid', 'status']
        return self.to_dict(keys)


class BrandInfo(BaseModel):
    """
    红码/品牌/类型关联
    """
    brandid = IntegerField(primary_key=True, default=0, verbose_name='品牌ID', help_text='品牌ID')
    brand = CharField(max_length=255, default='', verbose_name='品牌', help_text='品牌')
    createtime = CharField(max_length=19, default='', verbose_name='创建时间', help_text='创建时间')
    updatetime = IntegerField(default=0, verbose_name='更新时间', help_text='更新时间')
    authorid = CharField(max_length=32, default='', verbose_name='作者ID', help_text='作者ID')
    lankeyid = IntegerField(default=0, verbose_name='', help_text='')

    class Meta:
        table_name = 'brandinfo'
        verbose_name = '品牌信息'


class Ircode(BaseModel):
    """
    红码
    """
    fileid = BigIntegerField(primary_key=True, default=0, verbose_name='文件ID', help_text='文件ID')
    codestr = TextField(default='', verbose_name='string数据', help_text='string数据')
    codejson = TextField(default='', verbose_name='json数据', help_text='json数据')
    desc = CharField(max_length=255, default='', verbose_name='描述信息', help_text='描述信息')
    filename = CharField(max_length=255, default='', verbose_name='文件名称', help_text='文件名称')
    uploadtime = CharField(max_length=255, default='', verbose_name='上传时间', help_text='上传时间')
    bytecode = TextField(default='', verbose_name='字节码', help_text='字节码')
    staticfile = CharField(max_length=255, default='', verbose_name='文件路径', help_text='文件路径')

    class Meta:
        table_name = 'ircode'
        verbose_name = '红码'

    def _to_dict(self):
        keys = ['fileid', 'codejson']
        return self.to_dict(keys)
