from flask_login import UserMixin

from flaskLearn.model import db


class User(UserMixin):

    class Field():
        _id = '_id'
        phone = 'phone'
        password = 'password'
        name = 'name'
        gender = 'gender'
        email = 'email'

    class Gender():
        male = 0
        female = 1

    collection = db.user

    def __init__(self, **kwargs):
        UserMixin.__init__(self)
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def get_id(self):
        return self._id
