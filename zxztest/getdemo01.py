# -*- coding: utf-8 -*-
# @Time : 2021/7/22 9:36
# @Author : admin
# @File : getdemo01.py
# @Software: PyCharm
import requests

url ='http://192.168.1.6:8666/cloudApi/phone/teacher/checkAppInfo'
par={
    "applicationId":"cn.com.t600.teacher",
    'equipment':'phone'
}
r = requests.get(url,par)
print(r.text)