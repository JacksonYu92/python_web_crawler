class Student(object):
    class_name = "爬虫10期"
    class_num = 500

    def __init__(self, name):
        self.name = name

    def listen(self):
        print(f'{self.name}听课')

Student.class_num = 600

jackson = Student("jackson")
# jackson.class_num = 600
jack = Student("jack")
print(jack.class_num)