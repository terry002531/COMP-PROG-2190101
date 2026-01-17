# def make_int_list(x):
#     # 把字符串分割后转成 int 列表
#     return [int(i) for i in x.split()]
#
# def is_odd(e):
#     # 判断是否为奇数
#     return e % 2 == 1
#
# def odd_list(alist):
#     # 返回 alist 中所有奇数
#     return [i for i in alist if i % 2 == 1]
#
# def sum_square(alist):
#     # 返回 alist 中所有数的平方和
#     return sum(i * i for i in alist)
#
# # 必须保留这一行，判题器会调用
# exec(input().strip())


def make_int_list(x):
    return [int(i) for i in x.split()]
    # return list(map(int, x))

def is_odd(x):
    return x % 2 == 1

def odd_list(x):
    a = x
    # a = make_int_list(x)
    c = []
    for b in a:
        if b % 2 == 1:
            c.append(b)
    return c

def sum_square(alist):
    a = alist
    # a = make_int_list(alist)
    s = 0
    for b in a:
        s += b * b
    return s

exec(input().strip())


