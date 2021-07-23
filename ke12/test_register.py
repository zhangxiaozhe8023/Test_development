import requests
import pytest
from ke12.connect_mysql import execute_sql
s = requests.session()


@pytest.fixture()
def delete_user():
    # 先数据准备：先删除已经注册的用户
    delete_sql = 'DELETE FROM auth_user WHERE username="test123";'
    execute_sql(delete_sql)

@pytest.fixture()
def insert_user():
    # 先数据准备：先写入一个已经注册的用户
    insert_sql = 'insert '
    execute_sql(insert_sql)


def test_register_299(delete_user):
    '''测试注册接口-注册成功'''
    url = "http://49.235.92.12:9000/api/v1/register"
    body = {
        "username": "test123",
        "password": "123456",
        "mail": "1233@qq.com"
    }
    r = s.post(url, json=body)
    print(r.text)
    print(r.json())
    assert r.json()["msg"] == "注册成功!"
#
# def test_register_300(insert_user):
#     '''测试注册接口-用户已被注册'''
#     url = "http://49.235.92.12:9000/api/v1/register"
#     body = {
#         "username": "test321",
#         "password": "123456",
#         "mail": "1233@qq.com"
#     }
#     # r1 = s.post(url, json=body)   # 准备一个已经注册的数据
#     r2 = s.post(url, json=body)     # 重复注册
#     print(r2.text)
#     print(r2.json())
#     assert r2.json()["msg"] == "test321用户已被注册"
