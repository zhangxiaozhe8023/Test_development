import pytest
import requests
from ke16.add_teacher import *

@pytest.fixture(scope="session")
def login_xadmin_fix():
    s = requests.session()
    login_xadmin(s)
    return s


def test_add_teacher_1(login_xadmin_fix, delete_teacher_sql):
    s = login_xadmin_fix
    result = add_teacher(s, name="老师5xxx")
    # 判断
    actul_result = get_add_result(result)
    assert actul_result == "老师5xxx"