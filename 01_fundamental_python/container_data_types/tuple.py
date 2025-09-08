tuple_generator=(i for i in range(10))
print(tuple_generator)
tuple1=tuple(tuple_generator)
print(tuple1)
print(tuple1[2:4])

# 元组的不可变指的是元组所指向的内存中的内容不可变，但可以重新赋值。
tuple2 = (100, 200, 300)
print(id(tuple2), tuple2)
tuple2 = tuple2 + (1, 2, 3)
print(id(tuple2), tuple2)
