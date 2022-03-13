# -*- encoding:utf-8 -*-

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'forum.sqlite'),
    )# 这是缺省配置
    
    # 需要从`config.py`（缺省）或自定链接获取配置
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    # 确保`../instance`存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # 路由
    @app.route('/')
    def hello():
        return 'Hello, world.'
    
    return app