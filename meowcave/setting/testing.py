# -*- encoding:utf-8 -*-
"""
    meowcave/setting/testing.py
    ----------------
    
    应用在开发与测试阶段的配置。
"""
from meowcave.setting.default import DefaultConfig

class TestingConfig(DefaultConfig):
    
    # 测试环境
    DEBUG = False
    TESTING = True

    SQLALCHEMY_DATABASE_URI = (
        'sqlite://'
    )

    SERVER_NAME = '127.0.0.1:5000'


class DevelopmentConfig(DefaultConfig):
    
    ENV = 'development'
    DEBUG = True
    TESTING = True
    
    SERVER_NAME = '127.0.0.1:5000'
