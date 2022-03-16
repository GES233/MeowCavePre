# -*- encoding:utf-8 -*-
"""
    MoewCave
    ----------------
    
    一个轻论坛的实现，代码参（chao）考（xi）了`flaskbb`。
"""
import os

from flask import Flask

# from moewcave.configure import configure_app

def create_app():
    """
        创建应用。
    """
    app = Flask('MoewCave', instance_relative_config=True)
    '''app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'forum.sqlite'),
    )# 这是缺省配置'''
    
    
    '''# 需要从`config.py`（缺省）或自定链接获取配置
    if test_config is None:# `test_config`原为`create_app()`的一个参数，内容为 None。
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)'''
    
    
    # 确保`../instance`存在
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    
    
    # 路由
    @app.route('/')# index
    def hello():
        return 'Hello, world.'
    
    
    return app


'''
# 自动运行
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)# 如果不是在试验环境中记得关闭'''