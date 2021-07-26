#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 17:58
# @Author : apple
# @Software: PyCharm
a=None
# 布尔
b=False
c=True
# int类型
d = 999
# 浮点数
f = 12.000
# str类型
h = 'asdlkfjasdf'
i="333"
u = '''
sdfasdf
'''
# list类型
aaa= [1,2,4,5,'ssss',True,None,[333,333]]
print(aaa[-1])
# type查看类型
print(type(a))
# 字典类型'
dicbbb = {
    "a":1,
    "b":"aaaa",
    'c':[12222,333],
    'd':None,
    'f':True
}
print(dicbbb)
# 取值
print(dicbbb["d"])
# 取值2     这个方法比较好，如果没有取到可以给个默认值None，然后可以设置默认值
print(dicbbb.get("x",'hello'))
# 通过key添加字典
dicbbb['key'] = 'dddd'
dicbbb['key'] = 'dd2dd'
# 通过key删除字典
del (dicbbb['a'])
# 通过key改字典
dicbbb['b'] ='980778026'
# 通过key查字典
print(dicbbb['b'])
# 通过
print(dicbbb)