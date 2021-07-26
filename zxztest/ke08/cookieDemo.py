#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 22:18
# @Author : apple
# @Software: PyCharm
import requests
import re
#
s= requests.session()
print(s.cookies)
jsonParms={"account":"shuxue.","password":"5c1e18a0624ddb1ab428f3c06b19fb7e"}
url='http://guanchu.tifenpai.com:9097/cloudApi/front/teacher/login'
s.post(url,json=jsonParms)
print(s.cookies)
url2='http://guanchu.tifenpai.com:9097/cloudApi/rolePower/getCurrentTeacherRoleAndPower'
parms2={
    'teacherNowRoleId':'1248274854927663104'
}
r2=s.get(url2,params=parms2)
print ( r2.text )

url3='http://guanchu.tifenpai.com:9097/cloudApi/teacherOperate/getOldestCurrentCatalog'
r3=s.get(url3)
print('0000'+r3.text)
# 正则提取公式
# 知道前后取中间，遇到字符加转义
# name='csrfmiddlewaretoken' value='(.+?)'
# <span id="help"><a href="http://www.baidu.com/search/jubao.html" target
# url3='https://www.baidu.com/'
# r1=requests.post(url3,verify=False)
# print(r1.text)
# csrfmiddlewaretoken = re.findall('<span id="help"><a href="(.+?)" target', r1.text)
# print(csrfmiddlewaretoken[0])

