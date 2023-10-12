# 版本一
# class Student:
#
#     # 类属性
#     cls_number = 68
#
#     def __init__(self, name):
#         self.name = name
#
#     def show_class_num(self):
#         print(f"班级人数", self.cls_number)
#
#     def add_class_num(self):
#         self.cls_number += 1
#
# s = Student("jackson")
# s.add_class_num()
# s.show_class_num()
#
# s2 = Student("jack")
# s2.show_class_num()

# 版本二: 静态方法
# class Student:
#
#     # 类属性
#     cls_number = 68
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def show_class_num():
#         print(f"班级人数", Student.cls_number)
#
#     @staticmethod
#     def add_class_num():
#         Student.cls_number += 1
#
# # s = Student("jackson")
# # s.add_class_num()
# # s.show_class_num()
# #
# # s2 = Student("jack")
# # s2.show_class_num()
#
# Student.add_class_num()
# Student.show_class_num()

# 版本三: 类方法
class NewStudent:

    # 类属性
    cls_number = 68

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_class_num(cls):
        print("ID", id(cls))
        print(f"班级人数", cls.cls_number)

    @classmethod
    def add_class_num(cls):
        cls.cls_number += 1


print("id", id(NewStudent))
NewStudent.add_class_num()
NewStudent.show_class_num()