#

from meowcave.setting.default import DefaultConfig

class TestingConfig(DefaultConfig):
    
    # 测试环境
    DEBUG = False
    TESTING = True

    SQLALCHEMY_DATABASE_URI = (
        'sqlite://'
    )

    SERVER_NAME = '127.0.0.1:5000'