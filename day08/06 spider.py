import requests

res = requests.get("http://127.0.0.1:5000/books")
print(res.text)
print(res.json())