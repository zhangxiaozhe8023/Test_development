#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/8/1 10:26
# @Author : apple
# @Software: PyCharm
import os
# 环境变量设置host
def test_os1():
    os.environ['host1'] = '127.0.0.1'
    host1=os.environ['host1']
    def ddd():
        print(host1)
    ddd()