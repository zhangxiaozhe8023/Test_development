#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/31 10:59
# @Author : apple
# @Software: PyCharm



class Father():
    def fangzi(self):
        print('房子')
    def __siyou(self):
        print('私有的方法')
class Mather():
    def chezi(self):
        print('房子')
class People(Father,Mather):
    quanju =200
    def __init__(self,age=18):
        # 初始化类 加上self class  全局生效
        self.name ='人'
        self.age = 18
        # 全局变量放init
        self.fan = '吃饭饭'
        # self.chi = self.chifan()
    #     方法
    def chifan(self):
        # 局部变量
        fan = '吃饭饭'
        print('年龄%s'%self.age)

        print(fan)
    def shengxiaohai(self):
        self.dongxi =self.fan
        return '小孩',self.dongxi
    def fangzi(self):
        print('自己的房子')
        self.quanju =300
if __name__ == '__main__':
    # 实例化  init 内容 ，自动执行
    nvPY =People(age=19)
    a = nvPY.dachengtui ='大长腿'
    print(a)
    print ( nvPY.shengxiaohai () )
    nvPY.fangzi()
    nvPY.chezi()

    # print ( nvPY.chifan () )
    # a =nvPY.shengxiaohai()
    # print(a)


