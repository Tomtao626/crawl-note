# /usr/bin/env python
# -*- coding:UTF-8 -*-

#from urllib import request
from urllib import request
from bs4 import BeautifulSoup
import re
import time
import gevent
from gevent import monkey
monkey.patch_all()


# 解析器
def parser(html):
    try:
        soup = BeautifulSoup(html, 'html.arseer', from_encoding='GBK')
        # 获取所有的img
        imgs = soup.find_all('imgs', src=re.compile(r'/d/file/\d+/\w+\.jpg'))
        return imgs
    except Exception as e:
        print('in parser error=%s' % e)
        return None


# 保存图片
def save_img(path,data):
    try:
        with open(path,'wb') as f:
            f.write(data)
    except Exception as e:
        print('in save_img error=%s' % e)
# 下载器
def download(url):
    header = \
        {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Mobile Safari/537.36'
        }  # user-Agent就是一个铭牌
    try:
    # 包装一个请求
        req = request.Request(url=url, headers=header)
        response = request.urlopen(req,timeout=10)
        return response.read()
    except Exception as e:
        print('in download error=%s' % e)

# 主函数
def spider():
    first_url = "http://www.xiaohuar.com/list-1-1-%s.html"
    imgs = []
    for i in range(10):
        html = download(first_url%i)
    # html = download(first_url)
        if html:
            temp = parser(html)
        if temp !=[]:
            imgs += temp

    s_time = time.time()
    glist = []
    if imgs != []:
        for img in imgs:
            data = download( "http://www.xiaohuar.com" % img['src'])
            g = gevent.spawn(save_img,'%s.jpg' % img['alt'],data)
            glist.append(g)
            # save_img('%s.jpg'%img['alt'],data)
        gevent.joinall(glist)
        e_time = time.time()
        print("耗费%s秒" % (e_time - s_time))
    else:
        print('网络错误')
    print("耗费%s秒"% (e_time-s_time))


if __name__ == '__main__':
    spider()