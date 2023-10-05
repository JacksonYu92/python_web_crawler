import requests

res = requests.get("https://t7.baidu.com/it/u=4162611394,4275913936&fm=193&f=GIF")
print(res.text)
print(res.content)
with open("dog.jpg", "wb") as f:
    f.write(res.content)