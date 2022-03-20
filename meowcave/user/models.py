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
         - `get_id`：返回用户的id，必须叫做id
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
    # `email`：电邮地址，非空
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
    # `is_spectator`：表示该用户是否为旁观者的布尔值
    is_spectator = db.Column(db.Boolean, default=False)
    # `credit`：等级积分
    # 00000~65535(0000~FFFF)
    # credit = db.Column(db.Integer, default=32768)
    
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
    
    
    # -- 和别的表的关系
    '''# 邀请码表
    """
        先声明下关系，一个用户只能被一个邀请码所邀请，
        但是一个用户也可以邀请多个用户，也就是说，
        对任意用户而言，当他为「受邀者」时，
        仅存在一个对应的邀请码，也仅存在一个邀请者；
        但是当他为「邀请者」时，
        会有多个邀请码以及多个受邀者。
        ----
        简而言之，就是树形的结构。
        
        user.as_host:code => 1:n
        user.as_guest:code => 1:1
    """
    invitation_code = db.relationship(
        'InvitationCode', # 先把`InvitationCode`库链接过来
        # 照葫芦画瓢。
        #primaryjion=(invitation_code.c.host_id == id),
        #secondaryjion=(invitation_code.c.guest_id == id),
        #backref='user',
        #lazy='dymanic'
    )'''
    
    
    # 方法
    # 返回值：
    def __repr__(self):
        if not self.username:
            return '<User {}(id:{})>'.format(self.nickname, self.id)
        else:
            return '<User {}(@{}, id:{})>'.format(self.nickname, self.username, self.id)
    
    
    # 设置密码：
    def passwd_set(self, password):
        # 加16位盐，SHA256，256次迭代
        self.passwd = generate_password_hash(password, method='pbkdf2:sha256:256', salt_length=16)
    
    
    # 检查密码：
    def passwd_check(self, password):
        # 返回布尔值
        return check_password_hash(self.passwd, password)

'''
class InvitationCode(db.Model):
    """
       InvitationCode
       --------
       
       存储以及显示邀请码以及基于邀请而建立的联系的数据库。
    """
    __tablename__ = 'invitation_code'
    
    # `code`：邀请码文本
    code = db.Column(db.String(40),  primary_key=True, unique=True)
    
    # -- 关于邀请者以及基本信息
    # 邀请人
    host = db.relationship('User')
    # 邀请人的id
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # `rest_step`：剩余次数，0就是无效
    rest_step = db.Column(db.Integer, default=1)
    
    # -- 时间与有效相关
    # `generate_time`：生成时间
    generate_time = db.Column(db.DateTime, default=datetime.utcnow())
    # `end_time`：作废日期
    invalid_time = db.Coulmn(db.DateTime)
    
    # -- 关于受邀者
    # 受邀者
    guest = db.relationship('User')
    # 受邀者的id（如果有的话）
    guest_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    
    # 一些函数以及方法
    # 返回值：
    def __repr__(self):
        if self.guest:
            return '<Code:"{}", {} -> {}>'.format(code, self.host_id, self.guest_id)
        else:
            return '<Code:"{}", {} -> Null>'.format(code, self.host_id)
    
    
    # 生成邀请码：
    def generate(self):
        pass
    
    
    # 邀请用户：
    def guest_invited(self):
        pass
    
    
    # 邀请码作废：
    def code_invalid(self):
        pass
'''
