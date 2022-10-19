"""
__project_ = 'python_crawler'
__file_name__ = 'demo3'
__author__ = 'BroadLink'
__time__ = '2021/6/8 14:04'
__product_name = PyCharm
"""

import json


json_str = [
    {"username": "tom", "age": 20, "country": "china"},
    {"username": "alice", "age": 21, "country": "russia"},
    {"username": "张三", "age": 22, "country": "US"}
]

with open("person_demo2.json", 'w') as fp:
    fp.write(json.dumps(json_str))


with open("person_demo_3.json", "w", encoding='utf-8') as fp:
    json.dump(json_str, fp, ensure_ascii=False)