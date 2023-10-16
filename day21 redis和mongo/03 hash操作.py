import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# r.hset("info", "name", "rain")
# r.hset("info", "age", 23)

# r.hset("info2", mapping={"name": "eric", "age": 30})

# print(r.hget("info", "name"))
# print(r.hgetall("info2"))

