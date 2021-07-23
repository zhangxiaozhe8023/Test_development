import pytest


@pytest.fixture(scope="function")
def demo_fix():
    print("测试用例之前执行的：前置操作，数据准备")
    yield "hello"
    print("测试用例结束之后的操作：数据清理")
# yield上面类似setup（） yield下面类似teardown（）

def test_1(demo_fix):
    print("测试用例1")


def test_2():
    print("测试用例2")


def test_3(demo_fix):
    print(demo_fix)
    print("测试用例3")
