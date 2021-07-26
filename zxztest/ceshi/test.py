# -*- coding: utf-8 -*-
# @Time : 2021/7/21 15:05
# @Author : admin
# @File : test.py
# @Software: PyCharm

# 脚本路径
import os
import yaml


# 获取引用模块的文件的绝对路径
pyfile=os.path.dirname(os.path.realpath(__file__))
yamlfile =os.path.join( pyfile, "test.yaml" )

o=open(yamlfile,'r',encoding='utf-8')
ii=o.read()
# 转为字典类型的
p=yaml.load(ii,Loader=yaml.FullLoader)
print(type(p))
print(p)