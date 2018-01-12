from flask import jsonify

from flaskLearn.celery_app import do_something
from flaskLearn.otherpart import otherpart

@otherpart.route('/')
def bp():
    d = {
        "name" : "admin",
        "age" : 12
    }
    return jsonify(d = d)

@otherpart.route('/test_celery')
def test_celery():
    do_something.delay()
    return "test ok"