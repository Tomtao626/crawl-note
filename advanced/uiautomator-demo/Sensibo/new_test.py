import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


import uiautomator2 as ui2
import os
import pandas as pd
import time
import unittest
import json
import re
import csv
serial = 'ad5242a90506'
d = ui2.connect_usb(serial)
# 关闭APP
d.app_stop("com.sensibo.app")
# 启动App
d.app_start("com.sensibo.app")
time.sleep(5)
# 点击进入到面板
d.click(0.558, 0.325)
brand = "Gree"
# 切换到设置
d.click(0.846, 0.289)
# 向上滚动屏幕
d.swipe_ext("up", 0.2)
# 切换品牌
d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[10]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[13]').click_exists()
d.xpath('//*[@content-desc="Next"]').click_exists()
time.sleep(3)

d.xpath('//*[@content-desc="Set remote manually"]').click_exists()
import random
time.sleep(random.randint(1, 5))
# 切换到选择品牌栏
d.click(0.133, 0.408)

# 点开品牌列表
d.click(0.757, 0.48)
while not d.xpath(f'//*[@content-desc={brand}]').exists:
    d.swipe(0.5, 0.145, 0.5, 0.084)
# 选择品牌
d.xpath(f'//*[@content-desc={brand}]').click()
# 获取改品牌红码型号
d.click(0.724, 0.547)
for i in d.xpath('./android.view.View').all():
    print(i.text)
model_list = []
st = None
while True:
    for i in d.xpath('//android.view.View').all():
        if i.text == "" or i.text in model_list:
            continue
        else:
            model_list.append(i.text)
    if st == len(model_list):
        break
    st = len(model_list)
    d.swipe(0.5, 0.15, 0.5, 0.084)
# 退回界面
d.click(0.141, 0.624)
print(model_list)


if __name__ == '__main__':
    unittest.main()
