# -*- coding: utf-8 -*-
# @Time : 2021/7/28 10:56
# @Author : admin
# @File : mysqltest.py
# @Software: PyCharm

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "test123", "TESTDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")