#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/27 21:50
# @Author : apple
# @Software: PyCharm
import pytest

@pytest.mark.parametrize('nameParms,reposn',['ceshi01','ceshi02'],{'aa':'aa','bb':'bb'})
def test_update(loginfix,nameParms,reposn):
    s=loginfix
    parmsjson={"id":"1413293989259640832","name":nameParms,"beginTime":0,"endTime":0,"classIdList":["17"],"catalogIdList":["1367033025178894337"],"knowledgePointIdList":[]}
    url='http://guanchu.tifenpai.com:9097/cloudApi/studentTask/addOrUpdateStudyTask'
    r=s.post(url,json=parmsjson)
    print(r.text)
    print(reposn)