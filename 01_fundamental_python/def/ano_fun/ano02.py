print("*" * 100)

student_list = [
    {'name': 'Mike', 'age': 23},
    {'name': 'Joe', 'age': 21},
    {'name': 'Jane', 'age': 22},
    {'name': 'John', 'age': 20},
]
print(sorted(student_list, key=lambda x: x['age'], reverse=True))

print("*" * 100)

map_result = map(lambda x: x ** x, [1, 2, 3, 4, 5])
print(list(map_result))

print("*" * 100)
filter_result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(filter_result))

print("*" * 100)

from functools import reduce

reduce_result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(reduce_result)

print("*" * 100)


# 普通的自定义函数：
def dog(name, age, species):
    return (name, age, species)

# 添加了注释的自定义函数：
def dog(name: str, age: (1, 99), species: '狗狗的品种') -> tuple:
    return (name, age, species)

print(dog.__annotations__)

