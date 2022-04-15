# -*- encoding:utf-8 -*-
"""
    meowcave.forum.models
    ---------------
    
    圈子、讨论串以及贴子的模型与函数。
"""
# 导入库与模块
from datetime import datetime # 涉及时间戳

from meowcave.extensions import db


attendgroups = db.Table(
    'attendgroups',
    db.Column(
        'member_id',
        db.Integer(),
        db.ForeignKey('user.id', ondelete="CASCADE"),
        nullable=False
    ),
    db.Column(
        'group_id',
        db.Integer(),
        db.ForeignKey('group.id', ondelete="CASCADE"),
        nullable=False
    )
)



class Group(db.Model):
    """
        Group
        --------
        
        圈子，其实叫`Community`也没差，但是更多的还是小圈子。
    """
    __tablename__ = 'group'
    
    # `id`
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # `create_time`
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    # `group_name`：可以通过`/gruop/<group_name>`来查找
    group_name = db.Column(db.String(30), default=None)
    # `title`
    title = db.Column(db.String(255), nullable=False)
    # `locked`：内容对外人开放？
    locked = db.Column(db.Boolean, default=False, nullable=False)
    # `visible`：圈子可见？
    visible = db.Column(db.Boolean, default=False, nullable=False)
    
    # 和其他表的关系
    members = db.relationship(
        """
            many-to-many
        """
        'User',
        secondary=attendgroups
    )


class PostThread(db.Model):
    """
        PostThread
        --------
        
        讨论串，位于圈子下的内容的基本结构。
    """
    __tablename__ = 'thread'
    
    # `id`
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # `poster_id`
    poster_id = db.Coulmn(db.Interger, db.ForeginKey('user.id'))
    # `create_time`
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    # `dis_status`：展示状态，除了删除都仅有管理员可以操作
    """
    - `normal`：正常
    - `up`：置顶
    - `sink`：SEGA
    - `delete`：被删除
    """
    dis_status = db.Column(db.String, default='normal')
    # `post_status`：发贴状态
    """
    - `normal`：正常
    - `unpostedable`：无法发帖
    """
    post_status = db.Column(db.String, default='normal')
    
    """贴子"""
