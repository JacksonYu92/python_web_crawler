class Animal(object):

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

    def foo(self):
        self.swimming()

class Dog(Animal):

    def swimming(self):
        print("swimming...")

alex = Dog()
alex.foo()