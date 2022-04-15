# -*- encoding:utf-8 -*-
"""
    meowcave.setting.testing
    ----------------
    
    应用在开发与测试阶段的配置。
"""
from meowcave.setting.default import DefaultConfig

class TestingConfig(DefaultConfig):
    
    # 测试环境
    DEBUG = False
    TESTING = True

    # SQLALCHEMY_DATABASE_URI = (
    #     'sqlite://'
    # )

    SERVER_NAME = '127.0.0.1:5000'


class DevelopmentConfig(DefaultConfig):
    
    ENV = 'development'
    DEBUG = True
    TESTING = True
    
    SERVER_NAME = 'localhost:5000'
    # 先看看hosts改没改
    
    # 返回session所对应的SQL语句
    SQLALCHEMY_ECHO = True
