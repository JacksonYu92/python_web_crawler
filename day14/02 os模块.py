import os

# 创建文件夹
# os.mkdir("我的模块")

# os.remove("我的模块")

# print(os.path.sep)   # \

# 路径拼接
# path = os.path.join("我的模块", "apple.txt")
# print(path)
#
# with open(path, "w") as f:
#     pass

# 获取文件和文件夹的目录
# print(os.path.dirname(__file__))
# print(os.path.dirname(path))
# print(os.path.dirname("D:\Python爬虫\JS逆向爬虫VIP1期\day14"))


# print(os.path.exists("我的模块"))

path = "D:\Python爬虫\JS逆向爬虫VIP1期\day14\我的模块"
print(os.path.basename(path))
print(os.path.split(path))