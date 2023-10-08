import requests
import re
import os

session = requests.Session()


def get_first_m3u8():
    # (1) 爬取m3u8文件的链接
    url = "http://www.bdfzxj.net/play/9132-0-0.html"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    res = session.get(url, headers=headers, verify=False)

    first_m3u8_link = re.search('now="(.*?m3u8)"', res.text).group(1)
    print(first_m3u8_link)  # https://top.1080pzy.co/202310/06/hZWsXBGt4P3/video/index.m3u8
    # 顺便抓一个名字
    name = re.search(r'<title>(.*?)</title>', res.text).group(1).split('-')[0]
    print("name", name)
    return first_m3u8_link, name


def get_second_m3u8_link(first_m3u8_link):
    # (2) 爬取m3u8文件
    res = session.get(first_m3u8_link)
    # print(res.text.split("\n")[-2])
    # print(os.path.dirname(m3u8_link))

    # m3u8_detail_link = os.path.join(os.path.dirname(m3u8_link), res.text.split("\n")[-2])
    second_m3u8_link = os.path.dirname(first_m3u8_link) + '/' + res.text.split("\n")[-2].strip()
    print(second_m3u8_link)
    return second_m3u8_link

def parse_ts(second_m3u8_link):
    # (3) 爬取m3u8具体文件
    res = requests.get(second_m3u8_link)
    print(res.text)

    # (4) 解析ts文件
    ret = re.findall(r"\n(.*?\.ts)", res.text)
    print(ret)
    return ret

# (5) 下载每一个ts文件
# p = os.path.dirname(m3u8_detail_link)
def download_ts(ts, name):
    with open(name, "wb") as f:
        # path = os.path.join(p, ts)
        res = requests.get(ts)
        f.write(res.content)
        print(f"{name}下载完成！")


def main():
    # （1）爬取页面, 获取第一个m3u8链接
    first_m3u8_link, name = get_first_m3u8()
    # （2）获取第二个m3u8链接
    second_m3u8_link = get_second_m3u8_link(first_m3u8_link)
    # （3）解析ts文件
    ts_list = parse_ts(second_m3u8_link)
    # （4）下载
    p = os.path.dirname(second_m3u8_link)
    print(p)
    for ts in ts_list:
        name = ts.split('/')[-1]
        # path = os.path.join(p, ts)
        # print(path)
        download_ts(ts, name)

main()