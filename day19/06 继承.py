class Animal(object):

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")

class Dog(Animal):

    def swimming(self):
        print("swimming...")

class Cat(Animal):

    def climb_tree(self):
        print("climb_tree...")

alex = Dog()
alex.swimming()
alex.sleep()

c = Cat()
c.sleep()