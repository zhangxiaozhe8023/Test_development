import requests
import pytest

def qqfunc(qq, key):
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm = {
        "qq": qq,
        "key": key
    }
    r = requests.get(url=url, params=parm)
    print(r.text)
    return r.json()

def test_qq_8():
    '''QQ号码-必填项 key,输入正确的key值，请求成功 '''
    result = qqfunc(qq="123456", key="8dbee1fcd8627fb6699bce7b986adc45")
    expect_result = {"error_code": 0, "reason": "success"}
    # 断言
    assert result["error_code"] == expect_result["error_code"]
    assert result["reason"] == expect_result["reason"]


def test_qq_7():
    ''' QQ号码-必填项 key 不传 '''
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm = {
        "qq": "12345678"
    }
    r = requests.get(url=url, params=parm)
    print(r.text)

    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    reason = r.json()["reason"]
    print("取到的reason：%s"%reason)

    # if error_code ==0:
    #     print("测试通过")

    # 预期结果
    expect_result = {"error_code": 10001, "reason": "KEY ERROR!"}

    # 断言
    assert error_code == expect_result["error_code"]
    assert reason == expect_result["reason"]

def test_qq_10():
    ''' QQ号码-必填项 key 长度大于32任意字符'''
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm = {
        "qq": "12345678",
        "key": "8dbee1fcd8627fb6699bce7b986adc45xx"
    }
    r = requests.get(url=url, params=parm)
    print(r.text)

    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    reason = r.json()["reason"]
    print("取到的reason：%s"%reason)

    # if error_code ==0:
    #     print("测试通过")

    # 预期结果
    expect_result = {"error_code": 10001, "reason": "KEY ERROR!"}

    # 断言
    assert error_code == expect_result["error_code"]
    assert reason == expect_result["reason"]


def test_qq_15():
    '''QQ号码-必填项qq,长度大于32字符'''
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm = {
        "qq": "123456782222222222222222222222222",
        "key": "8dbee1fcd8627fb6699bce7b986adc45"
    }
    r = requests.get(url=url, params=parm)
    print(r.text)

    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    reason = r.json()["reason"]
    print("取到的reason：%s"%reason)

    # if error_code ==0:
    #     print("测试通过")

    # 预期结果
    expect_result = {"error_code": 216602,"reason": "错误的请求参数"}

    # 断言
    assert error_code == expect_result["error_code"]
    assert reason == expect_result["reason"]


