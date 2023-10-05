from cal import add, mul
from db.mysql import init_mysql
from db import redis

ret = add(1,3)
print(ret)

ret2 = mul(2,5)
print(ret2)

init_mysql()
redis.init_redis()