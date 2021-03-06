# -*- encoding:utf-8 -*-
"""
    blueprint.py
    ----------------
    
    蓝图索引。
"""
# 导入所有的蓝图
from meowcave.auth.views import load_blueprint as auth_bp
from meowcave.user.views import load_blueprint as user_bp

# 以列表的形式存在以便在`app.py`的`configure_route()`可以挨个注册
bp_index = [
    auth_bp,
    user_bp
]
