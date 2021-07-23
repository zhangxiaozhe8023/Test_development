

def func_api_1(a, b):
    '''第一个接口:
    :arg a  必填参数 int
    :arg b  必填参数 int'''
    if not isinstance(a, int):
        return "参数类型错误：a 必须是int类型"
    if not isinstance(b, int):
        return "参数类型错误：b 必须是int类型"
    # if not isinstance()
    c = a+b
    return c


if __name__ == '__main__':
    c = func_api_1("a", 1)
    print(c)
    d = func_api_1(1, "b")
    print(d)
    e = func_api_1(1, 11)
    print(e)
