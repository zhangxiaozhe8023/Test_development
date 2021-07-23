import requests
import re
from requests_toolbelt import MultipartEncoder
from lxml import etree
import os

# 设置一个环境变量

# host = "http://49.235.92.12:8020"

def login_xadmin(s):
    '''xadmin登陆'''
    url = os.environ["xadmin_host"]+"/xadmin/"
    r1 = s.get(url)
    # print(r1.text)
    tokens = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r1.text)
    print(tokens[0])

    body = {
        "csrfmiddlewaretoken": tokens[0],
        "username": "admin",
        "password": "yoyo123456",
        "this_is_the_login_form": "1",
        "next": "/xadmin/"
    }
    r2 = s.post(url, data=body)
    # print(r2.text)
    if "主页面 | 后台页面" in r2.text:
        print("登陆成功")
    else:
        print("登陆失败")

def add_teacher(s, name="yoyo老师4"):
    '''添加老师'''
    url2 =os.environ["xadmin_host"] +"/xadmin/hello/teacherman/add/"
    # multipart/form-data  类型post请求
    r3 = s.get(url2)
    tokens2 = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r3.text)
    print(tokens2[0])
    m = MultipartEncoder(
                fields=[
                    ("csrfmiddlewaretoken", tokens2[0]),
                    ("csrfmiddlewaretoken", tokens2[0]),
                    ("teacher_name", name),
                    ("tel", "13520000000"),
                    ("mail", "1352@qq.com"),
                    ("sex", "M"),
                    ("_save", ""),
                ]
    )
    r4 = s.post(url2, data=m, headers={'Content-Type': m.content_type})
    return r4.text

def get_add_result(result):
    '''获取添加文本的结果'''
    demo = etree.HTML(result)
    nodes = demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    print(nodes[0].text)
    return nodes[0].text

# def add_image(s, title="图片test_111"):
#     '''添加图片'''
#     url3 = "http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
#     r3 = s.get(url3)
#     # print(r1.text)
#     tokens = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r3.text)
#     print(tokens[0])
#
#     m = MultipartEncoder(
#                     fields=[
#                         ("csrfmiddlewaretoken", tokens[0]),
#                         ("csrfmiddlewaretoken", tokens[0]),
#                         ("title", title),
#                         # ("image", ('122.png', open('122.png', 'rb'), 'image/png')),
#                         ("fiels", ('122.png', open('122.png', 'rb'), 'image/png')),
#                         ("_save", ""),
#                     ]
#         )
#     r4 = s.post(url3, data=m, headers={'Content-Type': m.content_type})
#     print(r4.text)

if __name__ == '__main__':
    os.environ["xadmin_host"] = "http://49.235.92.12:8020"
    s = requests.session()
    login_xadmin(s)
    result = add_teacher(s, name="老师5xxx")
    # 判断
    actul_result = get_add_result(result)
    assert actul_result == "老师5xxx"

