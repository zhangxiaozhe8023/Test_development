'''
水仙花数
'''

# 1.三位数   range(100, 1000)

for i in range(100, 1000):
    s = sum([int(j)**3 for j in str(i)])
    if i == s:
        print("水仙花数：%s"%i)