import redis

# 连接池
from flask import json

pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
r = redis.StrictRedis(connection_pool=pool)

# # 管道
# pipe = r.pipeline()
# pipe.hset("student","name","demo")
# pipe.hset("student","age",12)
# pipe.hset("student","grade",6)
# pipe.execute()

# # String
# r.set("key1","value1")
# print(str(r.get("key1")))
# print(r.setnx("key1",1))
# print(r.setnx("key2",1))

# # Hash
# user1 = {
#     "name" : "demo",
#     "age" : 12,
#     "grade" : 4
# }
# r.hmset("user1",user1)
# print(r.hgetall("user1"))

# # List
# r.lpush("list1","a")
# r.lpush("list1","b")
# r.lpush("list1","c")
# print(r.rpop("list1"))

# # 删除
# keys = []
# r.delete(*keys)
