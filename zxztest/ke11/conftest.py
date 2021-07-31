#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/25 23:13
# @Author : apple
# @Software: PyCharm
import pytest
import requests

from zxztest.ke09 import loginDemo
# 练习pytest的fixture,级别不同，只需要修改scope的
# `"function"``
#    `"function"``     (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.
@pytest.fixture(scope='session')
def loginfix():
    s = requests.session()
    loginDemo.login(s)
    print ( '执行了登录' )
    return s