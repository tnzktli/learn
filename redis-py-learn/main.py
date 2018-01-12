import redis

pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)

r.lpush("list",1)
r.lpush("list",2)
r.lpush("list",3)
r.lpush("list",4)
r.lpush("list",5)
print r.brpop("list")
