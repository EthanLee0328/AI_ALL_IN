class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def __str__(self):
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next
        return "->".join(result)

    @property
    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    def insert(self, index, item):

        if index < 0 or index > self.__size:
            raise IndexError('索引超出范围')
        if index == 0:
            self.__head = Node(item, self.__head)

        else:

            node = self.__head
            for i in range(index - 1):
                node = node.next

            node.next = Node(item, node.next)

        self.__size += 1

    def append(self, item):
        self.insert(self.__size, item)

    def remove(self, index):
        """删除指定位置的元素"""
        # 1. 判断索引是否合法
        if index < 0 or index >= self.__size:
            raise IndexError("索引超出范围")

        # 2. 删除头结点
        if index == 0:
            # 直接把 head 指向下一个节点
            self.__head = self.__head.next
        else:
            # 3. 找到 index-1 位置的节点
            node = self.__head
            for i in range(index - 1):
                node = node.next

            # 4. 跳过 index 位置的节点
            # 原本：node -> 要删除的节点 -> 下一个节点
            # 现在：node -> 下一个节点
            node.next = node.next.next

        # 5. 更新链表大小
        self.__size -= 1

    def set(self, index, item):
        """修改指定位置的元素"""
        # 1. 检查索引是否合法
        if index < 0 or index >= self.__size:
            raise IndexError("索引超出范围")

        # 2. 从头结点开始往后走，直到 index 位置
        node = self.__head
        for i in range(index):
            node = node.next

        # 3. 修改该节点的数据
        node.data = item

    def get(self, index):
        """获取指定位置的元素"""
        # 1. 检查索引是否合法
        if index < 0 or index >= self.__size:
            raise IndexError("索引超出范围")

        # 2. 从头结点开始往后走，直到 index 位置
        node = self.__head
        for i in range(index):
            node = node.next

        # 3. 返回该节点的数据
        return node.data

    def find(self, item):
        """查找元素是否存在"""
        node = self.__head
        # 从头结点开始，逐个比较
        while node:
            if node.data == item:
                return True  # 找到
            node = node.next
        return False  # 没找到

    def for_each(self, func):
        """遍历链表，对每个节点执行函数 func"""
        node = self.__head
        while node:
            func(node)  # 把节点传给外部函数
            node = node.next

def test_linked_list():
        ll = LinkedList()

        print("===== 测试开始 =====")
        print("初始链表:", ll)
        print("链表是否为空:", ll.empty())
        print("链表大小:", ll.size)

        # 1. append 测试
        print("\n[测试 append]")
        for i in range(1, 6):  # 插入 1,2,3,4,5
            ll.append(i)
        print("插入 1~5 后:", ll)  # 1->2->3->4->5
        print("链表大小:", ll.size)

        # 2. insert 测试
        print("\n[测试 insert]")
        ll.insert(0, 100)  # 头部插入
        ll.insert(3, 200)  # 中间插入
        ll.insert(ll.size, 300)  # 尾部插入
        print("插入 100,200,300 后:", ll)
        print("链表大小:", ll.size)

        # 3. get 测试
        print("\n[测试 get]")
        print("第 0 个元素:", ll.get(0))  # 100
        print("第 3 个元素:", ll.get(3))  # 200
        print("最后一个元素:", ll.get(ll.size - 1))  # 300

        # 4. set 测试
        print("\n[测试 set]")
        ll.set(0, 111)
        ll.set(3, 222)
        ll.set(ll.size - 1, 333)
        print("修改元素后:", ll)

        # 5. find 测试
        print("\n[测试 find]")
        print("查找 222:", ll.find(222))  # True
        print("查找 999:", ll.find(999))  # False

        # 6. remove 测试
        print("\n[测试 remove]")
        ll.remove(0)  # 删除头
        print("删除头节点后:", ll)
        ll.remove(2)  # 删除中间
        print("删除中间节点后:", ll)
        ll.remove(ll.size - 1)  # 删除尾
        print("删除尾节点后:", ll)
        print("链表大小:", ll.size)

        # 7. for_each 测试
        print("\n[测试 for_each]")
        print("链表所有元素:", end=" ")
        ll.for_each(lambda node: print(node.data, end=" "))
        print()

        print("===== 测试结束 =====")

if __name__ == "__main__":
        test_linked_list()
