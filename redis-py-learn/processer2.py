import redis

pool = redis.ConnectionPool("127.0.0.1",port = 6379)
r = redis.StrictRedis(connection_pool=pool)

while True:
    print (r.brpop("mq"))