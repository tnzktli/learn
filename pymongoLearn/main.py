#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pymongo
import datetime
import pprint
from bson.objectid import ObjectId

client = MongoClient("127.0.0.1",27017)
db = client.school
collection = db.student

blog1 = {
    "author":"Mike",
    "text": u"我的第一个博客",
    "tags":["mongo","python","pymongo"],
    "date":datetime.datetime.utcnow()
}
blog2 = {
    "author":"Mike",
    "text": u"我的第一个博客",
    "date":datetime.datetime.utcnow(),
    "view":123
}

doc_id = collection.insert_one(blog1).inserted_id
print doc_id
collection.insert_many([blog1,blog2])

collection.remove({"author":"Mike"})

print db.collection_names(include_system_collections=False)

print collection.find_one({"author":"Mike"})
print collection.find_one({"_id":ObjectId(doc_id)})
print collection.count({"author":"Mike"})
cursor = collection.find({"author":"Mike"})
for docu in cursor:
    print docu

# $set用来指定一个键并更新键值，若键不存在并创建。update只是更新找到的第一个，update_many才是更新全部
collection.update({"author":"Mike"},{"$set":{"text": u"博客"}})
collection.update_many({"author":"Mike"},{"$set":{"text": u"博客"}})

collection.create_index([("author",pymongo.ASCENDING),("text",pymongo.DESCENDING)],unique = False)







