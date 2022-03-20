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
    url_for,# 参数是函数名，后面的view_func=...里的，全名（e.g. auth.login）
    Blueprint,
    render_template,
    flash
)
from flask.views import MethodView
from flask_login import(
    login_user,
    logout_user,
    login_required,
    current_user
)
from meowcave.utils.match import email_addr_valid, ascii_letter_valid
from meowcave.extensions import login_manager, db
from meowcave.user.models import User
from meowcave.auth.forms import(
    LoginForm, 
    RegisterForm
)


class Login(MethodView):
    __methods__ = ['GET', 'POST']
    
    def form(self):
        return LoginForm()
    
    
    def login_failer(self):
        # 密码错误或查无此人的情况
        flash('邮件或密码输入错误！')
        return redirect(url_for('auth.login'))
    
    
    def get(self):
        return render_template("auth/login.html", login_form=self.form())
    
    
    def post(self):
        if current_user.is_authenticated:# 已经登录的情况
            flash('您已经登录了！')
            return redirect(url_for('index'))
        
        login_form = self.form()
        
        if login_form.validate_on_submit():# 对表单的验证
            # 可能需要验证码
            # ...
            # 也可能需要对用户身份判定的部分内容
            """
            关于用户登录表单的`username`的流程：
            邮件 优先于 username 优先于 昵称（）
            邮件用'user@example.com'为过滤正则式，
            如果有结果那么通过邮件查询用户；
            首先通过「不是」纯ASCII字符来确定属于昵称；
            然后通过 username 查询，
            如果没有反馈再通过昵称。
            """
            
            # 初始的一些量
            _input = login_form.username.data
            pswd = login_form.password.data
            _me = login_form.remember_me.data
            
            
            def _login_success():
                # 为减少代码量用的函数
                login_user(user, remember=_me)
                return redirect(url_for('index'))
            
            
            # 逻辑部分
            if email_addr_valid(_input): # 匹配出是邮件
                user = User.query.filter_by(email=_input).first()
                if user is None or not user.passwd_check(pswd):
                    return self.login_failer()
                else:
                    # 通过邮件登录成功
                    return _login_success()
            else: # 不是邮件
                if not ascii_letter_valid(_input):
                    # 匹配结果显示肯定是昵称
                    user = User.query.filter_by(nickname=_input).first()
                    if user is None or not user.passwd_check(pswd):
                        return self.login_failer()
                    else:
                        return _login_success()
                        # return redirect(url_for('index'))
                else:
                    # 先查询`username`，这个人肯定少
                    user = User.query.filter_by(username=_input).first()
                    if user:
                        if not user.passwd_check(pswd):
                            return self.login_failer()
                        else:
                            return _login_success()
                            # return redirect(url_for('index'))
                    else: # 再用昵称查找
                        user = User.query.filter_by(nickname=_input).first()
                        if user is None or not user.passwd_check(pswd):
                            return self.login_failer()
                        else:
                            return _login_success()
                            # return redirect(url_for('index'))
            
        return render_template("auth/login.html", login_form=login_form)


class Logout(MethodView):
    decorators = [login_required]
    
    # 需要考虑未登录用户键入登出的情况
    
    # @login_required
    def get(self):
        logout_user()
        flash('成功登出！')
        return redirect(url_for('index'))


class Register(MethodView):
    __methods__ = ['GET', 'POST']
    
    def form(self):
        return RegisterForm()
    
    
    def get(self):
        return render_template("auth/register.html", reg_form=self.form())
    
    
    def post(self):
        if current_user.is_authenticated:# 已经登录的情况
            flash('您已经登录了，因此无需注册')
            return redirect(url_for('index'))
        
        
        reg_form = self.form()
        
        
        _nickname = reg_form.nickname.data
        pwsd = reg_form.passwd.data
        email = reg_form.email.data
        
        
        if reg_form.validate_on_submit():
            # 依旧需要验证码
            # 在把邀请码的逻辑与数据库导入后再管这个
            """
            照例说一波逻辑：
            1. 检查邀请码是否有效
            2. 确认邮箱是有效的（forms.py）
            3. 确定昵称是否与别人的昵称以及username重复（form.py）
            4. 确认密码是有被用户记住的（form.py）
            5. 载入数据
            """
            user = User(
                nickname = _nickname,
                email = email
            )
            user.passwd_set(pwsd)
            db.session.add(user)
            db.session.commit()
            flash('恭喜您！成为了我们的一员')
            # 接下来是登录逻辑
            # 理论上来讲，可以选择自动跳转，但是我不会
            return redirect(url_for('auth.login'))
        
        return render_template("auth/register.html", reg_form=reg_form)


def load_blueprint(app):
    # 向蓝图注册
    auth = Blueprint('auth', __name__)
    
    auth.add_url_rule('/login', view_func=Login.as_view('login'))
    auth.add_url_rule('/logout', view_func=Logout.as_view('log_out'))
    auth.add_url_rule('/register', view_func=Register.as_view('register'))

    app.register_blueprint(auth)
