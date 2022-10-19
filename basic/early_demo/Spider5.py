from bs4 import BeautifulSoup  #适合简单页面
from urllib.request import urlopen,urlretrieve
import re
#爬虫
url = input("请输入你的链接：")
html = urlopen(url)
content = html.read().decode()
urls = re.findall(r'"objURL":"(.*?)"',content)
print(urls)
index = 1
for url in urls:
    if index <= 7:
        try:
            print("Downloading....")
            if 'jpg' in url:
                urlretrieve(url,str(index)+'.jpg')
            elif 'png' in url:
                urlretrieve(url, str(index) + '.png')
            elif 'jpeg' in url:
                urlretrieve(url, str(index) + '.jpeg')
            else:
                urlretrieve(url, str(index) + '.png')
            index += 1
        except Exception:
            print("Download Failed...",index)
        else:
            print("Download complete")
    else:
        break
#"objURL" = ""
#html页面
# content = html.read()
# res = BeautifulSoup(content,'html.parser')
# name_list = res.findAll('span',{'class':'green'})
#res列表
# for name in name_list:
#     print(name.get_text())
# print(res.h1)
# print(res.)
# print(type(content))
# print(content)
#thumbURL
#middleURL
#hoverURL
#ObjURL
#objURL
