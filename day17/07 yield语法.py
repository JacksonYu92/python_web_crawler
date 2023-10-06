# yield: 迭代器和生成器：优化存储
# yield: 实现协程

def get_data():
    print("start")
    yield 1 # 暂时返回，保存状态
    print('come back')
    yield 2
    print('come back2')
    yield 3

gen = get_data() # <generator object get_data at 0x00000245E6F64350>
print(gen)
# gen.send(None)
ret = next(gen)
print(ret)
ret = next(gen)
print(ret)
ret = next(gen)
print(ret)