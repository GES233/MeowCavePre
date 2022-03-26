# -*- encoding:utf-8 -*-
"""
    meowcave/forum/models.py
    ---------------
    
    圈子、讨论串以及贴子的模型与函数。
"""
# 导入库与模块
from datetime import datetime # 涉及时间戳

from meowcave.extensions import db


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
