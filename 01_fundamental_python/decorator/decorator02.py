from math import sqrt

# 当我们使用 @decorator 前缀在 func 定义前，Python会自动将 func 作为参数传递给 decorator，
# 然后将返回的 inner 函数替换掉原来的 func。
# When we use the @decorator prefix before the definition of func, Python automatically passes func
# as an argument to the decorator,
# and then replaces the original func with the returned inner function.
def decorater(f):
    def inner(x):
        '''计算x的绝对值'''
        x = abs(x)
        return f(x)

    return inner


@decorater
def func(x):
    '''计算x的平方根'''
    return sqrt(x)


print(func.__doc__)
print(func(-9))
