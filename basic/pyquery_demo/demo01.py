from pyquery import PyQuery as pq

html_str = """
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
"""

doc = pq(html_str)
print(type(doc), '\n', doc)
print(doc('title').text())  # '标题'
print(doc('p.first').text())
print(doc('p').filter('.first').text())  # '文字1'
print(doc('p[class=first]').text())  # 同上，只是这种方法支持除了id和class之外的属性筛选

print(doc('p').text())  # '文字1 文字2'
print(doc('ul').filter('.list1').find('li').text())  # '列表1第1项 列表1第2项'
print(doc('ul.list1 li').text())  # 简化形式
print(doc('ul.list1 > li').text())  # 节点之间用>连接也可以，但是加>只能查找子元素，空格子孙元素

"""
如果你会jQuery,那么学pyquery将毫无难度。
pyquery可以像xpath语句一样，只输入一个字符串，里面是节点顺序以及属性筛选等，与xpath使用思路完全相同，只是语法不同而已，学好了xpath使用这个应该会很轻松
属性中有两个特例class和id，因为这两个是网页中用的最多的属性，所以使用时可以分别用.和#来表示
pyquery还定义了一些方法，每次进行一步操作，比如提取标签(find)、筛选属性(filter)等
"""
