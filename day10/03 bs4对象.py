from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<b>BBB</b>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.find_all("a"))


# 查找标签
# print(soup.body)
# print(type(soup.body))
#
# print(soup.b)

# print(soup.p.b)
# print(soup.p.a)

# print(soup.p.b.name) #"b"
# print(soup.a.name)
# print(soup.a["href"])
# print(soup.a.attrs)
# print(soup.a.string)
# print(soup.a.text)
#
# print(soup.p.string)
# print(soup.p.text)

# 获取 文档的标签信息，构建{a标签的文本：a的href作为值}

d = {}
ret = soup.find_all("a")
print(ret)
for tag in ret:
    # print(tag.text)
    # print(tag["href"])
    d[tag.text] = tag["href"]

print(d)

print({tag.text: tag["href"] for tag in soup.find_all("a")})