#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 18:34
# @Author : apple
# @Software: PyCharm
from zxztest.ke13.loginClass import CloudApi
from requests_toolbelt import MultipartEncoder
from lxml import etree
import pytest
import requests
@pytest.fixture(scope='session')
def loginfixture():
    s =requests.session()
    # 实例
    cloudAPi =CloudApi(sss=s)
    cloudAPi.login()
    return cloudAPi

def test_update_png(loginfixture):
    res =loginfixture.Xiugai01()
    print(res)
# /html/body/section/section/section/main/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[3]/div/div/a/span
demo =etree.HTML()