#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/24 18:22
# @Author : apple
# @Software: PyCharm
import json

dictbbb = {
    'b': '980778026',
    'c': [12222, 333],
    'd': None,
    'f': True,
    'key': 'dd2dd',
    "i": {
    "dd":33,
    'ss':'4444'
},
    'listdd':[222,333,444,True,{'ddd':'ddd','eee':222}]
}
print ( dictbbb )
print(type(dictbbb))
# dict转为json格式
jsondict2=json.dumps(dictbbb)
print(jsondict2)
print(type(jsondict2))
# json转dict
dict_json=json.loads(jsondict2)
print(dict_json)
# 字典转字符串
print(str(dict_json))
# eval 把字符串当成语法来执行
f = '1+1'
print(eval(f))

