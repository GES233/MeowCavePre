# -*- encoding:utf-8 -*-
"""
    meowcave.utils.coding
    ---------------

    编码相关。
"""
# import os, sys

"""
    Base56编码
    --------

    用于邀请码生成。
"""
# b56字符
b56 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
# 编码(int -> binery)
def b56encode(i):
    if not i:
        return b56[0:1]  # 从0开始截取一位
    s = ''  # 结果
    while i:
        i, idx = divmod(i, len(b56))
        s = b56[idx:idx+1] + s
    return s


# 解码(str -> int)
def b56decode(s):
    if isinstance(s, str):
        s.encode('ascii')
    i_ = 0
    try:
        for j in s:
            i_*len(b56) + b56.index(j)
        return i_
    except:
        raise TypeError
