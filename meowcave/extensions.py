# -*- encoding:utf-8 -*-
"""
    extensions.py
    ----------------
    
    将外部插件的有关代码收紧到此处。
"""
from flask_wtf import FlaskForm # 在这里没用到但是还是导入一下
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# 用`db`来表示数据库
db = SQLAlchemy(use_native_unicode='utf8')
# `migrate`主要设计有关数据库的迁移
migrate = Migrate()
# `login_manager`是关于用户登录的内容
login_manager = LoginManager()
