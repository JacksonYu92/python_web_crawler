# 一、读操作

# file = open("doubantop250.html", mode="r")
# print(file.read())
# print(file.readline())
# print(file.readlines())

# for line in file:
#     print(line)
from lxml import etree

with open("doubantop250.html") as f:
    data = f.read()

selector = etree.HTML(data)

# rets = selector.xpath('//ol[@class="grid_view"]/li//div[@class="hd"]//span[@class="title"][1]/text()')
# print(rets)

rets = selector.xpath('//ol[@class="grid_view"]/li')

infos = []

for item in rets:
    # print(item)
    name = item.xpath('./div//div[@class="hd"]//span[@class="title"][1]/text()')[0]
    rating_num = item.xpath('./div//div[@class="bd"]//span[@class="rating_num"][1]/text()')[0]
    comment_num = item.xpath('./div//div[@class="star"]//span[last()]/text()')[0]
    # print(name, rating_num, comment_num)
    info = (name, rating_num, comment_num)
    infos.append(info)

print(infos)

file = open("豆瓣优秀电影.json", mode="w")
import json
infosStr = json.dumps(infos,ensure_ascii=False)
file.write(infosStr+"\n")
file.close()