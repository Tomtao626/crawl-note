#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/3 3:03 下午
# @Author : admin
# @Software: PyCharm
# @File: sync_db.py

# from models.basemodel import _mdb
#
# tables = []
#
# for table in tables:
#     _mdb.create_tables([table])
# _mdb.commit()
ls = [
    {
        "serial": 11,
        "brand": "ViViD",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vicarage Science",
        "model": []
    },
    {
        "serial": 20,
        "brand": "Victor",
        "model": [
            "RM-C2130"
        ]
    },
    {
        "serial": 22,
        "brand": "Victory",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Video Concepts",
        "model": []
    },
    {
        "serial": 14,
        "brand": "Videocon",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Videon",
        "model": []
    },
    {
        "serial": 15,
        "brand": "ViewSonic",
        "model": []
    },
    {
        "serial": 13,
        "brand": "Viewpia",
        "model": []
    },
    {
        "serial": 3,
        "brand": "Viore",
        "model": []
    },
    {
        "serial": 10,
        "brand": "Vira brand",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vision",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vision Hui Pu",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vision Quest",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vistron",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vityas",
        "model": []
    },
    {
        "serial": 6,
        "brand": "Vivitek",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Vivo",
        "model": []
    },
    {
        "serial": 9,
        "brand": "Vizio",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Vlnc",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Vortec",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Voxson",
        "model": []
    },
    {
        "serial": 8,
        "brand": "WARUMAIA",
        "model": []
    },
    {
        "serial": 3,
        "brand": "WEIPAI",
        "model": []
    },
    {
        "serial": 9,
        "brand": "Wafa",
        "model": []
    },
    {
        "serial": 11,
        "brand": "Wahson",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Waltham",
        "model": []
    },
    {
        "serial": 6,
        "brand": "Walton",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Wansa",
        "model": []
    },
    {
        "serial": 6,
        "brand": "Watson",
        "model": []
    },
    {
        "serial": 12,
        "brand": "Wave",
        "model": []
    },
    {
        "serial": 19,
        "brand": "Wealthy",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Wega",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Weltblick",
        "model": []
    },
    {
        "serial": 10,
        "brand": "Westinghouse",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Wharfedale",
        "model": []
    },
    {
        "serial": 5,
        "brand": "Wolf Del",
        "model": []
    },
    {
        "serial": 11,
        "brand": "Wujin",
        "model": []
    },
    {
        "serial": 1,
        "brand": "X10",
        "model": []
    },
    {
        "serial": 194,
        "brand": "XIHU",
        "model": []
    },
    {
        "serial": 8,
        "brand": "XINAGHAI",
        "model": []
    },
    {
        "serial": 3,
        "brand": "XINFU",
        "model": []
    },
    {
        "serial": 3,
        "brand": "XINGMENBAN",
        "model": []
    },
    {
        "serial": 4,
        "brand": "XINRISONG",
        "model": []
    },
    {
        "serial": 21,
        "brand": "XUELIAN",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Xenius",
        "model": []
    },
    {
        "serial": 1,
        "brand": "XiGuan",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Xia Pu",
        "model": []
    },
    {
        "serial": 20,
        "brand": "Xiangyang",
        "model": []
    },
    {
        "serial": 14,
        "brand": "Xiangyu",
        "model": []
    },
    {
        "serial": 5,
        "brand": "Xiaomi",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Xin Adorable",
        "model": []
    },
    {
        "serial": 22,
        "brand": "Xin Meng ban",
        "model": []
    },
    {
        "serial": 21,
        "brand": "Xinghai",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Xu Jing",
        "model": []
    },
    {
        "serial": 8,
        "brand": "YONGBAO",
        "model": []
    },
    {
        "serial": 5,
        "brand": "YOULANASI",
        "model": []
    },
    {
        "serial": 9,
        "brand": "YOUSIDA",
        "model": []
    },
    {
        "serial": 7,
        "brand": "YUHANG",
        "model": []
    },
    {
        "serial": 8,
        "brand": "Ya Jun",
        "model": []
    },
    {
        "serial": 15,
        "brand": "Yamaha",
        "model": []
    },
    {
        "serial": 15,
        "brand": "Yellow America",
        "model": []
    },
    {
        "serial": 16,
        "brand": "Yi Minxin",
        "model": []
    },
    {
        "serial": 10,
        "brand": "Yingfeike",
        "model": []
    },
    {
        "serial": 12,
        "brand": "Yingge",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Yoko",
        "model": []
    },
    {
        "serial": 12,
        "brand": "Yongbao",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Youmeng",
        "model": []
    },
    {
        "serial": 2,
        "brand": "Yu",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Zanussi",
        "model": []
    },
    {
        "serial": 31,
        "brand": "Zenith",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Zepto",
        "model": []
    },
    {
        "serial": 11,
        "brand": "Zhuhai",
        "model": []
    },
    {
        "serial": 1,
        "brand": "Zinwell",
        "model": []
    },
    {
        "serial": 1,
        "brand": "acto",
        "model": []
    },
    {
        "serial": 3,
        "brand": "airtel",
        "model": []
    },
    {
        "serial": 1,
        "brand": "bairong",
        "model": []
    },
    {
        "serial": 1,
        "brand": "boigle",
        "model": []
    },
    {
        "serial": 2,
        "brand": "chase",
        "model": []
    },
    {
        "serial": 1,
        "brand": "chigo",
        "model": []
    },
    {
        "serial": 2,
        "brand": "cisco",
        "model": []
    },
    {
        "serial": 2,
        "brand": "clatronic",
        "model": []
    },
    {
        "serial": 1,
        "brand": "cllL",
        "model": []
    },
    {
        "serial": 2,
        "brand": "currency",
        "model": []
    },
    {
        "serial": 11,
        "brand": "curtis",
        "model": []
    },
    {
        "serial": 8,
        "brand": "cybermax",
        "model": []
    },
    {
        "serial": 22,
        "brand": "cybermaxx",
        "model": []
    },
    {
        "serial": 1,
        "brand": "exceptional",
        "model": []
    },
    {
        "serial": 1,
        "brand": "founder",
        "model": []
    },
    {
        "serial": 4,
        "brand": "fzfe",
        "model": []
    },
    {
        "serial": 20,
        "brand": "ganxin",
        "model": []
    },
    {
        "serial": 7,
        "brand": "htboy",
        "model": []
    },
    {
        "serial": 135,
        "brand": "huanghe",
        "model": []
    },
    {
        "serial": 1,
        "brand": "iQIYI",
        "model": []
    },
    {
        "serial": 1,
        "brand": "kelon",
        "model": []
    },
    {
        "serial": 1,
        "brand": "kenwood",
        "model": []
    },
    {
        "serial": 7,
        "brand": "kolin",
        "model": []
    },
    {
        "serial": 2,
        "brand": "kyushu",
        "model": []
    },
    {
        "serial": 8,
        "brand": "lgm,Le42A3030",
        "model": []
    },
    {
        "serial": 10,
        "brand": "lingxf",
        "model": []
    },
    {
        "serial": 1,
        "brand": "lotus",
        "model": []
    },
    {
        "serial": 1,
        "brand": "mooka",
        "model": []
    },
    {
        "serial": 2,
        "brand": "olevia",
        "model": []
    },
    {
        "serial": 169,
        "brand": "sanken",
        "model": []
    },
    {
        "serial": 1,
        "brand": "satellite",
        "model": []
    },
    {
        "serial": 4,
        "brand": "sbmtv",
        "model": []
    },
    {
        "serial": 6,
        "brand": "sonitron",
        "model": []
    },
    {
        "serial": 1,
        "brand": "sonying",
        "model": []
    },
    {
        "serial": 1,
        "brand": "sunny",
        "model": []
    },
    {
        "serial": 9,
        "brand": "technology",
        "model": []
    },
    {
        "serial": 1,
        "brand": "three Between",
        "model": []
    },
    {
        "serial": 4,
        "brand": "yonggu",
        "model": []
    },
    {
        "serial": 4,
        "brand": "yuyu168",
        "model": []
    }
]
print(len(ls))


