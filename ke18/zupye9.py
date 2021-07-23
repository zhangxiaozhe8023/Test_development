# a = 0
#
# s = []
# b = 1
# while 1:
#     n = a+b
#     if n > 100:
#         break
#     else:
#         print(n)
#         s.append(n)
#         a, b = b, n
# print(s)


l = []


def func():
    a = 0
    b = 1
    for i in range(15):
        a, b = b, a + b
        l.append(b)
    return l


print(func())
