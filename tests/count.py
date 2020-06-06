#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 16:54
# @Author  : 一叶知秋
# @File    : count.py
# @Software: PyCharm

# 实现简单计算器： +、 -、 *、 /、

class Calculator():
    '''实现两个数的加、 减、 乘、 除'''

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b
