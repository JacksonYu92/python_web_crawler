# 声明类
class Person(object):
    # 类属性
    isemotion = True
    legs = 2
    hasyuyan = True

    # 初始化方法
    def __init__(self, name, age):
        # print("初始化方法")
        print("self:", id(self))
        self.name = name
        self.age = age

    def __eq__(self, other):

        if self.name == other.name:
            return True

    # 实例方法
    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

    def run(self):
        print("run...")

# 实例化对象
# p1 = Person()
# p1.name = "jack"
# p1.age = 23
# p1.weight = 120

# 再实例化对象
# p2 = Person()
# p2.name = "jackson"
# p1.age = 33
# p2.weight = 130

# print(p1.name)
# print(p2.name)


p3 = Person("jackson", 23)
p2 = Person("jackson", 23)
print(p3 == p2)
# print(id(p3))
#
# p2 = Person()
# print(id(p2))