import requests

url = "http://49.235.92.12:8020/xadmin/"

h = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
   "Cookie": "easy-mock_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkZGQ0ZTZiYTQ5ZGMzMDAxNjgzOWE3NyIsImlhdCI6MTU3NTIwNDI4MCwiZXhwIjoxNTc2NDEzODgwfQ.c4Fllbb1Q-Gl3qCGYOut8DuHiTQDYdZ8q7Xhd7oPYN4; _ga=GA1.1.716475613.1575473793; csrftoken=2aHiffvbDit7vF0JW4CBF9G0WstLwgTuWBzikAEwFACxbAP4k5CTopUHfSKcq9H6; zentaosid=muaqcfq2fhe9eiqevpilnj25t4"
}

body = {
    # "csrfmiddlewaretoken": "7Ixbfau6dQ7mloCRMhmVf07UOmOKPAwu19pbkvDrf8gM1jrcaimdYglB7M5bJtk6",
    "username": "admin",
    "password": "yoyo123456",
    "this_is_the_login_form": "1",
    "next": "/xadmin/"
}

r = requests.post(url=url, headers=h, data=body)
# print(r.text)

# if "主页面 | 后台页面" in r.text:
#     print("登录成功")
# else:
#     print("登录失败")

# 返回html 乱码
print(r.content.decode("utf-8"))  # byte