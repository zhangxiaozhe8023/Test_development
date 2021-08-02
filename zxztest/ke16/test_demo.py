#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/8/1 09:45
# @Author : apple
# @Software: PyCharm
import pytest


@pytest.fixture(scope='function')
def demo_fix():
    print('测试之前运行')
    yield 'hello'
    print('清理工作')
def test_01(demo_fix):
    # 打印yield的返回值
    print(demo_fix)
    print('测试用例1')
def test_02():
    print('测试用例2')
def test_03():
    print('测试用例3')


