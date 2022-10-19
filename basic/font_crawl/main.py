# 字体反爬实践


import requests
from lxml import etree
from fontTools.ttLib import TTFont

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
}
# from fontTools.ttLib import TTFont
# TTFont()  用来打开woff文件的
# font_d35c3812 = TTFont('d35c3812.woff')
# 保存为xml格式
# font_d35c3812.saveXML('font_d35c3812.xml')


# 手动将从FontCreator中获取的映射关系对应起来
relation_table = {'&#xf2f4': '1', '&#xe122': '2', '&#xf7f6': '3', '&#xe87d': '4', '&#xf7c6': '5',
                  '&#xe326': '6', '&#xf399': '7', '&#xf572': '8', '&#xf185': '9', '&#xe4ad': '0'}

url = "http://www.dianping.com/hangzhou/ch10"
response = requests.get(url, headers=headers)
text = response.text
for i in relation_table:
    if str(i) in text:
        text = text.replace(str(i), relation_table[i].replace(";", ""))

selector = etree.HTML(text)
lists = selector.xpath('//*[@id="shop-all-list"]/ul/li')
for i in lists:
    st = i.xpath('.//svgmtsi[@class="shopNum"]/text()')
    print(st)
    print("-----------")

print(len(lists))
