# -*- encoding:utf-8 -*-
"""
    meowcave/user/forms.py
    ---------------

    用户相关表单的提交。
"""
# 导入相关的库
from flask_wtf import FlaskForm
from wtforms import (
    TextAreaField,  # 写个小作文
    # BooleanField,
    StringField,
    SubmitField
)
from wtforms.validators import DataRequired, Length

# from meowcave.user.models import User, UserPost

class UserPostForm(FlaskForm):
    """
        用户动态上传。
        --------

        写点啥
    """
    post = TextAreaField(
        '写点啥...',
        validators=[
            DataRequired('不能发空动态哟～'),
            Length(min=1, max=100)
        ]
    )
    submit_post = SubmitField('PO 上 網 ！')


class UserProfileModification(FlaskForm):
    """
        用户信息修改，暂略
    """
    new_nickname = StringField()
    new_username = StringField()
    new_info = TextAreaField()
    info_update = SubmitField('更改信息')