import pymysql
'''
pip install PyMySQL==0.9.3
'''

dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309}


class DbConnect():
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)

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
    db = DbConnect(dbinfo, database="apps")
    result = db.select(select_sql)  # 查询
    db.close()
    return result

def execute_sql(insert_sql):
    '''执行sql'''
    db = DbConnect(dbinfo, database="apps")
    db.execute(insert_sql)  # 查询
    db.close()


if __name__ == '__main__':
    # db = DbConnect(db_cof=dbinfo, database="apps")
    # sql = 'SELECT * from auth_user WHERE username="test";'
    # result = db.select(select_sql)
    # print(result[0]["username"])
    sql = 'SELECT * from auth_user WHERE username="test";'
    a = select_sql(sql)
    print(a)
