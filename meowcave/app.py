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
    '''app.config.from_mapping(
        SECRET_KEY='厕所，粑粑，美汁汁',
        DATABASE=os.path.join(app.instance_path, 'meowcave.sqlite'),
        # 我不想用sqlite说实话
    )# 这是缺省配置'''
    
    
    '''# 需要从`config.py`（缺省）或自定链接获取配置
    if test_config is None:# `test_config`原为`create_app()`的一个参数，内容为 None。
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)'''
    
    
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
    config = app.config.from_object('meowcave.setting.default.DefaultConfig')