import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

# collection.delete_one({"name": "yuan"})
# collection.delete_many({"name": "yuan"})
collection.delete_many({"age": {"$gt": 20}})

print(list(collection.find()))