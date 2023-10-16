import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

# 更新

# condition = {'name': 'yuan'}
# student = collection.find_one(condition)
# student['age'] = 100
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)
# print(collection.find_one({"name": "yuan"}))

# 在这里调用了update_one方法，第二个参数不能再直接传入修改后的字典，而是需要使用{'$set': student}这样的形式，
# 其返回结果是UpdateResult类型，然后调用matched_count和modified_count属性分别可以获得匹配的数据条数和影响的数据条数。

# 运行结果：
#
# <pymongo.results.UpdateResult object at 0x10d17b678>
# 1 0


# 我们再看一个例子：
# print(list(collection.find({"age": {"$gt": 20}})))
# condition = {'age': {'$gt': 20}}
# result = collection.update_one(condition, {'$inc': {'age': 1}})
# print(list(collection.find({"age": {"$gt": 20}})))
# 在这里我们指定查询条件为年龄大于20，然后更新条件为{'$inc': {'age': 1}}，执行之后会讲第一条符合条件的数据年龄加1。


# 如果调用update_many()方法，则会将所有符合条件的数据都更新，示例如下：

# condition = {'age': {'$gt': 20}}
# result = collection.update_many(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)
# 这时候匹配条数就不再为1条了，运行结果如下：
#
# <pymongo.results.UpdateResult object at 0x10c6384c8>
# 3 3
# 可以看到这时所有匹配到的数据都会被更新。
# print(list(collection.find({"age": {"$gt": 20}})))