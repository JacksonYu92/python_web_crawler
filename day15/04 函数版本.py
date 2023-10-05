import requests
from lxml import etree
import os
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}

session = requests.session()

def login():
    session.post("https://passport.17k.com/ck/user/login", data={
        "loginName": "YOURLOGINNAME",
        "password": "YOURPASSWORD",
    }, headers=headers)

def get_shelf_books():
    """
    params:
    :return: data [{},{},{}]
    """
    res = session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919")
    res.encoding = "utf8"
    # print(res.text)
    data = res.json().get("data")
    # print(data)
    return data

def get_books(data):

    for bookDict in data:
        # print(bookDict)
        bookId = bookDict.get("bookId")
        bookName = bookDict.get("bookName")
        # 创建一个书籍的文件夹
        book_path = os.path.join("我的书架", bookName)
        if not os.path.exists(book_path):
            os.mkdir(book_path)

        get_chapter(bookId, book_path, bookName)

def get_chapter(bookId, book_path, bookName):
    res = requests.get(f"https://www.17k.com/list/{bookId}.html")
    res.encoding = "utf8"
    selector = etree.HTML(res.text)
    items = selector.xpath('//dl[@class="Volume"]/dd/a')
    for item in items:
        # 每一本书籍的每一章节的信息
        chapter_href = item.xpath("./@href")[0]
        chapter_title = item.xpath("./span/text()")[0].strip()
        # print("href", href)
        # print("chapter_title", chapter_title)
        # 爬取章节内容
        res = requests.get("https://www.17k.com" + chapter_href)
        res.encoding = "utf8"
        chapter_html = res.text
        # print(chapter_html)

        selector = etree.HTML(res.text)
        chapter_text = selector.xpath('//div[contains(@class,"content")]/div[@class="p"]/p[position()<last()]/text()')
        print(chapter_text)

        # 章节进行下载，写入到一个文件中
        download(book_path, chapter_title, chapter_text)

        time.sleep(random.randint(1, 3))
        print(f"{bookName}书籍的{chapter_title}章节下载完成！")

def download(book_path, chapter_title, chapter_text):
    chapter_path = os.path.join(book_path, chapter_title)
    with open(chapter_path, "w") as f:
        for line in chapter_text:
            f.write(line + "\n")

login()
data = get_shelf_books()


# 创建个人书架的文件夹
root_path = "我的书架"
if not os.path.exists(root_path):
    os.mkdir(root_path)

get_books(data)
