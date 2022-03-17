# -*- encoding:utf-8 -*-
"""
    app.py
    ----------------
    
    应用与关于应用的配置设置。
"""
import os

from flask import Flask


def create_app():
    """
        创建应用。
    """
    app = Flask('meowcave', instance_relative_config=True)
    
    
    # 确保`../instance`存在
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    
    
    configure_app(app)
    
    
    # 路由
    @app.route('/')# index
    def hello():
        return 'Hello, world.'
    
    
    return app


def configure_app(app):
    # 缺省设置的导入
    config = app.config.from_object('meowcave.setting.testing.DevelopmentConfig')
