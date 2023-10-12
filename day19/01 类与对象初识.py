
# class Hero():
#     prop = []
#     shengming = 100
#
#     def attacked():
#         global shengming
#         print("攻击")
#         shengming -= 1
#
#     def buy_prop():
#         print("购买道具")

# class Teacher():
#     name = ""
#     age = 22
#
#     def teach(self):
#         print("讲课")
#
#     def homework(self):
#         print("布置作业")
#
# class Student():
#     name = ""
#     age = 22
#
#     def listen(self):
#         print("听课")
#
#     def homework(self):
#         print("写作业")

# 声明类
class Person(object):
    # 类属性
    isemotion = True
    legs = 2
    hasyuyan = True

    # 实例方法
    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

    def run(self):
        print("run...")

# 实例化对象
p1 = Person()

# 实例化对象调用属性和方法通过句点符
print(p1.legs)
print(p1.isemotion)
p1.sleep()
p1.run()

# 再实例化对象
p2 = Person()
print(p2.legs)
print(p2.isemotion)
p2.sleep()
p2.run()
p2.name = "jackson"

print(p1 == p2)
print(p2.name)