#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 11:43 上午
# @Author : admin
# @Software: PyCharm
# @File: __init__.py.py

result = {
            "code": 1,
            "msg": "成功",
            "data": {
                # 车身
                'car_body': {
                    'chassis_support': 2,  # 0表示不支持，1表示支持
                    'img': '',  # 下载地址
                    'filename': '',  # 名称
                    'version': 0,  # 版本号
                },
                # 底盘件
                'chassis_part': {
                    'chassis_support': 2,  # 0表示不支持，1表示支持
                    'img': '',  # 下载地址
                    'filename': '',  # 名称
                    'version': 0,  # 版本号
                },
                # 发动机
                'motor': {
                    'chassis_support': 2,  # 0表示不支持，1表示支持
                    'img': '',  # 下载地址
                    'filename': '',  # 名称
                    'version': 0,  # 版本号
                }
            }
        }

key = ["car_body", "chassis_part", "motor"]
for k in key:
    result["data"][k]["chassis_support"] = 1
print(result)