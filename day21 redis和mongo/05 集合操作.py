import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# s = {1, 2, 3, 4,4}
# print(type(s))
# print(s)

# r.sadd("name_set", "zhangsan", "lisi", "wangwu", "lisi")
# print(r.smembers("name_set"))
#
# print(r.srandmember("name_set", 2))

# r.srem("name_set", "lisi")
# print(r.smembers("name_set"))
