import requests
import re
s = requests.session()

print(s.cookies)
url = "http://49.235.92.12:9000/admin/login/?next=/admin/"
r1 = s.get(url)  # 第一次请求登录页
print(s.cookies)

# 获取页面csrfmiddlewaretoken
# print(r1.text)

# 知道前后取中间，遇到字符加转义
# name='csrfmiddlewaretoken' value='(.+?)'

csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value=\'(.+?)\'", r1.text)
print(csrfmiddlewaretoken[0])

# 登录
body = {
    "csrfmiddlewaretoken": csrfmiddlewaretoken[0],
    "username": "admin",
    "password": "yoyo123456",
    "next": "/admin/"
}
r = s.post(url, data=body)
# print(r.text)

# if "Site administration | Django site admin" in r.text:
#     print("登陆成功")
# else:
#     print("登陆失败")
assert "Site administration | Django site admin" in r.text

print(s.cookies)

# 登陆之后的页面访问
url3 = "http://49.235.92.12:9000/admin/authtoken/token/"
r3 = s.get(url3)
print(r3.text)

