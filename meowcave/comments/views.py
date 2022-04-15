# -*- encoding:utf-8 -*-
"""
    meowcave.comments.views
    ---------------
    
    提供评论相关的视图（本来打算不用类视图写一个的，但是保持代码的一致性还是继续吧）。
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
from flask.views import MethodView
from flask_login import(
    login_required,
    current_user
)
from meowcave.utils.match import email_addr_valid, ascii_letter_valid
from meowcave.extensions import login_manager, db
from meowcave.user.models import UserPost
from meowcave.comments.models import Comments
from meowcave.comments.forms import CommentForm

class CommentsUnderUserPost(MethodView):
    """
        路由仅能对整个评论树显示，表现为'/userpost/<id>'；
        后者为'/comment/...'，
    """
    decorators = [login_required]
    
    def fetch_comments(self, all_comments=True):
        comments = Comments.query.jion(parent_user_post_id).all()
    
    def get(self):
        pass
