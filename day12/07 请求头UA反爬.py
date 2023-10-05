import requests

res = requests.get("https://www.baidu.com", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
})

with open("baidu.html", "w") as f:
    f.write(res.text)