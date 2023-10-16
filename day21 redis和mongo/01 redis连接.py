import redis

# 方式一
# r = redis.Redis()
# print(r.get("name"))

# 方式二
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# r.set("aaa", "bbb")
r.set("name", "春天")
print(r.get("name").decode())
