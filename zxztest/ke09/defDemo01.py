#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 23:21
# @Author : apple
# @Software: PyCharm
def add(a, b):
    return a+b
def funApi01 (a,b):
    if isinstance(a,int):
        pass
    else:
        return '不是int类型'
    if not isinstance(b,int):
        return 'b不是int类型'
#     参数可以设置为默认值
def funApi02(a,b=0,c=True):
    return True,b,c
# 不定长参数,带等号的
def funApi03(*args,**kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    print(funApi01(3,'dddd'))
    print(add(1, 3))
    print(funApi02(2)[1])
    body={
        "a":1,
        "b":3
    }
    list=[1,2,3]

    # funApi03(1,2)
    funApi03(*list,**body)

