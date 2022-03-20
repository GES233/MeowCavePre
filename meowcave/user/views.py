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
from meowcave.user.models import User


class UserIndex(View):
	"""
	    用户主页
	"""
	user = User.query.filter_by(id=id).first_or_404()
	return None

def load_blueprint(app):
    # 向蓝图注册
    auth = Blueprint('user', __name__)
    
    auth.add_url_rule('/user/<id>', view_func=UserIndex.as_view('user'))

    app.register_blueprint(auth)
