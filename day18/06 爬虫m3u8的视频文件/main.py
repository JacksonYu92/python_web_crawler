import requests
import re
import os

session = requests.Session()

# (1) 爬取m3u8文件的链接
url = "http://www.bdfzxj.net/play/9132-0-0.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
res = session.get(url, headers=headers, verify=False)

m3u8_link = re.search('now="(.*?m3u8)"', res.text).group(1)
print(m3u8_link)  # https://top.1080pzy.co/202310/06/hZWsXBGt4P3/video/index.m3u8
# 顺便抓一个名字
name = re.search(r'<title>(.*?)</title>', res.text).group(1).split('-')[0]
print("name", name)
# (2) 爬取m3u8文件
res = session.get(m3u8_link)
print(res.text.split("\n")[-2])
print(os.path.dirname(m3u8_link))

# m3u8_detail_link = os.path.join(os.path.dirname(m3u8_link), res.text.split("\n")[-2])
m3u8_detail_link = os.path.dirname(m3u8_link)+'/'+res.text.split("\n")[-2].strip()
print(m3u8_detail_link)

# (3) 爬取m3u8具体文件

res = requests.get(m3u8_detail_link)
print(res.text)

# (4) 解析ts文件
ret = re.findall(r"\n(.*?\.ts)", res.text)
print(ret)

# (5) 下载每一个ts文件
p = os.path.dirname(m3u8_detail_link)
with open(name, "ab") as f:
    for ts in ret:
        path = os.path.join(p, ts)
        res = requests.get(path)
        f.write(res.content)
        print(f"{ts}下载完成！")