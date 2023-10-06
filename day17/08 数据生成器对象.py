# yield: 迭代器和生成器：优化存储

def get_data():
    for i in range(1000000):
        yield i

gen = get_data()

# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)
