#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/23 21:20
# @Author : apple
# @Software: PyCharm
import requests
import urllib3
#   忽略警告
urllib3.disable_warnings()

hosturl='http://guanchu.tifenpai.com:9097'
url ='/cloudApi/front/teacher/login'
body={
    'account':'333',
    'password':123456
}
# 证书核实设为false
# r=requests.get(url,verify=False)
r= requests.post(hosturl+url,json=body,headers="ddd")

print(r.text)