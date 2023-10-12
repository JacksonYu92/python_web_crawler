class Animal(object):

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

class Fly(object):
    def fly(self):
        print("fly...")

class Dog(Animal):
    pass

class Eagle(Animal, Fly):
    pass


class Bat(Animal, Fly):
    pass

b = Bat()
b.fly()