import pytest
from ke9.b import func_api_1


def test_b_1():
    c = func_api_1("a", 1)
    print(c)
    assert c == "参数类型错误：a 必须是int类型"

def test_b_2():
    d = func_api_1(1, "b")
    print(d)
    assert d == "参数类型错误：b 必须是int类型"

def test_b_3():
    f = func_api_1(1, 1)
    print(f)
    assert f == 2


