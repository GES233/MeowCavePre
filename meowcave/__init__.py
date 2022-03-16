# -*- encoding:utf-8 -*-
"""
    MoewCave
    ----------------
    
    一个轻论坛的实现，代码参（chao）考（xi）了`flaskbb`。
"""
import os

from flask import Flask

from meowcave.app import create_app
