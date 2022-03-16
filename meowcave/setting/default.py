# -*- encoding:utf-8 -*-
"""
    configue.py
    ----------------
    
    关于应用的配置。
"""
import os, sys
# `path`在`os`的下面！IT IS `os.path`!!

class DefaultConfig:
    # 获取关于系统以及环境的设置。
    # --------

    # basedir:
    # 工程的根目录
    #             <here>
    # Thisfile: ../MeowCave/moewcave/setting.default.py
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir))

    # py_version:
    # 获取环境的`Python`版本
    py_version = '{0.major}.{0.minor}.{0.micro}'.format(sys.version_info)

    # 关于`Flask`的设置。
    # --------
    DEBUG = False
    TESTING = False
    
    # 服务器的地址
    SERVER_NAME = '127.0.0.1:5000'

    # 数据库设置（使用SQLAlchemy）
    # --------
    # DATABASE=os.path.join(basedir, 'meowcave.sqlite')
    # 我不想用sqlite说实话
    
    # MySQL:
    # SQLALCHEMY_DATABASE_URI = ''
    # PostgreSQL:
    # SQLALCHEMY_DATABASE_URI = ''
    # sqlite:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/' + 'meowcave.sqlite'
    
    # 安全相关设置
    # --------
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '厕所，粑粑，美汁汁'