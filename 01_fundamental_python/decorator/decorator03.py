from math import sqrt


# 多个装饰器的装饰过程：离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰。
# When multiple decorators are applied, the one closest to the function is applied first,
# and then the outer decorators are applied in sequence.
def get_integer(func):
    def inner(x):
        x = int(x)
        return func(x)

    return inner


def get_absolute(func):
    def inner(x):
        x = abs(x)
        return func(x)

    return inner


@get_integer
@get_absolute
def func(x):
    '''计算x的平方根'''
    return sqrt(x)


print(func("-4"))  # 2.0
