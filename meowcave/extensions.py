# -*- encoding:utf-8 -*-
"""
    extensions.py
    ----------------
    
    将外部插件的有关代码收紧到此处。
"""
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 用`db`来表示数据库
db = SQLAlchemy()
# `migrate`主要设计有关数据库的迁移
migrate = Migrate()
