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
ret = selector.xpath("//a[1]/text()")
ret = selector.xpath("//a[1]/@href")
ret = selector.xpath("//a/@class")
ret = selector.xpath("//a/@id")
ret = selector.xpath("//a[@class='sister']")
ret = selector.xpath("//a[starts-with(@class,'sister')]")
print(ret)