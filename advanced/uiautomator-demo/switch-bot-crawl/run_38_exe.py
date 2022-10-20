# -*- coding: utf-8 -*-
import os
from pandas.core.frame import DataFrame
import json

source_path = os.getcwd()
ircode_path = os.path.join(source_path, "ir_code.txt")
errcode_path = os.path.join(source_path, "err_code.txt")
save_path = os.path.join(source_path, "redcode.txt")


def level2redcode(code_list, frequency=38000):
    listValue = []
    listValue1 = []
    if isinstance(code_list, str):
        code_list = eval(code_list)
    list1 = code_list
    if not list1:
        return 38000, []
    for li in range(len(list1)):
        n = round(int(list1[li]) / 305.0)
        if (n > 255):
            listValue1.append(0)
            listValue1.append(n >> 8 & 0xff)
            listValue1.append(n & 0xff)
        else:
            listValue1.append(n)
    q1 = round(int(frequency / 1000), 0)
    if (q1 > 255):
        listValue.append(q1 >> 8 & 0xff)
        listValue.append(q1 & 0xff)
    else:
        listValue.append(q1)
        listValue.append(0)
    if (len(listValue1) > 255):
        listValue.append(len(listValue1) & 0xff)
        listValue.append(len(listValue1) >> 8 & 0xff)
    else:
        listValue.append(len(listValue1))
        listValue.append(0)
    listValue = listValue + listValue1
    return listValue

"""
def re_exit_code():
    for line_code in exit_code:
        list_code = (list(line_code.split(" ")))
        code = []
        if len(list_code) > 4:
            for int_z in list_code:
                try:
                    code.append(int(int_z))
                except:
                    continue
            listvalue = str(level2redcode(code)) + "\n"
            with open(save_path, "a", encoding="utf-8") as fs:
                fs.write(listvalue)
"""


def re_noexit_code():
    for line_code in noexit_code:
        list_code = (list(line_code.split(" ")))
        code = []
        if len(list_code) > 4:
            for int_z in list_code:
                try:
                    code.append(int(int_z))
                except:
                    continue
            listvalue = json.dumps(level2redcode(code)) + "\n"
            with open(save_path, "a", encoding="utf-8") as fs:
                fs.write(listvalue)


if os.path.exists(save_path):
    os.remove(save_path)
# if os.path.exists(ircode_path):
#     with open (ircode_path,"r") as exit_code:
#         exit_code = exit_code.readlines()
#     re_exit_code()

if os.path.exists(errcode_path):
    with open(errcode_path, "r") as noexit_code:
        noexit_code = noexit_code.readlines()
    re_noexit_code()
# os.remove(ircode_path)
# os.remove(errcode_path)
# print("success")
