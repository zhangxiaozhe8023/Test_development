# -*- coding: utf-8 -*-
# @Time : 2021/7/27 14:29
# @Author : admin
# @File : oursTest.py
# @Software: PyCharm
# 首先导入json包
import json
import os

if __name__ == '__main__':
    # 字典类型
    dictfile = {
        "a" : 1,
        "b" : 2,
        "c" : True
    }
    print(type(dictfile))
    # 字典转json
    jsonFile = json.dumps(dictfile)
    print(jsonFile)
    print(type(jsonFile))
    # json转字典类型
    dictest = json.loads(jsonFile)
    print(type(dictest))

    # 大于0的或者小于0的数分别有几个
    a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
    # 使用传统的判断思维累加
    m=0
    n = 0

    for i in a :
        if i > 0:
            m+= 1
        elif i < 0:
            n+= 1
        else:
            pass
    print('大于0是%s'% m)
    print('小于0的%s'% n)
    # 字符串切片
    aa='123456789'
    spitaa=aa[2:6]
    print(spitaa)
    '''  3.
    字符串切割
    已知一个字符串为“hello_world_yoyo”, 如何得到一个队列["hello", "world", "yoyo"]'''
    a = "hello_world_yoyo"
    b = a.split("_")
    '''print(b)
    已知一个队列, 如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
     '''
    a = [1, 3, 5, 7]
    number01=a[0]
    a.insert(3,number01)
    print(a)
    # 删除对列指定数据
    del a[0]
    print(a)
    '''
    已知 a = 9, b = 8,如何交换a和b的值，得到a的值为8,b的值为9 '''
    a = 8
    b = 9
    a,b =b,a
    print(a)
    print(b)

    '''冒泡排序'''
    '''    a = [1, 3, 10, 9, 21, 35, 4, 6]

    s = range(1, len(a))[::-1]
    print(list(s))  # 交换次数

    for i in s:
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        print("第 %s 轮交换后数据：%s" % (len(s) - i + 1, a))
    print(a)
    '''
    a = [1, 3, 6, 9, 7, 3, 4, 6]
    # 正序排序
    a.sort()
    print(a)
    # 倒序排序
    a.sort(reverse=True)
    print(a)
    # 去重
    # b= list(set(a))
    # print(b)
    # 去重
    listnew =[]
    for i in a:
        if i not in listnew:
            listnew.append(i)
    print(listnew)




