list1 = [100, 200, 300, 400, 500]
print(list1[1])
print(list1[-2])

print(list1)
print(list1[:])  # [100, 200, 300, 400, 500]
print(list1[2:4])  # [300, 400]
print(list1[2:])
print(list1[:2])
print(list1[2:-1])
print(list1[::-1])  # [500, 400, 300, 200, 100]

list1.append(600)
print(list1)
list1.insert(2, 700)
print(list1)

list2 = ["a", "b", "c", "d", "e", "f"]

print(list1 + list2)

print(list1 * 2)

list1[0] = -1
print(list1)

list1[2:4] = ["a", "b", "c", "d", "e", "f"]
print(list1)

print(600 in list1)

print(len(list1))

for i in list1:
    print(i)

for i in range(len(list1)):
    print(i, list1[i])

for i, val in enumerate(list1):
    print(i, val)

print(list1[:])

del list1[1]
print(list1)
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in list2:
    print(i)

print("========================================")
squares1 = [x ** 2 for x in range(10)]
print(squares1)

squares2 = [x ** 2 for x in range(10) if x % 2 == 0]

print(squares2)

list3=[1,2,3,4,5,6,7,8,9,10]
list4=["a","b","c","d","e","f"]

tuple_list=[(i,j) for i in list3 for j in list4]
print(tuple_list)

zipped=zip(list3,list4)
print(zipped)
print(list(zipped))

