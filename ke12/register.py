import requests
from ke12.connect_mysql import execute_sql
s = requests.session()

# 先数据准备：先删除已经注册的用户
delete_sql = 'DELETE FROM auth_user WHERE username="test123";'
execute_sql(delete_sql)

url = "http://49.235.92.12:9000/api/v1/register"

body = {
    "username": "test123",
    "password": "123456",
    "mail": "1233@qq.com"
}
r = s.post(url, json=body)
print(r.text)
print(r.json())

assert r.json()["msg"] == "注册成功!"
