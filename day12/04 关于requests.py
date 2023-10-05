import requests

res = requests.get("https://www.taobao.com")

# print(type(res))  # <class 'requests.models.Response'>
#
# print(res.status_code)
# print(res.headers)
# print(res.text)  # 字符串
print(res.encoding)
print(res.content)

# with open("taobao.html", "w") as f:
#     f.write(res.text)


with open("taobao.html", "wb") as f:
    f.write(res.content)    
