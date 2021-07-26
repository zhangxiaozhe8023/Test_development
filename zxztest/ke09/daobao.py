#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/25 19:07
# @Author : apple
# @Software: PyCharm
# 两种导入方式（方式1
from zxztest.ke09.loginDemo import login
# 方式2
from zxztest.ke09 import loginDemo
# 方法3
from zxztest.ke09 import *

import requests

s= requests.session()
login(s)
loginDemo.login()