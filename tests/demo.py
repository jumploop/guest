#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 21:05
# @Author  : 一叶知秋
# @File    : demo.py
# @Software: PyCharm
class Host(object):
    def goodmorning(self, name):
        """Say good morning to guests"""
        return "Good morning, %s!" % name


if __name__ == '__main__':
    h = Host()
    hi = h.goodmorning('zhangsan')
    print(hi)
