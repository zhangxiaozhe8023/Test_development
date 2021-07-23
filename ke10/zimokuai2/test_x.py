def test_updata_info_32(login_fix):
    '''修改个人信息'''
    s = login_fix
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {"name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"}
    r = s.post(url, json=body)
    print(r.text)
    assert r.json()["message"] == "update some data!"
    assert r.json()["code"] == 0
    assert r.json()["data"]["mail"] == "283340479@qq.com"

