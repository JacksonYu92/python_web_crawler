import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# r.set("aaa", "bbb")
# print(r.get("aaa"))

# r.setex("a", 10, "1")
# print(r.get("a"))

# r.set("age", 22)
# print(r.get("age"))
# r.incrby("age", 10)
# print(r.get("age"))
# r.decrby("age", 10)
# print(r.get("age"))


