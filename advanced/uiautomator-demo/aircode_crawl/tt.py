import uiautomator2 as ui2
import os
import pandas as pd
import time
import unittest
import json
import re
import csv
import uiautomator2 as u2

d = u2.connect_usb()
file = open('pdd_2.txt', 'a', encoding='utf-8')
for i in range(10):
    d.xpath('//*[@resource-id="com.xunmeng.pinduoduo:id/cak"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
    for elem in d.xpath('//android.widget.TextView').all():
        print("Text:",elem.text)#获取当前视图所有文本视图文本
        file.write(str(elem.text) + ' ')#写入txt文件


# d(scrollable=True).scroll(steps=10)

# 关闭APP
d.app_stop("co.leanremote.universalremotecontrol.remotecontrol")
# 启动App
d.app_start("co.leanremote.universalremotecontrol.remotecontrol")

time.sleep(2)

fr = open("空调品牌.json", 'r')
brand_list = json.loads(fr.read())
fr.close()

fr = open("空调品牌—红码状态.json", 'r')
rel = json.loads(fr.read())
fr.close()

d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/default_text_view", text="IR Remote").click()
d.xpath(
    '//*[@resource-id="co.leanremote.universalremotecontrol.remotecontrol:id/gridview"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()
time.sleep(1)

for i in range(len(brand_list)):
    brand = brand_list[i]
    if brand in rel:
        # if rel[brand] == 1:
        #     print(brand, '有码')
        # else:
        #     print(brand, '无码')
        continue

    for j in range(i):
        d.swipe(0.045, 0.38221, 0.045, 0.311)
    # while True:
    #     try:
    #         d.xpath('//*[@text="{}"]'.format(brand)).click()
    #         break
    #     except Exception:
    #         d.swipe(0.045, 0.38221, 0.045, 0.311)
    d.xpath('//*[@text="{}"]'.format(brand)).click()
    try:
        val = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/instruction").get_text()
        d(resourceId="com.android.systemui:id/back").click()
        time.sleep(1)
        print(brand, '有码')
        rel[brand] = 1


    except Exception:
        print(brand, '无码')
        d(resourceId="com.android.systemui:id/back").click()
        time.sleep(1)
        rel[brand] = 0

    d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/default_text_view", text="IR Remote").click()
    d.xpath('//*[@resource-id="co.leanremote.universalremotecontrol.remotecontrol:id/gridview"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()
    time.sleep(1)



fr = open("空调品牌—红码状态.json", 'w')
fr.write(json.dumps(rel))
fr.close()



# try:
#     val = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/instruction").get_text()
# except Exception:
#     val = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/whatisirblaster").get_text()
# print(val)
# d(resourceId="com.android.systemui:id/back").click()
#
# d(scrollable=True).scroll.forward.to(description="Aux")
# d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/txt_pdt_name", text="Aux").click()
#

# 进入空调面板
# d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/PowerOn1").click()
# d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/working").click()
# time.sleep(3)
# d(text="REMIND ME LATER").click()

# brand_list = ["Philips"]
# brand_status = None
# while True:
#     # 滑动一格
#     d.swipe(0.045, 0.38221, 0.045, 0.311)
#     brand = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/txt_pdt_name").get_text()
#     if brand == brand_status:
#         break
#     else:
#         brand_status = brand
#         print(brand)
#         brand_list.append(brand)
# brand_list = brand_list + ['Yair', 'Yangzi', 'Yingyan', 'Yorkyork', 'Yuesheng', 'Yuetu', 'Zamil', 'Zanussi', 'Zapaozuzhuabgji', 'Zhengzhoujinda', 'Zhongyi']
# print(brand_list)

#
# # 获取当前面板温度
# temperature = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/display").get_text()
# print(temperature)
#
# # 获取当前风速
# speed = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/fanSpeed").get_text()
# print(speed)
#
#
# mode = None
# # 获取当前模式
# for i in ['modeSignCool', 'modeSignHot']:
#     try:
#         mode = d(resourceId="co.leanremote.universalremotecontrol.remotecontrol:id/{}".format(i)).info
#         mode = i
#         break
#     except Exception:
#         continue
# print(mode)


