# -*- encoding:utf-8 -*-
"""
    meowcave/auth/views.py
    ---------------
    
    提供认证相关的视图（主要是方法视图）。
"""
# 导入库与模块
from flask import (
    request,
    redirect,
    url_for,# 参数是函数名
    Blueprint,
    render_template,
    flash
)
from flask.views import MethodView

from flask_login import(
    login_user,
    logout_user,
    login_required
)

from meowcave.extensions import login_manager
from meowcave.auth.forms import(
    LoginForm
    # RegisterForm
)


class Login(MethodView):
    __methods__ = ['GET', 'POST']
    
    def form(self):
        return LoginForm()
    
    
    def get(self):
        return render_template("auth/login.html", login_form=self.form())
    
    
    def post(self):
        login_form = self.form()
        if login_form.validate_on_submit():# 对表单的验证
            # 可能需要验证码
            # 也可能需要对用户身份判定的部分内容
            """
            关于用户登录表单的`username`的流程：
            邮件 优先于 username 优先于 昵称
            邮件用'user@example.com'为过滤正则式，
            如果有结果那么通过邮件查询用户；
            首先通过「不是」纯ASCII字符来确定属于昵称；
            然后通过 username 查询，
            如果没有反馈再通过昵称。
            """
            flash(
                '已响应用户{}的登录请求，其中记住我为{}'.format(
                    login_form.username.data,
                    login_form.remember_me.data
                )
            )
            # 一般是跳转回主页
            return redirect('/')
        return render_template("auth/login.html", login_form=login_form)


class Logout(MethodView):
    decorators = [login_required]
    
    @login_required
    def get(self):
        logout_user()
        flash('成功登出！')
        return redirect(url_for('/'))


def load_blueprint(app):
    # 向蓝图注册
    auth = Blueprint('auth', __name__)
    
    auth.add_url_rule('/login', view_func=Login.as_view('login'))
    auth.add_url_rule('/logout', view_func=Logout.as_view('log_out'))

    app.register_blueprint(auth)
