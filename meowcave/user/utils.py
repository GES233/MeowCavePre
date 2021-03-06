# -*- encoding:utf-8 -*-
"""
    meowcave.user.utils
    ---------------
    
    关于认证的小函数。
"""
from random import randint
from meowcave.utils.coding import b56encode


def generator(prefix='mC', length=12):
    gen_len = length - len(prefix)
    s = ''
    for i in range(gen_len):
        s += b56encode(randint(0, 55))
    return prefix + s
