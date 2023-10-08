import requests
from lxml import etree
import os
import time
import asyncio
import aiohttp

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    }

async def get_img_urls():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.pkdoutu.com/",headers=headers, ssl=False) as response:
            selector = etree.HTML(await response.text())
            img_urls = selector.xpath('//li[@class="list-group-item"]/div/div/a/img[@data-backup]/@data-backup')
            print(img_urls)

            return img_urls

async def download_img(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            img_name = os.path.basename(url)
            path = os.path.join("imgs", img_name)

            with open(path,"wb") as f:
                f.write(await response.content.read())

            print(f"{img_name}下载完成！")

async def main():
    # (1) 爬取当前页的所有的img_url
    img_urls = await get_img_urls()
    # (2) 根据img_urls下载图片
    tasks = [asyncio.create_task(download_img(url)) for url in img_urls]
    await asyncio.wait(tasks)

# 主逻辑
start = time.time()
asyncio.run(main())
print(f"整体耗时{time.time() - start}秒")