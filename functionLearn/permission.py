# -*- coding: utf-8 -*-
"""
    permission
    ~~~~~~~~~~

    用户权限操作逻辑模块.

    :author: Jason Wang
    :copyright: (c) 2016, Tungee
    :date created: 2017-06-19
    :python version: 2.7
"""
from functools import wraps

from flask import jsonify, abort
from flask_login import current_user, logout_user

from app import app
from model.user import User
from model.group import Group


def auth(action):
    """
    权限验证
    :param action:
    :return:
    """

    def wrapper(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                # 使用登录模块返回
                return func
            actions = get_user_actions(current_user.__dict__)
            if action not in actions:
                # 认证失败
                abort(403)

            return func(*args, **kwargs)

        return func_wrapper

    return wrapper

# 看看当前用户是否有action
def auth_action(action):
    actions = get_user_actions(current_user.__dict__)
    if action not in actions:
        # 认证失败
        abort(403)
    return True

# 看看某个user是否有action
def check_privilege(user, action):
    """
    检查一个用户是否有权限执行某一个操作

    :param user:
    :param action:
    :return:
    """
    return action in get_user_actions(user)


def get_all_actions():
    """
    获取所有action

    :return:action_ids(list of str)
    """
    actions = list()
    for group in app.groups:
        actions.extend([action['_id'] for action in group['actions']])
    return list(set(actions))


def get_user_actions(user):
    """
    获取用户的所有权限

    :param user:
    :return: action_ids(list of str)
    """
    if user is None:
        return list()
    if user[User.Field.status] != User.Status.normal:
        return list()

    actions = list()
    if User.Field.actions in user:
        actions += user[User.Field.actions]

    groups = list(Group.s_col.find(
        {
            '_id': {'$in': user[User.Field.groups]}
        },
        [Group.Field.actions, Group.Field.group_name]
    ))
    for g in groups:
        if g[Group.Field.group_name] == u'超级管理员':
            actions.extend(get_all_actions())
        actions += g.get(Group.Field.actions, [])

    if User.Field.forbidden_actions in user:
        actions = [_ for _ in actions if _ not in
                   user[User.Field.forbidden_actions]]
    return list(set(actions))

# 查看actions(list of action_id)里面是否有action_id不是在原始权限组规定的action里面
def check_valid_actions(actions):
    """
    检查 action 列表是否存在非法 action

    :param actions:
    :return:
    """
    all_actions = set(get_all_actions())
    for action in actions:
        if action not in all_actions:
            return False
    return True
