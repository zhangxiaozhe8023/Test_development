#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 18:34
# @Author : apple
# @Software: PyCharm
from zxztest.ke13.loginClass import CloudApi
import requests
import pytest
@pytest.fixture(scope='session')
def loginfixture():
    s =requests.session()
    # 实例
    cloudAPi =CloudApi(sss=s)
    cloudAPi.login()
    return cloudAPi

def test_get_info(loginfixture):
    res =loginfixture.Xiugai01()
    assert res['code'] == 200