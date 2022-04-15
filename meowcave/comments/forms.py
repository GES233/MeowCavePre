# -*- encoding:utf-8 -*-
"""
    meowcave.comments.forms
    ---------------
    
    评论表单的提交。
"""
# 导入相关的库
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import (
    DataRequired
)

class CommentForm(FlaskFrom):
    """
        评论表单。
    """
    comment = StringField('评论',
        vadidators=[
            DataRequired(message='不评论了？那就不评论吧')
        ]
    )
    submit = SubmitField('喷射！（指评论')
