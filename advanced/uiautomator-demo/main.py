import os

import requests
import ujson
import base64

from models.Match import BrandInfo, AttachModels, Ircode, IrcodeInfo


# 读取json文件

# 获取品牌下多型号数据
def get_model_brand():
    with open('switch-bot-crawl/brand_model_fix.json', 'r', encoding='utf-8') as f:
        no_model_list = ujson.load(f)
    return no_model_list

# 获取类型为电视 状态为正常的 码文件id
IrcodeInfoQuery = IrcodeInfo.\
    select(IrcodeInfo.fileid).\
    filter(IrcodeInfo.devtypeid == 1, IrcodeInfo.status == '正常')
irfileid_list = [i.fileid for i in IrcodeInfoQuery]
# 获取json数据
IrcodeQuery = Ircode.\
    select(Ircode.fileid, Ircode.codejson).\
    filter(Ircode.fileid.in_(irfileid_list), Ircode.codejson != '')
# codestr文件解析 base64 -> json
for i in os.scandir("/Users/macos/Documents/workspaces/pywork/bluiautomator-note/switchbot_model"):
    print(i.name)
for filejson in [i._to_dict() for i in IrcodeQuery]:
    pass
