a = None     # null

b = False
c = True           # bool

d = 122
f = 12.001

# type()
g = "hello"
h = "122"
j = 'aaaxx' \
    ''
k = '''bbbb'''
l = """ccc
asss
ss
"""
print(type(l))

aaa = [1, 2, 3, 4, "aaa", True, [1222], None]
print(aaa[0])
print(aaa[-1])
bbb = {
    "a": 1,
    "b": "aaa",
    "c": [1222],
    "d": None,
    "f": True,
}
print(bbb)  # {'a': 1, 'b': 'aaa', 'c': [1222], 'd': None, 'f': True}
print(type(bbb))
# 取值
# print(bbb["x"])    # KeyError: 'x'
print(bbb.get("z", ""))  # None

bbb["key"] = "value1"
print(bbb)
bbb["a"] = "value2"
print(bbb)