# from ke9.func_login import login
# import pytest
# import requests
#
# @pytest.fixture(scope="function")
# def login_fix():
#     '''自定义一个前置的操作'''
#     print("先登陆")
#     s = requests.session()
#     login(s)
#     return s
#
# @pytest.fixture(scope="function")
# def unlogin_fix():
#     '''自定义一个前置的操作'''
#     print("不登陆")
#     s = requests.session()
#     s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
#     return s

def test_info_34(login_fix):
    s = login_fix
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    r = s.get(url)
    print(r.text)
    assert r.json()["msg"] == "sucess!"
    assert r.json()["code"] == 0

def test_info_35(unlogin_fix):
    # s = requests.session()
    # s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
    s = unlogin_fix
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    r = s.get(url)
    print(r.text)
    assert r.status_code == 401

