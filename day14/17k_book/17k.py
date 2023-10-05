import requests
import os
from bs4 import BeautifulSoup
import re

cookie = "GUID=d199ebf8-19f5-48e9-a442-23d8b4acbe0a; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1696339790; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F01%252F01%252F89%252F101928901.jpg-88x88%253Fv%253D1696340112618%26id%3D101928901%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BQ9j317YE9%26e%3D1711892112%26s%3D20954a64867b79c6; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22101928901%22%2C%22%24device_id%22%3A%2218af5bb0906e72-0aee48ceee0289-26031e51-1327104-18af5bb0907152c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22d199ebf8-19f5-48e9-a442-23d8b4acbe0a%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1696340404"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Referer": "https://user.17k.com/www/bookshelf/",
    "cookie":cookie,
}

url = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"

res = requests.get(url, headers=headers)
# print(res.json())
for book in res.json()['data']:
    bookName = book.get("bookName")
    bookId = book.get("bookId")
    path = "https://www.17k.com/book/"+ str(bookId)+".html"
    list_url = "https://www.17k.com/list/"+ str(bookId)+".html"
    res_book = requests.get(list_url, headers=headers)
    html_doc = res_book.content.decode("utf-8")
    soup = BeautifulSoup(html_doc, 'html.parser')
    # items = soup.find_all(class_="ellipsis")
    items = soup.find_all("dd")
    book_title = soup.find_all("h1")
    for title in book_title:

        print(title.text)
    # items = soup.find_all(href=re.compile("^/chapter/"))
    print(bookName, bookId, path, list_url)
    for item in items:
        # item.find_all(class_="ellipsis")
        # print(item)
        if "/chapter/" in item.a["href"]:
            chapter_url = "https://www.17k.com"+item.a["href"]

            # print(chapter_url)
            res_chapter_url = requests.get(chapter_url, headers=headers)
            html_doc = res_chapter_url.content.decode("utf-8")
            chapter_soup = BeautifulSoup(html_doc, 'html.parser')
            title = chapter_soup.find_all("h1")
            for t in title:
                print(t.text)
                contents = chapter_soup.find_all(class_="p")
                for content in contents:
                    print(content.text)
                with open(f"{t.text}.txt", "w") as f:
                    f.write(content.text)
                # print(contents)

# /html/body/div[5]/dl[2]/dd/a[1]
