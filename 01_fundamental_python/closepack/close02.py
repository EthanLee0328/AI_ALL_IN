# 所有函数对象都有一个 __closure__ 属性，如果它是一个闭包函数，则该属性返回单元格对象的元组，
# 每个单元格对象都对应着闭包所引用的外部函数作用域中的一个变量。对于普通函数，
# __closure__ 属性的值通常是None。
# All function objects have a __closure__ attribute. If the function is a closure,
# this attribute returns a tuple of cell objects, each corresponding to a variable
# from the outer function’s scope that the closure references.
# For regular functions, the value of the __closure__ attribute is usually None.
def linear(a, b):
    def calc(x):
        return a * x + b
    return calc
y = linear(2, 3)
objects = y.__closure__
print(objects)
print(objects[0].cell_contents)
print(objects[1].cell_contents)
print((objects[0].cell_contents, objects[1].cell_contents))
