import redis

pool = redis.ConnectionPool("127.0.0.1",port = 6379)
r = redis.StrictRedis(connection_pool=pool)

while True:
    input = raw_input("input message")
    r.lpush("mq",input)

