#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from flask import Flask,url_for
# from flask import request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     request.form['phone'].strip()
#     return '<h1>Home</h1>'
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
#
# #路径变量
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
# with app.test_request_context():
#     print url_for("index")
#
# if __name__ == '__main__':
#     app.run()

varmain = "flaskLearn"