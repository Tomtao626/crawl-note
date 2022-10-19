"""
__project_ = 'python_crawler'
__file_name__ = 'solution'
__author__ = 'BroadLink'
__time__ = '2021/6/8 15:58'
__product_name = PyCharm
"""
import re

"""
    爬虫往往不能在一个页面里面获取全部想要的数据，需要访问大量的网页才能够完成任务。
    这里有一个网站，还是求所有数字的和，只是这次分了1000页。
    网站url: http://www.glidedsky.com/level/web/crawler-basic-2?page=n
    由于网站策略发生变化，cookie无法直接从浏览器拿到，需要登录进行身份鉴权
"""
import parsel
import requests
from lxml import etree

base_url = 'http://www.glidedsky.com/level/web/crawler-basic-2?page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}
# 登录url
login_url = "http://www.glidedsky.com/login"
# 会话保持 在跨请求时保存某些参数
# 实例化session
session = requests.session()
# 根据session发送get请求 获取token
token_request = session.get(login_url, headers=headers)
# print(token_request.text)
_token = re.search('"_token" value="(.*?)"', token_request.text).group(1)
print(_token)
data = {
    "_token": _token,
    "email": "tp320670258@gmail.com",
    "password": "tp751825253"
}
# 发送post请求 登录
res = session.post(url=login_url, data=data)
# get请求获取目标页面数据
# 由于有1000页
sums = 0
for page in range(1, 1001):
    response = session.get(f"{base_url}{page}", headers=headers)
    data = etree.HTML(response.text)
    # print(response.text)
    last_list = "".join(data.xpath('//div[@class="row"]/div/text()')).split()
    # print(last_list)
    # 推导式
    sums += sum(int(i) for i in last_list)
print(sums)
# map
# print(sum(map(int, last_list)))

