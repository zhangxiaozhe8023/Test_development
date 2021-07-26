#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/25 20:58
# @Author : apple
# @Software: PyCharm
import pytest
# def setup_module():
#     print('模块调用')
#
#
# def setup_function():
#     print('执行了调用')

# 自定义的pytest方法,默认是函数级别的
@pytest.fixture(scope='function')
def login():
    print('先登录')
@pytest.fixture(scope='function')
def unlogin():
    print('不登录')

def test_1(login):
    print('执行了第一个')
def test_2(unlogin):
    print('执行了第二个')
