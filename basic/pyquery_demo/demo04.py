from pyquery import PyQuery as pq

# 根据位置识别

a = '''
    <title>标题</title>
    <body>
        <ul class='list1'>
            <li>列表1第1项</li>
            <li>列表1第2项</li>
        </ul>
        <p class='first'>文字1</p>
        <p class='second'>文字2</p>
        <ul class='list2'>
            <li>列表2第1项</li>
            <li>列表2第2项</li>
        </ul>
    </body>
'''

doc = pq(a)
print(doc('ul:nth-of-type(2) li').text())  # 选择第二个ul下的所有li
print(doc('ul li:nth-of-type(2)').text())  # 选择每个ul中第二个li
print(doc('ul li:even').text())  # :even取偶数  :odd取奇数（这里索引第一个是0）
print(doc('ul li:first').text())  # :first取第一个 :last取最后一个
print(doc('ul li:eq(0)').text())  # 还有 lt gt 索引从0开始
