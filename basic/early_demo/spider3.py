# 1.发送请求
from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen('http://desk.zol.com.cn/')
#返回数据
html = response.read()
#返回网页源码
print(response)
response.read()
#解析并返回数据（url/title）组成列表
soup = BeautifulSoup(html,'html.parser',from_encoding='gbk')
#获取所有图片li
li = soup.find_all('li',class_="photo_list_padding")
#数据列表
info_list =[]
for li in list:
    temp = []
    a = li.find_all('a')[0]
    img = li.find_all('img')[0]
    temp['url'] = 'http://desk.zol.com.cn/%s' % a['href']
    temp['title'] = img['alt']
    info_list.append(temp)
#循环数据表
for info in info_list:
    #每一条url发送请求
    response = request.urlopen(['url'])
    htm = response.read()
#解析获取大图列表
    soup = BeautifulSoup(htm,'htm.parser')
    ul = soup.find_all('ul',id = 'slwnImg')[0]
    img_lis = ul.find_all('li')
#获取大图列表
bigimg_list = []
for li in img_lis:
    img = li.find_all('img')[0]
    try:
        url = img['src']
    except Exception as e:
        url = img['src']
    bigimg_list.append(url)
#新建文件夹
s.mkdir(info['title'])
#循环下载图片
j = 1
for url in bigimg_list:
    img_data = request.urlopen(url.read())
    with open('%s\\%s.jpg' % (info['title'],j),'wb') as f:
        f.write(img_data)
        j+=1