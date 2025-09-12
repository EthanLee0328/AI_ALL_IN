import time
import random
import multiprocessing


def func1(queue):
    while True:
        queue.put(random.randint(1, 50))
        time.sleep(random.random())


def func2(queue):
    while True:
        print("=" * queue.get())


if __name__ == '__main__':
    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(2)
    pool.apply_async(func1, args=(queue,))
    pool.apply_async(func2, args=(queue,))
    pool.close()
    pool.join()
