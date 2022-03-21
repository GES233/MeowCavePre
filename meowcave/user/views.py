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

from meowcave.extensions import db
from meowcave.user.models import(
    UserPost,
    User
)
from meowcave.user.forms import UserPostForm


class UserIndex(View):
    """
        用户主页
    """
    methods = ['GET', 'POST']
    
    def dispatch_request(self, id):
        user = User.query.filter_by(id=id).first_or_404()
        content = UserPost.query.filter_by(owner_id=id)
    
        form = None
    
        if current_user:
            form = UserPostForm()
            if request.method == 'POST':
                if form.validate_on_submit():
                    post = UserPost(content=form.post.data, owner_id=current_user.id)
                    # https://stackoverflow.com/questions/29888698/sqlalchemy-exc-interfaceerror-unprintable-interfaceerror-object
                    db.session.add(post)
                    db.session.commit()
                    flash('看看是谁，又发了个贴子！')
                    return redirect(url_for('user.shown', id=id))
                return render_template("user/user.html", user=user, content_list=content, form=form)
            if request.method == 'GET':
                return render_template("user/user.html", user=user, content_list=content, form=form)
        return render_template("user/user.html", user=user, content_list=content)

def load_blueprint(app):
    # 向蓝图注册
    user = Blueprint('user', __name__)
    
    user.add_url_rule('/user/<id>', view_func=UserIndex.as_view('shown'))# 'user.shown'
    # user.all_url_rule('/people/<username>', end_point='username_page')

    app.register_blueprint(user)
