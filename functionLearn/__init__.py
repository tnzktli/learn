#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    Description of this file

    :author: Zhidong
    :copyright: (c) 2016, Tungee
    :date created: 2017-05-24
    :python version: 2.7

"""
from flaskLearn.app import app

# Permission module
app.groups = list()  # 权限组列表
app.check_relations = dict()
app.uncheck_relations = dict()

def register_actions(group, group_name, actions):
    """注册actions"""
    app.groups.append({
        '_id': group,
        'name': group_name,
        'actions': [{
            '_id': _[0],
            'name': _[1]
        } for _ in actions]
    })

#原始权限组s
# 权限组
G_GROUP = 'group-group'
A_GET_GROUPS = 'action-get-groups'
A_CREATE_GROUP = 'action-create-group'
A_UPDATE_GROUP = 'action-update-group'
A_UPDATE_GROUP_NAME = 'action-update-group-name'
A_DELETE_GROUP = 'action-delete-group'
register_actions(G_GROUP, '权限分组', [
    (A_GET_GROUPS, '查看权限分组'),
    (A_CREATE_GROUP, '新建分组'),
    (A_UPDATE_GROUP, '编辑'),
    (A_UPDATE_GROUP_NAME, '更名'),
    (A_DELETE_GROUP, '删除'),
])

# 用户管理
G_USER = 'group-user'
A_GET_USERS = 'action-get-users'
A_CREATE_USER = 'action-create-user'
A_UPDATE_USER = 'action-update-user'
A_UPDATE_USER_PASSWORD = 'action-update-user-password'
A_FORBIDDEN_OR_ACTIVE_USER = 'action-forbidden-or-active-user'
A_DELETE_USER = 'action-delete-user'
register_actions(G_USER, '用户管理', [
    (A_GET_USERS, '查看用户列表'),
    (A_CREATE_USER, '新建用户'),
    (A_UPDATE_USER, '编辑'),
    (A_UPDATE_USER_PASSWORD, '修改密码'),
    (A_FORBIDDEN_OR_ACTIVE_USER, '禁用/启用'),
    (A_DELETE_USER, '删除')
])

# 操作记录
G_OP_LOG = 'group-op-log'
A_GET_OP_LOGS = 'action-get-op-logs'
register_actions(G_OP_LOG, '操作记录', [
    (A_GET_OP_LOGS, '查看操作记录')
])

# 注册审批
G_APP = 'group-application'
A_GET_APPS = 'action-get-applications'
A_PASS_OR_REFUSE_APP = 'action-pass-or-refuse-application'
register_actions(G_APP, '注册审批', [
    (A_GET_APPS, '查看审批列表'),
    (A_PASS_OR_REFUSE_APP, '通过/不通过')
])

# 账户管理
G_COMPANY = 'group-company'
A_GET_COMPANIES = 'action-get-companies'
A_FORBIDDEN_OR_ACTIVE_COMPANY = 'action-forbidden_or_active_company'
A_RECHARGE = 'action-recharge'
register_actions(G_COMPANY, '账户管理', [
    (A_GET_COMPANIES, '查看账户列表'),
    (A_FORBIDDEN_OR_ACTIVE_COMPANY, '禁用/启用'),
    (A_RECHARGE, '线下充值')
])

# 代理商
G_AGENT = 'group-agent'
A_GET_AGENTS = 'action-get-agents'
A_CREATE_AGENT = 'action-create-agent'
A_EDIT_AGENT = 'action-edit-agent'
A_AGENT_RECHARGE = 'action-agent-recharge'
A_SET_AGENT_STATUS = 'action-set-agent-status'
A_GET_AGENT_BILLS = 'action-get-agent-bills'
A_AGENT_STATISTICS = 'action-get-agent-statistics'
register_actions(G_AGENT, '代理商', [
    (A_GET_AGENTS, '查看代理商列表'),
    (A_CREATE_AGENT, '新建代理商'),
    (A_EDIT_AGENT, '编辑代理商'),
    (A_SET_AGENT_STATUS, '启用/禁用'),
])



# 点击关联，这是给前端用的
# 就是说页面那里选中action_id那个权限，relation_id那个权限也会显示被选中
def register_check_relation(action_id, relation_id):
    """ 注册点击关联"""
    # app.check_relations(dict)
    if action_id not in app.check_relations:
        app.check_relations[action_id] = list()
    app.check_relations[action_id].append(relation_id)

# 页面那里action_id那个权限被点取消，relation_id也会显示被点取消
def register_uncheck_relation(action_id, relation_id):
    """ 注册取消点击关联"""
    # app.uncheck_relations(dict)
    if action_id not in app.uncheck_relations:
        app.uncheck_relations[action_id] = list()
    app.uncheck_relations[action_id].append(relation_id)


# 点击关联
check_relations = [
    (A_CREATE_GROUP, A_GET_GROUPS),
    (A_UPDATE_GROUP, A_GET_GROUPS),
    (A_UPDATE_GROUP_NAME, A_GET_GROUPS),
    (A_DELETE_GROUP, A_GET_GROUPS),
    (A_CREATE_USER, A_GET_USERS),
    (A_UPDATE_USER, A_GET_USERS),
    (A_UPDATE_USER_PASSWORD, A_GET_USERS),
    (A_FORBIDDEN_OR_ACTIVE_USER, A_GET_USERS),
    (A_DELETE_USER, A_GET_USERS),
    (A_PASS_OR_REFUSE_APP, A_GET_APPS),
    (A_FORBIDDEN_OR_ACTIVE_COMPANY, A_GET_COMPANIES),
    (A_RECHARGE, A_GET_COMPANIES),

    # 代理商
    (A_CREATE_AGENT, A_GET_AGENTS),
    (A_EDIT_AGENT, A_GET_AGENTS),
    (A_SET_AGENT_STATUS, A_GET_AGENTS),
    (A_GET_AGENT_BILLS, A_GET_AGENTS),
    (A_AGENT_STATISTICS, A_GET_AGENTS),
    (A_AGENT_RECHARGE, A_GET_AGENTS),
]

for relation in check_relations:
    # 赋予权限【0】时会自然赋予权限【1】
    register_check_relation(relation[0], relation[1])
    # 取消权限【1】时会自然取消权限【0】
    register_uncheck_relation(relation[1], relation[0])
