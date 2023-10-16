import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students


collection.insert_one({})
collection.insert_many([{},{}])
collection.find_one({})
collection.find({})
collection.update_one({})
collection.update_many({})
collection.delete_one({})
collection.delete_many({})