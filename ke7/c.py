import json

# a = {"aaa": 1, "bbb": None}  # dict
# print(a)
# print(type(a))
# print(str(a))  # 转字符串
# b = '{"aaa": 1, "bbb": None}'  # str 字符串
# print(b)
# print(type(b))
#
# # c = '{"aaa": 1, "bbb": null}'
# # print(c)
# c = json.dumps(a)  # json
# print(c)

d = '{"aaa": 1, "bbb": None}'
# 字符串 转dict
print(eval(d))
f = "11*10"
print(f)
print(eval(f))
print(json.dumps(eval(d)))
