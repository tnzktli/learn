import datetime
from bson import ObjectId
from celery import Celery

from flaskLearn.model.blog import Blog

app = Celery('flaskLearn.celery_app', broker='redis://localhost:6379')

@app.task
def do_something():
    blog1 = {
        "_id" : str(ObjectId()),
        "author": "Mike",
        "text": u"我的第一个博客",
        "tags": ["mongo", "python", "pymongo"],
        "create_date": datetime.datetime.utcnow()
    }
    Blog.collection.insert_one(blog1)