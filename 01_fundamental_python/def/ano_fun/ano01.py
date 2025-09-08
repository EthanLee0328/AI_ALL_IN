print("use ordinary function transfer  parameter")


def operator(a, b):
    return a + b


def function(a, b, operator):
    return operator(a, b)


print(function(1, 2, operator))


print("using a lambda function as an argument")

def function2(a, b, operator2):
    return operator2(a, b)

print(function2(1, 2, lambda a, b: a + b))
