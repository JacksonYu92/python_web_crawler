import requests


# 模拟登录获取cookie
session = requests.session()

session.post("http://127.0.0.1:5000/auth", data={
    "user": "root",
    "pwd": "123",
})


res2 = session.get("http://127.0.0.1:5000/books")
print(res2.text)