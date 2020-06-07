#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 22:29
# @Author  : 一叶知秋
# @File    : forms.py
# @Software: PyCharm

from django import forms
from django.forms import ModelForm
from sign.models import Event
from sign.models import Guest


# 添加发布会表单
class AddEventForm(forms.Form):
    name = forms.CharField(max_length=100)            # 发布会标题
    limit = forms.IntegerField()                      # 限制人数
    status = forms.BooleanField(required=False)       # 状态
    address = forms.CharField(max_length=200)         # 地址
    start_time = forms.DateTimeField()                # 发布会时间


# 添加嘉宾
class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['event', 'realname', 'phone', 'email', 'sign']

'''
DateTimeField¶
class DateTimeField(**kwargs)[source]¶
Default widget: DateTimeInput
Empty value: None
Normalizes to: A Python datetime.datetime object.
Validates that the given value is either a datetime.datetime, datetime.date or string formatted in a particular datetime format.
Error message keys: required, invalid
Takes one optional argument:

input_formats¶
A list of formats used to attempt to convert a string to a valid datetime.datetime object.

If no input_formats argument is provided, the default input formats are:

['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
 '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
 '%Y-%m-%d',             # '2006-10-25'
 '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
 '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
 '%m/%d/%Y',             # '10/25/2006'
 '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
 '%m/%d/%y %H:%M',       # '10/25/06 14:30'
 '%m/%d/%y']             # '10/25/06'
See also format localization.
'''