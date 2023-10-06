import requests
from lxml import etree
import os
import time

def get_img_urls():
    res = requests.get("https://www.pkdoutu.com/photo/list/", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    })
    # print(res.text)

    selector = etree.HTML(res.text)
    img_urls = selector.xpath('//li[@class="list-group-item"]/div/div/a/img[@data-backup]/@data-backup')
    # print(img_urls)

    return img_urls

def download_img(url):
    res = requests.get(url)
    # img_name = url.split("/")[-1]
    img_name = os.path.basename(url)
    path = os.path.join("imgs", img_name)

    with open(path,"wb") as f:
        for i in res.iter_content():
            f.write(i)

    print(f"{img_name}下载完成！")

start = time.time()

# (1) 爬取当前页的所有的img_url
img_urls = get_img_urls()
# (2) 根据img_urls下载图片
for img_url in img_urls:
    download_img(img_url)

print(f"整体耗时{time.time() - start}秒")