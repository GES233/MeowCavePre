# -*- encoding:utf-8 -*-
"""
    meowcave/tests/index_test.py
    --------
    
    对首页的测试
"""
from flask import Flask, render_template

from meowcave.app import create_app

app = create_app()

# index.html
@app.route('/')
def index():
    title = 'Index'
    me = {'name' : 'rLCpBA'}
    content_list = [
        {
            'author' : {'name' : '粑粑', 'id' : '126'},
            'cr_time' : '14:03:26',
            'content' : '吃屎啦你！'
        },
        {
            'author' : {'name' : 'Lemon', 'id' : '239'},
            'cr_time' : '14:23:57',
            'content' : '一眼丁真，鉴定为：假'
        },
        {
            'author' : {'name' : '爱国学者张维为', 'id' : '17'},
            'cr_time' : '14:33:16',
            'content' : 'nt'
        },
        {
            'author' : {'name' : '12345', 'id' : '12'},
            'cr_time' : '14:57:00',
            'content' : 'sb'
        }
        ]
    return render_template('index.html', title='Home', me=me, content_list=content_list)
