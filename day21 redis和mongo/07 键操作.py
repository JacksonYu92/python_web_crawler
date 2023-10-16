import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

print(r.keys("**"))
print(r.keys("*a"))
print(r.keys("*B*"))
print(r.keys("info*"))
print(r.exists("name"))

r.expire("name", 10)
