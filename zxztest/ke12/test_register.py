# -*- coding: utf-8 -*-
# @Time : 2021/7/29 8:33
# @Author : admin
# @File : test_register.py
# @Software: PyCharm
from zxztest.ke11.conftest import loginfix
import requests
import pytest

from zxztest.ke12.connet_mysql_demo import execute_sql
# 执行sql删除语句
@pytest.fixture(scope='function')
def deleteUser():
    execute_sql('DELETE FROM student WHERE studentId ="9807778";')
# @pytest.fixture(scope='funtion')
# def insterUser():
#     sql = ''

# 修改的方法
def test_Xiugai01(loginfix):
    s= loginfix
    url= 'http://222.128.6.177:8666/cloudApi/student/updateByStudent/111'
    parmse = {"name":"111","classId":17,"mac":"","classIdList":[17]}
    response =s.put(url,json=parmse)
    print(response.text)
# 注册的方法,方法执行前执行delete方法

def test_Zhuce01(loginfix,deleteUser):
    s= loginfix
    url= 'http://222.128.6.177:8666/cloudApi/student/add'
    parmse = {"studentId":"9807778","name":"9807778","classIdList":[17],"account":"9807778"}
    response =s.post(url,json=parmse)
    print(response.json())
    jsonResponse = response.json()
    assert jsonResponse['code'] == 200
# 已注册的校验返回值
def test_Chongfu(loginfix,deleteUser):
    s=loginfix
    url ='http://222.128.6.177:8666/cloudApi/student/add'
    parmsie = {"studentId":"9807778","name":"9807778","classIdList":[17],"account":"9807778"}
    response1 = s.post(url,json=parmsie)
    response2 = s.post(url, json=parmsie)
    jsonResponse1 = response1.json()
    jsonResponse2 = response2.json()
    print(jsonResponse2)
    assert jsonResponse2['code'] == 500