import requests


# 模拟登录获取cookie
res1 = requests.post("http://127.0.0.1:5000/auth", data={
    "user": "root",
    "pwd": "123",
})
# 响应cookie
print(dict(res1.cookies))

res2 = requests.get("http://127.0.0.1:5000/books", cookies=dict(res1.cookies))
print(res2.text)