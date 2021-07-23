'''
排序 去重
'''
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]

b = sorted(a)
print(b)
print(a)  # 不改变a

a.sort()
print(a)

# set  集合  {1, 6, 7, 8, 9, 11}
c = set(a)
print(c)
print(list(c))