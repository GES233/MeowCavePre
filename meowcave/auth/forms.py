# -*- encoding:utf-8 -*-
"""
    meowcave/auth/forms.py
    ---------------
    
    认证相关表单的提交。
"""
# 导入相关的库
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,# 是或不
    PasswordField,
    StringField,# 字符串
    SubmitField,# 提交键
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
        登录表单。
    """
    username = StringField(
        '昵称',
        validators=[DataRequired(message='请输入昵称或邮件地址')]
    )
    password = PasswordField(
        '密码',
        validators=[DataRequired(message='密码不知道... 不会不是本人吧？')]
    )
    remember_me = BooleanField('记住我？')
    submit = SubmitField('登录')


class ResisterForm(FlaskForm):
    """
        注册表单（特指邀请码+邮件等），个人信息的修改业务被放在了`/user`下面。
    """
    pass


class ForgotPasswordForm(FlaskForm):
    """
        忘记密码表单，暂略。
    """
    pass
