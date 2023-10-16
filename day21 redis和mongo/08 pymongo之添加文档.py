import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
"""
这样我们就可以创建一个MongoDB的连接对象了。另外MongoClient的第一个参数host还可以直接传MongoDB的连接字符串，以mongodb开头，
例如：client = MongoClient('mongodb://localhost:27017/')可以达到同样的连接效果。
"""
# 指定数据库
# MongoDB中还分为一个个数据库，我们接下来的一步就是指定要操作哪个数据库，在这里我以test数据库为例进行说明，所以下一步我们
# 需要在程序中指定要使用的数据库。

db = client.test
# 调用client的test属性即可返回test数据库，当然也可以这样来指定：
# db = client['test']
# 　两种方式是等价的。

# 指定集合
# MongoDB的每个数据库又包含了许多集合Collection，也就类似与关系型数据库中的表，下一步我们需要指定要操作的集合，
# 在这里我们指定一个集合名称为students，学生集合。还是和指定数据库类似，指定集合也有两种方式。

students_collection = db.students
# collection = db['students']
# 插入数据,接下来我们便可以进行数据插入了，对于students这个Collection，我们新建一条学生数据，以字典的形式表示：

# student = {
#     'id': '20230001',
#     'name': 'yuan',
#     'age': 20,
#     'gender': 'male'
# }
# 在这里我们指定了学生的学号、姓名、年龄和性别，然后接下来直接调用collection的insert()方法即可插入数据。

# result = students_collection.insert_one(student)
# print(result)

# print(list(students_collection.find()))

student1 = {
    'id': '20230002',
    'name': 'rain',
    'age': 24,
    'gender': 'male'
}

student2 = {
    'id': '20230003',
    'name': 'eric',
    'age': 26,
    'gender': 'male'
}

result = students_collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
print(list(students_collection.find()))

# insert_many()方法返回的类型是InsertManyResult，调用inserted_ids属性可以获取插入数据的_id列表，运行结果：

# <pymongo.results.InsertManyResult object at 0x101dea558>
# [ObjectId('5932abf415c2607083d3b2ac'), ObjectId('5932abf415c2607083d3b2ad')]