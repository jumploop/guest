#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 21:08
# @Author  : 一叶知秋
# @File    : Interface_demo.py
# @Software: PyCharm

from zope.interface import Interface
from zope.interface.declarations import implementer


# 定义接口
class IHost(Interface):
    def goodmorning(self, host):
        """Say good morning to host"""


@implementer(IHost)  # 继承接口
class Host:
    def goodmorning(self, guest):
        """Say good morning to guest"""
        return "Good morning, %s!" % guest


if __name__ == '__main__':
    p = Host()
    hi = p.goodmorning('Tom')
    print(hi)
