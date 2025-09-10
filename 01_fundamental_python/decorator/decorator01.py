# A decorator allows you to dynamically add or modify the functionality of
# a function without changing its original code. Essentially,
# a decorator is an object that takes a function as input and returns a new, wrapped function.
from math import sqrt


def func(x):
    '''计算x的平方根'''
    return sqrt(x)


def decorator(f):
    def wrapper(x):
        '''计算x的绝对值'''
        x = abs(x)
        return f(x)

    return wrapper


func = decorator(func)

print(func)

print(func.__doc__)
print(func(-9))
