#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 21:59
# @Author : apple
# @Software: PyCharm
import requests
import json

# url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
# parms={
#     'corpid':'ww11cf851bb266917f',
#     'corpsecret':'GeA7TubCqINVhVeX52O7D1KtR9uiPvKIPhvssQrlkXI'
# }
# r= requests.get(url=url,params=parms,verify=False)
# # 传data必须声明头部，传json=默认头部是herader
# # r= requests.get(url=url,data=parms,verify=False)
# # 解决乱码的问题
# # print(r.content.decode('utf-8'))
# jsond=r.text
# print (jsond)

# 相当于一个浏览器session
s=requests.session()
h={
    "Authorization": "Token %s" % "ddddddddddddd"
}
# 更新头部
s.headers.update(h)

# 然后再进行发布请求
dd=s.get(url="https://www.baidu.com/",verify=False)
print(dd.text)