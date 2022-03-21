# -*- encoding:utf-8 -*-
"""
    app.py
    ----------------
    
    应用与关于应用的配置设置。
"""
import os

from flask import(
    Flask,
    render_template,
    Blueprint
)
# 导入扩展
from meowcave.extensions import db, migrate, login_manager
# 导入模型
from meowcave.user.models import User
# 导入蓝图
from meowcave.blueprint_index import bp_index

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
    configure_errorhandlers(app)
    configure_blueprint(app, blueprint_index=bp_index)
    
    
    # shell环境，主要是数据库环境相关的
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'UserPost' : UserPost
        }
    
    
    # 路由
    # 其他地方的调用会采用函数名，`url_for('hello')`
    @app.route('/hello')
    def hello():
        return '<h1>Hello, world.</h1>'
    
    # 来自`/test_code/index-test.py`的测试代码
    @app.route('/')
    def index():
        title = 'Index'
        content_list = [
            {
                'author' : {'name' : '粑粑', 'id' : '126'},
                'cr_time' : '14:03:26',
                'content' : '吃屎啦你！'
            },
            {
                'author' : {'name' : 'Lemon', 'id' : '239'},
                'cr_time' : '14:23:57',
                'content' : '一眼丁真，鉴定为：假'
            },
            {
                'author' : {'name' : '爱国学者张维为', 'id' : '17'},
                'cr_time' : '14:33:16',
                'content' : 'nt'
            },
            {
                'author' : {'name' : '12345', 'id' : '12'},
                'cr_time' : '14:57:00',
                'content' : 'sb'
            }
        ]
        
        return render_template('index.html', title='Home', content_list=content_list)

    
    return app


def configure_app(app):
    """
        应用设置。
    """
    # 缺省设置的导入
    config = app.config.from_object('meowcave.setting.testing.DevelopmentConfig')


def configure_blueprint(app, blueprint_index):
    """
        蓝图的设置与初始化。
    """
    for _singal_func in blueprint_index:
        _singal_func(app=app) # 执行函数


def configure_extensions(app):
    """
        关于插件（`flask_xxx`）的初始化设置。
    """
    # 等价于`db = SQLAlchemy(app)`
    db.init_app(app)
    # 等价于`megrate = Megrate(app, db)`
    migrate.init_app(app, db)
    # 等价与`login_manager = LoginManager(app)`
    login_manager.init_app(app)
    # 参见 https://flask-login.readthedocs.io/en/latest/#how-it-works
    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(int(_id))# `User.query.get()`是按照表的主键查询的


def configure_errorhandlers(app):# 对应的模板未完成
    """
        错误异常代码巴拉巴拉
    """
    @app.errorhandler(400)
    def bad_request(e):
        # HTTP 400
        return render_template('errors/400.html', title='Bad request'), 400
    
    
    # 401
    
    
    @app.errorhandler(404)
    def page_not_found(e):
        # HTTP 404
        # “你来到了没有知识的荒原。”
        return render_template('errors/404.html', title='Page not found'), 404
    
    
    @app.errorhandler(418)
    def im_a_teapot(e):
        # HTTP 418
        return 'This page is generated by a TEAPOT.', 418
    
    
    @app.errorhandler(500)
    def internal_server_error(e):
        # HTTP 500
        # “我的锅我的锅 ————admin”
        return render_template('errors/500.html', title='Internal server error'), 500
    
    
    # 501
