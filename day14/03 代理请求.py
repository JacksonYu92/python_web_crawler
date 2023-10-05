import requests

res = requests.get("http://httpbin.org/ip",
             proxies={
                 "http": "101.132.25.152:50001"
             })

print(res.text)