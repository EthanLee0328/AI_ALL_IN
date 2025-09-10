from math import sqrt


class Decorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        x = abs(x)
        return self.f(x)


@Decorator
def func(x):
    return sqrt(x)


print(func(-4))
