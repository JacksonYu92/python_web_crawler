import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# r.lpush("courses", "chinese", "math", "english")
print(r.lrange("courses", 0, -1))

# r.linsert("courses", "AFTER", "math", "tiyu")
# print(r.lrange("courses", 0, -1))

# r.rpop("courses")
# print(r.lrange("courses", 0, -1))

# r.lpop("courses")
# print(r.lrange("courses", 0, -1))

print(r.lindex("courses", 1))