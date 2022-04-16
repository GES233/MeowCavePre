# -*- encoding:utf-8 -*-
"""
    meowcave.spectator.models
    ---------------

    提供与「观察者」（管理员）关的模型与函数，
    主要包括后台界面以及日志记录。
"""
# 导入库与模块
from datetime import datetime, timedelta

from meowcave.extensions import db
from meowcave.user.utils import *

class SensitiveLog(db.Model):
    """
        SensitiveLog
        --------
        
        记录所有管理的敏感操作（权限 require）的日志，
        向所有人公开。
    """
    __tablename__ = 'admin_log'
    
    # `id`
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # `oprator_id`
    oprator_id = db.Coulmn(db.Interger, db.ForeignKey('user.id'))
    # `oprate_time`
    oprate_time = db.Column(db.DateTime, default=datetime.utcnow())
