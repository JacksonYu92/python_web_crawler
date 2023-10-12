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
        print(f"{self.name} run...")


p1 = Person("jackson", 23)
p2 = Person("jack", 23)
print(p1.name)
print(p1.age)
p1.run()
p2.run()