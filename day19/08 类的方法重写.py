class Animal(object):

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

    def foo(self):
        print("foo")

class MyAnimal(Animal):
    # 父类方法重写
    def foo(self):
        # 调用父类方法
        # Animal().foo()
        super().foo()
        print("foo end")

ma = MyAnimal()
# ma.sleep()
# ma.eat()
ma.foo()