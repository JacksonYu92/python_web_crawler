
s = "i am 余"

# 编码方法
ret1 = s.encode("utf8")
ret2 = s.encode("GBK")

# 解码方法  字节数据对象.decode("规则")
print(ret1.decode("utf8"))
print(ret2.decode("GBK"))