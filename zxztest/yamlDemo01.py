# -*- coding: utf-8 -*-
# @Time : 2021/7/21 14:26
# @Author : admin
# @File : yamlDemo01.py
# @Software: PyCharm
import yaml
import os
# 获取当前脚本所在的文件夹路径
codefilePath =os.path.dirname(os.path.realpath(__file__))
#     获取yaml的路径
ymalfile = os.path.join(codefilePath,"test.yaml")

print(ymalfile)
# 打开yaml文件（IO）
f = open(ymalfile,'r',encoding="utf-8")
# 读取yaml文件
cfg=f.read()
print(type(cfg))
print(cfg)

d= yaml.load(cfg,Loader=yaml.FullLoader)
print(d)
print(type(d))
