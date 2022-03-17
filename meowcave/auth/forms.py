# -*- encoding:utf-8 -*-
"""
    meowcave/auth/form.py
    ---------------
    
    认证相关表单的提交。
"""
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
        登录表单。
    """
    username = StringField('昵称', validators=[DataRequired(message='请输入昵称或邮件地址')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不知道... 不会不是本人吧？')])
    remember_me = BooleanField('记住我？')
    submit = SubmitField('登录')


class ResisterForm(FlaskForm):
    pass
