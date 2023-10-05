import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Referer":"https://movie.douban.com/explore",
}

res = requests.get(
    "https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=",
    headers=headers
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