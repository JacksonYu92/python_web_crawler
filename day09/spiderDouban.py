with open("doubantop250.html") as f:
    s = f.read()


import re

ret = re.findall('<li>.*?class="item">.*?<div class="info">.*?<div class="hd">.*?<span class="title">(.*?)</span>.*?<span class="rating_num".*?>(.+?)</span>.*?<span>(.+?)</span>', s, re.S)
# ret = re.findall('<li>.*?class="item">.*?<span class="rating_num".*?>(.*?)</span>', s,re.S)
print(ret)
print(len(ret))