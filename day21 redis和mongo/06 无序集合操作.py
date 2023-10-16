import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

r.zadd("jiFenBang", {"yuan": 78, "rain": 20, "alvin":89, "eric":45})
print(r.zrange("jiFenBang", 0, -1))
print(r.zrange("jiFenBang", 0, 2))
print(r.zrange("jiFenBang", 0, -1, withscores=True))
print(r.zrevrange("jiFenBang", 0, -1, withscores=True))
