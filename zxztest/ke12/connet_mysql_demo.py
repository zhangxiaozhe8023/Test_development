# -*- coding: utf-8 -*-
# @Time : 2021/7/28 16:39
# @Author : admin
# @File : connet_mysql_demo.py
# @Software: PyCharm
import pymysql

mysqlConf = {
    'host' : '192.168.1.6',
    'user' : 'root',
    'password' : 'TQJzxc!@#$111',
    'port' : 3306
}
class dataConnect():
    def __init__(self,db_conf,database=""):
        self.db_conf =db_conf
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_conf)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
    def close(self):
        # 关闭连接
        self.db.close()
def select_sql(select_sql):
    '''查询数据库'''
    db = dataConnect(mysqlConf, database="ols_gaosan_new")
    result = db.select(select_sql)  # 查询
    db.close()
    return result
def execute_sql(insert_sql):
    '''执行sql'''
    db = dataConnect(mysqlConf, database="ols_gaosan_new")
    db.execute(insert_sql)  # 查询
    db.close()

if __name__ == '__main__':
    sql = 'SELECT * FROM student;'
    a = select_sql(sql)
    print(a)
