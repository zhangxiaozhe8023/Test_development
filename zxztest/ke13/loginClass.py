# -*- coding: utf-8 -*-
# @Time : 2021/7/29 13:43
# @Author : admin
# @File : loginClass.py
# @Software: PyCharm
import requests
from requests_toolbelt import MultipartEncoder
class CloudApi():

    def __init__(self, sss,host='http://222.128.6.177:8666/'):
        self.session = sss
        self.host = host
    def login(self,loginzhang = 'ceshi',password='90db7a241ee36462c1d24a2cc45c1c8c'):
        jsonParms = {"account": loginzhang, "password": password}
        url = self.host + 'cloudApi/front/teacher/login'
        # r = s.post(url, json=jsonParms)
        r = self.session.post(url, json=jsonParms)
        print('登录返回json是：%s' % r.text)
        # print('登录cookie是：%s' % s.cookies)
        print('登录cookie是：%s' % self.session.cookies)

    def Xiugai01(self):
        url= 'http://222.128.6.177:8666/cloudApi/student/updateByStudent/111'
        parmse = {"name":"111","classId":17,"mac":"","classIdList":[17]}
        response =self.session.put(url,json=parmse)
        print(response.text)
        return response.json()
    def shanghchuan(self):
        url ='http://222.128.6.177:8666/cloudApi/fileUpload/doUpload'
        res=self.session.post(url)
        m= MultipartEncoder(
            fields=[
                ('name','bussCode'),
                ('name','file'),
                ('filename','IMG_0647.JPG')
            ]

        )

    def weixinLogin(self):
        jsonParms = {
            "corpid": "ww11cf851bb266917f",
            "corpsecret": "GeA7TubCqINVhVeX52O7D1KtR9uiPvKIPhvssQrlkXI"
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = s.get(url, params=jsonParms,verify=False)
        response =r.json()
        return response['access_token']
# class TestClass():
#     def test_01(self,aa):
#         self.aa=aa
#         assert 'a' in aa
if __name__ == '__main__':
    # 学生云的登录
    s = requests.session()
    # 实例化
    olswCloud =CloudApi(s)
    # 调用
    olswCloud.login()
    # s =requests.session()
    # olswLogin =Login(s)
    # print(olswLogin.weixinLogin())
    # testclass =TestClass()
    # testclass.test_01('aa')
