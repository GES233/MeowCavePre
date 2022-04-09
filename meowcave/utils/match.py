# -*- encoding:utf-8 -*-
"""
    /mewocave/utils/match.py
    --------

    返回匹配字符串的结果
"""
import re

def email_addr_valid(string):
    """
    检测是否为邮件地址，返回布尔值。
    """
    regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    )
    # 抄袭自 https://zhuanlan.zhihu.com/p/438574574

    if re.fullmatch(regex, string):
        return True
    else:
        return False


def ascii_letter_valid(string):
    """
        检测是否为纯ASCII字符，返回布尔值。
    """
    regex = re.compile(r'[^\x00-x7F]+')

    if re.fullmatch(regex, string):
        return True
    else:
        return False