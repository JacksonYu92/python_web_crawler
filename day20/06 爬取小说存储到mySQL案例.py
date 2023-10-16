import requests
from lxml import etree
import os
import time
import random
import pymysql


class XiaoShuoSpider(object):
    def __init__(self, user, pwd, database):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }

        self.session = requests.session()

        # 数据库初始化操作
        self.initMySQL(user, pwd, database)
        # 初始化表
        self.init_table()

    def initMySQL(self, user, pwd, database):
        self.conn = pymysql.connect(host='localhost', user=user, passwd=pwd, port=3307, database=database,
                                    cursorclass=pymysql.cursors.DictCursor, charset="utf8")

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def init_table(self):
        # 使用 execute() 方法执行SQL 查询
        sql1 = """
            create table if not exists book(
            id int primary key auto_increment,
            bookName varchar(32),
            coverImg varchar (255),
            authorPenName varchar(32)
            ) character set=utf8;
        """
        self.query(sql1)

        sql2 = """
            create table if not exists chapter(
            id int primary key auto_increment,
            chapter_name varchar(32),
            chapter_content text,
            book_id INT NOT NULL
            ) character set=utf8;
        """
        self.query(sql2)

    def login(self):

        self.session.post("https://passport.17k.com/ck/user/login", data={
            "loginName": "13426749358",
            "password": "jackson1992",
        }, headers=self.headers)

    def get_shelf_books(self):
        """
        params:
        :return: data [{},{},{}]
        """
        res = self.session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919")
        res.encoding = "utf8"
        # print(res.text)
        data = res.json().get("data")
        # print(data)
        return data

    def get_books(self, data):

        for bookDict in data:
            # print(bookDict)
            bookId = bookDict.get("bookId")
            bookName = bookDict.get("bookName")
            coverImg = bookDict.get("coverImg")
            authorPenName = bookDict.get("authorPenName")

            # 添加book记录
            sql = f"""
                insert into book (bookName, coverImg, authorPenName) values(
                "{bookName}","{coverImg}","{authorPenName}");
            """
            print("sql:::", sql)
            self.query(sql)

            self.get_chapters(bookId)

    def get_chapters(self, bookId):
        res = requests.get(f"https://www.17k.com/list/{bookId}.html")
        res.encoding = "utf8"
        selector = etree.HTML(res.text)
        items = selector.xpath('//dl[@class="Volume"][position()>1]/dd/a')
        for item in items:
            # 每一本书籍的每一章节的信息
            chapter_href = item.xpath("./@href")[0]
            chapter_title = item.xpath("./span/text()")[0].strip()
            # print("href", href)
            # print("chapter_title", chapter_title)
            # 爬取章节内容
            res = requests.get("https://www.17k.com" + chapter_href)
            res.encoding = "utf8"

            selector = etree.HTML(res.text)
            chapter_text_list = selector.xpath(
                '//div[contains(@class,"content")]/div[@class="p"]/p[position()<last()]/text()')
            # print(chapter_text) #["","",""]
            chapter_content = "\n".join(chapter_text_list)

        sql = f"""
            insert into chapter (chapter_name, chapter_content, book_id) values (
            "{chapter_title}", '{chapter_content}', "{bookId}");
        """
        print("sql:::", sql)
        self.query(sql)

    def run(self):
        self.login()
        data = self.get_shelf_books()

        self.get_books(data)


s = XiaoShuoSpider("root", "root", "xiaoshuo17k")
s.run()
