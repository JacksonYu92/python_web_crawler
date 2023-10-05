# with open("我的一天", mode="r", encoding="GBK") as f:
#     data = f.read()
#
# print(data)

# with open("我的一天", mode="r") as f:
#     data = f.read()
#
# print(data)

# with open("hello", mode="r", encoding="utf8") as f:
#     data = f.read()


# with open("hello", mode="rb") as f:
#     data = f.read()

with open("hello", mode="wb") as f:
    data = f.read("我这辈子精彩极了！".encode())
print(data)