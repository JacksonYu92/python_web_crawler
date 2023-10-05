import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Referer":"https://movie.douban.com/explore",
}

url = "https://m.douban.com/rexxar/api/v2/movie/recommend"

res = requests.get(
    url,
    headers=headers,
    params={
        "count": "20",
        "tags": "悬疑",
    }
                   )
# print(res.text)

# 方法一
# import json
# data = json.loads(res.text)
# print(data)
# print(type(data))
#
# print(res.json())

for item in res.json()["items"]:
    if item.get("title"):
        print(item.get("title"))