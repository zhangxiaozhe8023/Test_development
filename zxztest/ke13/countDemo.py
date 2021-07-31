# -*- coding: utf-8 -*-
# @Time : 2021/7/29 10:30
# @Author : admin
# @File : countDemo.py
# @Software: PyCharm
class Count():
    def add (self,a,b):
        print(a+b)
        return a+b
    def acc(self,a,b):
        return a-b
    def aff(self,a,b):
        return self.add(a,b) * self.acc(a,b)
a =Count()
print(a.aff(a=1, b=2))
