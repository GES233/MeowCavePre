# -*- encoding:utf-8 -*-
"""
    meowcave.comments.models
    ---------------

    提供与评论有关的模型与函数。
"""
# 导入库与模块
import json
from datetime import datetime  # 时间戳

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
    parent_user_post_id = db.Column(
        db.Interger,
        db.ForeignKey('user_post.id', nullable=True)
    )
    # parent_thread_post_id = db.Column(
    #     db.Interger, db.ForeignKey('post.id', nullable=True)
    # )
    comment_lgt = db.Column(db.Integer, default=1)
    comment_rgt = db.Column(db.Integer, default=2)

    # 方法与函数

    def __repr__(self):
        if self.status != 'delete':
            if self.comment_rgt > 2:
                return '<Comment {} reply anothor comment>'.format(self.id)
            elif self.comment_rgt == 2:  # and parent_thread_id == None
                return '<Comment {} reply post {}>'.format(
                    self.id, self.parent_user_post_id)

    def comment_tree(self, parent_user_post_id):
        """
           返回一个贴子下所有的评论，以~~JSON~~id字典的形式返回
        """
        raw_comments_set = self.query.filter(
            parent_user_post_id=parent_user_post_id).all()
        init_tree = {'root': None}  # 为了确保只有一个评论的情况下字典能够存在
        """
        e.g.
        只有一个：{'root' : 25}
        很多个：{root' : {25 : [37, 49, 52], 39 : None}}
        """
        index = 1

        """
        检索方式：
        - 查看index是在右边还是在左边，
          - 左边就再加一个子节点；
          - 右边就结束添加字节点，把添加的权限给父节点，
            - 如果没有父节点就返回。
        - index += 1。
        """

    def comment_update(self, parent_node_id=None):
        # 可能需要把CURD包装下
        if not parent_node_id:  # 回复post而非评论
            self.comment_lgt = 1
            self.comment_rgt = 2
        else:
            # 获取 parent node 的右侧值
            parent = self.query.filter_by(id=parent_node_id)
            parent_rgt = parent.comment_rgt
            self.query.filter(  # rgt
                and_(
                    parent_user_post_id=parent_user_post_id,
                    self.comment_rgt.__lt__(parent_rgt))  # 刚好排除了parent node
            ).update(
                {'comment_rgt': self.comment_rgt + 2},
                synchronize_session=False)
            self.query.filter(  # lgt
                and_(
                    parent_user_post_id=parent_user_post_id,
                    self.comment_lgt.__lt__(parent_rgt))
            ).update(
                {'comment_lgt': self.comment_lgt + 2},
                synchronize_session=False)
            '''
            leftleftside_comments = self.query.filter(
                and_(
                    parent_user_post_id=parent_user_post_id,
                    self.comment_rgt.__lt__(parent_rgt) # 刚好排除了parent node
                )
            ).all()
            for right_or_root_node in leftleftside_comments:
                if right_or_root_node.comment_lgt > parent_node_id:
                    self.query.filter_by(id=right_or_root_node.id).update(
                        {'comment_rgt': right_or_root_node.comment_lgt + 2})
                self.query.filter_by(id=right_or_root_node.id).update(
                {'comment_lgt': right_or_root_node.comment_rgt + 2})
            '''

            self.query.filter_by(id=parent.id).update(
                {'comment_rgt': parent_rgt + 2})

            self.comment_lgt = parent_rgt
            self.comment_rgt = parent_rgt + 1
