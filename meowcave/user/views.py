# -*- encoding:utf-8 -*-
"""
    meowcave/user/views.py
    ---------------
    
    提供用户相关的视图（主要是方法视图）。
"""
# 导入库与模块
from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
    render_template,
    flash
)
from flask.views import View, MethodView
from flask_login import(
    login_user,
    logout_user,
    login_required,
    current_user
)

from meowcave.extensions import login_manager, db
from meowcave.user.models import(
    # UserPost,
    User
)
# from meowcave.user.forms import UserPostForm


class UserIndex(View):
    """
        用户主页
    """
    user = User.query.filter_by(id=id).first_or_404()
    return None

def load_blueprint(app):
    # 向蓝图注册
    user = Blueprint('user', __name__)
    
    user.add_url_rule('/user/<id>', view_func=UserIndex.as_view('shown'))# 'user.shown'
    # user.all_url_rule('/people/<username>')

    app.register_blueprint(user)
