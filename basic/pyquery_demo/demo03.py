from pyquery import PyQuery as pq

# 同时根据标签和属性识别

a = '''
<body>
    <h>标题</h>
    <p id='p1'>段落1</p>
    <p id='p2'>段落2</p>
    <p class='p3'>段落3</p>
    <p class='p3' id='pp'>段落4</p>
</body>
'''
doc = pq(a)
print(doc('p#p2').text())  # 段落2
doc('p#p1').text()  # '段落1'
print(doc('p.p3[id]').text())  # 段落4
doc('p.p3[id]').text()  # 含有id属性
print(doc('p.p3#pp').text())  # 段落4
doc('p.p3#pp').text()  # 使用多个属性筛选
doc('p[class=p3][id=pp]').text()
doc('p[class=p3], p[id=p1]').text()  # 或的关系
doc('p[class=p3],[id=p1]').text()  # 或者只用,隔开
doc('*#p1').text()  # 不指定标签名

# 否定
doc('p:not([id])').text()  # 不含有id属性
doc('body :not(p)').text()  # 选出不是p的子节点  '标题'
doc('p:not(.p3)').text()  # 选出class不是p3的
doc('p[id][id!=p2]').text()  # 也可以用!=，这里选择有id且id不是p2的

# 类似正则表达式
doc('p[id^=p]').text()  # 首端匹配
doc('p[id$=p]').text()  # 尾端匹配
doc('p[id*=p]').text()  # 包含

# 根据标签内内容来识别
c = '''
<p id='p1'>段落1</p>
<p class='p3'>段落2</p>
<p class='p3'>文章</p>
<p></p>
'''

doc = pq(c)
# :contains查找内容中包含某字符串的标签
doc('p:contains(段落1)').text()  # '段落1'
doc('p:contains(段落)').text()  # '段落1 段落2'
doc('p:contains("1")').text()
