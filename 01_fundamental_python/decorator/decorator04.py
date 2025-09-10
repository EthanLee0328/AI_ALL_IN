from math import sqrt


def times(n):
    def get_absolute(f):
        def inner(x):
            x = abs(x)
            for i in range(n):
                x = f(x)
            return x

        return inner

    return get_absolute


@times(2)
def func(x):
    '''计算x的平方根'''
    return sqrt(x)


print(func(-4))
