#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/25 22:44
# @Author : apple
# @Software: PyCharm
def test_getStudyTaskByPage(loginfix):
    s=loginfix
    url='http://guanchu.tifenpai.com:9097/cloudApi/studentTask/getStudyTaskByPage'
    json = {"taskType":"","classId":"","name":"","beginTime":"","endTime":"","pageSize":10,"pageNum":1}
    r=s.post(url,json=json)
    print(r.text)
    assert r.json()['code'] == 200
def test_demo(loginfix):
    s = loginfix
    url='http://guanchu.tifenpai.com:9097/cloudApi/studentTask/getStudyTaskByPage'
    json = {"taskType":"","classId":"","name":"","beginTime":"","endTime":"","pageSize":10,"pageNum":1}
    r=s.post(url,json=json)
    print(r.text)


