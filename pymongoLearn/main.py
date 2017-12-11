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
# doc_id = collection.insert_one(blog1).inserted_id
# print doc_id

# print db.collection_names(include_system_collections=False)

# print collection.find_one({"author":"Mike"})

# print collection.find_one({"_id":ObjectId(doc_id)})

# collection.insert_many([blog1,blog2])

collection.create_index([("author",pymongo.ASCENDING),("text",pymongo.DESCENDING)])

cursor = collection.find({"author":"Mike"})
for docu in cursor:
    print docu

print collection.count({"author":"Mike"})


# collection.remove({"author":"Mike"})

