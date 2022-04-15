# -*- encoding:utf-8 -*-
"""
    meowcave.auth.forms
    ---------------

    认证相关表单的提交。
"""
# 导入相关的库
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,  # 是或不
    PasswordField,
    StringField,  # 字符串
    SubmitField  # 提交键
)
from wtforms.validators import (  # 一堆验证器
    DataRequired,
    EqualTo,
    ValidationError
)

from meowcave.utils.match import email_addr_valid
from meowcave.user.models import (
    User,
    InvitationCode
)

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


class RegisterForm(FlaskForm):
    """
        注册表单（特指邀请码+邮件等），个人信息的修改业务被放在了`/user`下面。
    """
    nickname = StringField(
        '昵称',
        validators=[DataRequired(message='我总得知道怎么称呼您吧？')]
    )
    invitation_code = StringField(
        '邀请码',
        validators=[DataRequired(message='请输入邀请码')]
    )
    email = StringField(
        '邮件地址',
        validators=[
            DataRequired(message='我总得知道怎么联系您吧？嗯哼')
            # Email(message='话说，你写的是邮件地址码？') # 不想自己造轮子了，WTForms的高版本移除了对其的支持
            ]
    )
    passwd = PasswordField(
        '密码',
        validators=[DataRequired(message='我很想叫这个为「口令」的...喂，话说赶快写啊！')]
    )
    confirm_pswd = PasswordField(
        '确认密码',
        validators=[
            DataRequired(),
            EqualTo('passwd', message='两次的密码不一样，如果是因为忘记了最好还是重新再想一个')
        ]
    )
    submit = SubmitField('加入MeowCave！')

    # 给这玩意整点小函数，是WTForm的自定义项

    # 验证昵称

    def validate_nickname(self, nickname):
        # 昵称不能与别人的昵称重名，也不允许和别人的用户名重名
        user1 = User.query.filter_by(nickname=nickname.data).first()
        user2 = User.query.filter_by(username=nickname.data).first()
        if user1 is not None or user2 is not None:  # 有结果， i.e. 重名了
            raise ValidationError('这个名字已经被别人占有了。')  # 此处该有颜文字（？）

    # 验证邮件
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('电邮地址重名了。')
        if not email_addr_valid(string=email.data):
            raise ValidationError('话说，你写的是邮件地址码？')

    # 验证邀请码
    def validate_invitation_code(self, _ivcode):
        # 不是从User导入的了，需要一个新表以及一堆新的逻辑。
        i_code = InvitationCode.query.filter_by(code=_ivcode)  # 不要加`.first()`！
        if i_code is None:
            raise ValidationError('')  # IDK，有用吗？


class ForgotPasswordForm(FlaskForm):
    """
        忘记密码表单，暂略。
    """
    pass