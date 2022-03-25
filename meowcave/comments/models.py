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
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
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
    | post-id | thread-id | comment-id |  location |
    +---------+-----------+------------+-----------+
    |   Null  |    Null   |     > 2    |  comments |
    +---------+-----------+------------+-----------+
    | not Null|    Null   |    1, 2    |  UserPost |
    +---------+-----------+------------+-----------+
    |   Null  |  not Null |    1, 2    |   Thread  |
    +---------+-----------+------------+-----------+
    
    ----
    为了便于检索打算采用前序排序（不是计算机专业学生，没学过数据结构，见谅）
    """
    parent_user_post_id = db.Column(db.Interger, db.ForeignKey('user_post.id', nullable=True))
    # parent_thread_post_id = db.Column(db.Interger, db.ForeignKey('post.id', nullable=True))
    # parent_comment_id = db.Coulmn(db.Interger, db.ForeignKey('comment.id', nullable=True))
    # 相对应的，自我引用
    # comment_to_comment = db.relationship('Comments', backref='child_commit'， lazy='dynamic')# 这块没绕过弯来说实话
    comment_lgt = db.Column(db.Integer)
    comment_rgt = db.Column(db.Integer)
    
    
    # 方法与函数
    def __repr__(self):
        if self.status != 'delete':
            if self.comment_rgt > 2:
                return '<Comment {} reply anothor comment>'.format(self.id)
            elif self.comment_rgt == 2: # and parent_thread_id == None
                return '<Comment {} reply post {}>'.format(slef.id, self.parent_user_post_id)
    
    
    def comment_tree(self, parent_user_post_id):
        """
           返回一个贴子下所有的评论
        """
        raw_comments_set = self.query.filter(parent_user_post_id=parent_user_post_id).all()
        init_tree = []
        index = 1
        
        # ...
        
        pass
    
    
    def comment_update(self, parent_node_id=None):
        if not parent_node_id: # 回复post而非评论
            self.comment_lgt = 1
            self.comment_rgt = 2
        else:
            update_comments_set = self.query.filter(
                and_(parent_user_post_id=parent_user_post_id,
                    or_(comment_lgt > parent_node_id, comment_rgt > parent_node_id) # 两次查询如果有重叠怎么办？
                )
            ).all()
            
            # ...
            
            pass
