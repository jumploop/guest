#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 14:15
# @Author  : 一叶知秋
# @File    : common.py
# @Software: PyCharm
from django.http import JsonResponse


def response(status=None, message=None, data=[]):
    """
    实现Api的固定格式的返回
    :param status: 状态码
    :param message: 提示信息
    :param data: 数据
    :return:
    """
    if status is None:
        status = 10200

    if message is None:
        message = "successful"

    response_dict = {
        "status": status,
        "message": message,
        "data": data
    }
    return JsonResponse(response_dict)
