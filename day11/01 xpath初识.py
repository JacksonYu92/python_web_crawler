from lxml import etree
()
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

selector = etree.HTML(html_doc)
# print(type(selector))   # <class 'lxml.etree._Element'>
ret = selector.xpath("//a")
print(ret)   # [<Element a at 0x294e206f500>, <Element a at 0x294e206f540>, <Element a at 0x294e206f580>]

for linkE in ret:
    name = linkE.xpath("./text()")[0]
    href = linkE.xpath("./@href")[0]
    print(name, href)