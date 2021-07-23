import requests

s = requests.session()

def fuc_y(*args, **kwargs):
    print(args)
    print(kwargs)
a=[1,2,3,4]
body = {

    "a":1,
    "b":2,
    "c":3
}

fuc_y(*a,**body)

c = range(1, 101)
print(list(c))
fuc_y(c)




# def func_x(a, b=0, c=None):
#     return a*a
#
# print(func_x(a=1))



c = lambda x: x*x
print(c(3))
