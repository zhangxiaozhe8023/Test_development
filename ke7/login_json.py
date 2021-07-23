import requests
import json

url = "http://49.235.92.12:9000/api/v1/login"

body = {
    "username": "test",
    "password": "123456"
}
h = {"Content-Type": "application/json"}
# 转json
r = requests.post(url, data=json.dumps(body), headers=h)
print(r.text)     # str
print(r.content)  # byte
print(r.json())   # dict

# 拿到token
token = r.json().get("token")
print("取到token:%s" % token)

url2 = "http://49.235.92.12:9000/api/v1/userinfo"

h2 = {
    "Authorization": "Token %s" % token
}
r2 = requests.get(url2, headers=h2)
print(r2.text)

# mail
print(r2.json()["data"])
print(r2.json()["data"][0])
print(r2.json()["data"][0]['mail'])
mail = r2.json()["data"][0]['mail']
assert mail == "283340479@qq.com"

