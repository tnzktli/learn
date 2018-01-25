# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect

from flaskLearn.model.user import User
from flaskLearn.otherpart import otherpart

app = Flask(__name__)
app.debug = True
app.secret_key = "asdadasdasdesafrhakfhiash"
app.register_blueprint(otherpart, url_prefix='/otherpart')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user_dir = User.collection.find_one({"_id":user_id})
    # print(user_dir)
    return User(**user_dir)

@app.route('/login', methods=['POST'])
def login():
    data = {
        "phone" : request.form["phone"],
        "password" : request.form["password"]
    }
    user_dir = User.collection.find_one(data)
    # print(user_dir)
    if user_dir is None:
        return "phone or password not match"
    login_user(User(**user_dir))
    return "ok"

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return "logout ok"

@app.route('/show_user', methods=['GET'])
@login_required
def show_user():
    user_info = []
    user_info.append(current_user._id)
    user_info.append(current_user.name)
    user_info.append(current_user.gender)
    user_info.append(current_user.phone)
    user_info.append(current_user.password)
    user_info.append(current_user.email)
    return str(user_info)


#http://127.0.0.1:5000/
@app.route('/')
def hello_world():

    return 'localhost!'

@app.route('/up',methods = ['POST'])
def printUP():
    app.logger.debug(type(int(request.form['num'])))
    return "ok"

@app.route('/redirect')
def index():
    return redirect('http://127.0.0.1:5000/')

@app.route('/abort')
def abort():
    abort(401)

@app.errorhandler(401)
def unauth(error):
    print (error)
    return '401'

@app.route('/s')
def s():
    session['value'] = 'value'
    return redirect('http://127.0.0.1:5000/s1')

@app.route('/s1')
def s1():
    return session['value']

@app.route('/return_json')
def return_json():
    num = 1
    studs = [
        {
            "name":"demo",
            "grade":1
        },
        {
            "name": "demo",
            "grade": 1
        },
        {
            "name": "demo",
            "grade": 1
        },
    ]
    return jsonify(studs=studs,num=num)



