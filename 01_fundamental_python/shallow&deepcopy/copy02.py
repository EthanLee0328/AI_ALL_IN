# 可以看到拷贝后，新的列表地址与列表中各个可变类型元素的地址都发生了改变，不可变类型元素拷贝后地址不变。

import copy

list1 = [1, 2, 3, [100, 200, 300]]
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)

list3 = copy.deepcopy(list1)
print(id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3]), list3)


list1[0] = 100

print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)

print(id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3]), list3)


list1[3].append(400)

print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)

print(id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3]), list3)
