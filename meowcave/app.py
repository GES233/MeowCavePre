# -*- encoding:utf-8 -*-
"""
    app.py
    ----------------
    
    应用与关于应用的配置设置。
"""
import os

from flask import Flask
# 导入扩展
from meowcave.extensions import db, migrate
# 导入应用
from meowcave.user.models import User

def create_app():
    """
        创建应用。
    """
    app = Flask('meowcave')
    
    
    # 确保`../instance`存在
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    
    
    configure_app(app)
    
    
    configure_extensions(app)
    
    
    # 路由
    @app.route('/hello')# index
    def hello():
        return 'Hello, world.'
    
    
    return app


def configure_app(app):
    """
        应用设置。
    """
    # 缺省设置的导入
    config = app.config.from_object('meowcave.setting.testing.DevelopmentConfig')


def configure_extensions(app):
    """
        关于插件（`flask_xxx`）的初始化设置。
    """
    # 等价于`db = SQLAlchemy(app)`
    db.init_app(app)
    # 等价于`megrate = Megrate(app, db)`
    migrate.init_app(app, db)
