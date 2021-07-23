import requests
import pytest

def test_qq_2():
    '''QQ号码-必填项 key,输入正确的key值，请求成功 '''
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm = {
        "qq": "12345678",
        "key": "8dbee1fcd8627fb6699bce7b986adc45"
    }
    r = requests.get(url=url, params=parm)
    print(r.text)

    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    reason = r.json()["reason"]
    print("取到的reason：%s"%reason)

    if error_code ==0:
        print("测试通过")

    # 预期结果
    expect_result = {"error_code": 0, "reason": "success"}


