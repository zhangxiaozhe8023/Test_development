import pytest
import requests
from ke9.func_login import login

@pytest.fixture(scope="module")
def login_fix():
    '''自定义一个前置的操作'''
    print("先登陆")
    s = requests.session()
    login(s)
    return s

@pytest.fixture(scope="function")
def unlogin_fix():
    '''自定义一个前置的操作'''
    print("不登陆")
    s = requests.session()
    s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
    return s

