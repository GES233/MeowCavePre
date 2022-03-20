# -*- encoding:utf-8 -*-
"""
    meowcave/user/models.py
    ---------------
    
    提供与用户业务有关的模型与函数。
"""
# 导入库与模块
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from meowcave.extensions import db

class User(db.Model, UserMixin):
    """
        Uder
        --------
        
        承载用户模型的类。
        
        `UserMixin`是关于用户数据库模型的一个类，
        其中四个类以及方法是必需的：
         - `is_authenticated`：布尔值，表示是否登录
         - `is_active`：布尔值，和「记住我？」有密切联系
         - `is_anonymous`：布尔值，表示是否是申必人（？）
         - `get_id`, "given a User instance, 
         returns the unique ID for that object"
         (from https://stackoverflow.com/questions/63231163/what-is-the-usermixin-in-flask)
    """
    __tablename__ = 'user'
    # -- 关于帐号的设置
    # 
    # `id`：使用者的id，递增的非空整数，主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # `nickname`：昵称，非空字符
    # 考虑到登录的问题，昵称不能重复，用户A的昵称也不能和其他用户的`username`相冲突
    nickname = db.Column(db.String(80), nullable=False, unique=True)
    # `username`：纯ASCII字符，可空，不可更改
    username = db.Column(db.String(40), unique=True)
    # `e-mail`：非空
    email = db.Column(db.String(120), index=True, nullable=False, unique=True)
    # `passwd`：混淆后的密码（SHA-256）
    passwd = db.Column(db.String(256))
    # `jion_time`：用户填写邀请码提交时的日期
    jion_time = db.Column(db.DateTime, default=datetime.utcnow())
    
    # -- 关于帐号权限的设置
    # 
    # `user_status`：表示帐号状态的字符串
    # - normal：正常
    # - deleted：被删除
    # - blocked：被禁用
    # - frozen：被冻结（用户主动）
    user_status = db.Column(db.String, default='normal')
    # `spectator`：表示该用户是否为旁观者的布尔值
    is_spectator = db.Column(db.Boolean, default=False)
    
    # -- 用户信息
    # 
    # `birth`：出生日期
    birth = db.Column(db.DateTime, default=None)
    # `gender`：性别
    gender = db.Column(db.String(2), default=None)
    # `info`：用户介绍自己的内容
    info = db.Column(db.Text(1024),default=None)
    # `website`：用户的网站
    website = db.Column(db.String(1256), default=None)
    
    
    # 方法
    def __repr__(self):
        if not self.username:
            return '<User {}(uid:{})>'.format(self.nickname, self.id)
        else:
            return '<User {}(@{}, uid:{})>'.format(self.nickname, self.username, self.id)
    
    
    # 设置密码：
    def passwd_set(self, password):
        # 加16位盐，SHA256，256次迭代
        self.passwd = generate_password_hash(password, method='pbkdf2:sha256:256', salt_length=16)
    
    
    # 检查密码：
    def passwd_check(self, password):
        # 返回布尔值
        return check_password_hash(self.passwd, password)

'''
class SocialConnection(db.Model):
    """
       特指关注等的社交行为与社交关系。
    """
    pass'''
