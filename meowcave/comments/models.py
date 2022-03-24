# -*- encoding:utf-8 -*-
"""
    meowcave/comments/models.py
    ---------------
    
    提供与评论有关的模型与函数。
"""
# 导入库与模块
from datetime import datetime # 时间戳

from meowcave.extensions import db

class Comments(db.Model):
    """
        Comments
        --------
        
        承载评论。
    """
    __tablename__ = 'comments'
    
    # 一些基本属性
    # `id`：就是评论的id
    id = db.Column(db.Integer, primary_key=True)
    # `author_id`：就是作者的id，「评论者」
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # `create_time`：建立时间，在此就是「评论时间」
    create_time = db.Coulmn(db.DateTime, default=datetime.utcnow())
    # `content`：内容
    content = db.Column(db.Text)
    # `status`：状态
    """
    # - `normal`：正常
    # - `deleted`：被删除
    """
    status = db.Column(db.String, default='normal')
    
    """
    再次涉及逻辑。
    ----
    一个评论有可能回复：
    - UserPost
    - 另一条评论
    - (Post)
    ==>
    +---------+-----------+------------+-----------+
    | post-id | thread-id | comment-id | situation |
    +---------+-----------+------------+-----------+
    |   Null  |    Null   |  not Null  |  comments |
    +---------+-----------+------------+-----------+
    | not Null|    Null   |    Null    |  UserPost |
    +---------+-----------+------------+-----------+
    |   Null  |  not Null |    Null    |   Thread  |
    +---------+-----------+------------+-----------+
    """
    parent_user_post_id = db.Coulmn(db.Interger, db.ForeignKey('user_post.id', nullable=True))
    # parent_thtread_post_id = db.Coulmn(db.Interger, db.ForeignKey('post.id', nullable=True))
    parent_comment_id = db.Coulmn(db.Interger, db.ForeignKey('comment.id', nullable=True))
    # 相对应的，自我引用
    comment_to_comment = db.relationship('Comments', backref='child_commit'， lazy='dynamic')# 这块没绕过弯来说实话
    
    
    # 方法与函数
    def __repr__(self):
        if self.status != 'delete':
            if self.parent_comment_id:
                return '<Comment {}: -> comment {}>'.format(self.id, self.parent_comment_id)
            elif self.parent_user_post_id:
                return '<Comment {}: -> userpost {}>'.format(self.id, self.parent_user_post_id)
