#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 18:49
# @Author : apple
# @Software: PyCharm
import requests

url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
parms={
    'corpid':'ww11cf851bb266917f',
    'corpsecret':'GeA7TubCqINVhVeX52O7D1KtR9uiPvKIPhvssQrlkXI'
}
# r= requests.get(url=url,params=parms,verify=False)
# 传data必须声明头部，传json=默认头部是herader
# r= requests.get(url=url,data=parms,verify=False)
# 解决乱码的问题
# print(r.content.decode('utf-8'))
# jsond=r.text
# print (jsond)
token = 'O-Vlzm2PATrC0mw3z8iO6I_bklYqGnUcbl4PLV-v3i69EDoxKuyPLbMdJAlN5pX0AkXApbEE46jDgwb-Yffd_KqcLjWr8Uvk8Awm4--6tQuMXB01QRmDsY3xuG6xnDHAr7_nlIYkTmas1qu3hzkKOi04KBvMy4Z3Ias8r0XlNeG6RUdljguU-uI5zToGDQLlg0Neml-JZoCkCGna9Uhc_A'
# 创建学生
cjStudentUrl='https://qyapi.weixin.qq.com/cgi-bin/school/user/create_student'
jsonparms={
    "student_userid": "zhangsan",
    "name": "张三",
    "department": '15481124955233409'
}
parmsstr={
    'access_token':token
}

r=requests.post(cjStudentUrl,params=parmsstr,json=jsonparms,verify=False)
print(r.text)