import re


while True:
    text = input("请输入邮箱格式：")
    if text.upper() == "Q":
        quit()
    if re.search(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.com$', text):
        username = re.findall('^(.+?)@', text)
        print('username:%s' % username[0])
        companyname = re.findall('@(.+?)\.com', text)
        print("companyname:%s"%companyname[0])
    else:
        print('incorrect email format')