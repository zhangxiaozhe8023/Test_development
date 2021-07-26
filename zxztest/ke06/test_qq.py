#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 12:35
# @Author : apple
# @Software: PyCharm
import requests

def qqdef(qq,key):
    url = "http://japi.juhe.cn/qqevaluate/qq"
    param = {
        'qq': qq,
        'key':key
    }
    r = requests.get ( url, params=param )
    return r.json()

def test_qq01():
    resqult= qqdef("980778026",'ff37047dc39e412967553d4c22def838')
    error_code=resqult['error_code']
    reason= resqult['reason']
    if(error_code==0):
        print("测试通过")
    reslutdd={error_code:0,reason:'success'}
    # 断言
    assert error_code==reslutdd[error_code]
    assert reason ==reslutdd[reason]

