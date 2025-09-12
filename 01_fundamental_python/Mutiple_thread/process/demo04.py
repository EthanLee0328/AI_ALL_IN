import os
import multiprocessing

# 子进程向传入的列表中添加元素，最终发现主进程与子进程之间的列表结果不同
def func(list):
    for i in range(10):
        list.append(i)
        print(os.getpid(), list)


if __name__ == '__main__':
    list1 = []
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(os.getpid(), list1)
