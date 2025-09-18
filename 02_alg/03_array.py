"""模拟数组"""


class MyArray:
    def __init__(self):
        self.__capacity = 8
        self.__size = 0
        self.__items = [0] * self.__capacity
        # arr=MyArray()
        # for item in arr._MyArray__items:
        #     print(item)

    def __str__(self):
        res_str = "["
        for i in range(self.__size):
            res_str += str(self.__items[i])
            if i < self.__size - 1:
                res_str += ","
        res_str += "]"
        return res_str

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __grow(self):
        self.__capacity *= 2
        new_items = [0] * self.__capacity
        for i in range(self.__size):
            new_items[i] = self.__items[i]
        self.__items = new_items

    def insert(self, index, item):
        if index < 0 or index > self.__size:
            raise IndexError("索引越界")
        if self.__size == self.__capacity:
            self.__grow()
        for i in range(self.__size, index, -1):
            self.__items[i] = self.__items[i - 1]
        self.__items[index] = item
        self.__size += 1

    def append(self, item):
        self.insert(self.__size, item)

    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("索引越界")
        for i in range(index, self.__size - 1):
            self.__items[i] = self.__items[i + 1]
        self.__size -= 1

    def set(self, index, item):
        if index < 0 or index >= self.__size:
            raise IndexError("索引越界")
        self.__items[index] = item

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("索引越界")
        return self.__items[index]

    def find(self, item):
        if item < 0 or item > self.__size:
            raise IndexError("索引越界")
        for i in range(self.__size):
            if self.__items[i] == item:
                return i
        return -1

    def foreach(self, func):
        for i in range(self.__size):
            func(self.__items[i])


if __name__ == '__main__':
    ma = MyArray()
    ma.insert(0, 11)
    ma.insert(1, 22)
    ma.insert(1, 33)
    print(ma)
    ma.append(44)
    ma.append(55)
    ma.append(66)
    ma.append(77)
    ma.append(88)
    ma.append(99)

    print(ma)

    ma.foreach(print)


    








