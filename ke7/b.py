import json

# dict
bbb = {
    "a": 1,
    "b": "aaa",
    "x": (1, 2, 3),  # tuple 元组
    "c": [1222, 222, True, None, False, {"aaaa": "222"}],
    "d": None,
    "f": True,
    "g": 122.2,
    "h": {
        "aaa": "HELLO",
        "bbb": "122"
    }
}
print(bbb)
print(type(bbb))
dict_json = json.dumps(bbb)
print(dict_json)
print(type(dict_json))   # json  字符串

json_dict = json.loads(dict_json)  # 转dict
print(json_dict)


