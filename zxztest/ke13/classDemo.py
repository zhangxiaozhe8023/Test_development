# -*- coding: utf-8 -*-
# @Time : 2021/7/29 10:24
# @Author : admin
# @File : classDemo.py
# @Software: PyCharm

# 全局作用
a =33
class People ():
    # 整个类有效
    b=33
    def __init__(self,frind='白手',live='生活'):
        # 整个类有效
        self.c =33
        self.frind =frind
        self.live =live
        # 本方法有效
        d =33

    def hand (self):
        cc ='我对象的手%s and %s'%(self.frind,self.live)
        return cc
    def foot(self):
        # 真个类有效
        self.e =33
        f=33
    def oo(self):
        f=22
        h=a+self.b+self.c+self.e+f
if __name__ == '__main__':
    girlPeople = People('黑手','没好')
    print(girlPeople.hand())
    print(girlPeople.foot())

