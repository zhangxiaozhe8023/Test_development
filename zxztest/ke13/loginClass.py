# -*- coding: utf-8 -*-
# @Time : 2021/7/29 13:43
# @Author : admin
# @File : loginClass.py
# @Software: PyCharm
import requests
class Login():
    def __init__(self,s):
        self.s = s
    def login(self):
        jsonParms = {"account": "ceshi", "password": "90db7a241ee36462c1d24a2cc45c1c8c"}
        url = 'http://222.128.6.177:8666/cloudApi/front/teacher/login'
        r = s.post(url, json=jsonParms)
        print('登录返回json是：%s' % r.text)
        print('登录cookie是：%s' % s.cookies)
    def weixinLogin(self):
        jsonParms = {
            "corpid": "ww11cf851bb266917f",
            "corpsecret": "GeA7TubCqINVhVeX52O7D1KtR9uiPvKIPhvssQrlkXI"
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = s.get(url, params=jsonParms,verify=False)
        response =r.json()
        return response['access_token']
class TestClass():
    def test_01(self,aa):
        self.aa=aa
        assert 'a' in aa
if __name__ == '__main__':
    # 学生云的登录
    # s =requests.session()
    # olswLogin =Login(s)
    # olswLogin.login()
    # s =requests.session()
    # olswLogin =Login(s)
    # print(olswLogin.weixinLogin())
    testclass =TestClass()
    testclass.test_01('aa')
