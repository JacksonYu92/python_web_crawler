import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}

session = requests.session()

session.post("https://passport.17k.com/ck/user/login", data={
    "loginName": "YOURLOGINNAME",
    "password": "YOURPASSWORD",
}, headers=headers)


res = session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919")
res.encoding = "utf8"
# print(res.text)
data = res.json().get("data")
# print(data)

for bookDict in data:
    print(bookDict)
    bookId = bookDict.get("bookId")
    res = requests.get(f"https://www.17k.com/list/{bookId}.html")
    print(res.text)
    break
