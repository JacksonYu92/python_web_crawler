class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def test(self):
        pass


yuan = Student("yuan", 100)
print("获取所有的属性列表")
print(dir(yuan))

print("获取自定义属性字段")
print(yuan.__dict__)


import requests
res = requests.get("https://www.baidu.com")
print(dir(res))