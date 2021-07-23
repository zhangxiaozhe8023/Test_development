import pytest
# 前置是登录

# 用例1 头部传用户登陆token，可以查询个人信息

# 用例2 头部传用户错误的token，无权限

@pytest.fixture(scope="function")
def login():
    '''自定义一个前置的操作'''
    print("先登陆")

@pytest.fixture(scope="function")
def unlogin():
    '''自定义一个前置的操作'''
    print("不登陆")

# def setup_module():
#     print("整个用例只调用一次")
#
# def setup_function():
#     '''函数级别的前置'''
#     print("函数级别的前置：每个用例都会调用一次")

def test_1(login):
    print("用例1 头部传用户登陆token，可以查询个人信息")

def test_2(unlogin):
    print("用例2 头部传用户错误的token，无权限")

    