# 当调用的函数执行完毕后，函数内的变量就会被销毁。但有时希望在调用函数后函数内的数据能够保存下来重复使用，这时候可以用到闭包。闭包可以避免使用全局值，并提供某种形式的数据隐藏。
# 构建闭包的条件：
# 外部函数内定义一个内部函数。
# 内部函数用到外部函数中的变量。
# 外部函数将内部函数作为返回值。
# When a called function finishes execution, the variables inside the function will be destroyed. However, sometimes we want the data inside the function to be preserved and reused after the function call. In this case,
# we can use a closure. A closure can avoid the use of global values and provide a certain form of data hiding.
# Conditions for constructing a closure:
# An inner function is defined inside an outer function.
# The inner function uses variables from the outer function.
# The outer function returns the inner function as its return value.
def linear(a, b):
    def calc(x):
        return a * x + b
    return calc
calc1 = linear(2, 3)
print(calc1) # <function linear.<locals>.calc at 0x106a9f880>

print(calc1(1)) # 5


