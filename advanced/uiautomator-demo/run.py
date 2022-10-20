import random
# 电频波形码转38开头红码
def level2redcode(code_list, frequency=38000, state=305):
    listValue = []
    listValue1 = []
    if isinstance(code_list, str):
        code_list = eval(code_list)
    # list1 = code_list[2:]  # 去掉频率和长度
    list1 = code_list  # 去掉频率和长度
    if not list1:
        return 38000, []
    for li in range(len(list1)):
        n = round(int(list1[li]) / state)
        if (n > 255):
            listValue1.append(0)
            listValue1.append(n >> 8 & 0xff)
            listValue1.append(n & 0xff)
        else:
            listValue1.append(n)
    q1 = round(int(frequency / 1000), 0)  # 要取小数将第一个int改为float，最后0改要求小数位
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


# 获取电频波形码
def get_redcode():
    fr = open("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt", "r")
    levelcode = fr.read().split("\n")[-2]
    fr.close()
    redcode = level2redcode([int(i) for i in levelcode.split(" ")])
    return redcode


# 获取无型号多方案品牌数据
def get_no_model_brand():
    with open('switch-bot-crawl/no_model.json', 'r', encoding='utf-8') as f:
        no_model_list = ujson.load(f)
    return no_model_list


# 根据switchbot键位获取bl键位码
def get_blkey_by_swbkey(key_name: str) -> str:
    import ujson
    with open('switch-bot-crawl/function_key.json', 'r', encoding='utf-8') as f:
        key_func_list = ujson.load(f)
    for k in key_func_list:
        if k['switch_code'] == key_name:
            return k['bl_code']


# 获取普通码json数据格式
def get_ircode_json():
    ircode_json_dict = {
        "devtypeid": 1,  # 设备类型id
        "brand": "",  # 品牌中文名
        "branid": "",  # 品牌id
        "elecModel": "",  # 设备型号，可以为空
        "remoteModel": "",  # 遥控器型号，可以为空
        "origin": "switch bot",  # 该红码从哪获取的
        "old_ircodeid": "1",  # 在原app处的排序, 如果没有可以随便写
        "upload_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "functionList": []
    }
    return ircode_json_dict


# 根据switchbot品牌获取对应的博联码库品牌
def get_blbrand_by_swbrand(brand_name: str):
    import ujson
    with open('switch-bot-crawl/blbrand.json', 'r', encoding='utf-8') as f:
        bl_brand_list = ujson.load(f)
    for b in bl_brand_list:
        if b['brand'] == brand_name:
            return b['brandid']
        else:
            return 0


# 连接设备 模拟操作
import time
import uiautomator2 as u2

d = u2.connect_usb('d06ec202')
# d.app_stop("com.theswitchbot.switchbot")
# time.sleep(2)
# d.app_start("com.theswitchbot.switchbot")
# 等待出现“在线”字样 再进行点击
# d(text="离线").wait(timeout=2.0)
time.sleep(3)
while not d(resourceId="com.theswitchbot.switchbot:id/remote_status").exists:
    time.sleep(random.randint(1, 3))
d(resourceId="com.theswitchbot.switchbot:id/remote_status").click()
# 添加电器
while not d(resourceId="com.theswitchbot.switchbot:id/add_appliance_tv").exists:
    time.sleep(random.randint(1, 3))
d(resourceId="com.theswitchbot.switchbot:id/add_appliance_tv").click()
# 选择电器
time.sleep(random.randint(1, 3))
d(text="电视").wait(timeout=3.0)
time.sleep(random.randint(1, 3))
while not d.xpath('//*[@resource-id="com.theswitchbot.switchbot:id/rvAddDeviceList"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').exists:
    time.sleep(random.randint(1, 3))
d.xpath('//*[@resource-id="com.theswitchbot.switchbot:id/rvAddDeviceList"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()
time.sleep(random.randint(1, 3))
# %%
import os
# 根据品牌及型号进行模拟点击操作 并记录红码数据
import ujson

success_brand_list = list()
brandJsonList = get_no_model_brand()
for brand_key, brand in enumerate(brandJsonList):
    time.sleep(random.randint(1, 5))
    if brand in success_brand_list:
        continue
    print("当前时间为："+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(f"当前品牌为：{brand['brand']}")
    print(f"当前进度为：{brand_key + 1}/{len(brandJsonList)}")
    brand_path = f"./switchbot/{brand['brand'].replace(' ', '_')}/"
    if not os.path.exists(brand_path):
        os.mkdir(brand_path)
    if brand_key == 0:
        # 处理品牌下没有型号按键(直接跳转到按键界面)
        while not d(resourceId="com.theswitchbot.switchbot:id/filter_edit").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/filter_edit").set_text(brand['brand'])
        while not d.xpath(
                '//*[@resource-id="com.theswitchbot.switchbot:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').exists:
            time.sleep(random.randint(1, 3))
        d.xpath(
            '//*[@resource-id="com.theswitchbot.switchbot:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        while not d(resourceId="com.theswitchbot.switchbot:id/text_item_name").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/text_item_name").click()
        # 点击品牌
        # d(resourceId="com.theswitchbot.switchbot:id/text_item_name", text="A.R.SYSTEMS").click()
        d(text="等待红外信号").wait(timeout=5)
        # 搜索新品牌
        while not d(resourceId="com.theswitchbot.switchbot:id/tvWaitManualButton").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/tvWaitManualButton").click()
        # samsung
        while not d(resourceId="com.theswitchbot.switchbot:id/filter_edit").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/filter_edit").set_text(brand['brand'])
        while not d.xpath(
                '//*[@resource-id="com.theswitchbot.switchbot:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').exists:
            time.sleep(random.randint(1, 3))
        d.xpath(
            '//*[@resource-id="com.theswitchbot.switchbot:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        while not d(resourceId="com.theswitchbot.switchbot:id/text_item_name").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/text_item_name").click()
        # 点击空白区域
        while not d.xpath('//*[@resource-id="com.theswitchbot.switchbot:id/tvGuideTitle"]').exists:
            time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.theswitchbot.switchbot:id/tvGuideTitle"]').click()
        # 方案计数
        plan_count = int(
            d(resourceId="com.theswitchbot.switchbot:id/tvRemoteTVIndex").info['text'].split(" ")[-1].split("/")[-1])
        # 无型号 但是键位方案有多种  第一个方案的键位点击结束 程序需要中断 然后将其所得的普通红码与键位绑定并标记 完成 然后再次页面右滑0.1(经过测试只能是0.1，不能大于0.1)，剩下操作同上。
        for i in range(1, plan_count + 1):
            time.sleep(random.randint(1, 5))
            print(f"当前品牌方案为：{brand['brand']}-{i}")
            print(f"当前品牌下方案进度为：{i}/{plan_count + 1}")
            # 逐个按键模拟
            ircode_json_dict = get_ircode_json()
            # 按键数组 多个按键对象
            func_key_list = list()
            # 更新品牌
            ircode_json_dict.update({'brand': brand['brand'], 'brandid': get_blbrand_by_swbrand(brand['brand'])})
            # 第1屏键位 9个键
            click_keys_1 = ["iv_TVMute", "iv_TVPowerOnOff", "iv_TVMenuOff", "iv_ChannelDelete", "iv_ChannelAdd",
                            "iv_VolumeDelete", "iv_VolumeAdd", "iv_tv_input", "iv_tv_data"]
            for c1 in click_keys_1:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/iv_TVMute").info['enabled']:
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c1}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c1), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第2屏键位
            click_keys_2 = ["iv_tv_subtitle", "iv_tv_audio", "iv_Top", "iv_Bottom", "iv_Left", "iv_Right", "iv_Center",
                            "iv_tv_back", "iv_tv_list"]
            for c2 in click_keys_2:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c2}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c2}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c2), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第3屏键位
            click_keys_3 = ["iv_tv_blue", "iv_tv_red", "iv_tv_green", "iv_tv_yellow", "iv_tv_number1", "iv_tv_number2",
                            "iv_tv_number3", "iv_tv_number4", "iv_tv_number5", "iv_tv_number6"]
            for c3 in click_keys_3:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c3}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c3}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c3), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第4屏键位
            click_keys_4 = ["iv_tv_number7", "iv_tv_number8",
                            "iv_tv_number9", "iv_tv_number10", "iv_tv_number11",
                            "iv_tv_number12", "iv_tv_number10", "iv_tv_number11",
                            "iv_tv_number12", "iv_tv_program_list", "iv_tv_fav",
                            "iv_tv_bs", "iv_tv_cs", "iv_tv_dttv"]
            for c4 in click_keys_4:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c4}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c4}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c4), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第5屏键位
            click_keys_5 = ["iv_tv_internet", "iv_tv_three_code", "iv_tv_fast_reverse", "iv_tv_play",
                            "iv_tv_fast_forward", "iv_tv_last", "iv_tv_pause",
                            "iv_tv_next", "iv_tv_record", "iv_tv_stop", "iv_tv_take_out"]
            for c5 in click_keys_5:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c5}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c5}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c5), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            # 聚合全部按键保存
            ircode_json_dict.update({'functionList': func_key_list})
            with open(f"{brand_path}plan{i}-ircode.json", 'a', encoding='utf-8') as f:
                ujson.dump(ircode_json_dict, f, ensure_ascii=False)
                f.write('\n')
            print(f"{brand['brand']}-plan-{i}-抓取结束")
            d.swipe_ext("left", 0.5)
            while not d(resourceId="com.theswitchbot.switchbot:id/iv_TVMute").exists:
                for _ in range(5):
                    d.swipe_ext("down", 1)
            time.sleep(5)
            if i == plan_count:
                success_brand_list.append(brand['brand'])
                break
    else:
        while not d(resourceId="com.theswitchbot.switchbot:id/tvBackTip").exists:
            continue
        d(resourceId="com.theswitchbot.switchbot:id/tvBackTip").click()
        while not d(resourceId="com.theswitchbot.switchbot:id/filter_edit").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/filter_edit").set_text(brand['brand'])
        while not d.xpath(
                '//*[@resource-id="com.theswitchbot.switchbot:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').exists:
            time.sleep(random.randint(1, 3))
        d.xpath(
            '//*[@resource-id="com.theswitchbot.switchbot:id/fragment_container"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        while not d(resourceId="com.theswitchbot.switchbot:id/text_item_name").exists:
            time.sleep(random.randint(1, 3))
        d(resourceId="com.theswitchbot.switchbot:id/text_item_name").click()
        # 点击空白区域
        while not d.xpath('//*[@resource-id="com.theswitchbot.switchbot:id/tvGuideTitle"]').exists:
            time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.theswitchbot.switchbot:id/tvGuideTitle"]').click()
        # 方案计数
        plan_count = int(
            d(resourceId="com.theswitchbot.switchbot:id/tvRemoteTVIndex").info['text'].split(" ")[-1].split("/")[-1])
        # 无型号 但是键位方案有多种  第一个方案的键位点击结束 程序需要中断 然后将其所得的普通红码与键位绑定并标记 完成 然后再次页面右滑0.1(经过测试只能是0.1，不能大于0.1)，剩下操作同上。
        for i in range(1, plan_count + 1):
            time.sleep(random.randint(1, 5))
            print(f"当前品牌方案为：{brand['brand']}-{i}")
            print(f"当前品牌下方案进度为：{i}/{plan_count + 1}")
            # 逐个按键模拟点击
            ircode_json_dict = get_ircode_json()
            # 按键数组 多个按键对象
            func_key_list = list()
            # 更新品牌
            ircode_json_dict.update({'brand': brand['brand'], 'brandid': get_blbrand_by_swbrand(brand['brand'])})
            # 第1屏键位 9个键
            click_keys_1 = ["iv_TVMute", "iv_TVPowerOnOff", "iv_TVMenuOff", "iv_ChannelDelete", "iv_ChannelAdd",
                            "iv_VolumeDelete", "iv_VolumeAdd", "iv_tv_input", "iv_tv_data"]
            for c1 in click_keys_1:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/iv_TVMute").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c1}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c1), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第2屏键位
            click_keys_2 = ["iv_tv_subtitle", "iv_tv_audio", "iv_Top", "iv_Bottom", "iv_Left", "iv_Right", "iv_Center",
                            "iv_tv_back", "iv_tv_list"]
            for c2 in click_keys_2:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c2}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c2}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c2), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第3屏键位
            click_keys_3 = ["iv_tv_blue", "iv_tv_red", "iv_tv_green", "iv_tv_yellow", "iv_tv_number1", "iv_tv_number2",
                            "iv_tv_number3", "iv_tv_number4", "iv_tv_number5", "iv_tv_number6"]
            for c3 in click_keys_3:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c3}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c3}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c3), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第4屏键位
            click_keys_4 = ["iv_tv_number7", "iv_tv_number8",
                            "iv_tv_number9", "iv_tv_number10", "iv_tv_number11",
                            "iv_tv_number12", "iv_tv_number10", "iv_tv_number11",
                            "iv_tv_number12", "iv_tv_program_list", "iv_tv_fav",
                            "iv_tv_bs", "iv_tv_cs", "iv_tv_dttv"]
            for c4 in click_keys_4:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c4}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c4}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c4), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            d.swipe_ext("up", 1)
            # 第5屏键位
            click_keys_5 = ["iv_tv_internet", "iv_tv_three_code", "iv_tv_fast_reverse", "iv_tv_play",
                            "iv_tv_fast_forward", "iv_tv_last", "iv_tv_pause",
                            "iv_tv_next", "iv_tv_record", "iv_tv_stop", "iv_tv_take_out"]
            for c5 in click_keys_5:
                if os.path.exists("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                    os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
                if d(resourceId=f"com.theswitchbot.switchbot:id/{c5}").info['enabled']:
                    time.sleep(random.randint(1, 3))
                    d(resourceId=f"com.theswitchbot.switchbot:id/{c5}").click()
                    time.sleep(random.randint(1, 3))
                    if os.path.exists(
                            "D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt"):
                        func_dict = {"function": get_blkey_by_swbkey(c5), "code": []}
                        func_dict.update({"code": get_redcode()})
                        time.sleep(random.randint(1, 3))
                        func_key_list.append(func_dict)
                        os.remove("D:/workspace/IRReader/IRReader2015/demo20190619-1/IRDemo/bin/Debug/err_code.txt")
            # 聚合全部按键保存
            ircode_json_dict.update({'functionList': func_key_list})
            with open(f"{brand_path}plan{i}-ircode.json", 'a', encoding='utf-8') as f:
                ujson.dump(ircode_json_dict, f, ensure_ascii=False)
                f.write('\n')
            print(f"{brand['brand']}-plan-{i}-抓取结束")
            d.swipe_ext("left", 0.5)
            while not d(resourceId="com.theswitchbot.switchbot:id/iv_TVMute").exists:
                for _ in range(5):
                    d.swipe_ext("down", 1)
            time.sleep(2)
            if i == plan_count:
                success_brand_list.append(brand['brand'])
                break
