#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/20 11:34
# @Author : Tom_tao
# @Site :
# @File : display.py
# @Software: PyCharm


from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Pie
import pymysql

# pip install pyecharts -U

class DataBase:
    host = "localhost"
    user = "root"
    password = "root"
    database = "college_bak"

    def __init__(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()


def college_map():
    db = DataBase()
    sql = "select area, count(id) from college group by area"
    db.cur.execute(sql)
    ret = db.cur.fetchall()
    db.close()
    college_map = Map(init_opts=opts.InitOpts(width="1400px", height="900px")) \
        .set_global_opts(title_opts=opts.TitleOpts(title="全国高校分布图"), visualmap_opts=opts.VisualMapOpts(max_=150), )
    college_map.add('高校数量', list(ret), ).set_series_opts(
        label_opts=opts.LabelOpts(is_show=True, color="#00f", formatter="{b}:{c}"))
    college_map.render('college_map.html')


def subject_map():
    subject_map = Bar().add_xaxis(["物理", "化学", "生物", "政治", "历史", "地理"]) \
        .add_yaxis("", [11931, 5414, 3153, 761, 1057, 1015]) \
        .set_global_opts(title_opts=opts.TitleOpts(title="学科统计图"))
    subject_map.render("subject_map.html")


def subject_pie():
    # 学科占比图
    subject_count = [("物理", 11931), ("化学", 5414), ("生物", 3153), ("政治", 761), ("历史", 1057), ("地理", 1015)]
    subject_pie = Pie().add("", subject_count).set_global_opts(title_opts=opts.TitleOpts(title="学科比例图")) \
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    subject_pie.render("subject_pie.html")


if __name__ == "__main__":
    college_map()
    subject_map()
    subject_pie()
    print('Done')
