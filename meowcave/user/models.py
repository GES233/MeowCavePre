# -*- encoding:utf-8 -*-
"""
    meowcave/user/models.py
    ---------------
    
    提供与用户业务有关的模型与函数。
"""

import datetime

from meowcave.extensions import db

class User(db.Model):
    __tablename__ = 'user'
    # -- 关于帐号的设置
    # 
    # `uid`：使用者的id，递增的非空整数，主键
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # `nickname`：昵称，非空字符
    nickname = db.Column(db.String(80))
    # `username`：纯ASCII字符，可空，不可更改
    username = db.Column(db.String(40), unique=True)
    # `e-mail`：非空
    email = db.Column(db.String(120), index=True, unique=True)
    # `passwd`：混淆后的密码（SHA-256）
    passwd = db.Column(db.String(256))
    # `create_time`：用户填写邀请码提交时的日期
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    
    # -- 关于帐号权限的设置
    # 
    # `user_status`：为帐号的状态
    # - normal：正常
    # - delete：被删除
    user_status = db.Column(db.String, default='normal')
    
    # -- 用户信息
    # 
    # `birth`：出生日期
    birth = db.Column(db.DateTime, default=None)
    # `gender`：性别
    gender = db.Column(db.String(2), default=None)
    # `info`：个人简介
    info = db.Column(db.Text(1024),default=None)
    
    
    def __repr__(self):
        if not self.username:
            return '<User {}(uid:{})>'.format(self.nickname, self.uid)
        else:
            return '<User {}(@{}, uid:{})>'.format(self.nickname, self.username, self.uid)
