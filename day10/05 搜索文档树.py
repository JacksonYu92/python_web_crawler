from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story01</b><b>The Dormouse's story02</b></p>
<b>BBB</b>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 一 name 参数
# 1 字符串，即标签名
# ret = soup.find_all(name="b")
#
# print(ret)

# 2 正则
# ret = soup.find_all(name=re.compile('^b'))
# print(ret)

# 3 列表
# ret = soup.find_all(name=['a','b'])
# print(ret)

# 4 方法
# def has_class_has_id(tag):
#     return tag.has_attr('class') and tag.has_attr('id')
#
# print(soup.find_all(name=has_class_has_id))


# 二 关键字参数

# ret = soup.find_all(href="http://example.com/elsie")
# ret = soup.find_all(attrs={"href":"http://example.com/elsie"})
# ret = soup.find_all(href=re.compile("^http://"), id=re.compile("^link"))
# ret = soup.find_all(href=re.compile("^http://"), class_="sister")
# print(ret)

# 按文本过滤
# ret = soup.find_all(string="Elsie")
# ret = soup.find_all(string=re.compile("Dormouse"), limit=2)
# print(ret)

# find方法
# print(soup.find("a"))
# print(soup.a)

# 兄弟方法
# print(soup.a.next_sibling)
# print(soup.a.find_next_sibling())


# tag.find_all
tag = soup.p

ret = tag.find_all("b")
print(ret)