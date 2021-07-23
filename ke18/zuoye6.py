'''
完全数
'''

for i in  range(1, 1000):
    s = []
    for j in range(1, i):
        if i%j == 0:
            s.append(j)
    # print(s)
    if i == sum(s):
        print("完全数：%s" % i)


