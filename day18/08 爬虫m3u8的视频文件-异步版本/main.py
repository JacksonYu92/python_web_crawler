import requests
import re
import os
import time
import asyncio
import aiohttp


async def get_first_m3u8():
    # (1) 爬取m3u8文件的链接
    url = "http://www.bdfzxj.net/play/9132-0-0.html"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
            text = await response.text()

            first_m3u8_link = re.search('now="(.*?m3u8)"', text).group(1)
            print(first_m3u8_link)  # https://top.1080pzy.co/202310/06/hZWsXBGt4P3/video/index.m3u8
            # 顺便抓一个名字
            name = re.search(r'<title>(.*?)</title>', text).group(1).split('-')[0]
            print("name", name)
            return first_m3u8_link, name


async def get_second_m3u8_link(first_m3u8_link):
    # (2) 爬取m3u8文件
    async with aiohttp.ClientSession() as session:
        async with session.get(first_m3u8_link, ssl=False) as response:
            text = await response.text()

            second_m3u8_link = os.path.dirname(first_m3u8_link) + '/' + text.split("\n")[-2].strip()
            print(second_m3u8_link)
            return second_m3u8_link

async def parse_ts(second_m3u8_link):
    # (3) 爬取m3u8具体文件
    async with aiohttp.ClientSession() as session:
        async with session.get(second_m3u8_link, ssl=False) as response:
            text = await response.text()

            # (4) 解析ts文件
            ret = re.findall(r"\n(.*?\.ts)", text)
            print(ret)
            return ret

# (5) 下载每一个ts文件
# p = os.path.dirname(m3u8_detail_link)
async def download_ts(ts, name):
    # path = "ts文件"+ "/" +ts
    async with aiohttp.ClientSession() as session:
        async with session.get(ts, ssl=False) as response:
            with open(name, "wb") as f:
                f.write(await response.content.read())
                print(f"{name}下载完成！")

def merge(filename="out"):
    os.chdir("ts文件")
    os.system(f"ffmpeg -i index.m3u8 -c copy {filename}.mp4")


async def main():
    # if not os.path.exists("ts文件"):
    #     os.mkdir("ts文件")
    # （1）爬取页面, 获取第一个m3u8链接
    first_m3u8_link, name = await get_first_m3u8()
    # （2）获取第二个m3u8链接
    second_m3u8_link = await get_second_m3u8_link(first_m3u8_link)
    # （3）解析ts文件
    ts_list = await parse_ts(second_m3u8_link)
    # （4）下载
    p = os.path.dirname(second_m3u8_link)
    print(p)
    tasks = []
    for ts in ts_list:
        name = ts.split('/')[-1]
        with open("index.m3u8", "a") as f:
            f.write(name + "\n")
        tasks.append(asyncio.create_task(download_ts(ts, name)))

    await asyncio.wait(tasks)
    merge(name)


start = time.time()
# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(f"耗时时间{time.time() - start}秒")