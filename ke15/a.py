def func(i):
    a=i+1
    return a
def func1(func):
    b= func+2
    print(b)

func1(func(3))