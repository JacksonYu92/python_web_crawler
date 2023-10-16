import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

# 查询，插入数据后我们可以利用find_one()或find()方法进行查询，find_one()查询得到是单个结果，find()则返回多个结果。

result = collection.find_one({'name': 'yuan'})
print(type(result))
print(result)
# 在这里我们查询name为yuan的数据，它的返回结果是字典类型，运行结果： <class'dict'>
# {'_id': ObjectId('5932a80115c2606a59e8a049'), 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
# 可以发现它多了一个_id属性，这就是MongoDB在插入的过程中自动添加的。

# 我们也可以直接根据ObjectId来查询，这里需要使用bson库里面的ObjectId。


result = collection.find_one({'_id': ObjectId('64255f6012345f5a41fb4f56')})
print(result)
# 其查询结果依然是字典类型，运行结果：

# {' ObjectId('593278c115c2602667ec6bae'), 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
# 当然如果查询_id':结果不存在则会返回None。

# 对于多条数据的查询，我们可以使用find()方法，例如在这里查找年龄为20的数据，示例如下：

results = collection.find({'age': 20})
print(results, type(result))
for result in results:
    print(result)

# 如果要查询年龄大于20的数据，则写法如下：

results = collection.find({'age': {'$gt': 20}})

print("results:::", results)
print("results:::", list(results))
# 在这里查询的条件键值已经不是单纯的数字了，而是一个字典，其键名为比较符号$gt，意思是大于，键值为20，这样便可以查询出所有
# 年龄大于20的数据。

# 在这里将比较符号归纳如下表：
"""
符号含义示例
$lt小于{'age': {'$lt': 20}}
$gt大于{'age': {'$gt': 20}}
$lte小于等于{'age': {'$lte': 20}}
$gte大于等于{'age': {'$gte': 20}}
$ne不等于{'age': {'$ne': 20}}
$in在范围内{'age': {'$in': [20, 23]}}
$nin不在范围内{'age': {'$nin': [20, 23]}}
"""
# 另外还可以进行正则匹配查询，例如查询名字以M开头的学生数据，示例如下：

results = collection.find({'name': {'$regex': '^M.*'}})
# 在这里使用了$regex来指定正则匹配，^M.*代表以M开头的正则表达式，这样就可以查询所有符合该正则的结果。
print(results)
# 在这里将一些功能符号再归类如下：
"""
符号含义示例示例含义
$regex匹配正则{'name': {'$regex': '^M.*'}}name以M开头
$exists属性是否存在{'name': {'$exists': True}}name属性存在
$mod数字模操作{'age': {'$mod': [2, 0]}}年龄模2余0
$where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数
"""
# 这些操作的更详细用法在可以在MongoDB官方文档找到：
# https://docs.mongodb.com/manual/reference/operator/query/

# 计数
# 要统计查询结果有多少条数据，可以调用count()方法，如统计所有数据条数：

count = collection.count_documents({})
print(count)
# 或者统计符合某个条件的数据：

count = collection.count_documents({'age': 20})
print(count)
# 排序
# 可以调用sort方法，传入排序的字段及升降序标志即可，示例如下：

results = collection.find().sort('age', pymongo.ASCENDING)
print("sort:::", [(result['name'],result['age']) for result in results])



# 偏移,可能想只取某几个元素，在这里可以利用skip()方法偏移几个位置，比如偏移2，就忽略前2个元素，得到第三个及以后的元素。

results = collection.find().sort('age', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# 值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，很可能会导致内存溢出，
# 可以使用类似find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}}) 这样的方法来查询，记录好上次查询的_id。
