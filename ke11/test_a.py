import pytest




@pytest.mark.parametrize("test_input,expect",
                         [
                             ({"user": "test", "pws": "1233"}, {"code":0, "msg":""}),
                             ("2+4", 6),
                             ("6*9", 54),
                         ])
def test_demo(test_input, expect):
    assert eval(test_input) == expect



def test_1():
    a = "3+5"
    assert eval(a) == 0

def test_2():
    a = "2+4"
    assert eval(a) == 6

def test_4():
    a = "6*9"
    assert eval(a) == 54