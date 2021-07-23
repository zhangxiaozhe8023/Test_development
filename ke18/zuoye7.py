'''
open文件读写
'''
a = [
       {"yoyo1": "123456"},
       {"yoyo2": "123456"},
       {"yoyo3": "123456"}
    ]

for i in a:

    with open("xxx.txt", "a", encoding="utf-8") as fp:
        for j in i.keys():
            print(i[j])
        fp.write(j+","+i[j]+"\n")
